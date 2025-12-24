# Function Replication

*Document Summary: This explains what causes functions to run where, and how to tame it to your needs.**Document Changelog: Last updated by Michiel Hendriks, converted to an UDN document. Original author was Mike Lambert (UdnStaff?).*

* [Function Replication](#function-replication)
  + [Overview](#overview)
    - [A Time for Function Replication](#a-time-for-function-replication)
    - [Reliability of Functions](#reliability-of-functions)
      * [Reliable function calls](#reliable-function-calls)
      * [Unreliable function calls](#unreliable-function-calls)
      * [Semi-reliable function calls](#semi-reliable-function-calls)
  + [Function Replication, and Simulation](#function-replication-and-simulation)
    - [Rep/Sim Function Rules](#repsim-function-rules)
    - [Rep/Sim Function Rules Restatement](#repsim-function-rules-restatement)
    - [Rep/Sim Function Summary](#repsim-function-summary)
    - [Spawning Within Simulated Functions](#spawning-within-simulated-functions)
    - [Simulated States](#simulated-states)

## Overview

While in a singleplayer game, functions are always executed, networking throws another wrinkle into the matter. A function can either be execute on the local machine, replicated accross the network to be executed on the remote machine, or ignored altogether. The process of sending a function across the network to be executed is sometimes called remote procedure calls (RPC), but Unreal calls it function replication.Internally, the Unreal Engine uses a very simple system for its function stuff. It calls a function to determine if it can call an UnrealScript? function on that machine. If it can, it does, if it cannot, then it does not. That's all that simulation and replication entails, and the only additions to this system are the origin of UnrealScript? simulation, events, (which will be discussed later), and the function replication itself (much of which you know already.)This document is part of the [NetworkingTome](https://udn.epicgames.com/Two/NetworkingTome).

### A Time for Function Replication

Replicated functions are replicated immediately after they are called. So if you call two functions, they are inserted onto the outgoing network queue right then. So if you change a variable, and then call a function, that function is very likely going to reach the client before the replicated variable reaches the client. Since the variable won't be replicated until the end of the current tick, it will either be later in the current network packet, or in a later packet. Unless some out-of-ordering goes on, the client will receive and process them in the order sent, and the function will be called before the variable is received. So if you need a variable on the client for the execution of a function, make sure you pass that variable in to the function. Note that this will work only for simple datatypes, because any actors are replicated with an index into the packagemap for that actor, and so you're only replicating a reference to the actor as the argument to the function, not the actor itself.

### Reliability of Functions

Functions normally can be reliable or unreliable. Reliable functions are guaranteed to be processed in the same order that they were sent. Unreliable functions make no guarantees about reaching the other side, or even about being processed in the correct order. There is an inbetween that is useful for often-called functions that should not be processed out-of-order, but which don't care if any given function is dropped. These types are all discussed below.

#### Reliable function calls

Reliable functions should be used whenever you need guarantees of the function being executed on the remote machine. Although it is fine to have many reliable functiosn defined, they should be called sparingly. Within an actor, multiple reliable functions are guaranteed to be called on the remote machine in the same order that they were called on the local machine. To do this, any dropped packets containing reliable function calls will need to have the function call resent, and this will delay the execution of subsequently-called functions. So by over-using reliable function calls, you risk delaying the execution of functions that you really need executed, and clogging up bandwidth on packet-lossy conditions with the re-sending of these reliable function calls. If a connection's bandwidth is saturated, reliable functions are still sent out, which only worsens the saturation problem. As an example, reliable functions should be used when the player hits the 'feigndeath' key, since you want to make sure the server knows about that. Sending a reliable function for each click/unclick of the mouse is bad, since there's a high possibility that they will be pressing the key rapidly. (In fact, using unreliable functions for this is bad too, but that's not the point here.)

#### Unreliable function calls

To balance out reliable functions, there are unreliable functions which make no guarantees about ordering or reaching the other end of the connection. Unreliable functions are sent out if there is room on the connection, and ignored if there is no available bandwidth. It is important to remember that functions are replicated immediately, as they are called. This means that it is possible for a flurry of unreliable functions to saturate the network connection, leaving no room for the variable data to replicate, at the end of the level tick. Due to out-of-order packets and packet loss, unreliable functions reserve the right to be processed in any order on the other end of the connection, and/or not even run on the remote connection. Unreliable functions are used to play sounds on a given client. If the function to play a given sound for a PlayerController in *ClientPlaySound* does not make it through, it is better to just drop the sound than hog up the network forcing a resend of the information. A late sound is a wrong sound, and so it's better to not play the sound at all, and so it's better to not worry about ensuring that the *ClientPlaySound* is reliably replicated.

#### Semi-reliable function calls

Sometimes, you may want to ensure that functions are executed in the right order, but don't mind if they get dropped. Here is an example. Due to the differences in where a client thinks he moves, and where the server thinks he moves, the server sends unreliable *ClientAdjustPosition* calls to the client which update the local client's information about where the player is. If any one of these is dropped, subsequent *ClientAdjustPositions* will make up for the error. However, Unreal should not process these out of order, because then the player's pawn will appear to jump around more than is necessary. This same logic applies when the client sends updates to the server via *ServerMove* about their current `bFire`, `bJump`, `ViewRotation`, etc. Older *ServerMoves* should not be processed after the most recent data has been processed. In these cases, it is much better to simply discard old data to emulate a lossy-but-in-order sequence of function calls. To implement this, the UnrealScript? code manually passes around a `TimeStamp` value in each function, which is calculated from `Level.TimeSeconds`. Using any sort of `TimeStamp` (and storing the current value in your actor to disregard old function calls) will work fine, but it's usually easiest to replicate the `Level.TimeSeconds` float, since you can get fine-grained differences between two times, without having to worry about overflowing the value of the integer or whatnot. (Although, at some point you will have to worry about the float value increasing enough to lose the lower digits which help differentiate two closely-spaced ticks.)

## Function Replication, and Simulation

### Rep/Sim Function Rules

I will first present the basic simple rules to determine if a client or server is able to execute the function locally. The following conditions will determine whether that happens. Again, if a condition matches, then the checking stops there, and it executes locally depending upon the resulting clause of that condition.

1. If it is a static function, it can be called on that machine.
2. If we're on a standalone server, it can be called on that machine.
3. If it's not a replicated function, then go to step 10.   
    **(The rest apply ONLY to replicated functions, per condition three.)**
4. If we are the server, and there is no parent PlayerController to this actor, (at any point in the parent hierarchy,) or if the player does not have a connection (listen servers for the player on the server,) then it is executed locally.
5. If the replication condition is not met for the current machine, (meaning that it was replicated to us, or that it is not a valid replication statement), then go to step 10.   
    **(The rest apply ONLY to replicated functions where the replication condition is met, and it is a valid function to replicate.)**
6. If it is an unreliable function, and the connection (server-client or client-server) is saturated, then 'pretend' it was executed remotely, (eg: do not execute it locally.)
7. Replicate the function, and then do not execute it locally.   
    **This last step is only used if it is called upon by the above steps.**
8. If we are on the server, then it can be called.
9. If we are on the client as an Autonomous Proxy, it can be called locally.
10. If we are on the client as a Dumb Proxy or Simulated Proxy (NOT an Autonomous Proxy,) and we are a simulated function, then it can be called locally.

While this may seem complex, it accurately describes in every detail how Unreal does it's function handling, and RPC (remote procedure call) nature. Hopefully, in the next paragraph or two, I'll be able to simplify it into a few simple rules.

### Rep/Sim Function Rules Restatement

In order for a function to be replicated to the other end of the connection, it must be all of the following:

1. Owned by a network PlayerController at some point it it's parent hierarchy.
2. It must be a reliable function, or an unreliable function with available bandwidth.

In order for that replicated function to actually be executed on the other end of the machine, it must pass rule number 10. Additionally, if we are on the client, it must meet any of the following rules.

1. A static function.
2. A simulated function.
3. In an actor with an AutonomousProxy? Role (a local PlayerController or local GuidedWarhead? on the client.)

The above rules need to be passed for ANY function that is executed on the client, whether it is through simulation or replication.

### Rep/Sim Function Summary

With those rules in mind, I'll try to summarize the whole situation below.On a server, every function is executed, unless it is a (client-server) replicated function and meets the checks above. So you can be assured of all your functions running on the server, unless you specifically tell them not to.On the client, every function has to originate from a 'source'. A source can be a server-client replicated function, an exec function, or an event. Events, while not covered previously, are quite simple. An event is any function that is called from native code. Events happen both on the server and on the client. The server does not directly tell the client to execute the event, but the client knows to execute the event based upon the game state (colliding actors, hitting a wall, a timer event, ticking of the game state, etc). If that event is simulated, then it can also serve as a 'source' of clientside function calls. A source can call any function it wishes, assuming it meets the client-side execution conditions, which can then call any...and so on.What happens if a function is called, but doesn't meet the conditions for execution, either because it was replicated to the other end, or because it does not meet the conditions for running client-side. In that case, it is as if the function never ran in the first place. The return value of such a function is `0`, `""`, or `None`, depending upon the context. Any out parameters defined by the function are passed back exactly as they were entered. Relying on the result of a function that is never executed is the source of many accessed nones that appear only on the client. Exec functions (functions that can be bound to keystrokes) naturally evaluate on the client. Again, remember to make it simulated, (unless you are in an Autonomous Proxy, like a PlayerController subclass.) In some cases, you may want to have it replicated to the server, as in the case of a Server-Administrator command (there are plenty of these defined in PlayerController). Exec functions can be replicated to the server, the same as any other function can.

### Spawning Within Simulated Functions

There are other interesting hidden behaviors that may not be immediately apparent. For example, because of the requirements that an actor be owned by a PlayerController at some point in its parent hierarchy, a function can only be replicated to a single player in the game. (No, making a player owned by another player will not work. ;) Multicast function replication does not exist. You can try to get this behavior using simulated functions, but no data can be passed between the server and the client, (since they both originate on their local machine, and exist only on that local machine.) Or you can use replicated variables, which can and are replicated to all players in the game, assuming they are relevant to them.If a spawn is performed in a simulated function (simulated functions are explained later), then multiple copies of the actor are spawned: the server, and each of the clients that the simulated function was run on. The server's version is normally then replicated to the client, so the client would see two versions. This would create strange behavior as the two became out of sync, and the client-spawned one could easily be mistaken for the 'official one' that for some reason, isn't having it's variables replicated.If you need to do a spawn in simulated code (there are many valid reasons, like spawning effects clientside, etc), then you must account for this. If you are attempting to make clientside effects, then make sure you set the `RemoteRole` to `ROLE_None` immediately afterwards. Since relevancy is only checked between ticks, this will ensure that when that check does come around, it will not be relevant, and thus not replicated. That way, the server and the client will each have their local copy of the effects that run their course and then destroy themself. This is not useful for permanent effects, since simulated functions are not run on ALL clients, only clients where the actor containing the simulated function is relevant. That means that if the simulated function didn't run (because it's actor was not relevant at the time), then the effect will not be visible when you come into view of that effect. That is why it should only be used for temporary effects that run their course and then destroy themselves.If however, you are spawning something that is intended to be permanent, or needs data replicated from the server, (like a crosshair dot), then you **should not** spawn it on the client. Usually, you can accomplish this with a '`If (Level.NetMode = NM_Client)`' check before you perform the spawn. This way, the spawned actor will then become relevant (assuming the conditions match), and it's variables will be replicated to the clients. If a client-side actor had been spawned, then there would be two actors, one of which would just sit there without information from the server

### Simulated States

Another, many times overlooked feature is that of simulated states. You probably have already seen state code, code that exists outside of functions, but in states, usually prefixed with labels. This code, when in a regular state, is executed on the server alone. But by prefixing the `state statename` with `simulated`, you can make the state code itself simulated. So the revised state declaration would be `simulated state statename`. Just beware that state changes are NOT replicated or sent to the client by default. However, if a *gotostate* is executed in a function that is run on the client (either through replication or simulation), then the client will know of the new state. PlayerController's inherent simulation allows all it's functions to be able to control the state, but other classes would need to have simulated functions that are executed from a simulated source and chain of function calls in order to know of the state change.

