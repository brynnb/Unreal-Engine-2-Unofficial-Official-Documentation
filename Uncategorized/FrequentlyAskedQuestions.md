# UE2 Frequently Asked Questions

*Document Summary: Here you will find a FAQ page for people just starting to use the Unreal Engine 2.**Document Changelog: Last updated by Michiel Hendriks, link to mod community page. Updated by Andrew Moise (DemiurgeStudios?), removed link to dead document. Original Author - Jason Lentz (DemiurgeStudios?)*

* [Frequently Asked Questions](FrequentlyAskedQuestions.md#frequently-asked-questions) 
  + [Content Creation](FrequentlyAskedQuestions.md#content-creation)
    - [How do I make outdoor areas?](FrequentlyAskedQuestions.md#how-do-i-make-outdoor-areas)
    - [How do I add moving parts to my level?](FrequentlyAskedQuestions.md#how-do-i-add-moving-parts-to-my-level)
    - [How can I create complex scenes and/or improve the performance of my level?](FrequentlyAskedQuestions.md#how-can-i-create-complex-scenes-andor-improve-the-performance-of-my-level)
    - [What kinds of special effects can be created?](FrequentlyAskedQuestions.md#what-kinds-of-special-effects-can-be-created)
    - [How can I make my level react to players?](FrequentlyAskedQuestions.md#how-can-i-make-my-level-react-to-players)
    - [How can I add characters to a level?](FrequentlyAskedQuestions.md#how-can-i-add-characters-to-a-level)
  + [Technical and Programming](FrequentlyAskedQuestions.md#technical-and-programming)
    - [How can I build menus a HUD, and import fonts for my project?](FrequentlyAskedQuestions.md#how-can-i-build-menus-a-hud-and-import-fonts-for-my-project)

## Content Creation

### How do I make outdoor areas?

There are several techniques to making convincing outdoor environments. Here are three docs that describe how to use these techniques.

|  |  |
| --- | --- |
| **[TerrainTutorial](../Content%20Creation/Primitives/TerrainTutorial.md)** - Unreal Ed has a special tool that specifically geared towards allowing you to quickly and easily create landscapes. This tool is call the Terrain Editor. The [TerrainTutorial](../Content%20Creation/Primitives/TerrainTutorial.md) will guide you through the process of setting up your level for Terrain as well as show you how to take advantage of all of its features. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |
| **[ExampleMapsSkyZones](ExampleMapsSkyZones.md)** - SkyZones are used to create SkyBoxes, SkyCylinders, and SkyDomes in Unreal. This example maps document steps you through the creation process of each type of SkyZone highlighting the advantages | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |
| **[ExampleMapsAdvLighting](ExampleMapsAdvLighting.md)** - This example map shows off several techiniques for lighting both in and outdoors. Some of the outdoors lighting effects include forest canopy shadows with light beams, intricate single tree shadows, rolling cloud shadows, ground fog, and water caustics. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |

### How do I add moving parts to my level?

Adding moving geometry to your level can be done in two ways, adding Movers and adding KarmaActors. Movers are special StaticMeshes that can move along a series of predefined key frames and KarmaActors are meshes that have been endowed with their own physics properties for realistic physics simulations. Each of these two types of moving geometry are described below.

|  |  |
| --- | --- |
| **[MoversTutorial](../Content%20Creation/Primitives/MoversTutorial.md)** - This type of geometry is ideal for doors, rotating fans, raising platforms or anything that you want to move in a consistent path each time it is activated. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |
| **[IntroToKarma](../Content%20Creation/Physics/IntroToKarma.md)** - KarmaActors are much more complex and as a result you can do a lot more with them. This document introduces the various documents that explain all of the Karma features. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |

### How can I create complex scenes and/or improve the performance of my level?

Complex scenes can be created in Unreal using StaticMeshes within a well optimized level. StaticMeshes are geometry initially created in a 3rd party modeling program and then imported into the editor. They render extremely fast and as a result allow for much greater detail to be added to the levels. Once your level is fully optimized, you can create even more complex environments. These two documents explain the basics of using StaticMeshes and optimizing your level from within the editor.

|  |  |
| --- | --- |
| **[StaticMeshesTutorial](../Content%20Creation/Primitives/StaticMeshesTutorial.md)** - This document introduces StaticMeshes as well as how to use the StaticMesh Browser. Because of the ease of creating StaticMeshes and their ability to render quickly, they are essential to creating complex environments. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |
| **[LevelOptimization](../Content%20Creation/Techniques/LevelOptimization.md)** - Optimization can occur on several levels, from steamlining the code, to tweaking models, and also within the level itself. As a level designer, there are several tools to making sure that your level runs as smoothly as it can. This doc outlines all the guidelines you can follow to ensure your level is properly optimized for best performance. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |

### What kinds of special effects can be created?

There are a variety of special effects that can be created within Unreal Ed -more than can reasonably be listed in one document. Here you will find a few good places to get started.

|  |  |
| --- | --- |
| **[ExampleParticleSystems](../Content%20Creation/Effects/ExampleParticleSystems.md)** - The Unreal Engine has a very robust system for creating [ParticleSystems](../Content%20Creation/Effects/ParticleSystems.md). In the [ExampleParticleSystems](../Content%20Creation/Effects/ExampleParticleSystems.md) document you can see how to create a variety of effects including by not limited to explosions, lightning, breaking glass, and waterfalls. *Note: these examples all assume you are using the new Particle System Editor, for additional examples using the old style of editing emitters see the [EmittersExamples](EmittersExamples.md) doc.* | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |
| **[MaterialTutorial](../Content%20Creation/Lighting%20and%20Textures/MaterialTutorial.md)** - Unreal Ed has its own texture manipulation tools which may appear complex at first, can be used to create amazing effects such as environment reflections, oscillating and panning textures, and many more. This document explains how to use the Material Browser and guides you through each of the different Material Types. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |
| **[MirrorsAndWarpZones](MirrorsAndWarpZones.md)** - With special BSP zones and surfaces you can create Mirrors and WarpZones within your level. Mirrors will reflect everything just as a real mirror would, but there are some limitations and special steps involved in setting them up. WarpZones are spaces that not only teleport you to another space, but the also act as a window to that space. This document explains how to use both of these features. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |
| **[Teleporters](ExampleMapsTeleporters.md)** - Teleporters are Actors that can teleport players and bots from location to location or even between maps (see the [LevelTransitions](../Content%20Creation/Techniques/LevelTransitions.md) doc). Teleporters can be set up to change player speeds and orientation as the teleport, and they can also be made to be one way or choose a destination spot randomly. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |
| **[FluidSurfaceTutorial](../Content%20Creation/Primitives/FluidSurfaceTutorial.md)** - A FluidSurfaceInfo is an Actor that creates a surfaces that behaves like water as in it will ripple when objects (including players) pass through it. To learn more about how to set up FluidSurfaceInfos in your level, check out this doc. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |
| **[ExampleMaps](../Content%20Creation/Techniques/ExampleMaps.md)** - For other specific effects, check out the [ExampleMaps](../Content%20Creation/Techniques/ExampleMaps.md) page. There are several examples on how to set up various effects in your level and each document of course comes with it's own map with which you can download and follow along. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |

### How can I make my level react to players?

Other than adding features into the code of your game, there are three main ways to make your level react to players using UnrealEd as is; Triggers, Movers, and adding Bots with AI. Each of these topics are described in detail in the linked docs below.

|  |  |
| --- | --- |
| **[TriggersTutorial](TriggersTutorial.md)** - Triggers are what Unreal uses to activate events. There are several types of Triggers available to you and a wide variety of actions can be set into motion with them. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |
| **[MoversTutorial](../Content%20Creation/Primitives/MoversTutorial.md)** - This type of geometry is ideal for doors, rotating fans, raising platforms or anything that you want to move in a consistent path each time it is activated. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |
| **[ScriptedSequenceTutorial](../Content%20Creation/Scripted%20Sequences/ScriptedSequenceTutorial.md)** - This is the introduction to setting up Artificial Intelligence to the bots in your level, although you will also want to read the [NavigationAI](../Content%20Creation/Scripted%20Sequences/NavigationAI.md) document to see how to set up path nodes. With AI in your level you can set up bots to run away, attack, or play any animation upon interacting with or seeing a player. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |

### How can I add characters to a level?

Every engine handles characters differently. The below two docs explain what steps you need to take not only in how to best create the characters in 3rd party modeling programs but also how to import them into UnrealEd and set up your level so that non player characters can navigate your levels.

|  |  |
| --- | --- |
| **[ModelingTableOfContents](ModelingTableOfContents.md)** - This document will direct you to all the documents you will need in order to correctly model, texture, rig, and import your model into UnrealEd. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |
| **[NavigationAI](../Content%20Creation/Scripted%20Sequences/NavigationAI.md)** - This document explains how to use PathNodes to create navigation paths for the bots to follow. The document also explains how to set up special destinations like Doors, JumpPads, JumpDesitinations, Lifts, and Ladders. | ![pagepic.jpg](../assets/![pagepic.jpg](../assets/pagepic.jpg)) |

## Technical and Programming

### How can I build menus a HUD, and import fonts for my project?

Complex scenes can be created in Unreal using StaticMeshes within a well optimized level. StaticMeshes are geometry initially created in a 3rd party modeling program and then imported into the editor. They render extremely fast and as a result allow for much greater detail to be added to the levels. Once your level is fully optimized, you can create even more complex environments. These two documents explain the basics of using StaticMeshes and optimizing your level from within the editor.

|  |
| --- |
| **[UserInterfaceDesign](../Technical%20and%20Programming/User%20Interface/UserInterfaceDesign.md)** - This document introduces you to the GUI system and how extend it to create new controls and elements. |
| **[HeadsUpDisplayReference](../Technical%20and%20Programming/User%20Interface/HeadsUpDisplayReference.md)** - This is a reference to creating in-game information displays. |
| **[LocalizationReference](../Technical%20and%20Programming/User%20Interface/LocalizationReference.md)** - Here you will find information on localizing the text in your project. |

---
