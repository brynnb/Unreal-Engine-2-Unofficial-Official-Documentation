# AI Controllers

*Document Summary: A quick guide to the different classes of AIControllers.**Document Changelog: Last updated by Michiel Hendriks to update for v3323. Perviously updated by Chris Linder(DemiurgeStudios?) to update for 2226 and to clarify a few points. Original author was Hugh Macdonald ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).*

* [AI Controllers](#ai-controllers)
  + [Overview](#overview)
  + [AIController](#aicontroller)
    - [ScriptedController](#scriptedcontroller)
      * [ScriptedTriggerController](#scriptedtriggercontroller)
      * [Bot](#bot)
        + [xBot](#xbot)
          - [InvasionBot](#invasionbot)
      * [MonsterController](#monstercontroller)
    - [TurretController](#turretcontroller)
      * [LinkTurretController](#linkturretcontroller)
      * [ONSTurretController](#onsturretcontroller)
      * [SentinelController](#sentinelcontroller)
        + [ASSentinelController](#assentinelcontroller)
  + [Related Documents](#related-documents)

## Overview

The AI Controller classes define how a pawn, or group of pawns, act. The basic AI Controller will look after pawns, or groups of pawns, which are just allowed to wander, or stand in a level. A ScriptedController is used with a ScriptedSequence, to allow a much more detailed script to be put together, detailing exactly what the pawn should do.The **Level** contains a linked-list of all the Controllers in the level, so one **Controller** can work through to find out what else is there.

## AIController

Most **AIController** classes are linked to by **AIScript** actors. In turn, the **AIScript** is linked to by a **Pawn**. When the level starts, each **Pawn** will check to see if it has anything in **AIScriptTag** - if it does, then it will find the **AIScript** with that tag, and link to it. The **AIScript** will then spawn an **AIController** for each **Pawn** that links to it.Some pawns may already have a ControllerClass associated with it. This can be overridden with with **AIScript**, though.NOTE: If you link an AIController from a ScriptedSequence, you are not able to change it's properties. This is because you only link to the AIController class, and there is no instance of the controller until the level begins.

### ScriptedController

**ScriptedController** and it's subclasses can be selected as the controller for a [Scripted Sequence](ScriptedSequenceTutorial.md). They will allow the [actions](ScriptedSequenceActions.md) to control the pawn.

#### ScriptedTriggerController

This controller is used by a ScriptedTrigger to play its scripted sequence. It will never have a pawn.

#### Bot

This is the controller that is used for enemy bots. They can also be controlled with a ScriptedSequence, but when they are released, they will use all the AI that normal bots have.
The bot controller is an AI implementation for UT2004 multiplayer style enemies. Unless your game has very similar gameplay, we recommend subclassing ScripterController. The bot AI implementation can be used as a reference for creating a new AI.

##### xBot

AIController class used for most gametypes in UT2004. Doesn't contain any additional AI code, it only sets up its pawn using a PlayerRecord.

###### InvasionBot

The controller used for bots in the UT2004 Invasion gametype. This controller reacts on the non-player pawns (the Monsters) spawned during this gametype.

#### MonsterController

Simple AI that always has and hunts down a player enemy. Used by the Monster pawns for the Invasion gametype. This controller is almost identical to the Bot controller except for the AI.

### TurretController

AI for a sentry turret that scans for and attacks enemy players. As soon as an enemy is visible to the turret it will attack the enemy.

#### LinkTurretController

Same as the TurretController but with a alternate rotation algorithm.

#### ONSTurretController

This controller uses the the Onslaught weapon system.

#### SentinelController

##### ASSentinelController

This turret controller has an awake and sleep state, because of this there's a delay before the turret will attack an enemy. The controller awakes when an enemy has been spotted.

## Related Documents

[ScriptedSequenceTutorial](ScriptedSequenceTutorial.md) - This is a document about how to use ScriptedSequences which are covered only briefly here.[ScriptedSequenceActions](ScriptedSequenceActions.md) - This document talks about the types of actions ScriptedSequences can do.AIReferenceDocument? - This document talks about the technical side of AI. It goes over Controllers, AIControllers, and ScriptedControllers, as well as AIScripts and ScriptedSequences.

