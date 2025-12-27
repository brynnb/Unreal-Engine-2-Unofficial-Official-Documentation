# SCopter Reference

*Create on 9/15/03 by Chris Linder (DemiurgeStudios?) for v2226.*
  
*Updated on 9/16/03 by Chris Linder (DemiurgeStudios?), first public release.*
*Updated on 2005-03-23 by Michiel Hendriks, v3323 update.*

* [SCopter Reference](SCopterReference.md#scopter-reference)
  + [Related Documents](SCopterReference.md#related-documents)
  + [Introduction](SCopterReference.md#introduction)
  + [Editable SCopter Variables](SCopterReference.md#editable-scopter-variables)
    - [Thrust and Linear Damping](SCopterReference.md#thrust-and-linear-damping)
    - [Turning](SCopterReference.md#turning)
    - [Pitching](SCopterReference.md#pitching)
    - [Rolling](SCopterReference.md#rolling)
    - [Hovering](SCopterReference.md#hovering)
    - [MPH meter](SCopterReference.md#mph-meter)
    - [Not Used](SCopterReference.md#not-used)

## Related Documents

[SVehicleReference](SVehicleReference.md), [SVehicleCreation](SVehicleCreation.md), [SVehicleMayaMAXFix](https://udn.epicgames.com/Two/SVehicleMayaMAXFix), [KarmaReference](../Content%20Creation/Physics/KarmaReference.md)

## Introduction

*SCopters* are vehicles that hover, have six degrees of freedom in their linear movement (up/down, left/right, forward/back), and can turn towards a particular compass direction. This document goes over the editable variables in *SCopter* and how to use them. It also gives general overview of how *SCopters* operate and what they can do.Just like with [SCar](SCarReference.md) this class is not longer calls SCopter in v3323 but it's called ONSChopperCraft. To keep the information and references consistent throughout the UDN it will be refered to as SCopter and not ONSChopperCraft.

|  |  |
| --- | --- |
| Old name (2226) | New name (3323) |
| **SCopter** | **ONSChopperCraft** |

## Editable SCopter Variables

### Thrust and Linear Damping

#### MaxThrustForce

`var() float MaxThrustForce`This is the max forward (or back) thrust applied when you press forward (or back). The amount of thrust is based on how much the "throttle" is pressed (see the [Controls](SVehicleReference.md#controls) sections of the *SVehicle* doc). The thrust is applied in the direction the copter is facing on the X-Y plane.

#### LongDamping

`var() float LongDamping`This is the damping of linear velocity in the longitudinal direction (the direction the copter is facing on the X-Y plane). This damping will be applied in inverse to how much the throttle is being pressed. Damping should never be negative.

#### MaxStrafeForce

`var() float MaxStrafeForce`This is the max sideways thrust applied when you press left or right. The amount of thrust is based on how far the "steering" is turned (see the [Controls](SVehicleReference.md#controls) sections of the *SVehicle* doc). The thrust is applied perpendicular to the direction the copter is facing on the X-Y plane.

#### LatDamping

`var() float LatDamping`This is the damping of linear velocity in the latitudinal direction (perpendicular to the direction the copter is facing on the X-Y plane). This damping will be applied in inverse to how much the "steering" is turned. Damping should never be negative.

#### MaxRiseForce

`var() float MaxRiseForce`This is the max vertical thrust applied when you press up or down. The amount of thrust is based on how far the "rise" input (see the [Controls](SVehicleReference.md#controls) sections of the *SVehicle* doc). The thrust is applied on the world Z axis (up and down).

#### UpDamping

`var() float UpDamping`This is the damping of linear velocity in the vertical direction. This damping will be applied in inverse to how much the "rise" input is pressed. Damping should never be negative.

### Turning

You turn *SCopters* by pointing the player's view (using the mouse or thumb-stick on a console) in the direction you want to go and the *SCopter* will turn towards that direction. The *SCopter* only turns on the X-Y plane so with pitch of the player's view is ignored. The greater the difference between the direction the copter is pointing and the direction the view is facing, the harder the copter will turn.

#### TurnTorqueFactor

`var() float TurnTorqueFactor`*TurnTorqueFactor* will be multiplied by a number from -1 to 1 based on if the copter is turning as hard as it can either left or right (note: in most cases the turning multiplier will be much closer to 0 than 1 or -1. This is because [MaxYawRate](SCopterReference.md#maxyawrate) is usually small). The result of this multiply is the torque with which the copter will try to turn (before it is clamped by [TurnTorqueMax](SCopterReference.md#turntorquemax)).

#### TurnTorqueMax

`var() float TurnTorqueMax`This is the maximum amount of torque (either positive or negative) that will be applied to turn the copter. See [TurnTorqueFactor](SCopterReference.md#turntorquefactor) for an explanation of how the amount of torque is calculated.

#### MaxYawRate

`var() float MaxYawRate`This is maximum rate, in radians per second, at which the copter can turn. The larger this number is, the less effect it will have clamping the rotation and consequently, the copter will use more torque to turn (see [TurnTorqueFactor](SCopterReference.md#turntorquefactor)). Making this rate larger will allow the copter to turn faster and also use more torque but if [TurnTorqueMax](SCopterReference.md#turntorquemax) is too small, this effect might be hard to notice.

#### TurnDamping

`var() float TurnDamping`*TurnDamping* is the rotational damping for turning. The faster the *SCopter* is turning (rotating about the Z axis) the more damping will be applied. Damping is accomplished by applying negative torque on the Z axis. *TurnDamping* should always be positive.

### Pitching

*SCopters* pitch based on the "throttle". (see the [Controls](SVehicleReference.md#controls) sections of the *SVehicle* doc). This means that if the throttle is pressed forward, the copter will point its nose down. The pitch of the copter is purely cosmetic.

#### PitchTorqueFactor

`var() float PitchTorqueFactor`*PitchTorqueFactor* will be multiplied by the "throttle" of *SCopter* (see the [Controls](SVehicleReference.md#controls) sections of the *SVehicle* doc). The result of this multiply is the torque used to pitch the copter. The copter only pitches forward so far and does not spin about the Y axis because the Karma properties for *SCopters* have [bKStayUpright](../Content%20Creation/Physics/KarmaReference.md#karmaparams) set to true.

#### PitchTorqueMax

`var() float PitchTorqueMax`This is the maximum amount of torque (either positive or negative) that will be applied to pitch the copter. See [PitchTorqueFactor](SCopterReference.md#pitchtorquefactor) for an explanation of how the amount of torque is calculated.

#### PitchDamping

`var() float PitchDamping`*TurnDamping* is the rotational damping for pitching. The faster the *SCopter* is pitching (rotating about the Y axis) the more damping will be applied. Damping is accomplished by applying negative torque on the Y axis. *PitchDamping* should always be positive.

### Rolling

*SCopters* roll based on two things; the first is if they are turning, and the second is if they are strafing, a.k.a. "steering". (see the [Controls](SVehicleReference.md#controls) sections of the *SVehicle* doc). The roll of the copter is purely cosmetic.

#### RollTorqueTurnFactor

`var() float RollTorqueTurnFactor`*RollTorqueTurnFactor* is very similar to [TurnTorqueFactor](SCopterReference.md#turntorquefactor) because both are multiplied by a number which represent how hard the copter is turning. The result of this multiply is used to roll in the direction of the turn. The copter only rolls so far and does not spin about the X axis because the Karma properties for *SCopters* have [bKStayUpright](../Content%20Creation/Physics/KarmaReference.md#karmaparams) set to true.

#### RollTorqueStrafeFactor

`var() float RollTorqueStrafeFactor`This is used to roll the copter when it is strafing. Strafing is based on the "steering" (see the [Controls](SVehicleReference.md#controls) sections of the *SVehicle* doc) input of the *SCopter*. *RollTorqueStrafeFactor* is very simlar to [PitchTorqueFactor](SCopterReference.md#pitchtorquefactor).

#### RollTorqueMax

`var() float RollTorqueMax`This is the maximum amount of torque (either positive or negative) that will be applied to roll the copter. See [RollTorqueTurnFactor](SCopterReference.md#rolltorqueturnfactor) and [RollTorqueStrafeFactor](SCopterReference.md#rolltorquestrafefactor) for an explanation of how the amount of torque is calculated.

#### RollDamping

`var() float RollDamping`*TurnDamping* is the rotational damping for rolling. The faster the *SCopter* is rolling (rotating about the X axis) the more damping will be applied. Damping is accomplished by applying negative torque on the X axis. *RollDamping* should always be positive.

### Hovering

A small amouth of force and torque is applied to make the vehicle to appear to be hovering. At set intervals the force and torque are reset.

#### MaxRandForce

`var() float MaxRandForce`The maximum random force and torque to apply in each directory, the X, Y and Z components are calculated independently.

```

2 * (appFrand() - 0.5) * MaxRandForce;
```

#### RandForceInterval

`var() float RandForceInterval`The number of seconds between recalculations of the random force.

### MPH meter

The MPH meter is the UI element at the bottom of the HUD. It displays the forward speed of the *SCopter*.These variables no longer exist in v3323, however the MPH is still caculated and stored in the *CopterMPH* variable.

#### MPHMeterPosX

`var() float MPHMeterPosX`This is the X position of the MPH meter on the HUD. Position is given as a ratio with 0.0 being the far left and 1.0 being the far right.

#### MPHMeterPosY

`var() float MPHMeterPosY`This is the Y position of the MPH meter on the HUD. Position is given as a ratio with 0.0 being the top and 1.0 being the bottom.

#### MPHMeterScale

`var() float MPHMeterScale`This the scale that converts *CopterMPH* to a screen ratio. *CopterMPH* is divided by *MPHMeterScale* to get the ratio of the HUD the MPH meter should take up.

#### MPHMeterSizeY

`var() float MPHMeterSizeY`*MPHMeterSizeY* is the screen ratio for how tall the MPH meter should be on the HUD.

### Not Used

#### StopThreshold

`var() float StopThreshold`*StopThreshold* is not used.

#### UprightStiffness

`var() float UprightStiffness`*UprightStiffness* is not used.

#### UprightDamping

`var() float UprightDamping`*UprightDamping* is not used.
