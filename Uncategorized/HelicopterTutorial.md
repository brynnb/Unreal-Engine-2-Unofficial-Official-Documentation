# Helicopter Tutorial

*Create on 9/18/03 by Chris Linder (DemiurgeStudios?) for v2226.*
  
*Updated on 9/30/03 by Chris Linder (DemiurgeStudios?), first public release. Updated on 2004-12-22 by Michiel Hendriks, update for v3323.*

* [Helicopter Tutorial](HelicopterTutorial.md#helicopter-tutorial)
  + [Related Documents](HelicopterTutorial.md#related-documents)
  + [Introduction](HelicopterTutorial.md#introduction)
  + [Design Goals](HelicopterTutorial.md#design-goals)
  + [Accomplishing the Design Goals](HelicopterTutorial.md#accomplishing-the-design-goals)
    - [Getting Started](HelicopterTutorial.md#getting-started)
    - [Designing the Physics (Goal 1)](HelicopterTutorial.md#designing-the-physics-goal-1))
    - [Designing the Control Scheme (Goal 2)](HelicopterTutorial.md#designing-the-control-scheme-goal-2))
    - [Balancing the Difficulty (Goal 3)](HelicopterTutorial.md#balancing-the-difficulty-goal-3))
    - [Aiming (Goal 4)](HelicopterTutorial.md#aiming-goal-4))
  + [Debugging](HelicopterTutorial.md#debugging)
    - [Show Graph](HelicopterTutorial.md#show-graph)
    - [KDraw](HelicopterTutorial.md#kdraw)
    - [Defaultproperties are Tricky](HelicopterTutorial.md#defaultproperties-are-tricky)
  + [Installing the Helicopter Code](HelicopterTutorial.md#installing-the-helicopter-code)
    - [v3323 and up](HelicopterTutorial.md#v3323-and-up)
  + [Flying the Helicopter](HelicopterTutorial.md#flying-the-helicopter)
    - [Rotor](HelicopterTutorial.md#rotor)
    - [Movement](HelicopterTutorial.md#movement)
    - [Turning](HelicopterTutorial.md#turning)

## Related Documents

[SVehicleReference](SVehicleReference.md), [SVehicleCreation](SVehicleCreation.md), [SVehicleMayaMAXFix](https://udn.epicgames.com/Two/SVehicleMayaMAXFix), [KarmaReference](../Content%20Creation/Physics/KarmaReference.md)

## Introduction

This document is a tutorial on how to create a helicopter using the Karma *SVehicle* code. The goal of this document is not only to illustrate the construction of a helicopter but to generally outline how one might go about constructing any custom *SVehicle*. The document starts with design goals and then goes over how to accomplish these goals. It also provides general debugging tips relevant for any *SVehicle* creation. At the end of the document the resulting *SHelicopter* code is included along with installation instruction and an example map.

## Design Goals

1. Create a helicopter that flies based loosely on the principals that make real helicopters fly.
2. Design a control scheme for the helicopter that is logical and accessible.
3. Balance the helicopter such that newbies can fly it without crashing (much) but that advanced users will have a sufficiently complex system to master.
4. Ensure that it is not too difficult for the helicopter to keep its nose (weapons) pointed at a target.

## Accomplishing the Design Goals

### Getting Started

The first thing I needed to do was create my own *SVehicle* class (both in C++ and in UnrealScript) and make it so I could drop instances of my new class in the game. I did this by copying the [SCopter](SCopterReference.md) classes and doing a find and replace in the files changing "SCopter" to "SHelicopter". I created *SHelicopter.uc* from *SCopter.uc* (I needed to rename "struct native CopterState" to "struct native HelicopterState" in addition to the find and replace), *SHelicopter.cpp* from *SCopter.cpp*, and *CTLChopper.uc* from *COGChopper.uc*. I created all these in the *Vehicles* project directory and added them to the *Vehicles* project in Dev Studio. Next I rebuilt the "Vehicles.u" file and then rebuilt the engine in accordance with the new changed headers. At this point I could place a *CTLChoppter* in the game in UnrealEd.In code drop v3323 and later the Vehicle package is stripped down to only contain the KVehicle example class (the BullDog). Most of the important base classes from the old Vehicles package are now part of the Onslaught package. The "SCopter" is now called "ONSChopperCraft", the code (both native and script) is close to identical, some parts have been changed (mostlikely for the better). This document assumes you're working off the 2226 code drop (e.g. using the Vehicles package), when something has changed completely in v3323 it will be noted. In any other case just read "ONSChopperCraft" instead of "SCopter".

### Designing the Physics (Goal 1)

*Create a helicopter that flies based loosely on the principals that make real helicopters fly.*Before the design of the physics is discussed, we should go over how to influence an *SVehicle*. All the code to exert force or torque (or calculate wheel physics) happens in the *UpdateVehicle* function. In the case of *SHelicopter* this function is " `void ASHelicopter::UpdateVehicle(FLOAT DeltaTime)` ". In the course of *UpdateVehicle* all forces and torques are totaled up into two variable, *Force* and *Torque*. These variables are then applied to the karma actor in one call at the end of the function as follows:

```

// Apply force/torque to body.
KAddForces(Force, Torque);
```

To make physics for a helicopter, [SCopter](SCopterReference.md) seemed like a good place to start, but it was not enough of a helicopter simulation. For example, *SCopter* does not apply forces in local helicopter space. This means that if the *SCopter* is nosed down completely vertically and you press the raise button (jump), the helicopter will move up tail first. Also, the only implementation of *SCopter*, *COGChopper*, is not affected by gravity.The first decision I made was that the helicopter would be affected by gravity. To accomplish this goal I set [KActorGravScale](../Content%20Creation/Physics/KarmaReference.md#karmaparams) to 1.0 as opposed to 0.0. I set this value in *CTLChopper.uc* which is the only place that a *KarmaParams* is defined for *SHelicopter*.The second decision I made when designing my helicopter was that the main rotor would be the only thing to apply a force to helicopter. To fly forward one would have tilt the helicopter forward so the force of the rotor would be divided between keeping the helicopter in the air and moving it forward. To do this I would need to apply a force in local helicopter space as opposed to world space. I got the local coordinate system of the helicopter and applied the rotor force as follows:

```

FCoords Coords = GMath.UnitCoords / Rotation;
FVector DirX = Coords.XAxis;
FVector DirY = Coords.YAxis;
FVector DirZ = Coords.ZAxis;

...

Force += RotorForce * DirZ;
```

The next choice I made was that linear damping would always be applied. This is different from *SCopter* which applies damping conditionally based on if the movement keys for that direction are not pressed. I felt that this was simpler and also modeled air resistance more accurately. Linear Damping is allied as follows:

```

// Linear Damping - Local
Force -= LongDamping * ForwardVelMag * DirX;
Force -= LatDamping * RightVelMag * DirY;
Force -= UpDamping * UpVelMag * DirZ;
```

As you can see the damping is applied in local space but it could be applied in world space. There are advantages to both ways. If you use global damping you can damp up and down ( *UpDamping* ) motion but leave going forward undamped ( *LongDamping* ). This means you will be able to go faster forward even when the helicopter is pitched very far forward. In the local case, being pitched far forward would mean that *UpDamping* is used.

```

//// Linear Damping - Global
Force -= LongDamping * ForwardVelMag * Forward;
Force -= LatDamping * RightVelMag * Right;
Force -= UpDamping * UpVelMag * Up;
```

Rotational damping, like linear damping, is always applied. Rotational damping is applied in local space; unlike linear damping, rotational damping does not seem to work well in global space. I don't really understand why but the helicopter turns oddly. The important part about damping is that you apply damping in an orthogonal coordinate system. For example, do not apply damping on the axes on which the helicopter is torqued because that is two local axes and one global axis which means the damping axes can become gimbal-locked. Rotational damping is applied as follows:

```

// Get body angular velocity (JTODO: Add AngularVelocity to Actor!)
FKRigidBodyState rbState;
KGetRigidBodyState(&rbState);
FVector AngVel(rbState.AngVel.X, rbState.AngVel.Y, rbState.AngVel.Z);

// Rotational Damping
FVector RotDamping( AngVel.X * RollDamping, AngVel.Y * PitchDamping, AngVel.Z * TurnDamping);
Torque -= RotDamping;
```

And that is pretty much it for the physics of the helicopter. All in all, it is pretty simple. Obviously I have not gone over the controls of the helicopter but that is covered in the next section.

### Designing the Control Scheme (Goal 2)

*Design a control scheme for the helicopter that is logical and accessible.*I wanted to make flying an *SHelicopter* reasonably similar to walking around in an FPS. Or at least more similar than really flying a helicopter and really walking around which I imagine are fairly different. I also wanted to do this without giving up the [first design goal](HelicopterTutorial.md#designing_the_physics_goal_1_).I decided to work on the general scheme that pressing forward and back would make you go forward and back respectively; that pressing left and right would make you strafe/slide left and right; that jumping would make you go up; that crouching would make you go down; that moving the mouse left and right would affect which way you were aiming; and that mouse up and down would affect which way you were looking but would not affect the movement direction or orientation of your avatar. This control scheme is similar to that of a standard FPS.The control scheme of an [SCopter](SCopterReference.md) was very close to what I wanted but given that I drastically changed the physics, I also had to greatly change the control code. Given that the only linear force on the *SHelicopter* was the main rotator blade, all control of the helicopter would have to come from torquing the body to aim the rotor in a different direction.

#### Pitching and Rolling

Pitching and rolling are very simple because all this involves is mapping an input variable to a local torque axis. For example, the *OutputThrust* variable (which is the same as the [Throttle](SVehicleReference.md#throttle) in *SVehicles*) is mapped to the pitch axis and *OutputStrafe* (same as [Steering](SVehicleReference.md#steering)) is mapped to the roll axis. This is done as follows:

```

//// ROLL /////
Torque += ( OutputStrafe * RollTorqueMax * DirX );

//// PITCH /////
Torque += ( OutputThrust * PitchTorqueMax * DirY );
```

The torque is applied on local axes *DirX* and *DirY*, not the global axis *Forward* and *Right*.

#### Rotor Speed

The speed of the main rotor uses *OutputRise* (which is the same as [Rise](SVehicleReference.md#rise) in *SVehicles*) but is not bound directly to *OutputRise*. Mainly this is that so people who have no means of analog input can set the speed at a level between full on and off. The faster the rotors spin the more lift they provide. The speed can remain were you set it or it can slow down if you are not pressing anything based on *RoterSpeedDecelRate*. For more details on controlling the rotor speed the see [Rotor](HelicopterTutorial.md#rotor) section. The rotor speed and the thrust is calculated as follows:

```

// Main Rotor
RotorSpeed -= (1.0f - Abs(OutputRise)) * DeltaTime * RoterSpeedDecelRate;
RotorSpeed += OutputRise *               DeltaTime * RotorSpeedAccelRateMax;
RotorSpeed = Clamp<FLOAT>( RotorSpeed, RotorSpeedIdle, RotorSpeedMax );

FLOAT RotorForce = RotorSpeed * RotorSpeedForceFactor; //Force per (rotation per second)
Force += RotorForce * DirZ;
```

#### Yawing

Yawing is much trickier. This is mainly because we have used all the [three input variables](SVehicleReference.md#controls) for *SVehicles*. Yawing, therefore, will not be directly controlled by the player; yaw torque will be calculated based on where the view is looking and which way the helicopter is facing. This is done exactly the way *SCopters* calculate yaw torque. Yaw torque is applied on the global Z axis because it made a bit more intuitive sense when flying the helicopter than a local axis. While this is less realistic, local torque made the helicopter harder to fly. Yaw torque is calculated as follows:

```

// Project Look dir into z-plane
FVector PlaneLookDir = LookDir;
PlaneLookDir.Z = 0.0f;
PlaneLookDir.Normalize();

FLOAT CurrentHeading = HeadingAngle(Forward);
FLOAT DesiredHeading = HeadingAngle(PlaneLookDir);

// Move 'target heading' towards 'desired heading' as fast as MaxYawRate allows.
FLOAT DeltaTargetHeading = FindDeltaAngle(TargetHeading, DesiredHeading);
FLOAT MaxDeltaHeading = DeltaTime * MaxYawRate;
DeltaTargetHeading = Clamp<FLOAT>(DeltaTargetHeading, -MaxDeltaHeading, MaxDeltaHeading);
TargetHeading = UnwindHeading(TargetHeading + DeltaTargetHeading);

// Then put a 'spring' on the copter to target heading.
FLOAT DeltaHeading = FindDeltaAngle(CurrentHeading, TargetHeading);
FLOAT TurnTorqueMag = (DeltaHeading / PI) * TurnTorqueFactor;
TurnTorqueMag = Clamp<FLOAT>( TurnTorqueMag, -TurnTorqueMax, TurnTorqueMax );
Torque += ( TurnTorqueMag * Up );
```

### Balancing the Difficulty (Goal 3)

*Balance the helicopter such that newbies can fly it without crashing (much) but that advanced users will have a sufficiently complex system to master.*Balancing the difficulty had more to do with the settings in *CTLChopper* than with the code in *SHelicopter*. *SHelicopters* can be tuned to be very easy or very hard to fly. The helicopters that are harder to fly often can do more and maneuver better once you are used to them. (It is also possible to make helicopters that are very hard to fly that have no benefits but try to avoid making those.) The main variables that affect difficulty are related to linear damping, rotational damping, torque, and *bKStayUpright* (*UprightStiffness* and *UprightDamping*). The more the helicopter is damped or the more it is inclined to stay upright, the easier it will be to not crash. Also, the less torque that is applied to the helicopter body, the more stable it will be. Unfortunately, all the damping and lack of torque act like training wheels that prevent you from doing anything really interesting in the helicopter.

#### KStayUpRight

*bKStayUpright* in [KarmaParams](../Content%20Creation/Physics/KarmaReference.md#karmaparams) along with *UprightStiffness* and *UprightDamping* probably affect the balance and easy of flight of the helicopter more than any other variables. If *bKStayUpright* is true, the helicopter will always be trying to turn itself upright and level. *UprightStiffness* and *UprightDamping* set *StayUprightStiffness* and *StayUprightDamping* in [KarmaParams](../Content%20Creation/Physics/KarmaReference.md#karmaparams) which affect how strongly the helicopter will try to stay upright. If these variables are large the helicopter will level out easily but be hard to turn or bank sharply. By default in *CTLChopper*, *bKStayUpright* is true, *UprightStiffness* is 7.5, and *UprightDamping* is 5.0.

#### Linear Damping

To affect linear damping you should change *LongDamping*, *LatDamping*, and *UpDamping*. Damping takes place in local helicopter space but as mentioned in the [Designing the Physics](HelicopterTutorial.md#designing_the_physics_goal_1_) section, you can change the code to use global space easily.Damping acts to slow the helicopter in the direction it is moving. It is helpful because it allows you to stop in one place more easily. It also prevents the helicopter from picking up too much speed in one direction. Damping is like air resistance in that the faster you are moving the more force damping applies in the opposite direction. Because of this, damping acts like a terminal velocity. If the helicopter has too much *UpDamping* for example, it will never be able to plummet from the sky in an exciting manner. If *LongDamping* is too large, the helicopter will never be able to go very fast. By default in *CTLChopper*, all linear damping is set to 0.03.

#### Rotational Toque and Damping

Torque and damping both affect how quickly the helicopter can rotate. Large toque values and small damping values result in a very quick and nimble helicopter that is also easy to crash. Small torque values and large damping values result in a stable helicopter that responds slowly.Pitching and rolling is controlled by *PitchTorqueMax*, *PitchDamping*, *RollTorqueMax*, and *RollDamping*. Yawing (a.k.a. Turning) is more complicated because it not controlled directly by the user. In the case of turning, making sure that *TurnDamping* balances with *TurnTorqueMax* is much more important because the system can oscillate. To affect turning make sure you consider all these variables: *TurnTorqueFactor*, *TurnTorqueMax*, *TurnDamping*, and *MaxYawRate*.

### Aiming (Goal 4)

*Ensure that it is not too difficult for the helicopter to keep its nose (weapons) pointed at a target.*This is not much of an issue because the current *SHelicopter* does not have guns. But it was still a goal to make sure this was possible for when/if guns were added. Aiming was greatly helped by yawing about a global Z axis as opposed to a local one. While the helicopter was easier to fly with a global yaw, it was MUCH easier to aim with global yaw. The aiming is what really finalized the decision to implement a the less realistic global yaw. Also, aiming was helped by making the rotor speed something the player could set as opposed to keep tapping the jump key to hover.

## Debugging

### Show Graph

You can turn on a real time line graph of variables that might be helpful in debugging by typing `"GRAPH SHOW"` at the console. This graph will show all the variables you have set up data points for in C++ with the *AddDataPoint* function. This function should be called every tick for the variable you want to graph. For example in *UpdateVehicle* you could add these lines to graph the force applied to the helicopter:

```

GStatGraph->AddDataPoint(FString(TEXT("ForceX")), Force.X, true);
GStatGraph->AddDataPoint(FString(TEXT("ForceY")), Force.Y, true);
GStatGraph->AddDataPoint(FString(TEXT("ForceZ")), Force.Z, true);
```

See the [GraphsAndMemory](https://udn.epicgames.com/Two/GraphsAndMemory) UDN for more details on how to use the `"GRAPH"` command as well as other realtime graphing tools.

### KDraw

KDraw is a useful command for drawing what is going on with karma objects. It is documented in the [SCarReference](SCarReference.md#kdraw).

### Defaultproperties are Tricky

Be careful when you change settings in defaultproperties and also change properties in UnrealEd. Once you change a variable in UnrealEd, any changed you apply in the UC file's defaultproperties will not affect that instance in UnrealEd. This makes sense but it also confounded my debugging at one point so I thought I would mention it.

## Installing the Helicopter Code

[Download](../assets/[helicopter.zip](../assets/helicopter.zip)) the attached zip file and extract it into a CodeDrop2226 build. I have only tested this with a clean 2226 but it should work with most builds that have SVehicles. Make sure you have a build that has the executables such as uw.exe and ucc.exe built.Next open Dev Studio and go to the "Vehicles" project and add *SHelicopter.cpp* to the "Src" folder. Now delete the *Vehicles.u* file and rebuild it by typing "ucc make" or "uccdepend" in the system directory. Now build the solution and you should be ready to go. You can open up any map and drop in a *Pawn->SVehicle->SHelicopter->CTLChopper*. Or you can load *HelicopterMapBig.unr* which has helicopter spawners and a terrain to fly around in.

### v3323 and up

Because th *SHelicopter* class directly subclasses *SVehicle* it can simply be used without depending on the base classes in the Onslaught package. The *SHelicopter* class works out of the box. However the *CTLChopper* class has a few issues. Most important, the mesh used for this class `COGChopperAsset.COG_Copter2` (can be found in the v2226 code drop) doesn't load in v3323. Also a few properties set in the `defaultproperties` section no longer exist

1. `EntryPositions` ; SVehicle now only has one `EntryPosition`
2. `SafeTimeMode` ; this property no longer exists in the *KarmaParams* , it has been replaced with the `bDoSafetime` variable.

## Flying the Helicopter

### Rotor

You control the rotors of the helicopter using "jump" and "crouch". In the CodeDrop2226 build these are "space" and "c" respectively by default. Jump will speed up the rotors and crouch will slow down rotors. The speed of the rotors is represented by the bar at the bottom of the HUD. The faster the rotors are going the more lift the helicopter has. This lift is used for both staying aloft and moving around. In the default configuration of *CTLChopper* the rotor speed stays where you put it which means you can hover in place without pressing any buttons. You can configure the helicopter so the rotor speed goes down when you are not pressing jump (see *RoterSpeedDecelRate*). This means you will have to keep pressing and releasing jump to hover in place.

### Movement

As mentioned above, you must use the force of the rotor to move. You can do this by pitching or rolling the helicopter. If the helicopter is pitched forward it will move forward for example. If the helicopter is rolled to the left it will strafe left. This does mean that the helicopter will have less lift though.Use the forward and backward movement keys (or joystick axis) to pitch the helicopter. Do not hold these keys because it will keep pitching the helicopter; for example if you hold forward you will pitch forward into a nose dive.Use the strafe left and right movement keys (or joystick axis) to roll the helicopter. Like the pitch keys you should not hold these.

### Turning

Turning the helicopter is done by aiming the view where you want to go and the helicopter will turn towards that direction. On the PC this is done using the mouse for example. The yaw of the view is used to set the direction and pitch of the view is ignored. When the helicopter turns, it rotates about the world Z axis, not the local helicopter yaw.
