# Karma Example UT2003

*Document Summary: An example map with brief documentaion on how to set up various Karma effects in UT2003.**Document Changelog: Last updated by James Golding.*

* [Karma Example UT2003](KarmaExampleUT2003.md#Karma Example UT2003)
  + [Introduction](KarmaExampleUT2003.md#Introduction)
    - [Catapult](KarmaExampleUT2003.md#Catapult)
    - [Swing Door](KarmaExampleUT2003.md#Swing Door)
    - [Fan](KarmaExampleUT2003.md#Fan)
  + [Downloads](KarmaExampleUT2003.md#Downloads)

## Introduction

This really simple map (KarmaExample.ut2) just shows a few things you can do with Karma actors in UT2003.**NOTE!** *You MUST set your Physics Detail to High before loading this map.*

### Catapult

This uses a KHinge between the panel and the ground, with its KAltDesiredAngle set to about 45 degrees. KHingeType is then set to HT\_Springy, and its initial state (under Object in the properties window) is set to ToggleDesired. That means, each time it is triggered, it will toggle whether it goes to KDesiredAngle or KAltDesiredAngle. When you touch the trigger nearby, the springyness causes the panel to rise and throw the pipes into the air. Tiggering it again causes it the spring back to the floor. If we left bKDisableCollision at its default of 'true', the panel would pass through the ground as collision between is and the level would be disabled. So we set that to 'false'.

### Swing Door

This uses another HT\_Spring KHinge to hold the door to the world. We leave bKDisableCollision as true so the door doesn't rub against the level geometry. However, to prevent the door swinging open too far (or in this example, at all!), we use a KConeLimit as well. We set the direction of the cone limit to point across the doorway, and set the cone KConeHalfAngle to be about +\- 22.5 degrees (or about 4000 in ureal units). We also increase the stiffness of the limit quite a lot so the stops are quite hard. At this time you can only open the doors by shooting them, not by pushing them.

### Fan

This again uses a KHinge to hold the fan up, but this time we set KHingeType to HT\_Motor. Then we set its initial state to ToggleMotor - this means Triggering it will turn the motor on, and triggering it again will turn the motor off. Note that when you trigger the motor off, it will try to maintain its new position, by setting itself to HT\_Controlled until triggered again. This allows you to build cranes etc.

## Downloads

Below you can download a compressed archive that contains the content for this example:

* [KarmaExample.zip](../assets/KarmaExample.zip) (for UT2003)
