# Scripted Sequences Tutorial - Actions

*Document Summary: A comprehensive reference for the Actions available for use in Scripted Sequences.**Document Changelog: Last update by Michiel Hendriks, updated for v3323. Previous update by Jason Lentz to clarify SetViewTarget and playANIM settings (DemiurgeStudios?). Original author was Hugh Macdonald ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).*

* [Scripted Sequences Tutorial - Actions](#scripted-sequences-tutorial-actions)
  + [Overview](#overview)
  + [AIScript Actions](#aiscript-actions)
    - [Pawn Control Actions](#pawn-control-actions)
      * [ChangeTeam](#changeteam)
      * [ChangeWeapon](#changeweapon)
      * [Crouch](#crouch)
      * [DamageInstigator](#damageinstigator)
      * [DestroyPawn](#destroypawn)
      * [FinishRotation](#finishrotation)
      * [FireWeapon](#fireweapon)
      * [FireWeaponAt](#fireweaponat)
      * [ForceMoveToPoint](#forcemovetopoint)
      * [Freeze](#freeze)
      * [FreezeOnAnimEnd](#freezeonanimend)
      * [Jump](#jump)
      * [KillInstigator](#killinstigator)
      * [KnockOffHelmet](#knockoffhelmet)
      * [MoveToPlayer](#movetoplayer)
      * [MoveToPoint](#movetopoint)
      * [PlayAnim](#playanim)
      * [PlayAnnouncement](#playannouncement)
      * [PlayerViewShake](#playerviewshake)
      * [PlayLIPSinc](#playlipsinc)
      * [Run](#run)
      * [SetAlertness](#setalertness)
      * [SetHidden](#sethidden)
      * [SetPhysics](#setphysics)
      * [SetPosture](#setposture)
      * [SetViewTarget](#setviewtarget)
      * [ShootTarget](#shoottarget)
      * [StopAnimation](#stopanimation)
      * [StopShooting](#stopshooting)
      * [TeleportToPoint](#teleporttopoint)
      * [ThrowWeapon](#throwweapon)
      * [TurnTowardPlayer](#turntowardplayer)
      * [Use](#use)
      * [Walk](#walk)
      * [WaitForLIPSincAnimEnd](#waitforlipsincanimend)
    - [Script Control Actions](#script-control-actions)
      * [ChangeLevel](#changelevel)
      * [ChangeScript](#changescript)
      * [DisableThisScript](#disablethisscript)
      * [EndSection](#endsection)
      * [GotoAction](#gotoaction)
      * [GotoMenu](#gotomenu)
      * [IfCondition](#ifcondition)
      * [IfRandomPct](#ifrandompct)
      * [LeaveSequence](#leavesequence)
      * [WaitForAnimEnd](#waitforanimend)
      * [WaitForEvent](#waitforevent)
      * [WaitForPlayer](#waitforplayer)
      * [WaitForTimer](#waitfortimer)
    - [Other Actions](#other-actions)
      * [ChangeObjectiveTeam](#changeobjectiveteam)
      * [ConsoleCommand](#consolecommand)
      * [DamageActor](#damageactor)
      * [DestroyActor](#destroyactor)
      * [DisableObjective](#disableobjective)
      * [DisplayMessage](#displaymessage)
      * [DrawHUDMaterial](#drawhudmaterial)
      * [FadeView](#fadeview)
      * [HealActor](#healactor)
      * [KeepCurrentRotation](#keepcurrentrotation)
      * [LocalizedMessage](#localizedmessage)
      * [PlayAmbientSound](#playambientsound)
      * [PlayLocalSound](#playlocalsound)
      * [PlayMusic](#playmusic)
      * [PlaySound](#playsound)
      * [SetCorona](#setcorona)
      * [SetObjectiveActiveStatus](#setobjectiveactivestatus)
      * [SubTitles](#subtitles)
      * [SpawnActor](#spawnactor)
      * [SpawnRagdoll](#spawnragdoll)
      * [TriggerEvent](#triggerevent)
  + [Conclusion](#conclusion)
  + [Related Documents](#related-documents)

## Overview

The Actions that are used by a ScriptedSequence script are the commands that tell the script what to do. This document will describe exactly what each one does, and how it affects the pawn being controlled by the script.

## AIScript Actions

### Pawn Control Actions

#### ChangeTeam

(v3323 and later) Changes the team of the controller.

#### ChangeWeapon

Makes the pawn that this **ScriptedController** is controlling change weapon to whatever is in **NewWeapon**.

#### Crouch

Makes the controlled pawn crouch.

#### DamageInstigator

This will cause the controlled pawn to take damage. The amount of damage is defined by **Damage**, and the type by **DamageType**

#### DestroyPawn

This will destroy both the pawn that is being controlled, and the ScriptedController that is doing the controlling. Without the controller or the pawn, there is not much more that the Script can do.

#### FinishRotation

If the pawn has a target selected, but is not facing it, this will cause it to rotate towards that target.

#### FireWeapon

(v3323 and up) Enables or disables firing of both primary and secondary fire modes of the current weapon. If the value is true the weapon fire will start, when false it will be stopped.

#### FireWeaponAt

(v3323 and later) This will fire the current weapon at the actor matching the given tag.

#### ForceMoveToPoint

This will immediately move the pawn to the point where the actor with **DestinationTag** as it's tag is. If there is no actor with this tag, then the pawn will immediately move to the point that it is currently heading for.

#### Freeze

This will cause the pawn to completely come to a halt - mid-animation and move.

#### FreezeOnAnimEnd

This will let the current animation finish, and then freeze the pawn.

#### Jump

(v3323 and up) This will make the pawn jump, before executing the jump the physics will first be set to `PHYS_Walking`.

#### KillInstigator

This will kill the controlled pawn, using whichever **DamageType** you have selected.

#### KnockOffHelmet

(pre-3323 only) This will spawn a helmet actor (depending on what the HelmetActor in the pawn is set to - if it is none, nothing will happen here) and cause the pawn to lose it's helmet. The helmet's velocity is set by **HelmetVelocity**.

#### MoveToPlayer

This will cause the controlled pawn to move towards the player that instigated this ScriptedSequence.

#### MoveToPoint

This will do the same thing as MoveToPlayer, but will use the actor with a tag of whatever is in **DestinationTag**. If this is either blank, or non-existant, then it will move to wherever the ScriptedSequence actor is.

#### PlayAnim

This will cause the controlled pawn to play an animation. The animation's name is specified by **BaseAnim**. **BlendInTime** is the time it will take blending between the current animation, and the new one. **BlendOutTime** is currently not used. The **AnimIterations** does not currently work and will function just like the **bLoopAnim** if it is set to anything above 0. If **bLoopAnim** is **True**, then the animation will continue playing until it is interupted by the next Action.

#### PlayAnnouncement

(v3323 and up) This will queue a sound to be played as an in-game announcement.

#### PlayerViewShake

(v3323 and up) Shake the player's view within a radius with a certain intensity. Against ViewShakes?, it works client side.

#### PlayLIPSinc

(v3323 and up and compiled with Impersonator support) This will play a lipsync animation. Also see [WaitForLIPSincAnimEnd](#waitforlipsincanimend).

#### Run

This will set the controlled pawn to run next time they are told to move - on it's own, nothing will happen here.

#### SetAlertness

This will set how the controlled pawn reacts to enemies.

|  |  |
| --- | --- |
| **IgnoreAll** | This will mean that the pawn will be completely oblivious to any enemy, or any damage that is inflicted on it (this includes physics - it will act as if nothing has happened). |
| **IgnoreEnemies** | This will cause the pawn to ignore any enemies, even if fired upon, but it will react to being shot, even though it won't try to fight back. |
| **StayOnScript** | This forces the pawn to follow the script, however, it will fight back when it has the chance. |
| **LeaveScriptForCombat** | When the pawn sees an enemy, it will leave the script, and engage in combat with that enemy. |

#### SetHidden

This will cause the pawn associated with this to become hidden (if **bHidden** is true) or visible (if **bHidden** is false).

#### SetPhysics

This will change how the controlled pawn reacts and moves. It gives you the option of any of the physics types that can be used in the engine, although most of them need a lot of setting-up, and so can't be used properly here.

|  |  |
| --- | --- |
| **None** | The pawn will stay still, wherever it is |
| **Walking** | The pawn has to be touching the ground at all times (otherwise it changes to Falling). The pawn is allowed to move along the surface of the ground. |
| **Falling** | The pawn is affected by gravity |
| **Swimming** | The pawn is under-water, and swims |
| **Flying** | The pawn is not affected by gravity - the same as swimming, but works outside water |
| **Rotating** | This will make your pawn constantly rotate - this may not work, as the variable for the rotation rate cannot be set. |
| **Projectile** | DO NOT USE |
| **Interpolating** | DO NOT USE - This will not work, as you cannot set what path you want your pawn to interpolate along |
| **MovingBrush** | DO NOT USE |
| **Spider** | This should allow your pawn to walk on any surface - floor, walls or ceiling. However, it currently does not work. |
| **Trailer** | DO NOT USE |
| **Ladder** | This is for when your pawn is climbing a ladder. |
| **RootMotion** | DO NOT USE |
| **Karma** | DO NOT USE - This is used for actors which have Karma properties set. Therefore, it will not work with your pawns. |
| **KarmaRagDoll** | DO NOT USE - See Karma |

#### SetPosture

This will set what kind of posture your pawn is in. They are pretty much self-explanatory - **Normal**, **Relaxed**, **Patroling** and **Alert**. This purely changes what your pawn looks like - you need to use [SetAlertness](#setalertness) to change how they act.This is broken in 2226 and completely removed from 3323.

#### SetViewTarget

This will cause the the pawn to face the actor with the tag specified in **ViewTargetTag.** Note that the pawn must either be in motion or the **SetViewTarget** action must be followed with a **WaitForAnimEnd** Action for the pawn to actualy turn and face the specified **ViewTargetTag.**

#### ShootTarget

Your pawn will shoot at the actor that you specified in SetViewTarget. **FiringMode** depends on the weapon. For the coders out there, this ends up in BotFire() in the weapon. In the [CodeDrop2226](https://udn.epicgames.com/Two/CodeDrop2226), the COG Assault Rifle is an example of a weapon that has different firing modes - **MODE\_Single**, **MODE\_Burst**, **MODE\_Auto**, **MODE\_Grenade**.

#### StopAnimation

This will stop any animation that is currently playing.

#### StopShooting

If the pawn is in the middle of shooting, then this will stop it. This can be useful if you want a pawn to contunie shooting until something is triggered.

#### TeleportToPoint

This will immediately move the controlled pawn to the point with the tag specified in **DestinationTag**. The only difference between this and ForceMoveToPoint is that this one will affect the player that triggered the sequence if there is no controlled pawn.

#### ThrowWeapon

This will cause the pawn to throw it's weapon. The velocity of the weapon can be defined by **WeaponVelocity** or, if **WeaponVelocity** is (0,0,0), it add a vertical velocity of 250, and a forward (in the direction the pawn is facing) velocity of 300 to the velocity of the pawn itself.

#### TurnTowardPlayer

This will cause the controlled pawn to turn towards the player that activated the sequence.

#### Use

(v3323 and up) This will trigger the "use" command for the pawn. If the pawn is driving a vehicle it will exit it, otherwise if it is close to a vehicle it will try to enter it. If neither is the case it will "use" all touching actors.

#### Walk

This will set the controlled pawn to walk next time they are told to move - on it's own, nothing will happen here.

#### WaitForLIPSincAnimEnd

(v3323 and up; only when compiled with Impersonator support) This will wait for the current lipsync animation to finish.

### Script Control Actions

#### ChangeLevel

Changes to a new level (defined by **URL**). **bShowLoadingMessage** is self-explanatory - it sets whether the 'LOADING' is shown on-screen while the level is loading.

#### ChangeScript

Searches for the script with the tag specified in **NextScriptTag**, and starts executing that script.

#### DisableThisScript

(v3323 and later) Disables the script completely.

#### EndSection

This is used in conjunction with IfCondition and IfRandomPct. If either of these decide that they do not want to execute the next section, they will skip on to the next occurence of this action.

#### GotoAction

Skips to the action specified by **ActionNumber**.

#### GotoMenu

(v3323 and up) This will open a GUI Menu page. If **bDisconnect** is true the current level will be disconnected when the menu is opened.

#### IfCondition

If the **TriggeredCondition** pointed to by **TriggeredConditionTag** is true, then it will continue as normal. If it is false, then it will skip to the next **EndSection**.

#### IfRandomPct

The value specified in **Probability** is the chance that the next section is executed. The game picks a random number between 0 and 1. If this is less that **Probability**, then it continues on, otherwise it skips on to the next **EndSection**.

#### LeaveSequence

This will stop the current ScriptedSequence from playing.

#### WaitForAnimEnd

This will wait until the current animation has finished before continuing. **Channel** is the animation channel to wait for - 0 is the main animation channel, and the most often used one.

#### WaitForEvent

This will wait until the event specified by **ExternalEvent** is called.

#### WaitForPlayer

This will wait until the player that activated the sequence is closer than **Distance** from the pawn.

#### WaitForTimer

This will pause for the length of time specified by **PauseTime**.

### Other Actions

#### ChangeObjectiveTeam

(v3323 and later) Sets the team value of the GameObjective who's tag is the same as **GameObjective**.

#### ConsoleCommand

Executes a console command.

#### DamageActor

(v3323 and later) Damages the actor with the matching tag. Works just like [DamageInstigator](#damageinstigator) except this can damage any actor.

#### DestroyActor

This will destroy any actors with the tag in **DestroyTag**. (This is purely down to whether the actor exists - no explosions to go with it, I'm afraid.)

#### DisableObjective

(v3323 and later) This is disable the GameObjective with the matching tag. If **bClearInstigator** is false the instigator used for modifying the GameObjective will be the intestigator of the current controller. If **bTriggerObjectiveInstantly** is true *DisableObjective()* will be called before the objective is set to completed.

#### DisplayMessage

This will display a message on the client's screen. If **bBroadcast** is true, then it will appear on the screens of everyone in the game. Otherwise, it will just be on whichever computer is running the ScriptedSequence. The message to be displayed is in **Message**, and the message type is in **MessageType**. At the moment, most \*MessageType\*'s don't make a difference. The only ones that do are 'Say' and 'TeamSay'. These both just add the player's name to the front of the message.

#### DrawHUDMaterial

(v3323 and later) This will draw a material on the the HUD for a given time (**DisplayTime**). If the position and dimension variables are below 1 it will be relative to the screen resolution.

#### FadeView

Will cause the view to be faded to a certain color for a certain time. This is done by modifying the ViewFlash value of the current PhysicsVolume.

#### HealActor

(v3323 and up) the opposite of [DestroyActor](#destroyactor), meant to heal the actor matching the tag with the defined heal DamageType.

#### KeepCurrentRotation

(pre-3323 only) This will prevent the pawn from rotating during the script execution.

#### LocalizedMessage

(v3323 and later) This will broadcast a LocalMessage class.

#### PlayAmbientSound

This applies the AmbientSound properties to the ScriptedSequence actor. If you want to stop this sound, you have to call the same action again, with 0 in **SoundVolume**. If you leave **AmbientSound** blank, this will not work. The command will not be executed if there is nothing in **AmbientSound**.

#### PlayLocalSound

This will play a sound for all players that are linked to the controller.

#### PlayMusic

If **bAffectAllPlayers** is true, then this will play the selected music for all the players in the level. Otherwise, it will only play for the player who started this controller. The **Transition** is one of the following:

|  |  |
| --- | --- |
| **None** |  |
| **Instant** | The old music will immediately go, and the new one will start |
| **Segue** | Longer fade in, shorting fade out. |
| **Fade** | One music track will fade out, as the new one fades in |
| **FastFade** | A faster fade |
| **SlowFade** | A slower fade |

#### PlaySound

This will play the appropriate sound. If there is a pawn that is being controlled, then that will be where the sound is played from. Otherwise, the sound will be from the SciptedSequence actor. Setting **bAttenuation** to true will make the sound quieter, depending on the distance from the source. **Volume** and **Pitch** are self-explanatory.

#### SetCorona

(v3323 and up) This will set the value of **bCorona** of the actors matching the **HideActorTag**.

#### SetObjectiveActiveStatus

(v3323 and up) This will set a GameObjective's active state.

#### SubTitles

(v3323 and later) This will perform an action on the current processing of the SceneSubtitles. There's only one mode option:

|  |  |
| --- | --- |
| **ESST\_SkipToNextLine** | Skip the current subtitle line |

#### SpawnActor

This will, understandably, spawn a new actor into the level. **ActorClass** is the class of actor that you want to spawn, and **ActorTag** is the tag that you want to give it. if **bOffsetFromScriptedPawn** is true, then **LocationOffset** and **RotationOffset** are the offsets from the pawn that you want it to be spawned at. Otherwise, these are relative to the ScriptedSequence.

#### SpawnRagdoll

(pre-3323 only) This will spawn a 'KRagDoll' actor at the position of the ScriptedSequence actor. **Friction** is the friction that the Rag-Doll has with the ground. **LinDamping** and **AngDamping** are the linear and angular damping on the Rag-Doll.If you want the Rag-Doll to start, having just had an impulse to one of it's bones, you need to name the bone in **HitBoneName**. The impulse direction/force is specified by **HitBoneImpulse**. If you leave **HitBoneName** blank, the Rag-Doll will activate normally.**InitialVel** will give the whole skeleton an initial velocity, letting you set the whole thing in motion from the start.

#### TriggerEvent

This will trigger the event that is specified in **Event**.

## Conclusion

This tutorial is meant to be used in conjuntion with the [Scripted Sequence Tutorial](ScriptedSequenceTutorial.md), which explains the overview of how to use Scripted Sequences.

## Related Documents

[ScriptedSequenceTutorial](ScriptedSequenceTutorial.md) - This is a document about how to use ScriptedSequences which are covered only briefly here.[AIControllers](AIControllers.md) - This document goes over all the types of AIControllers as well as how to set up AIControllers in Unrealed.AIReferenceDocument? - This document talks about the technical side of AI. It goes over Controllers, AIControllers, and ScriptedControllers, as well as AIScripts and ScriptedSequences.

