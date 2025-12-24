# Artificial Intelligence Reference

*Last updated by Chris Linder (DemiurgeStudios?) for creation. Original author was Chris Linder (DemiurgeStudios?) Please feel free to contact me with questions or comments at [chris@demiurgestudios.com](mailto:chris@demiurgestudios.com).*

* [Artificial Intelligence Reference](#artificial-intelligence-reference)
  + [Introduction](#introduction)
  + [Hints](#hints)
    - [Use "showdebug"](#use-showdebug)
    - [Use "F5"](#use-f5)
    - [Use the UnrealScript Debugger](#use-the-unrealscript-debugger)
  + [How to Control a Pawn](#how-to-control-a-pawn)
  + [Controller and the Great Functions You Need](#controller-and-the-great-functions-you-need)
    - [Non-Latent Functions](#non-latent-functions)
      * [FindPathTo](#findpathto)
      * [FindPathToward](#findpathtoward)
      * [FindRandomDest](#findrandomdest)
      * [PointReachable](#pointreachable)
      * [ActorReachable](#actorreachable)
      * [LineOfSightTo](#lineofsightto)
      * [CanSee](#cansee)
      * [FindPathTowardNearest](#findpathtowardnearest)
      * [FindPathToIntercept](#findpathtointercept)
    - [Latent Functions](#latent-functions)
      * [MoveTo](#moveto)
      * [MoveToward](#movetoward)
      * [FinishRotation](#finishrotation)
    - [Events and Notifies](#events-and-notifies)
      * [SeePlayer](#seeplayer)
      * [SeeMonster](#seemonster)
      * [EnemyNotVisible](#enemynotvisible)
      * [HearNoise](#hearnoise)
      * [NotifyTakeHit](#notifytakehit)
      * [NotifyAddInventory](#notifyaddinventory)
      * [PrepareForMove](#prepareformove)
  + [AIController](#aicontroller)
    - [Scripting](#scripting)
    - [Movement](#movement)
      * [bAdjustFromWalls](#b-adjustfromwalls)
      * [GetFacingDirection](#getfacingdirection)
    - [Mover Functionality](#mover-functionality)
    - [Misc](#misc)
      * [Startle](#startle)
      * [DisplayDebug](#displaydebug)
  + [ScriptedController](#scriptedcontroller)
    - [Control Flow](#control-flow)
      * [Entry Point](#entry-point)
      * [Begin](#begin)
      * [SetMoveTarget Step](#setmovetarget-step)
      * [MoveToward Step](#movetoward-step)
      * [Am I There Yet?](#am-i-there-yet)
      * [Other Cases](#other-cases)
  + [AIScript](#aiscript)
    - [How AIScripts are Used](#how-aiscripts-are-used)
  + [ScriptedSequence](#scriptedsequence)
  + [Dynamic AI - Bot as an Example](#dynamic-ai-bot-as-an-example)
  + [Related Documents](#related-documents)

## Introduction

This document will go over AI basics in the Unreal engine. It will cover the classes involved with AI as well as useful UnrealScript functions and how to use these function to create both scripted and dynamic AI. This document will also go over the control flow in [ScriptedController](#scriptedcontroller) as an example of how to use movement functions in latent code. This document will also go over how to use states and events to control behavior using [Bot](#dynamic-ai-bot-as-an-example-) as an example.

## Hints

These are a few hints that might help you create your own AI or understand an existing AI. I used these techniques extensively to create this document.

### Use "showdebug"

This is an extremely useful console command that displays a lot of information about the current *Viewtarget*. It will tell you the state, the *MoveTarget*, the amount of health of the pawn, its animation data, current frame, and many other things. At first this many not seem useful because your player is the current *ViewTarget* but it is useful when you press "F5".

### Use "F5"

This will cycle the *ViewTarget* between all pawns in the game. This will put a camera behind an AI you want to watch and see what it is doing. This command is very useful when used with "showdebug".

### Use the UnrealScript Debugger

The [UnrealScript Debugger](UnrealScriptDebugger.md) is a great help when trying to figure out the flow of code in an AI. This will allow you to set break points anywhere in script including latent code. You can then step though the code and see what is happening. The debugger also lets you watch variables, view the call stack, and perform many other debugging actions.

## How to Control a Pawn

Pawns can be controlled by two types of *Controllers*, *PlayerControllers* and *AIControllers*. Or they can just sit there but that is sort of dull and we won't talk about that. We will also not talk about the *PlayerController* case in this document. Instead we will focus on AI controlling a pawn and how *AIControllers* can be used.AI can be divided basically into two types; AI that does a predefined script of actions, and AI that reacts dynamically to its environment. There is clearly a fuzzy boarder between these two but the distinction is useful at least for this document. It is important to note that there is not a class hierarchy branch for these two types of AI. The same class (*Bot* for example) will often be capable of doing both type; what matters is how you set up your controller and pawn.If you want an AI to do a script of actions you should use an [AIScript](#aiscript) of some sort which you place in Unrealed and link to a specific pawn or set of pawns. If you want an AI that will respond to its environment and make choices and not need to be configured in Unrealed, you should set the *ControllerClass* in defaultproperties of the pawn you want to control. The *ControllerClass* should be some subclass of *AIController* but not necessarily a direct subclass. [Bot](#dynamic-ai-bot-as-an-example-) is an example of such a controller and it is the default *ControllerClass* for all *UnrealPawns*.

## Controller and the Great Functions You Need

*Controller* is the base class for actors that control pawns. This class is implemented in *Controler.uc* and *UnController.cpp*. I will be talking mainly about the script interface and the native functions that are accessible from script. These functions are very useful for writing both scripted AI and dynamic AI.

### Non-Latent Functions

#### FindPathTo

Actor FindPathTo(vector aPoint)This function returns the path node that is next in the sequence of path nodes that will lead to *aPoint*. Given that this function only returns actors, if can not be used on the final leg of your journey to the given arbitrary point. This function will return the path node nearest to the given point on the last step of the journey. Consider using [PointReachable](#pointreachable) to see if you can get to the point and then simply call [MoveTo](#moveto). Beware of calling FindPathTo too often because it is very computational expensive given that is re-computes the entire path every time you call it even if the path has not changed. In most cases though, you will need to call this function for every path node you encounter on the way to your destination. After you call this function is it traditional to call [MoveToward](#movetoward) to actually move towards to the given actor.

#### FindPathToward

Actor FindPathToward(actor anActor, optional bool bWeightDetours)This function is much like [FindPathTo](#findpathto) but it gives you a path to a given actor. Consequently it does not have [FindPathTo](#findpathto)'s problem of not being useful for the last part of the journey. If the target actor is not a path node this function will return that all the nodes up that actor and then return that actor. Sometimes this has undesired results; for example if the actor you want to reach is standing right next to a path node this function will take your pawn to the path node first, then the actor even if the actor is closer to your pawn than the path node. You can fix this by using the [ActorReachable](#actorreachable) function to limit the calls to this function as well as make your pawns behave more logically. Beware of calling FindPathToward too often because it is very computational expensive given that is re-computes the entire path every time you call it even if the path has not changed. In most cases though, you will need to call this function for every path node you encounter on the way to your destination. After you call this function is it traditional to call [MoveToward](#movetoward) to actually move towards to the given actor.

#### FindRandomDest

NavigationPoint FindRandomDest()This function returns a random NavigationPoint.

#### PointReachable

bool PointReachable(vector aPoint)This returns true if a direct path from your pawn to *aPoint* is traversable using the current locomotion method.

#### ActorReachable

bool ActorReachable(actor anActor)This returns true if a direct path from your pawn to *anActor* is traversable using the current locomotion method.

#### LineOfSightTo

bool LineOfSightTo(actor Other)LineOfSightTo returns true if controller's pawn can see *Other*. Checks line to center of other actor, and possibly to head or box edges depending on distance

#### CanSee

bool CanSee(Pawn Other)CanSee returns true if [LineOfSightTo](#lineofsightto) object and it is within creature's peripheral vision.

#### FindPathTowardNearest

Actor FindPathTowardNearest(class GoalClass, optional bool bWeightDetours)This function does not appear to work.

#### FindPathToIntercept

Actor FindPathToIntercept(Pawn P, Actor RouteGoal, optional bool bWeightDetours)This function appears to do that same thing as [FindPathToward](#findpathtoward).

### Latent Functions

Latent functions stop the flow of latent state code until they "return". Every latent function in script has two latent functions in C++. These functions are execFunctionName() and execPollFunctionName(). execFunctionName() is called when the function is first called from script in latent state code. Every subsequent tick, execPollFunctionName() is called until this function sets GetStateFrame()->LatentAction = 0. This will cause the latent function to "return".

#### MoveTo

latent function MoveTo( vector NewDestination, optional Actor ViewFocus, optional bool bShouldWalk)First, MoveTo sets up the controller and the pawn to move. *Destination* is set based on *NewDestination*, walking is set if bShouldWalk is true, and *Focus* of the controller is set to *ViewFocus* if it given and the *Destination* otherwise. The *MoveTimer* is also set by calling Pawn->setMoveTimer(...) based on the distance to the destintation. This timer is decremented in performPhysics(...) and when it runs out MoveTo will return. This is so that if the pawn gets caught on something or is knocked off the path by something and can not reach its destination, the latent code does not hang here forever. Once all the move info is set up, Pawn->moveToward(...) is called which does the actual moving of the pawn. Pawn->MoveToward(...) is also called every tick from execPollMoveTo(...) until MoveTo returns. MoveTo will return when the either the pawn reaches the destination or the destination is determined to be unreachable or when the *MoveTimer* runs out.

#### MoveToward

latent function MoveToward(actor NewTarget, optional Actor ViewFocus, optional float DestinationOffset, optional bool bUseStrafing, optional bool bShouldWalk)MoveToward is very similar to [MoveTo](#moveto) but it moves towards an Actor, not a point. MoveToward also special cases moving towards *NavigationPoints* so that the pawn cuts corners and travels more logically on a set of path nodes. *MoveTimer* is additionally useful in MoveToward because the destination can be a moving actor that can move out of view. When *MoveTimer* runs out MoveToward returns control to the latent state code which can find a new path if the target is no longer visible. *MoveTimer* is set to a short time when the target is a Pawn for this reason. Pawn->moveToward(...) is called when the actual destination is calculated and all the other movement information is set up. Pawn->MoveToward(...) is also called every tick from execPollMoveToward(...) until MoveToward returns. MoveToward will return when the either the pawn reaches the destination or the destination is determined to be unreachable or when the *MoveTimer* runs out. Pawn->MoveToward is called every tick from PollMoveToward.

#### FinishRotation

latent function FinishRotation()This function will return when the yaw of the pawn is within 2000 unreal rotation units of the yaw of *DesiredRotation*. This function as well as the corresponding execPollFinishRotation(...) do nothing to effect the rotation of the pawn, this is handled in physicsRotation(...).

### Events and Notifies

#### SeePlayer

event SeePlayer( Pawn Seen )SeePlayer is called whenever this controller's pawn can see another "player". This will be every tick when a player is in view. It worth noting that "player" is any controller with *bIsPlayer* set to true (Bot for example), not just human players. In most cases once you receive this event you will disable SeepPlayer by calling Disable(`SeePlayer') or switching to a state that ignores SeePlayer.

#### SeeMonster

event SeeMonster( Pawn Seen )This is just like [SeePlayer](#seeplayer) but with monsters (those controllers with *bIsPlayer* set to false).

#### EnemyNotVisible

event EnemyNotVisible()This event is called whenever the *Enemy* is not visible. Like [SeePlayer](#seeplayer) this will be called very frequently unless you switch to a state that ignores EnemyNotVisible or call Disable(`EnemyNotVisible').

#### HearNoise

event HearNoise( float Loudness, Actor NoiseMaker)HearNoise is called when the controller's pawn hears a noise.

#### NotifyTakeHit

function NotifyTakeHit(pawn InstigatedBy, vector HitLocation, int Damage, class damageType, vector Momentum)NotifyTakeHit is called when *TakeDamage(...)* is called on this controller's pawn. Generally this occurs when the pawn has been shot.

#### NotifyAddInventory

function NotifyAddInventory(inventory NewItem)This function is called when *AddInventory(...)* is called on the controller's pawn.

#### PrepareForMove

event PrepareForMove(NavigationPoint Goal, ReachSpec Path)This event is called from C++ if the reachspec for the current movement does not support the pawn's current configuration. *PrepareForMove(...)* gives the pawn a change to prepare for the move by doing something special. What to do is up to you, however, because this function is not implemented. By default, the pawn will crouch when it hits an actual obstruction. However, Pawns with complex behaviors for setting up their smaller collision may want to call that behavior from here. *bPreparingMove* is set to true.

## AIController

AIController extends Controller. This class adds basic support for [AIScripts](#aiscript) as well as several useful AI functions. This class also includes game specific concepts, such as *Skill*, that I will not go over.

### Scripting

The scripting functionality of AIController is not extensive. There is a variable *MyScript* that contains a reference to the current [AIScript](#aiscript). This variable is none if there is no script. Trigger events are passed to this script by calling *TriggerScript(...)* when the controller is triggered.

### Movement

#### bAdjustFromWalls

When *bAdjustFromWalls* is true, the controller is given a chance to adjust around an obstacle and keep moving. The C++ AAIController::AdjustFromWall(...) function does the actual adjusting from a wall.

#### GetFacingDirection

int GetFacingDirection()This function returns the direction faced relative to movement direction. This means if the pawn is facing the direction it is running, this function will return 0 no matter which way the pawn is running. The function will return an int between 0 and 65535 in the standard unreal rotation scheme (0 = forward, 16384 = right, 32768 = back, 49152 = left).

### Mover Functionality

AIController has a few functions that deal with movers. These functions include *WaitForMover (Mover M)*, *MoverFinished()*, and *UnderLift(Mover M)* which set up the movement of the pawn to deal with movers properly and to use lifts and doors. These functions are called by Movers or NavigationPoints associated with Movers.

### Misc

#### Startle

Startle(Actor A)This function is called from the *AvoidMarker* class which is a type of trigger. Startle is not implemented in *AIController* but the idea of a startle function is useful. Consider implementing this function and maybe calling it more.

#### DisplayDebug

DisplayDebug(Canvas Canvas, out float YL, out float YPos)*DisplayDebug(...)* displays useful debug info on the HUD. This information includes such thing as the *MoveTarget*, *Destination*, *Focus*, *PendingMover*, and *RouteGoal*. *DisplayDebug(...)* will be called when *bShowDebugInfo* is true, which can be toggled by using the exec command "ShowDebug".

## ScriptedController

ScriptedController extends [AIController](#aicontroller) and adds the ability to get actions from a [ScriptedSequence](#scriptedsequence). To examine how ScriptedControllers work, we will look at the control flow when the pawn is being controlled by a script.

### Control Flow

This is an example of flow of execution when a ScriptedController is controlling a pawn with instructions from a [ScriptedSequence](#scriptedsequence) which is a type of [AIScript](#aiscript). For simplicity this example will only go over actions in the [ScriptedSequence](#scriptedsequence) that direct the movement.

#### Entry Point

Initially the ScriptedController does nothing. There is no code in any \*BeginPlay function that puts the controller on any sort of control path. The control over a pawn starts in the *TakeControlOf(Pawn aPawn)* function which is called by the [ScriptedSequence](#scriptedsequence) associated with this controller. This function possesses the given pawn so that it is under the control of this ScriptedController and then goes to state 'Scripting'. State 'Scripting' is where all the control of the pawn happens starting at the state label [Begin:](#begin).

#### Begin

At the Begin: label the next [action](ScriptedSequenceActions.md) is chosen from the [ScriptedSequence](#scriptedsequence) by calling *InitforNextAction()*. This function sets the *CurrentAction* which will be used to determine what to do next. A few things are also done to setup weapons and shooting. Next the Pawn is made ready to move by calling:

```

Pawn.SetMovementPhysics();
WaitForLanding();
```

#### SetMoveTarget Step

SetMoveTarget() is called next. This function first gets the ultimate goal of this move from the action itself. The function then asks if the goal is reachable by using the native function [ActorReachable](#actorreachable)(actor anActor). This function determines if the pawn can move directly towards the goal. If the goal is reachable, the *MoveTarget* of the ScriptedController is set to the goal. If not, [FindPathToward](#findpathtoward)(...) is called and *MoveTarget* is set to the result [FindPathToward](#findpathtoward)(...). The *Focus* is also set in this function. The pawn will turn towards the focus while moving towards *MoveTarget*. If there is a scripted focus point, the *Focus* will be set to that, otherwise, the Focus will be set to the *MoveTarget*.Once SetMoveTarget() is called MayShootTarget() is called which will set up the Pawn to shoot at something if it wants too.

#### MoveToward Step

Now [MoveToward](#movetoward)(MoveTarget, Focus,,,Pawn.bIsWalking) is called. This is a native latent function. This will move the pawn towards its reachable goal until it has reached the goal or the *MoveTimer* runs out while walking. This function will also return and stop movement if it has some sort of trouble reaching its goal like it got stuck above or below or the move target is no more or the move target is swimming and this pawn can't swim.

#### Am I There Yet?

Now the ScriptedController asks if the current *MoveTarget* is the ultimate goal and that the pawn successfully moved the current move target. If either of these are false, the ScriptedController starts again from the [SetMoveTarget Step](#setmovetarget-step). Otherwise *CompleteAction()* is called which increments the action and goes back to the [Begin:](#begin) tag.

#### Other Cases

As mentioned above this example on goes over the basics of movements. To investigate the other actions carried out by ScriptedController, I highly suggest using the [UnrealScript Debugger](UnrealScriptDebugger.md). This will allow you to step though the state code and easily see what is happening.

## AIScript

AIScript extends Keypoint and is not part of the controller hierarchy at all. This class is used to contain information that a controller will use to control its pawn. The [AIController](#aicontroller) has a reference to an AIScript and reads from this script to determine the pawn control; the AIScript does not actively exert any control over the controller or the pawn.

### How AIScripts are Used

In most cases AIScripts are placed in Unrealed and are associated with Pawns also placed in Unrealed. This is done be setting the *AIScriptTag* (In the AI category of properties) of the Pawn to be the same as the *Tag* (In the Events category pf properties) of the AIScript. The AIScript determines the class of the Controller for the pawn. The AIScript spawns the controller in the SpawnControllerFor(Pawn P) function and takes control of a pawn in the TakeOver(Pawn P) function. SpawnControllerFor(...) is called from PostBeginPlay() of the Pawn with the associated *AIScriptTag*. A single AIScript can be used for as many Pawns as you want.AIScripts can also be dynamically created and associated with a particular controller but you would need to subclass AIScript and provide and implementation of TakeOver(...) which is currently empty. (See *ScriptedSequence.uc* for an example of a TakeOver(...) function.)

## ScriptedSequence

ScriptedSequence extends [AIScript](#aiscript) and adds the ability to store a list of [Actions](ScriptedSequenceActions.md) which a [ScriptedController](#scriptedcontroller) can read from. When SpawnControllerFor(...) is called in a ScriptedSequence, it also calls TakeOver(...) so as soon as Pawn starts in a level and is associate with a ScriptedSequence, it will be controlled immediately by ScriptedController.Once a ScriptedController exists it can be assigned new ScriptedSequences with the the SetNewScript(ScriptedSequence NewScript) function in ScriptedController. Scripts can also be changed with the [ChangeScript](ScriptedSequenceActions.md#ChangeScript) action within the ScriptedSequence. This means that ScriptedSequences can not only be used to control multiple pawns but can also be used modularly and fit together to form more complex behaviors.For example you could have a ScriptedSequence for every area in a map and have controllers switch scripts as the pawn moves between areas. ScriptedSequences can also be used to temporarily control more complex AI. Any class that extends ScriptedSequences can simply call SetNewScript(...) and it will perform the script. When the script is over or when the [LeaveSequence](ScriptedSequenceActions.md#LeaveSequence) action is called the AI will resume its normal behavior.

## Dynamic AI - Bot as an Example

Dynamic AI can be done in many many ways. To narrow the scope of the general problem of dynamic game AI, I will use *Bot.uc* as an example and discus the ideas and theories of this method of dynamic AI. Basically, Bot uses different states to represent different behaviors and switches between the states by periodically calling a decision making function or receiving an event. States are very useful because they can ignore certain events and override functions and this provides a great deal of flexibility for creating different behaviors. States are also useful because they have latent code which as shown above in [ScriptedController](#scriptedcontroller) is a good way to direct pawns. Events are useful because they can interrupt the control flow of latent code and allow the controller to respond to immediately as opposed to waiting for a latent function to return.In *Bot.uc* control flow starts in *Restart()* which is called from *RestartPlayer(...)* in GameInfo (or some subclass of GameInfo like DeathMatch) on game start. *Restart()* calls *GotoState('Roaming','DoneRoaming')* which puts the AI in state *Roaming* at the tag *DoneRoaming*.At this point the *WaitForLanding()* is called which waits for the pawn to land and then *WhatToDoNext(...)* is called. *WhatToDoNext(...)* calls *ExecuteWhatToDoNext()* which is the main decision making function in Bot.*ExecuteWhatToDoNext()* makes decisions based on the status of the controller, the pawn, the squad, and the environment. Decisions take the form of calling functions like [Startle(...)](#startle) or *DoRetreat()*. Calling functions is preferred over directly making a call to *GotoState(...)* because states can override functions and therefore handle the situation differently.If nothing interrupts the controller, it will keep periodically calling *WhatToDoNext(...)* from different states and make decisions in this manner. Obviously this will not yield fast responses to a changing environment though. This is why Bot also makes use of events and notify functions to change its behavior quickly. We will briefly discuss [event SeePlayer(...)](#seeplayer) and [function NotifyTakeHit(...)](#notifytakehit).[event SeePlayer(...)](#seeplayer) is used to optionally set up enemy information based on the current *Enemy* and the *SeenPlayer* and then call *WhatToDoNext(...)*. By calling *WhatToDoNext(...)* on this event, that controller can immediately respond to the environment and figure out in a general way what it should be doing.In a similar way to [SeePlayer(...)](#seeplayer), [NotifyTakeHit(...)](#notifytakehit) will sometimes call *WhatToDoNext(...)* to quickly response to the environment in a general way. In some cases though, *WhatToDoNext(...)* will not be called because the state this function is overridden wants to handle the getting shot more specifically than just asking the general question of what should I be doing now. For example in state *Charging*, [NotifyTakeHit(...)](#notifytakehit) is used to take evasive maneuvers and still rush towards a given goal.And that is pretty much how Bot works on a high level. There are many more states and events than I mentioned and of course the decision making functions have many more complexities than I talked about but this is the general ideas of what is going on in Bot.

## Related Documents

These are documents on the content side of things.[AIControllers](AIControllers.md) - This document goes over all the types of AIControllers as well as how to set up AIControllers in Unrealed.[ScriptedSequenceTutorial](ScriptedSequenceTutorial.md) - This is a document about how to use ScriptedSequences.[ScriptedSequenceActions](ScriptedSequenceActions.md) - This document talks about the types of actions ScriptedSequences can do.

