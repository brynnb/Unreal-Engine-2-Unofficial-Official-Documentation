# SCar Reference

*Create on 9/8/03 by Chris Linder (DemiurgeStudios?) for v2226.*
  
*Updated on 9/15/03 by Chris Linder (DemiurgeStudios?), first public release.*
*Updated on 2005-04-05 by Michiel Hendriks, v3323 update.*

* [SCar Reference](SCarReference.md#scar-reference)
  + [Related Documents](SCarReference.md#related-documents)
  + [Introduction](SCarReference.md#introduction)
  + [Code Changes](SCarReference.md#code-changes)
  + [Editable SCar Variables](SCarReference.md#editable-scar-variables)
    - [Engine](SCarReference.md#engine)
    - [Transmission](SCarReference.md#transmission)
    - [Suspension](SCarReference.md#suspension)
    - [Friction and Brakes](SCarReference.md#friction-and-brakes)
    - [Steering](SCarReference.md#steering)
    - [Misc](SCarReference.md#misc)
    - [Air control](SCarReference.md#air-control)
    - [Jumping](SCarReference.md#jumping)
    - [Stunt info](SCarReference.md#stunt-info)
  + [Network Issues](SCarReference.md#network-issues)
    - [Problems in 2226](SCarReference.md#problems-in-2226)
  + [Tuning / Debugging Tips](SCarReference.md#tuning--debugging-tips)
    - [KDraw](SCarReference.md#kdraw)
    - [Max Speed](SCarReference.md#max-speed)

## Related Documents

[SVehicleReference](SVehicleReference.md), [SVehicleCreation](SVehicleCreation.md), [SVehicleMayaMAXFix](https://udn.epicgames.com/Two/SVehicleMayaMAXFix), [KarmaReference](../Content Creation/Physics/KarmaReference.md), [AnimBrowserReference](../Content Creation/Animation/AnimBrowserReference.md), [KarmaCarCreation](KarmaCarCreation.md), [KarmaCars](KarmaCars.md), [HotRod](HotRod.md)

## Introduction

SCar is the base class for making wheeled vehicles in Unreal using the [SVehicle](SVehicleReference.md) system. SCars include the idea of an engine which has its own inertia independent of the wheels, a 4 speed transmission, steering that not only turns the wheels but also turns a steering wheel, and brakes as well as an e-brake. SCar also includes engine sounds and a HUD meter to show the current engine RPMs as well as the current speed.This document will go over the editable variables in SCar. SCar does not contain all the variables necessary to tune cars and so you will need to understand and change variables in [SVehicle](SVehicleReference.md) as well. In some cases, to make tuning easier, variables in SCar override variables in SVehicle, like the properties of SVehicleWheels.This document will also go over some advice and tips on tuning cars and getting them to drive how you want them to. Additionally you may also want to check the native source code, it's (unlike the rest of the UnrealEngine) quite well documented.SVehicles are not completely polished in 2226, particularly in network games. This is diffirent with later builds (3323 and up). Another things that is diffirent since 2226 is that the SCar is no longer called SCar, instead it's called ONSWheeledCraft. ONSWheeledCraft is ofcourse based on the original SCar. For legacy reasons the name SCar will be used throught the document. Also take note that some things might have changed between 2226 and 3323, the document will focus on 3323, in case of changes a note will be added about the old 2226 behavior.

|  |  |
| --- | --- |
| Old name (2226) | New name (3323) |
| **SCar** | **ONSWheeledCraft** |

## Code Changes

There are a couple code changes you need to make to a stock 2226 build before SVehicles will work as well as they can.SVehicles are ticked twice. The second ticked can be skipped which is discussed in [this unprog post](https://udn.epicgames.com/lists/showpost/php?list=unprog&id=34006&lessthan=&show=20).If you want to make vehicles in 3D Studio MAX, or you want to make suspension and wheels rotate on non-orthogonal axes, you will need this fix; [SVehicleMayaMAXFix](https://udn.epicgames.com/Two/SVehicleMayaMAXFix).

## Editable SCar Variables

### Engine

#### TorqueCurve

`var() InterpCurve TorqueCurve`This is an interpolated curve that takes the current engine RPMs as its input and returns the base engine torque. The base engine torque is sent through the gearbox and the differential to determine the torque for each wheel. *TorqueCurve* should not start with an output value of 0 or else it would be very hard to start. In most cases the curve should end with an output value of 0 which is the equivalent of red-lining a car; at very high RPMs the engine should stop being able to provide power. If you don't end *TorqueCurve* in a 0, which will create a smooth transition to 0, the transition to 0 will be sharp drop after the last *InVal*. See that SCar go ;)

#### EngineBrakeFactor

`var() float EngineBrakeFactor`This is used to slow down the engine if the gas is not being pressed. This will consequently slow down the car if the gas is not being pressed. The square of the scaled engine RPMs (see [EngineBrakeRPMScale](SCarReference.md#enginebrakerpmscale)) is multipled by *EngineBrakeFactor*

#### EngineBrakeRPMScale

`var() float EngineBrakeRPMScale`*EngineBrakeRPMScale* is used to scale the engine RPMs for engine braking. See [EngineBrakeFactor](SCarReference.md#enginebrakefactor).

#### EngineInertia

`var() float EngineInertia`This is the pre-gearbox inertia of the engine. You can think of *EngineInertia* as being like a flywheel. If you set this too large, some of the flaws and approximations used to make SVehicles will be obvious. Most obvious is that all the wheels can be spinning but the car will not moving forward.

### Transmission

#### GearRatios

`var() float GearRatios[5]`This array contains the gear ratios for the transmission. 0 is reverse and 1-4 are forward. The entry for reverse should be negative. For the forward gears, each ratio should be larger than the previous ratio. The car is always in a *Gear* which corresponds to an index in this array. The engine torque is divided by a scaled version of the gear ratio (see [TransRatio](SCarReference.md#transratio)) to get the actual torque applied to the wheel. This means there is less torque for gears with larger numbers but more spins of the wheel for every "turn" of the engine. The speed of the engine, *EngineRPM*, is directly linked to the speed of the drive wheels. The drive wheels have a shared differential though which means one wheel could be spinning super fast and all the other wheels could be stopped.

#### NumForwardGears

`var() int NumForwardGears;`Defines the actual number of forward gears, max is ofcourse 4 but this allows you to limit it to less than 4.

#### TransRatio

`var() float TransRatio`This is a constant gearing factor applied to all gears in the [GearRatios](SCarReference.md#gearratios) array. This allows you to work with whatever scale numbers you want in the GearRatios array as well as easily adjust the total gearing of car.

#### ChangeUpPoint

`var() float ChangeUpPoint`When the speed of the engine, *EngineRPM*, reaches this point, the transmission will shift up into the next gear unless you are in the highest gear. Note that the RPMs displayed on the HUD include the additional [IdleRPM](SCarReference.md#idlerpm) value but the transmission does not use the [IdleRPM](SCarReference.md#idlerpm) in its calculations. Be careful about setting *ChangeUpPoint* too close to [ChangeDownPoint](SCarReference.md#changedownpoint) because if the gears are spread out, the engine will oscillate between two gears. Ofcourse in case of manual gear shifting you want to set this to a very high (unreachable) value.

#### ChangeDownPoint

`var() float ChangeDownPoint`When the speed of the engine, *EngineRPM*, falls to this point, the transmission will shift down a gear unless you are in the lowest gear (since gear #0 is reverse the lowest gear would be gear #1). Note that the RPMs displayed on the HUD include the additional [IdleRPM](SCarReference.md#idlerpm) value but the transmission does not use the [IdleRPM](SCarReference.md#idlerpm) in its calculations. Be careful about setting *ChangeDownPoint* too close to [ChangeUpPoint](SCarReference.md#changeuppoint) because if the gears are spread out, the engine will oscillate between two gears. And ofcourse for a manual gear shift this value should be negative.

#### LSDFactor

`var() float LSDFactor`

![LSDFactor.jpg](../assets/lsdfactor.jpg)

*LSDFactor* affects how the torque of the engine is distributed. If it is 0.0, the torque will be split evenly between the wheels. This will not necessarily yield wheels that all spin at the same rate; in fact, in most cases it doesn't. If *LSDFactor* is 1.0, more torque will be sent to the slower wheels in the ratio of how fast the wheels are spinning. By setting *LSDFactor* between 0.0 and 1.0, you will have a balance between these two methods.

#### IdleRPM

`var() float IdleRPM`This value is added to the current engine RPMs ( *EngineRPM* ) to calculate the engine sound and display the engine RPMs. *IdleRPM* is used for nothing else; if you want to know what the engine is really doing, subtract this value from the RPM value displayed on the HUD. This value functions best for engine sounds if it is 1/4 of [ChangeUpPoint](SCarReference.md#changeuppoint).

#### EngineRPMSoundRange

`var() float EngineRPMSoundRange`The current engine RPMs are added to [IdleRPM](SCarReference.md#idlerpm) and this value is divided by *EngineRPMSoundRange* and multiplied by 255. The pitch of the engine [IdleSound](SCarReference.md#idlesound) is then set to this value. In general, you want adjust *EngineRPMSoundRange* so that the pitch of the sound varies between 16 (which is half the default pitch) and 128 (which is twice the default pitch). This value works best for engine sounds if it is 2 \* ( [ChangeUpPoint](SCarReference.md#changeuppoint) + [IdleRPM](SCarReference.md#idlerpm) ).

#### IdleSound

`var() sound IdleSound`This is the ambient sound of the SCar actor. It is increased and decreased in pitch based on the speed of the engine. See [EngineRPMSoundRange](SCarReference.md#enginerpmsoundrange).

### Suspension

These variables override the suspension settings for all the wheels defined in the [Wheels](SVehicleReference.md#wheels) array of SVehicle.

#### WheelSoftness

`var() float WheelSoftness`This is the "softness" for the suspension of this wheel. The larger this number is the more the suspension will compress. Setting *Softness* to zero, however, does not prevent the suspension from compressing. Softness is used partly for when the car turns and the weight shifts from one side to the other. See [SuspensionTravel](SCarReference.md#suspensiontravel) for more details on turning suspension. Softness is also a measure of forgivingness of the suspension; if there is no softness the car will drive more roughly. A reasonable value for softness is 0.01 (this of course depends on the mass of your car and the other suspension settings).

#### WheelPenScale

`var() float WheelPenScale`This is the penetration scale of the suspension of this wheel. This number will scale how stiff the suspension is. If this number is less than 1.0, the suspension will be squishier and have more travel. The wheels will interpenetrate with the chassis more. If this value is 0, the wheels will be entirely pushed into the chassis when a bump is hit. If this number is larger than 1.0, the suspension will be stiffer and interpenetrate with the chassis less. If this value is very large, 100 for example, the car will bounce into the air as soon as a wheel touches the ground. 1.0 is reasonable value for *PenScale*. Note that this value primarily affects forces on the wheels from going over bumps, not from turning.

#### WheelSuspensionTravel

`var() float WheelSuspensionTravel`*SuspensionTravel* affects the suspension of this wheel when turning. The larger this number is the more the vehicle will list from side to side while turning. This value works with [WheelSoftness](SCarReference.md#wheelsoftness) so if either are too small you will not be able to see the effect of the other.

#### WheelSuspensionOffset

`var() float WheelSuspensionOffset`This is the vertical offset of the suspension. This is the number of unreal units to offset the initial position of the wheels by. Positive number will make the wheels closer to the car (more like a sports car) while negative numbers will make the wheels further below the car (like a monster truck).

#### WheelRestitution

`var() float WheelRestitution`This doesn't seem to do anything.

#### WheelAdhesion

`var() float WheelAdhesion`This doesn't seem to do anything.

### Friction and Brakes

Friction in this simulation of cars is not based on traditional models of friction. For example, in the real world, tires don't have different coefficients of friction in different directions ([WheelLongFrictionScale](SCarReference.md#wheellongfrictionscale) and [WheelLatFrictionScale](SCarReference.md#wheellatfrictionscale)). But in the real world tires (like any object) have two different coefficients of friction for static and kinetic friction which is a concept not represented here. Also the idea of "slip" is a computationally efficient cheat for sliding as opposed to "real physics" as taught by most physics classes. This is not to say that *SCars* can not be made to seem like real cars, on the contrary quite realistic simulations can be created. It is just worth noting that the parameters to set up friction may be unfamiliar.

#### WheelLongFrictionFunc

`var() InterpCurve WheelLongFrictionFunc`This is the longitudinal (in the direction of roll) friction curve. The input of this curve is the difference in linear velocity between the ground and the wheel at the point of contact. It is best to start this curve with (0,0) because otherwise the wheels and engine will jump, jiggle, and oscillate. It is worth noting that the input to this curve, the slip velocity, is not exclusively in the direction of wheel's roll but in any direction.

#### WheelLongFrictionScale

`var() float WheelLongFrictionScale`This is a scale for the amount of longitudinal friction (in the direction of roll). Think of this as a coefficient of friction for the tires in the longitudinal direction. This allows you to easily change the amount of friction wheels have without altering the way wheels have friction which is represented by the [WheelLongFrictionFunc](SCarReference.md#wheellongfrictionfunc).

#### WheelLatFrictionScale

`var() float WheelLatFrictionScale`This is a scale for the amount of friction in the lateral direction (perpendicular to the direction of roll). Think of this as a coefficient of friction for the tires in the lateral direction. Unlike longitudinal friction, there is no friction function.

#### WheelLatSlipFunc

`var() InterpCurve WheelLatSlipFunc`This is the lateral (perpendicular to the direction of roll) slip curve. For more details on slip, see the *KCar* section of [KarmaCarCreation](KarmaCarCreation.md#kcar). The input to this curve is either the rotational velocity of the wheel in radian per second. The larger slip is, the more the wheels will slide sideways when turning. This makes it harder to turn but also harder to flip while turning.

#### WheelLongSlip

`var() float WheelLongSlip`*WheelLongSlip* is the longitudinal slip (in the direction of roll) for this wheel. Unlike [longitudinal friction](SCarReference.md#wheellongfrictionfunc) and [lateral slip](SCarReference.md#wheellatslipfunc) this is not a function but a constant value. For more details on slip, see the *KCar* section of [KarmaCarCreation](KarmaCarCreation.md#kcar).

#### MinBrakeFriction

`var() float MinBrakeFriction`There are two methods for braking using in *SCars*. Wheels can have friction which slows the cars down. *MinBrakeFriction* is this friction. The other methods of braking is applying a counter torque to the wheel (see [MaxBrakeTorque](SCarReference.md#maxbraketorque)).

#### MaxBrakeTorque

`var() float MaxBrakeTorque`There are two methods for braking using in *SCars*. Wheels can have friction which slows the cars down (see [MinBrakeFriction](SCarReference.md#minbrakefriction)). The other method of braking is applying a counter torque to the wheel which is what *MaxBrakeTorque* is. If the full application of *MaxBrakeTorque* would cause the wheel to start spinning in the opposite direction, an amount less than *MaxBrakeTorque* will be applied.

#### HandbrakeThresh

`var() float HandbrakeThresh`If the velocity of the *SCar* is greater than *HandbrakeThresh* and the brakes are being pressed and then car is turning, the "handbrake" is pulled. When the handbrake is on, the friction and slip of those wheels with [bHandbrakeWheel](SVehicleReference.md#bhandbrakewheel) set to true will be adjusted by [WheelHandbrakeFriction](SCarReference.md#wheelhandbrakefriction) and [WheelHandbrakeSlip](SCarReference.md#wheelhandbrakeslip).

#### WheelHandbrakeFriction

`var() float WheelHandbrakeFriction`*WheelHandbrakeFriction* is a multiplier for the lateral friction of those wheels in the *SVehicle's* [Wheels array](SVehicleReference.md#wheels) with [bHandbrakeWheel](SVehicleReference.md#bhandbrakewheel) set to true. In most cases you want to set this less than 1.0 so that the handbrake wheels slide more when the handbrake is on.

#### WheelHandbrakeSlip

`var() float WheelHandbrakeSlip`*HandbrakeSlipFactor* is a multiplier for the lateral slip of those wheels in the *SVehicle's* [Wheels array](SVehicleReference.md#wheels) with [bHandbrakeWheel](SVehicleReference.md#bhandbrakewheel) set to true. In most cases you want to set this larger than 1.0 so that the handbrake wheels slip more when the handbrake is on.

#### FTScale

`var() float FTScale`*FTScale* is used as a multiplier for the radius of the wheel during *GripTorque* calculations. I don't know what the "FT" stands for nor do I understand how to use this parameter.

### Steering

#### MaxSteerAngle

`var() float MaxSteerAngle`This is the maximum angle in degrees which the steered wheels turn. Steered wheels are those that do not have [SteerType](SVehicleReference.md#steertype) equal to *ST\_Fixed*. The wheels do not instantly turn to this angle, instead they approach it at a rate given by [SteerSpeed](SCarReference.md#steerspeed). (v2226 only, replaced with [MaxSteerAngleCurve](SCarReference.md#maxsteeranglecurve) in newer builds)

#### MaxSteerAngleCurve

`var() InterpCurve MaxSteerAngleCurve`Defines the maximum steer angle (in degrees) as function of the current speed. This way the current speed has an influence on the steering ability. (v3323 and up, replaces [MaxSteerAngle](SCarReference.md#maxsteerangle))

#### SteerSpeed

`var() float SteerSpeed`This is the rate at which the wheels turn to [MaxSteerAngle](SCarReference.md#maxsteerangle) in degrees per second when a turning button is pressed. This is also the rate at which the wheels return to centered if no turning button is pressed.

#### SteerBoneName

`var() name SteerBoneName`This is the name of steering wheel bone. The steering wheel bone is rotated based on the current angle of the steered wheels.

#### SteerBoneAxis

`var() EAxis SteerBoneAxis`*SteerBoneAxis* is the axis about which to rotate the steering wheel bone given by [SteerBoneName](SCarReference.md#steerbonename).

#### SteerBoneMaxAngle

`var() float SteerBoneMaxAngle`This is the maximum angle to which the steering wheel bone given by [SteerBoneName](SCarReference.md#steerbonename) will rotated to.

### Misc

#### WheelInertia

`var() float WheelInertia`*WheelInertia* is the inertia for the wheels of this car. The larger this number is, the harder it will be both to stop and start this wheel spinning. Large values for this number will also cause the chassis of the vehicle to be torqued more by the wheels (see also [ChassisTorqueScale](SCarReference.md#chassistorquescale)). There are some cases where wheel inertia behaves very oddly. The most problematic is when the inertial is large and you brake, the car will come to stop **before** the wheels stop spinning. The larger the inertia and the lower the brake power the more obvious this problem is; you can have all the wheels of the car spinning on the ground while the car is stopped for several seconds. The wheels will however change speed instantly in a few cases. When you change from any forward gear to reverse or visa versa, the wheels will stop instantly. This change in motion will not torque the chassis at all.

#### ChassisTorqueScale

`var() float ChassisTorqueScale`*ChassisTorque* is the torque applied back to the chassis (equal-and-opposite) from the wheels when the wheels change rotational speed. For example, if this value is large, when you stop the wheels the chassis will pitch forward sharply. *ChassisTorqueScale* is most relevant for controlling the pitch of the vehicle in the air like you would do with a dirt bike.

#### StopThreshold

`var() float StopThreshold`If the *SCar* is moving more slowly than the velocity specified in *StopThreshold*, then the car will be considered to be stopped. This is relevant for switching from braking when going forward to driving in reverse for example.

### Air control

`var() bool bAllowAirControl;`Setting this variable to true will grant the vehicle air control. This way a player can maneuver the vehicle while in the air. The `Air*` variables below control the level of control.

#### AirTurnTorque

`var() float AirTurnTorque;`Controls the amouth of turning force to apply when steering the vehicle in the air. The result of the following function will be added to the initial air control force calculated by [AirPitchTorque](SCarReference.md#airpitchtorque): `worldUp * Steering * -AirTurnTorque`, but only if `bIsWalking` is false.

#### AirPitchTorque

`var() float AirPitchTorque;`Controls the pitching force to apply. Together with `worldRight` and `OutputPitch` this will modify the final force to apply: `worldRight * OutputPitch * -AirPitchTorque`

#### AirPitchDamping

`var() float AirPitchDamping;`This is used even if bAllowAirControl is false. It will damp the final result of the pitch rotation force. A higher value results into more damping.

#### AirRollTorque

`var() float AirRollTorque;`This is the 3rd variable that will have an effect on the air control force to apply, together with [AirTurnTorque](SCarReference.md#airturntorque) and [AirPitchTorque](SCarReference.md#airpitchtorque). This variable is only used if `bIsWalking` is true. It will add the result of the following function to the final force `worldForward * Steering * -AirRollTorque`.

#### AirRollDamping

`var() float AirRollDamping;`Just like [AirPitchDamping](SCarReference.md#airpitchdamping) this will apply some damping force but on the roll angle. This variable is also used even if bAllowAirControl is false.

#### MinAirControlDamping

`var() float MinAirControlDamping;`To limit max speed you can spin/flip at. This will be used with AirRollDamping and AirPitchDamping when bAllowAirControl is true. The value has to be between 0 and 1, where 1 will give the maximum damping force.

### Jumping

#### bAllowChargingJump

`var() bool bAllowChargingJump;`When set to true the player will be able to jump with the car. When `bPushDown` is true the jump will be charged until it's released, after which the car will jump.

#### MaxJumpForce

`var() float MaxJumpForce;`The maximum up force of a jump, this force will be reached after [JumpChargeTime](SCarReference.md#jumpchargetime) as passed (while charging the jump). Otherwise a percentage of this force will be applied.

#### MaxJumpSpin

`var() float MaxJumpSpin;`This controls how much the car will be able to turn in the air after the jump.

#### JumpChargeTime

`var() float JumpChargeTime;`The time required to reach the [MaxJumpForce](SCarReference.md#maxjumpforce).

#### Jump HUD notification

```

var() float JumpMeterOriginX, JumpMeterOriginY;
var() float JumpMeterWidth, JumpMeterHeight, JumpMeterSpacing;
var() color JumpMeterColor, SpinMeterColor;
```

The above variable will control where on the HUD the jump charge meter will be drawn. It's not a very fancy meter since it's not used in UT2004.

### Stunt info

In v3323 the SCar class (called ONSWheeledCraft) has an option for calculating a stunt score. Stunting information is only calculated when `bDoStuntInfo` is set to true. When a car is air born and depending on the various threshhold values (the `DaredevilThreshInAir*` variables) the air time and air distance a value will be calculated. For the exact calculation check the native code in *AONSWheeledCraft::Tick()* . When the stunt score is positive the *eventOnDaredevil()* event will be called. The stunt score doesn't have any other effect on the vehicle.

```

var() bool         bDoStuntInfo=
var() float         DaredevilThreshInAirSpin;
var() float         DaredevilThreshInAirPitch;
var() float         DaredevilThreshInAirRoll;
var() float         DaredevilThreshInAirTime;
var() float         DaredevilThreshInAirDistance;
var() class<LocalMessage>   DaredevilMessageClass;
```

## Network Issues

SVehicles are designed to work in network situations and do so reasonably well. There are a small number of obvious problems but most of these are cosmetic or easy to get around. Most of these problems seem to have been fixed in the 3323 code-base.SVehicles are a little tricky because there is no client side prediction. This [unprog post](https://udn.epicgames.com/lists/showpost/php?list=unprog&id=34042&lessthan=&show=20) talks more about the issue of client side prediction with SVehicles (which are the types of vehicles being used in 3323). It helps to keep this in mind when working with the older SVehicles in a network game.

### Problems in 2226

* **Driver Attachment** -- The driver does not stay in the driver position in a network game. It starts in the driver position and then the vehicle drives out from under it. Sometime the character model will then fall through the world and can be seen zooming around the level every once in a while.

* **Twitching** -- In a network game, SCars driven by other players twitch and jiggle in some cases. If you are driving an SCar, that car will not twitch. If you are playing on a listen server, no cars twitch. The twitching of other players cars seems to happen most often when the car is on an incline. The problem is exaggerated when the car is moving but also happens when the car in "stationary". The twitching does not affect the driving or collision of the car; it is just affects appearance.

* **Adjusting Default Properties in UnrealEd** -- The changes made to an instance of an object in UnrealEd are not sent to clients on a network. For example if you place a *Lynx* in a level and then change the mesh, the car will still look like a *Lynx* on all the clients. The server knows the car has a different mesh and it will do its calculations accordingly. This will cause the car on the clients to be very jerky.

## Tuning / Debugging Tips

For now this section will be short because SVehicles in 2226 are not completely polished, particularly in network games. UT2004 uses SVehicles and several changes have been made to make SVehicles usable in a final game. When UT2004 goes gold and that code becomes available, this document will be updated accordingly.Below are some general tips that apply for almost any SVehicle situation.

### KDraw

The console command "KDraw" is very useful for debugging what is going on with an *SCar*. These commands can be typed at the console.

| [Command](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=2;up=0#sorted_table-sort-by-this-column) | [Description](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=2;up=0#sorted_table-sort-by-this-column) |
| --- | --- |
| KDraw Collision | This shows the collision information used by karma. This is only collision information for the chassis; the wheels in *SCars* do not use karma collision. See the [KarmaCarCreation](KarmaCarCreation.md#step_2_add_karma_collision_volum) document for adding collision. |
| KDraw Contacts | This shows karma contact position and penetration as well as roll and lateral directions. |
| KDraw Triangles | This shows the triangles (with normals) currently considered by karma collision. |
| KDraw Com | This shows the center of mass as purple star. |
| KDraw Wheel | This draws a blue line for every wheel which is the line on which the wheel will move when the suspension compresses. It also draws a purple line perpendicular to the blue line that represents the top suspension stop. Sometimes it is hard to see these lines in a normal view; switching to "rmode 1" makes it easier. |

### Max Speed

Karma objects have a max speed in the Unreal engine. If you want to make very fast vehicles you will either need to make them very small or increase the max Karma speed. To increase the max Karma speed, change **ME\_MAX\_KARMA\_SPEED** in *Engine/Src/KarmaSuport.h* to a larger number.
