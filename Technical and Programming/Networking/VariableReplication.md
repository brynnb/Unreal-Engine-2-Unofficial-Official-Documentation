# Variable Replication

*Document Summary: explains how variables are replicated from one game instance to the other.**Document Changelog: Last updated by Michiel Hendriks, converted to an UDN document. Original author was Mike Lambert (UdnStaff?).*

* [Variable Replication](#variable-replication)
  + [Overview](#overview)
  + [Reliability of Variable Data](#reliability-of-variable-data)
  + [Newly Relevant Actors (Spawning)](#newly-relevant-actors-spawning))
  + [A Time for Variable Replication](#a-time-for-variable-replication)
  + [Client->Server Replication](#client-server-replication)
  + [Native Replication](#native-replication)
  + [Replication Only When Necessary](#replication-only-when-necessary)
  + [Special Replication Variables](#special-replication-variables)
  + [Variable Replication Examples](#variable-replication-examples)
    - [In PlayerPawn](#in-playerpawn)

## Overview

Variables are one of two types of data that can be sent through replication statements, (the other being functions.) Here, we'll be discussing how data is replicated from one Unreal instance to another. There's a lot of little things that serve to complicate the process a bit more than may be expected at first.Variables are replicated to keep the other machine updated about changes on the local machine. In most cases, this means the Unreal server replicates variables to the client to tell it about changed information. If the velocity of a player changes, it needs to replicate it to the client so that the client can properly simulate the behavior of this player for the time inbetween two network updates.This document is part of the [NetworkingTome](https://udn.epicgames.com/Two/NetworkingTome).

## Reliability of Variable Data

The simple answer, is that variables are always reliable. When an actor's variables are replicated, the retirement associated with the variable for that object gets a copy of the outgoing packetid. If a negative acknowledgement comes in for that packet, then the variables associated with that packetid are put in the channel's Dirty array. The next time the actor is replicated, it will add all of these variables if they weren't going to be replicated otherwise. So variable data is guaranteed to reach the other side, but it is not reliable in the sense that one must wait for update one before processing update two.

## Newly Relevant Actors (Spawning)

When an actor becomes relevant to a client, a new `UActorChannel` is created on the connection, which causes an actor of the appropriate class to be spawned on the client, with the defaultproperties of the actor. If the server set variables immediately after the spawning of the actor, (before the relevancy checks), then assuming those variables meet the replication statements, they will be sent to the client as an addendum to the actor's data. Since replication is not done until the end of the current tick, you have a lot of time in which to set the variables for their initial replication with the actor itself. These variables that are set on the actor will be received on the other end, and the other end will then call *PostNetBeginPlay* (since *PostBeginPlay* is called before the actor's variables are read off the network, into memory.)In deciding what vars to replicate initially, the server will send any variables that differ from the defaultproperties. If the server has a different idea of the defaultproperties of an actor versus the client, then the server will only replicate the variable if it differs from the server's version. (By the same token, if a variable is changed in client-side code, the server will not know about it, and so the server will not replicate changed data.) You might think that changing an actor's defaultproperties on both the client and the server might solve the problem, but if an actor goes un-relevant, than simulated functions cannot be called on the actor, and when the actor becomes relevant again, the defaultproperties on the server and the client will be different. In general, don't change the defaultproperties of a variable unless the variable has no networking properties.As an example of the bad things that can happen, an Unreal Tournament mod had set both the `Mesh` and `Default.Mesh` to the playerclass's mesh that the player had chosen. Players however, go in and out of scope, to save on network bandwidth. Normally they are only relevant when you can see them, and for about three seconds once they disappear from view. Let's say the player changed their playerclass at that point, after they had gone out of relevancy. Or say they changed their class at the start of the game while the round has not started and they are invisible, and thus not relevant. When they do become relevant to the client again, (say they turned a corner or the round just started and they are spawned and made visible,) the `Mesh == Default.Mesh`, and so the `Mesh` is never replicated. The skin however, was still replicated normally. To clients in the game, they saw the player as the original mesh, with a inappropriate skin that was intended for another model. Strange behavior that can easily be avoided by treading lightly on the default variables for network variables. In this case, the `Default.Mesh` was not needed for everything, and removing that assignment caused everything to work fine.

## A Time for Variable Replication

Replicated variables are only replicated at the end of each tick. That means that if you change the variable repeatedly during a loop, or some other block of code, only the final value will be replicated. If you change a variable many times during a tick, and change it back to its original value when the tick completes, then no variable change will have been seen, and no network bandwidth will have been spent.Of course, there is an exception to this. If you spawn a new actor on the server, you have until the end of the tick before the variables are replicated. However, if you call any replicated functions, those replicated functions get sent immediately, and in order for the other side to receive them, it must have an actor to operate on. So if the actor has not been replicated yet, Unreal will force-replicate the actor and it's variables when the first replicated function is called. At the end of the tick, it will then re-check the actor for what variables to send out.

## Client->Server Replication

Another quirk to be aware of is that client-server replication exists ONLY for your own PlayerController. That means that if you want a variable replicated from the client to the server, it needs to be done in your current PlayerController (or in one of the parent class definitions). Since client->server functions are executed for the PlayerController and everything owned by it, replicated functions can be used to get around this limitation. While many pawns will exist on the client as their locations and velocities are replicated to you, only your current pawn is possessed by you, and only that one will be able to replicate variables to the server. If one were able to replicate information about other actors to the server, the server would have a problem, as would it take client A's value for actor Z, or client B's. Since there's nothing to distinguish them, the server only allows pawn variable replication to the server.

## Native Replication

Some base classes with frequently replicated data use native (C++) replication instead of script replication. You can recognize these classes by the `nativereplication` keyword in their class definition. These classes ignore the script conditions and replicate properties based on the C++ GetOptimizedRepList() function instead. However, the UnrealScript? replication block is still required to list all properties that could be replicated so the compiler can mark them as such, which is required for the properties to be sent correctly.

## Replication Only When Necessary

Further optimizations exist for variable replications as well. A variable will only be replicated to the client if the server thinks the client has the incorrect version compared to the server's latest version. When the server goes to replicate data, it compares the current value against the value that was last sent out, stored in the Recent array. If this is the first time being replicated, the code checks the current value against the value in the default properties of the actor. So the server will send out a changed variable regardless of what is on the client. If a value is changed in a simulated function that is run on both the client and the server, the server will not know about the client's value, and will still replicate it's own value. If this variable can guaranteed to be changed on both the client and server in all cases, then you could remove the replication conditions on this value. If this actor goes in and out of relevancy, then when it becomes relevant, it will be initialized on the client to the defaultproperties, as mentioned earlier. If this is incorrect, and you have no replication values, it will stay incorrect. One can use the `bNetInitial` variable to replicate something when the actor is first relevant, and then rely upon simulated functions executing on both the server and client to change the value from then on. The variable `bNetInitial`, and it's friends, is discussed next.

## Special Replication Variables

When writing replication conditionals, there are a few helpful variables which you can use in evaluating whether a function/variable should be replicated. These variables are defined in actor, and are:

bNetInitial
:   true if this is the first time this actor is being replicated across the network. Useful for variables that differ from the defaultproperties, yet will not change over the life of the actor.

bNetOwner
:   true if the player we are replicating to owns this actor directly.

bNetRelevant
:   Actor is currently relevant. Only valid server side.

bDemoRecording bClientDemoRecording bRepClientDemo bClientDemoNetFunc bDemoOwner
:   used for demo recording purposes.

## Variable Replication Examples

Now would probably be a good time to go through some important examples of replication and how it is used with variables, to give you a better idea of how things work, and to help give examples for your own adventures in coding.Let's take a few examples, and describe exactly what they do. We'll start off with the easy ones, and gradually work our way up in complexity. The following examples are all taken from Actor, unless specified otherwise.*Note:* these examples actually come from Unreal Tournament, the actual code is not relevant anymore. However the examples below are still useful to understand variable replication.

### In PlayerPawn

```

reliable if ( Role < ROLE_Authority ) Password, bReadyToPlay;
```

This here shows where your Password is sent to the server, when trying to join passworded servers, or to log in as an admin to that server. The server needs your password in order to validate it, and this code sends it to the server. Let's evaluate this check both on the server and on the client.

Server
:   On the server, `Role == ROLE_Authority`. Looking at the conditional, it can easily be shown to be false, and so the Password is not replicated server-side. This means that the server does not send the Password to the other end of the connection.

Client
:   Since on the client, the `Role` is not `ROLE_Authority` (remember it's only Authority on the server itself), this replication check evaluations to true on the client. And since variable replication only works in your current PlayerPawn, it will be sent to the server for yourself alone. (It makes sense not to send other's passwords, doesn't it? ;)

This also shows how `bReadyToPlay`, which is used in Tournament style games, where everyone has to click to start the game. Note that this is only sent for yourself, since the client can only replicate variables to the server if they are part of it's own playerpawn actor.

```

unreliable if( Role == ROLE_Authority ) Owner, Role, RemoteRole;
```

This ensures that the owner of an object is always replicated to the client. Remember that the owner's variables themselves are not replicated, (because there is no recursive replication,) but the actor itself is. This means that simple comparisons `if (PlayerPawn? = Owner) will work fine because the reference to the =Owner` is replicated to the client. Remember that the unreliable versus reliable makes no difference in UT, as they are both treated equivilently. They may have had an effect at some point during the Unreal 1 days, but they no longer play a factor in development. Don't let that confuse you.Replicating `Role` and `RemoteRole` may seem strange at first, since they should be reversed on the client. However, there's native code that causes that switch to be made. On the client, it will ensure that those two variables are reversed, so that `RemoteRole` is `ROLE_Authority`. You may wonder why they are even replicated in the first place. While the client never has any direct use for these variables in the code, there is one easy-to-overlook place where they are vitally important: Replication Statements. When the client is evaluating whether it needs to replicate a certain function call to the server, or a playerpawn's variable to the server, the client needs accurate copies of what `Role` and `RemoteRole` are. Without those, it would be unable to make the necessary decisions on what to send to the server. And since the server checks the validity of the replication data sent to the server with `Role/RemoteRole`, the client needs the latest copy in order to successfully replicate that data.

```

unreliable if( bNetOwner && Role == ROLE_Authority ) bNetOwner, Inventory;
```

Inventory is the head of the linked list that lists the entire Inventory for the Actor (usually only utilized with `Pawn`). We want the inventory to be replicated to the client, so that he knows what Inventory he has, to display on his HUD, and stuff (makes sense, right?). Simply replicating the head of a linked list (where each object points to the next in the list) is not enough however. Each actor must itself be relevant (satisfied by the criterion that it must be owned by the current playerpawn), and each link itself must be replicated. And since Inventory subclass Actor somewhere in the chain, Inventory also has a replicated Inventory variable. And that's how you are able to see your Inventory client-side. And since I don't need to know the full Inventory list of what every other player in the game has (the current weapon and the shieldbelt effect are transferred via other means), the Inventory will only be replicated if the client is the owner.The other variable in the above replication statement is bNetOwner. Since this is set natively on both the client and server, this variable does not need to be replicated. It could be argued that it adds a tiny amount to bandwidth, but its effect is probably negligible. Perhaps it will be removed in a future patch.

```

unreliable if( DrawType == DT_Mesh && Role == ROLE_Authority )
    Mesh, PrePivot, bMeshEnviroMap, Skin, MultiSkins, Fatness, AmbientGlow,
    ScaleGlow, bUnlit;
```

Here we see that all these mesh-specific variables are ONLY replicated if this actor is currently being displayed as a mesh. If it's a sprite, or a brush, or even no drawtype at all, there is no reason to send these variables.Now let's get into some of the more complex variable replication statements...

```

unreliable if( RemoteRole == ROLE_SimulatedProxy ) Base;
```

Here we see a slightly more complex replication statement, that does not involve `Role == ROLE_Authority`. Here we see that the current `Base` (set via *SetBase*) is only replicated if the actor is set to be a simulated proxy. If you set the actor to a `DumbProxy`, you'll see no `Base` change clientside, and instead will get the jerky `Location` updates that the server sends to you, (more on this later). So if you are using *SetBase*, make sure it's a simulated proxy, or if it's not a simulated proxy, use something other than *SetBase*. Or if you need both *SetBase* and a simulated proxy, the Base will not be replicated for you. You'll have to work out some other mechanism to do that, probably a simulated function that sets the base, so it is run on the client, (more on this later, too.) You might still have troubles when the actor gets its simulated function called while the actor was not relevant. This results in the simulated function never being called clientside, and then when the actor does finally become relevant, it's as if that function was never called (and the base isn't set), which will result in those things affectionately referred to as 'bugs.' You can make the actor being attached (and what it's being attached to) `bAlwaysRelevant` so that the simulated functions will always be called, but that might be a bit too harsh on network bandwidth.

```

unreliable if( RemoteRole == ROLE_SimulatedProxy && Physics == PHYS_Rotating
    && bNetInitial )
    bFixedRotationDir, bRotateToDesired, RotationRate, DesiredRotation;
```

This one is still relatively easy, but it's getting more complex. Here we have similar logic to what was seen above, with the server only sending these variables to the client if the client is a simulated proxy. However, since all these variables apply ONLY to `PHYS_Rotating`, there is no need to replicate these variables to the client if the client is not using `PHYS_Rotating`. And finally, a very important clause at the end is the `bNetInitial` one. This states that these variables will only be replicated to the client when it is being replicated for the first time.

```

unreliable if( bSimFall || (RemoteRole == ROLE_SimulatedProxy && bNetInitial
    && !bSimulatedPawn) )
    Physics, Acceleration, bBounce;
```

Here we have some of the interesting variables replicated. We see that if the `bSimFall` is set to true, it will replicate the `Physics` to the client. This is used when tossing weapons from your inventory. When they are tossed, they require a `Physics` change from `PHYS_None` while sitting in your Inventory to `PHYS_Falling` as they fly through the air. They then get set back to `PHYS_None` when they land on the ground. All these `Physics` changes are accomplished by setting `bSimFall` at the key points during the TournamentWeapon's life. It is set to true when it is thrown from the inventory, to capture the change, and left on until it hits the ground, where it changes `Physics` again. After it finally hits and has its physics reset, `bSimFall` is set to false so no further `Physics` changes occur. Looking at the second half of the statement, we see that the `Physics` is replicated ONLY if it's a simulated proxy, it's the first time this actor is being replicated over the internet, AND it's not a simulated pawn. The `bSimulatedPawn` variable is set to true if it's a Pawn with a `RemoteRole` of `ROLE_SimulatedProxy` (who would have thought? :) This means any changes to the `Physics` of a simulated proxy non-pawn actor before it is replicated will be replicated to the client. The `Physics` are never replicated for pawns. Rather, the code for their physics is hard-wired into the code to cause them to be pushed to the ground. Basically, when a pawn jumps, the server sets his vertical velocity so that he travels upwards. That Velocity is then replicated to the client (described below). The client then checks if the pawn is a player (eg: a bot or a playerpawn), that they are currently unable to fly (set via the Pawn's `bCanFly` variable), and that they are not in a water zone (since that involves different gravities and physics). So in fact, the `Physics` for a pawn is never replicated to the client, it only appears to do so. If you are attempting to create alternate physics with the playerpawn, you will need to ensure that you set `bCanFly` to true so that the native code does not enforce the falling Physics upon the player when he's on the wall or in the air. You must then implement the alternate means of transportation yourself.

```

unreliable if( !bCarriedItem && (bNetInitial || bSimulatedPawn
    || RemoteRole < ROLE_SimulatedProxy) && Role == ROLE_Authority )
    Location;
```

Here we see another important variable, `Location`, and it's replication. We see that it is not replicated for carried items. This is useful in the case of `Inventory`. When a player is carrying it, there's no reason its location should be replicated, since it isn't used for anything. replicating a player's entire inventory would be quite the strain on network bandwidth. Let's look at the next section of the statement. The location is replicated if this is the first time the actor is being replicated (assuming the other parts of the conditional are true). This is very useful, since all pawns will be spawned in different locations when you enter the game, and rockets will need their start locations set when they spawn out of a rocket launcher, etc. The location is also sent if this is a `bSimulatedPawn`. This helps correct any errors that may occur in replicating pawns. Since a pawn can change direction, and a client may not always know about it (due to lag, etc), this location resetting is the only way in which the locational updates can be 'corrected'. Note that this is not used to correct your own location when you experience lag. When that happens, you are an `AutonomousProxy`, and functions specific to PlayerPawn handle that (namely `ClientAdjustPosition`). For example, `PHYS_Walking` is not like `PHYS_Projectile`, where the position can be predicted with great accuracy. `PHYS_Walking` just means "keep them attached to the ground", basically, The client's only updates (without location) would have been their velocity, which can easily lead to errors in the player's movements over any significant amount of time. This location is used as a correcting factor, making sure the client's view does not stray too far from where he expects the player to be, while at the same time keeping the velocity's replication so he can be predicted inbetween server updates. The other option for allowing the `Location` to replicate is that of where the `RemoteRole` is less than a `ROLE_SimulatedProxy`, namely, a `ROLE_DumbProxy`, since the `ROLE_None` prevents relevancy in the first place. `DumbProxies` get periodic updates from the server every few ticks, and would create a jumpy effect in netplay. It was the cause of a jerky puck in the hockey mod I attempted a while ago, although I knew nowhere near enough to fix it at the time. A `SimulatedProxy` would not get sent `Location` updates, since it would be predicted through the use of the `Velocity` and the current Physics. Since `DumbProxies` aren't simulated client-side to achieve smoothness, they only get the `Location` updates. I'm going to clear this all up after the examples of the various replicated variables.

```

unreliable if( !bCarriedItem && (DrawType == DT_Mesh || DrawType == DT_Brush)
    && (bNetInitial || bSimulatedPawn || RemoteRole < ROLE_SimulatedProxy)
    && Role == ROLE_Authority )
    Rotation;
```

Here we see another important variable, `Rotation`. This also has the same `!bCarriedItem` clause, for the same reasons as described above. The rotation is also only replicated if this actor is a mesh or a brush. Since sprites always face the player, replicating their rotation is useless. The `bNetInitial` also causes the rotation to be replicated the first time through, (again, assuming if the other conditions are true,) since rockets need to be facing in the right direction when it has them flying through the air. Their velocity determines their direction of movement, but the direction they are facing which is equally important, is determined by their rotation. The rotation is replicated if they are a simulated pawn (every playerpawn and bot in the level except your own self). This is so you can see what direction the other people are facing. The `ViewRotation` (which determines where the client is looking), is sent to the server via *ServerMove*, where it is translated into a rotation. it is this rotation that is then replicated to the clients. And finally, if it is a `DumbProxy` (the only valid one less than `SimulatedProxy`), it also gets the rotation updates. Rotation updates do not need any interpolating between updates like location does. Location lag is much more noticeable when the player is moving quickly, but you never really notice `Rotation` lag. Besides, there is no real way to predict or forecast rotation. It depends entirely upon the other user's mouse.

```

unreliable if( bSimFall || ((RemoteRole == ROLE_SimulatedProxy
    && (bNetInitial || bSimulatedPawn)) || bIsMover) )
    Velocity;
```

Here's one of the last important variables with a complex replication statement. The velocity is replicated if it has `bSimFall` set, (used when throwing weapons from your inventory). The `PHYS_Falling` alone isn't enough. It needs to know exactly what it's initial velocity is when it is launched from the pawn. And no, `bNetInitial` will not work here, since it's not the first time it's being replicated. It's existed as a weapon for quite some time. It's just for the initial velocity of when it's being thrown from the player that we want updates. Moving along, we see that `SimulatedProxies` get their `Velocities` replicated if it the first time on the replication channel, for newly spawned rockets, or for grenades, or shock projectiles, etc. `SimulatedProxies` also get their velocities replicated if they are a simulated pawn, as all the various pawns need their velocities replicated so that they can be predicated locally. And finally, movers get their velocities replicated, so that the client can accurately predict the mover's movement locally. In the early Unreal 1 days, mover's velocity was not replicated, and so the client got periodic update locations because it was a `DumbProxy`. This resulted in very jumpy movers in netplay, something that was fixed for Unreal 224+.

```

unreliable if( DrawType == DT_Mesh && ((RemoteRole <= ROLE_SimulatedProxy
    && (!bNetOwner || !bClientAnim)) || bDemoRecording) )
    AnimSequence, SimAnim, AnimMinRate, bAnimNotify;
```

There are a few more variables here, all of which relate to animation. These variables are only replicated if it is currently being drawn as a Mesh. If we are recording a demo, then the animations are always sent. Otherwise, it checks the somewhat confusing conditional. If the actor is a `DumbProxy`, and the player is not the owner of this object, and `bClientAnim` is not set, then it replicates the animation variables. In the case of weapons, you see those animations clientside, and so the animation variables do not need to be replicated from the server. That is because all TournamentWeapons have the `bClientAnim` set to true, indicating that their animations are handled clientside. If the animations are not handled clientside, and the actor is a dumb proxy, then it will send them from the server. Simulated proxies, which include pawns and rockets and other projectiles, are all simulated proxies, and so they do not receive animations from the server. Instead, the client animates them with its client-side prediction. In the case of pawns, this is handled internally in the engine (for another tutorial ;), and you need not worry about it.

