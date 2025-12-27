# Placing Triggers in Maps

*Document Summary: A reference and tutorial for setting up Triggers.**Document Changelog: Last updated by Jason Lentz (DemiurgeStudios?), to include ViewShaker Trigger and to remove broken Example Maps. Original author was Richard 'vajuras' Osborne ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).*

* [Placing Triggers in Maps](TriggersTutorial.md#placing-triggers-in-maps)
  + [What is a Trigger?](TriggersTutorial.md#what-is-a-trigger)
    - [Setting up a generic Trigger](TriggersTutorial.md#setting-up-a-generic-trigger)
    - [Breaking it Down](TriggersTutorial.md#breaking-it-down)
  + [Other Types Of Triggers](TriggersTutorial.md#other-types-of-triggers)
    - [MusicTrigger](TriggersTutorial.md#musictrigger)
    - [LineOfSightTrigger](TriggersTutorial.md#lineofsighttrigger)
    - [MaterialTrigger](TriggersTutorial.md#materialtrigger)
    - [UseTrigger](TriggersTutorial.md#usetrigger)
    - [ViewShaker](TriggersTutorial.md#viewshaker)
    - [ZoneTriggers](TriggersTutorial.md#zonetriggers)
    - [Timed Trigger](TriggersTutorial.md#timed-trigger)
  + [Gameplay Triggers](TriggersTutorial.md#gameplay-triggers)
    - [Counter](TriggersTutorial.md#counter)
    - [RedirectionTrigger](TriggersTutorial.md#redirectiontrigger)
    - [TeamTrigger](TriggersTutorial.md#teamtrigger)
  + [Triggers can be used for many purposes](TriggersTutorial.md#triggers-can-be-used-for-many-purposes)

## What is a Trigger?

Triggers are basically just 'alarms' that- once triggered, can cause a series of events to occur. There are many different types of triggers available for level designers to use such as proximity of a nearby player/pawn, damage taken, and many other more specialized types of triggers (these are covered later). Most of these types can be setup simply by using the Trigger class.

### Setting up a generic Trigger

Let's go through the process of adding a simple trigger to the level that will display a message when a player enters its proximity. Open the Unreal Editor and construct a basic level. After you add a PlayerStart, you'll notice that Unreal Ed has a list of different types of triggers that you can select from.

![triggersbrowser.gif](../assets/![triggersbrowser.gif](../assets/triggersbrowser.gif))

Select the *Trigger* actor and place it in your map. A simple sprite will appear where you added the trigger actor. Right click on the Trigger and go to *Properties*. Expand the *Advanced* section and change the **bHidden** attribute to *false* as shown in the image below. Now we will be able to see the trigger when we run the sample map.

![triggerproperties.jpg](../assets/![triggerproperties.jpg](../assets/triggerproperties.jpg))

Close the advanced tree. Next, expand the Trigger property section. In the **Message** field, enter the text that will be displayed when the player enters the trigger's proximity. For this example, the Message text is "Hi, You have entered my proximity." Note, that the default type for a generic trigger is TT\_PlayerProximity.

![triggerproperties2.jpg](../assets/![triggerproperties2.jpg](../assets/triggerproperties2.jpg))

Now we must setup the collision bounds of the trigger. This way, the trigger will be able to detect the player whenever they enter their field. Expand the **Collision** section. Note by default, the trigger's collision fields are set. *bCollideActors* is set to true and the CollisionHeight and CollisionRadius are set to 40. The engine will notify this trigger when the actor encroaches, its collision bounds if they are within a distance of 40.Now save the level and run your map. If you placed your trigger close to the PlayerStart, you should see it right in front of you (because we set *bHidden* attribute to false).

![test1.jpg](../assets/![test1.jpg](../assets/test1.jpg))

Walk to the trigger. The text you entered into the *Message* field will be displayed.

![test2.jpg](../assets/![test2.jpg](../assets/test2.jpg))

### Breaking it Down

This section describes all the properties of a trigger:

* TriggerType - defines the type of action that will be the catalyst for the trigger. There are 6 different choices that will trigger this actor:

a) TT\_PlayerProximity - any pawn that is controlled by AI or an actual player.b) TT\_PawnProximity - by default this means any pawn.c) TT\_ClassProximity - means this trigger is activated by any actor that belongs to the **ClassProximityType** argument (it can be a subclass of the argument as well). For example, Engine.Pawn would apply to any pawn.

![classproximity.jpg](../assets/![classproximity.jpg](../assets/classproximity.jpg))

Picking a parent type such as *Inventory* will be applicable to any children classes that fall under that type. For instance, looking at the Actor Browser- you can see all the child classes that conform to the Inventory type. All of these child classes are also affected when you set their parent type as the ClassProximityType. In this example, *Weapon*, *Powerups*, and many other child types are affected as shown in the picture below.

![inventory.jpg](../assets/![inventory.jpg](../assets/inventory.jpg))

d) TT\_AnyProximity - any game entity (actor) within the proximity. This applies to weapons, inventory, pawns, and just basically any solid object in the game. Note, particles are not actual game entities and so- won't activate the trigger.e) TT\_Shoot - when the trigger is impacted by a projectile. If **DamageThreshold** is set for the trigger, then the damage inflicted by the projectile must be greater than this number. Note that if the trigger is set to this type, the engine will automatically set the drawtype of the trigger to None- even though the *bHidden* attribute is set to false.

![tt_shoot.jpg](../assets/![tt_shoot.jpg](../assets/tt_shoot.jpg))

Other properties of a Trigger:

* Message - this string/message is displayed when the trigger is activated.
* bTriggerOnceOnly - this actor becomes inactive after it's activated once.
* bInitiallyActive - set to true by default- meaning that the trigger is active. If this property is set to false, this trigger can only be activated by another trigger.
* ClassProximityType - useful only if the TriggerType is set to TT\_ClassProximity. Any game entity matching this class type will activate the trigger.
* RepeatTriggerTime - if this value is set to greater than 0, the **Message** will be repeated every few seconds as long as the trigger is still colliding with the entity that activated it.
* ReTriggerDelay - duration of time in seconds that must expire before this trigger can be reactivated.
* DamageThreshold - minimum amount of damage this trigger must be inflicted if the **TriggerType** is set to TT\_Shoot.

## Other Types Of Triggers

There are many other types of Triggers that provide more specialized functions than the generic Trigger class. There are three basic parts to the trigger, the Event, Tag, and ExcludeTags. The Event is the action or the object that is being triggers such as music playing or a light toggling. The Tag is the name of the trigger itself. More information on ExcludeTags coming soon. With Triggers a player can activate things in a map with their mere presence. The following are how some of the different types of triggers can be used.

### MusicTrigger

When this actor is triggered, it plays the song specified by it's default settings. If this trigger is 'triggered' again, it will stop the current song that's playing. Unlike a generic Trigger, this special trigger must be triggered by another event. For instance, setup a generic trigger that uses TT\_PlayerProximity for the *TriggerType* and set its Event/Event property to *MusicPlay* (this will be the EventName).

![eventtrigger.gif](../assets/![eventtrigger.gif](../assets/eventtrigger.gif))

Next, select a MusicTrigger in the Actor Browser and add it to the level. Set the Event/Tag property of this actor to the *MusicPlay* event name.

![musictrigger.gif](../assets/![musictrigger.gif](../assets/musictrigger.gif))

Now when the player encroaches, the generic trigger's radius, it will trigger the MusicTrigger.The MusicTrigger has a few easy to understand properties. Let's break this class down:

* Song - this is the music file that will be played when this trigger is activated.
* FadeInTime - the number of seconds the music will transition into the new track.
* FadeOutTime - the number of seconds the music will fade out.
* FadeOutAllSongs - this property simply cancels the current song. If you set the **Song** property- it will simply be ignored if this property is set to true.

### LineOfSightTrigger

The Line Of Sight trigger was designed for single player games for situations the mapper may desire to trigger an event when a PlayerController (human game player) views the user defined object. Hence, this unique trigger does not work in multiplayer mode (only for the human player that either owns a local or listen server). The LineOfSightTrigger can be used with any group of actors and is very straight forward to use. You should not use it for the trigger itself but instead for an entity in the level. For example, if the player sees just the LOS trigger, an event isn't triggered *unless* the actor associated with the trigger via the **SeenActorTag** is in view. Pawns controlled by an AIController will not trigger this actor.To use a Line Of Sight Trigger, simply add the trigger to the level. Next, adjust the **SeenActorTag** property to match the **Tag** property of the actor you want to trigger the LOS event.Below is an example of a Trigger with the **SeenActorTag** set followed by explanations of each of the properties:

![losproperty.jpg](../assets/![losproperty.jpg](../assets/losproperty.jpg))

* bEnabled - Disables this trigger. Internally, a LineOfSightTrigger does not disable itself. However, if the trigger is disabled, the engine will stop running LOS checks.
* MaxViewAngle - this is the *angle* in degrees that the player must view the **SeenActor** in order to trigger Line Of Sight.
* MaxViewDist - maximum distance the player can be in order for *Line Of Sight* to occur. This value is in unreal units.
* SeenActorTag - this is a required property used by the trigger to determine Line Of Sight for an actor that exists in the level. During initialization, the trigger will find this actor and begin observing it for line of sight events. This functionality seems to be rather restricted though since the only Tag that seems to work is that of the LineOfSight Trigger itself.

During initialization, the trigger searches the level for the indicated actor. Thus, you do not want to set the trigger to point to an actor that does not exist in the level until after gameplay has started. The LineOfSightTrigger should ideally be linked to an actor/decoration that is saved into the actual map.**NOTE: Currently LineOfSight Triggers only work in single player mode and they can only be activated once. Also, as described in the above properties, the SeenActorTag should be set to the tag of the LineOfSight Actor's Tag.**

![loslevel.jpg](../assets/![loslevel.jpg](../assets/loslevel.jpg))

### MaterialTrigger

The **MaterialTrigger** is one of the most unique triggers. Unlike the others that have been described, this trigger works with a **MaterialSwitch** material. A MaterialSwitch material simply iterates through an internal list of materials whenever it is triggered. Note, you can actually trigger any material using a MaterialTrigger in which will proceed to trigger it's **FallbackMaterial** material. However, only the MaterialSwitch material will actually do *something* once triggered by default.First, create a MaterialSwitch material in unrealed. Open up the texture browser and click New. Create a new package or simply use the included UDNMat.utx file which contains an example MaterialSwitch material.

![materialswitch1.jpg](../assets/![materialswitch1.jpg](../assets/materialswitch1.jpg))

Configure the material using the desired shaders. Personally, in version 927, I've found the only type of materials that tend to crash unrealed are **Combiners** but most other shaders seem okay. For this example, I have chosen two very simple shaders.

![materialswitch3.jpg](../assets/![materialswitch3.jpg](../assets/materialswitch3.jpg))

As you can tell from the screenshot, a MaterialSwitch has only two basic properties:

* Current - this property refers to the current material in the array/group that is being displayed. This number increments until it reaches it's max, and then it resets back to 0. By default it refers to the first image you add to the array but you can change this to indicate which material you want to start with.
* Materials Array - this is the group of materials you want to alternate through.

Next, you should setup the MaterialTrigger. A MaterialTrigger CANNOT be triggered alone. It must be triggered by an external event (like a Player Proximity trigger) like most of the other specialized triggers. For the pictured example, a generic player proximity trigger is added to the level with the *bHidden* property set to false. Additionally, a message will appear when the player activates the trigger. The **Event** property is set to equal *MaterialSwitch*. The event name is of course not important, as long as it matches the **Tag** property in the MaterialTrigger.

![materialswitch2.gif](../assets/![materialswitch2.gif](../assets/materialswitch2.gif))

In this example, you would notice the bubble texture displayed by default (because it was at the **Current** index 0). When you walk up to the trigger, a message is displayed and the **MaterialSwitch** activates. The action may happen really fast- so you will want to set a delay in the generic trigger so the materials don't change so fast.

![materialswitch4.jpg](../assets/![materialswitch4.jpg](../assets/materialswitch4.jpg))

### UseTrigger

This is one of the most straight forward triggers to use. If a human controlled pawn is within the proximity of this trigger and hits their **USE** key, it activates this trigger. In turn, this trigger will alert all actors whose **Tag** matches the *Event* property set by this trigger.Note that it is also possible to send a message to the screen with this trigger. In the **UseTrigger** section, there is a *Message* field. This will send a message to the screen when a player comes within the proximity of the trigger, which can be changed in the **Collision** section, in the *CollisionHeight* and *CollisionRadius* fields.

![usetrigger1.jpg](../assets/![usetrigger1.jpg](../assets/usetrigger1.jpg))

### ViewShaker

![viewshaker.jpg](../assets/![viewshaker.jpg](../assets/viewshaker.jpg))

The ViewShaker is a Trigger that affects the players. Once activated by a generic Trigger or some other event, the ViewShaker will cause all the player cameras within a specified radius to shake for a specified amount of time. Here are the variables that determine how the ViewShaker will shake the player cameras.

| Property | Explanation | Default value |
| --- | --- | --- |
| OffsetIterations | This value determines how many times the player's view will be offset, or in other words, how long the player's view will be shaken linearly. | *500.0* |
| OffsetMagHorizontal | This value is the maximum distance that the player's view will be offset in the horizontal direction. | *0.0* |
| OffsetMagVertical | This value is the maximum distance that the player's view will be offset in the vertical direction. | *10.0* |
| OffsetRateHorizontal | This value is how fast the players view will be offset linearly in the horizontal direction. | *353.0* |
| OffsetRateVertical | This value is how fast the players view will be offset linearly in the vertical direction. | *400.0* |
| RollMag | This value determines how far to roll the view of the player. | *0.0* |
| RollRate | This value determines how quickly to roll the view of the player. | *0.0* |
| ShakeRadius | All players within this radius from the ViewShaker will experience the effect of the ViewShaker. | *2000.0* |
| ViewRollTime | This value is how long the effected player's view will roll back and forth. | *0.0* |

### ZoneTriggers

When this actor is touched, the event is triggered for all *ZoneInfo* actors that contains the matching **Tag** property. As of version 927, there really aren't any ZoneInfo subclasses that a ZoneTrigger would be useful to use in conjunction with.

* bTriggerOnceOnly - turns the trigger off after it's been activated.

![zonetrigger1.jpg](../assets/![zonetrigger1.jpg](../assets/zonetrigger1.jpg))

### Timed Trigger

This trigger is obsolete. Don't use it, or the editor will give you a warning, in addition to it not working.

## Gameplay Triggers

This section references all triggers that belong to the *Gameplay* package (Gameplay.u).

### Counter

This trigger performs the simple purpose of counting down from a user defined number to 0. When the count equals 0, the **Event** property for this actor is triggered.The Counter trigger is triggered by an outside event (such as a separate proximity trigger).

* NumToCount is the initial/current value of this Counter. When this value equals 0, the **Event** is triggered for this actor.
* bShowMessage is the boolean property that indicates that this actor will publish a message when the **NumToCount** value is decremented.
* CountMessage is the message that is displayed when the NumToCount value is decremented. This message is displayed only if the **bShowMessage** property is set to true. The %i character is replaced during runtime with the value of **NumToCount**. For instance, if NumToCount=6 and the CountMessage equals "Only %i to go" then the message "Only 6 to go" will be displayed during the game.
* CompleteMessage is the message that is displayed when the countdown has finished.

The image below is an example of how to setup the properties of a Counter:

![counter.jpg](../assets/![counter.jpg](../assets/counter.jpg))

Below is an image of what happens during a countdown:

![counter-countdown.jpg](../assets/![counter-countdown.jpg](../assets/counter-countdown.jpg))

The image below shows the **CompletedMessage** that gets displayed when the count equals zero.

![counter-completed.jpg](../assets/![counter-completed.jpg](../assets/counter-completed.jpg))

### RedirectionTrigger

This trigger accepts an event and **redirects** it to a pawn in the level. This functionality isn't currently used anywhere but could be useful for pawn subclasses that implements some function for a specific **Event**. Unlike the other triggers previously described, the Event that you wish to trigger is set by a separate property called **RedirectionEvent**.

* RedirectionEvent is the event that is triggered for all pawns in the level.

### TeamTrigger

This trigger expands upon the *generic trigger* base by providing several restrictions. Unlike the other triggers, this one is only applicable to team games (such as WarfareTeamDeathmatch). This trigger will not work in regular deathmatch or single player modes.Below is a list of restrictions this trigger adds:

* Any damage taken by a teammate will not be processed normally.
* Any event that is related to a certain pawn in the level will not be processed if the instigator is on the same team that is indicated by the **Team** byte property.

As you can tell, this trigger is useful to help exclude events from being processed or activated for all pawns that belong to a certain team.This is a list of all the properties of a TeamTrigger:

* bTimed is a boolean property that will cause this trigger to trigger an Event every 2.5 game seconds for any pawn in the level that is not does not match the same **Team**.
* Team is the id of the team this trigger should exclude events for.

Below is an example of how to setup a TeamTrigger. Notice how it also includes a *Trigger* property section.

![teamtrigger1.jpg](../assets/![teamtrigger1.jpg](../assets/teamtrigger1.jpg))

## Triggers can be used for many purposes

You can disable a playerstart by using a trigger. Instead of using a normal PlayerStart, use a TriggeredPlayerStart. If this special actor is triggered by an event, this PlayerStart will be disabled (Note, this depends on the gametype. The base gametype code checks to see if a PlayerStart is enabled if the PlayerStart's *bSinglePlayerStart* property is set to true.To see an example map of how Triggers can be used, see the [ExampleMapsTriggers](ExampleMapsTriggers.md) document.
