# Game State: Replication Roles

*Document Summary: Explains the various replication roles an actors can have.**Document Changelog: Last updated by Michiel Hendriks, converted to an UDN document. Original author was Mike Lambert (UdnStaff?).*

* [Game State: Replication Roles](#game-state-replication-roles)
  + [Roles](#roles)
  + [ROLE\_Authority](#role_authority)
  + [ROLE\_None](#role_none)
  + [ROLE\_DumbProxy](#role_dumbproxy)
    - [Other quirks](#other-quirks)
  + [ROLE\_SimulatedProxy](#role_simulatedproxy)
    - [Non-Pawn ROLE\_SimulatedProxy](#non-pawn-role_simulatedproxy)
    - [Pawn ROLE\_SimulatedProxy](#pawn-role_simulatedproxy)
  + [ROLE\_AutonomousProxy](#role_autonomousproxy)
  + [Role Summary](#role-summary)
    - [Roles:](#roles)
    - [RemoteRoles:](#remoteroles)

## Roles

In addition to their varying priorities and properties mentioned earlier, actors also have different 'ways' of replicating data. A rocket or grenade needs only the initial position and velocity, and the client is able to simulate the rest of it's behavior on it's own. A player in the game needs both location and velocity information replicated to all other clients so that they can simulate the motion of the player for the brief period of time between updates. These different networking behaviors correspond to different roles.If an actor exists on both the server and client, it's `Role` value will generally be `ROLE_Authority` on the server, and be one of `ROLE_DumbProxy`, `ROLE_SimulatedProxy`, or `ROLE_AutonomousProxy` on the client, corresponding to three fundamental different roles that an actor can play in netplay. The `Role` of the actor on the client is normally specified in `RemoteRole` 's value in the defaultproperties of the actor, but one is free to change the value dynamically in-game without any problems. The value of the Role is set in the current `Role` field, with `RemoteRole` indicating what `Role` is set on the other side of the connection. This allows code on the server, where `Role` is `ROLE_Authority`, to check what kind of simulation is being provided on the client. In general, the `Role` is `ROLE_Authority` for whatever machine spawned the actor. If an actor is spawned on the client, the client will have a `Role` of `ROLE_Authority`, but the actor will not be replicated to the server, due to the ease with which one could cheat and create weapons for themselves, on the client.Now that you understand how Roles and RemoteRoles work, let's go through an overview of each of the various roles individually.This document is part of the [NetworkingTome](https://udn.epicgames.com/Two/NetworkingTome).

## ROLE\_Authority

This role is different from the others in that it is always the `Role` on the server. On the server, all Roles will be= ROLE\_Authority=, and the `RemoteRole` will be one of the following values. On the client, the reverse will be true. This role doesn't have any real significance, beyond it's use in replication statements, which are described later.

## ROLE\_None

This role is probably the simplest. It simply tells the server not to make this actor relevant to the client. No information will be sent about it, and it will exist only on the machine on which it was created. If a given actor was created independantly on both the client and the server (via a simulated function, described later), and given a `RemoteRole` of `ROLE_None`, then there would be two seperate, non-connected instances of the actor on the server and the client. This is used rather often for special effects for which replication is not needed, and can instead be spawned on both machines independantly.

## ROLE\_DumbProxy

This role is used for simple actors that require no real client-side prediction. They don't need any Physics prediction, but they only need to be relevant to the client to get their variables replicated. This is used for all Inventory actors when they reside on the ground, which prevents any higher-bandwidth Simulated Proxy stuff, but yet allows you to see all the stuff you need for the inventory actor. If you do try to manually move this actor, the client will get periodic updates, usually around every half-second or so on a normal connection. This creates quite a jumpy effect if you are using Dumb Proxy with a particular Physics type, since you get locational updates every fractrion of a second, and there is no simulation or prediction being performed. Rather, the Location updates are useful for when moving the actor across the level, like a flag respawn, etc where the jumpy periodic location updates don't matter since it's only one location update. The same is done with rotation updates, with periodic changes coming in to the client every so often. This role also causes animation updates to be sent from the server to the client, unless the client specifically tells it not to via `bClientAnim`. In summary, an actor with this role is force-fed data from the server. It's intended for actor's that don't move (except in jumps like transportation, respawn, etc), yet still need to be relevant. This role type is used rather infrequently in practice. In most cases you can use Simulated Proxy with some code to handle every case you'll need.

### Other quirks

There's a few quirks that can have a significant effect on your netplay development. Dumb Proxy actors do not have a variety of events run clientside. Simulated *Tick()*, *Timer()*, and state code, along with the physics calculations, are not performed on Dumb Proxy actors on the client. These actors are supposed to be dumb proxy actors that are "dumb" and simply get data sent over the net, without any simulation behavior. One exception to the above rule is that falling physics are performed clientside for Dumb Proxy actors if the actor has a falling physics, which allows tossed weapons to fall correctly in netplay. In an early attempt at the weapon in the tutorial, I attempted to create a client-side physics that would combine with the location and rotation updates that were inherently sent via the Dumb Proxy role, but since the client would not run my *Tick()* -based physics calculations, that idea had to be thrown out the window.

## ROLE\_SimulatedProxy

This is used for anything that should be simulated over the network, via prediction. Take a rocket, for example. It always travels in a straight line, and is an ideal candidate for Simulated Proxy. By the same token, the game can predict the falling physics clientside, and so grenades, and falling people are also good candidates for this role. Anything that can be predicted clientside because of Physics or clientside physics should use this Role. All `Controllers` use this role as well, since when a player is running, he's more than likely to continue to run, and so they can take advantage of the simulation as well. It's the best prediction method that can be used, for unpredictable players. The only exception to this guideline for players is the pawn you yourself are playing as, since you don't want to simulate your own behavior.In practice, there are two types of Simulated Proxy actors. Simulated Pawns and Simulated Non-Pawns both have different but similar behavior. The differences are delineated below.

### Non-Pawn ROLE\_SimulatedProxy

This one is basically the opposite of Dumb Proxy. It expects full client-side prediction of the actor, given initial values. It's like extrapolating out a curve given some data, where the current Physics is the curve fit, and you have initial data available to extrapolate from. `ROLE_SimulatedProxy` gives you an initial Location, Rotation, and Physics. It then keeps you updated with the Velocities, should they change. These variables should enable the client to perform full client-side prediction on this object, assuming it continues along the physics prediction. In the case of `PHYS_Falling` and `PHYS_Projectile`, this is the case. There can be no aberration from these behaviors, (unless you play around with the Physics variables `bBounce` and such, which are very useful in prediction.) Finally, for this role, you also get animation updates, assuming the client is not the owner and it's not set for client-side animation. In summary, this Role is for actors that smoothly predict their data on the client.

### Pawn ROLE\_SimulatedProxy

When `ROLE_SimulatedProxy` is combined with Pawns, a different sort of simulated proxy is created, that act differently in netplay. Pawns are one of the most complex actors in terms of replication, because of their need for clientside prediction, yet inherent unpredictability in their movement. There is no way to duplicate this behavior except by subclassing pawn, so don't expect to achieve it in your projectile subclass. A Simulated Pawn gets the best of dumbproxy and simulatedproxy. It gets velocity updates for the clientside prediction, while at the same time getting location updates from the server to 'readjust' the player's locations. You might then wonder why the pawn does not jump when a new location update comes in. Again, there is native code that causes the actor to smoothly head towards the location given by the server if the location position is too far off from the player's real position. This again ensures seamless movement of player's while keeping them accurate to the server's version. All non-players will get by with velocity-only client-side prediction. No physics will be taken into account for these pawns. This is because some non-players can be `PHYS_Spider`, or a variety of other physics that don't work with the following always-walking/falling prediction. Only player pawns get the special client-side prediction to have falling/walking physics. This physics is an assumed physics, which is accomplished by applying the zone's gravity if the player is not on the ground. This logic will be bypassed if the pawn's `bCanFly` variable is set, which frees it of the clientside physics, but must be accounted for in your code, since there is no physics replication in pawns. This logic is also bypassed if the pawn is in a water zone, which also differs from the default walking/falling physics. In water zones, actors are predicted using velocity alone, which is sufficient with the low amount of gravity that exists in those zones. The actor's get their locations 'adjusted' anyway, so it doesn't make any real difference in the long run. Finally, pawns get rotation updates. Since rotation (which is directly based off the ViewRotation?, or the direction the player is looking) can change quite radically, no prediction is done with it. Instead, the player's rotation is adjusted as new player rotation information comes in from the client. Animation is handled the same as any other non-pawn simulated proxy.

## ROLE\_AutonomousProxy

This is used for you. When you play online, you yourself should be treated differently from all other PlayerControllers. You don't want your own self being predicted based upon the server's expectations. Rather, you want to control yourself and tell the server where you are moving. That is the purpose of this role. This is used for things that the client directly controls. In most cases, this will only be used by the PlayerControllers. When Unreal sees an Autonomous Proxy actor, it finds the top owner of the actor (`owner->owner->owner...`), which should be a PlayerController. If this Top Owner is not the player we are currently replicating to, we change the `RemoteRole` to `ROLE_SimulatedProxy` temporarily. `UnChan` 's *UActorChannel::ReplicateActor* This allows Autonomous Proxy actors to be treated as Simulated Proxy actors to eveyone else, and treated as Autonomous Proxy actors to ourself. When the actor's `RemoteRole` is set to `ROLE_AutonomousProxy`, it appears to be a Simulated Proxy for everyone BUT the owner of the actor. Note that this technique is also used with the guided redeemer, to ensure that it works the same way and lets the controlling player have a different proxy setting from the other clients that are just simulating it. Having the server tell you where your guided redeemer is flying would not be appropriate. Rather, you want to tell the server where your guided redeemer is. While Autonomous Proxy doesn't make this just 'work' for you, it does differentiate you from the other people viewing your redeemer, which is what is needed to have it act differently for you, as compared to everyone else.

## Role Summary

### Roles:

* `ROLE_Authority` is used for the server or the machine which is controlling the actor.

### RemoteRoles:

* `ROLE_None` is used to indicate the actor should not be relevant at all.
* `ROLE_DumbProxy` is used for actors that have no need for clientside simulation or behavior. It's used rarely in practice.
* `ROLE_SimulatedProxy` is used for any actor that needs clientside simulation based upon initial rotation, location, and velocity settings. Simulated pawns get those three varviables over time in addition to everything Simulated Proxies get.
* `ROLE_AutonomousProxy` is used for client-controlled actors which need to be treated seperately for their owner, which will provide client->server movement information, versus other players in the game, which will use Simulated Proxy to simulated the actor on their client.

The actual code that defines these various Roles will be shown later in the actor's variable replication statements. It is this code which makes a role do what it does (in addition to some internal native code, of course.)

