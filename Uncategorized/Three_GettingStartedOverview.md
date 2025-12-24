# Getting Started: Unreal Engine 3

* [Getting Started: Unreal Engine 3](GettingStartedOverview.md#Getting Started: Unreal Engine 3)
  + [Overview](GettingStartedOverview.md#Overview)
    - [Platform Specific Considerations](GettingStartedOverview.md#Platform Specific Considerations)
  + [Planning and Preproduction](GettingStartedOverview.md#Planning and Preproduction)
  + [Engine Acquisition and Setup](GettingStartedOverview.md#Engine Acquisition and Setup)
  + [UnrealScript and the UE3 Codebase](GettingStartedOverview.md#UnrealScript and the UE3 Codebase)
  + [Gameplay Element Creation](GettingStartedOverview.md#Gameplay Element Creation)
  + [Level Creation](GettingStartedOverview.md#Level Creation)
  + [Content Creation](GettingStartedOverview.md#Content Creation)
  + [Compiling and Testing](GettingStartedOverview.md#Compiling and Testing)
  + [Packaging and Distribution](GettingStartedOverview.md#Packaging and Distribution)

## Overview

This document is an overview of the process of planning, producing, and publishing a game using Unreal Engine 3. Starting out on a new project using Unreal Engine 3 can be a daunting task. The engine is complex and knowing how to get started as well as how to move from phase to phase is not always immediately obvious. This overview is here to help you along the way; pointing you in the right direction as to what needs to be done to get started, where documentation can be found for the various aspects of the production cycle, and where to go once production of your game wraps.The sections are laid out chronologically starting from planning and ending with publishing. Along the way, each section will have a brief summary of what is involved in that task or aspect of development along with links to more detailed documents covering important areas of the aspect in question.This is by no means a complete or comprehensive list of each and every document on the Unreal Developer Network, and you may find that your particular game does not follow the steps or aspects of development listed here precisely. This is meant to give you an idea of what is involved and provide a basis for performing the important tasks required to develop a game using Unreal Engine 3.

### Platform Specific Considerations

When developing for various platforms other than PC, there are some aspects of the "Getting Started" process that are specific to the target platform. See the pages below for more information on getting started with specific platform development:

* [Getting Started: Developing Mobile Projects](GettingStartedMobile.md)

## Planning and Preproduction

Before production begins, in fact before you even decide Unreal Engine is the right fit for your game, there are some important aspects to go over and sort out in order to avoid any gotchas down the line.

* What features required by your game are supported by Unreal Engine 3?
* Do Unreal Engine 3's minimum specifications fit your target market?
* Do you have enough and sufficiently skilled workers to meet your release schedule?
* Does the content pipeline for Unreal Engine 3 suit your needs?
* What legal guidelines will need to be followed?
* What support outlets does Epic provide for Unreal Engine 3?

To answer these questions and more, visit the [Getting Started: Production](GettingStartedProduction.md) page for detailed information.

## Engine Acquisition and Setup

Whether for trial purposes or when the actual production is ready to begin, the first step is to acquire the appropriate version of the engine: Unreal Engine 3 or Unreal Development Kit. For obtaining Unreal Engine 3, the process can seem tricky for first-time users, but Epic provides a detailed guide for each step along the way. If you have a working knowledge of Perforce depots, this should be a relatively painless process. In addition, Epic provides a custom tool for quickly upgrading to new QA-approved builds. Acquiring Unreal Development Kit is a quick and easy process requiring only that you download the installer and install the application.Once you have acquired the appropriate version of the engine, there is some additional setup required before you can start work on your own custom game project. Licensees have a more involved setup process as they must create a new project in the engine solution and set up Visual Studio. UDK users only need to set up a new script project and the coding environment of their choosing. Again, detailed guides are provided for the setup process to help you along the way.See the [Getting Started: Engine Setup](GettingStartedEngine.md) page to get started.

## UnrealScript and the UE3 Codebase

Knowing and understanding the UnrealScript language as well as the codebase of the engine, both native and script, is extremely important. This will enhance your ability to leverage the full power of the engine and make implementing new features much more efficient as you will not be constantly searching through documentation and wandering aimlessly through code trying to find which class to extend or where a function is implemented.Of course, gaining an understanding and knowledge of a codebase the size of Unreal Engine 3 is not really a practical expectation. However, you should be able to grasp an overview of the major aspects and classes along with a solid understanding of those pertinent to your particular area of expertise in a reasonable amount of time.The [Getting Started: Programming](GettingStartedProgramming.md) page contains information and links to additional documents over these aspects to get you started learning how to program with Unreal Engine3.

## Gameplay Element Creation

Creating custom gameplay elements is an integral part of getting your game off the ground. Gameplay elements in this sense refer to elements such as the gametype (or game rules), the player (including camera and input), and the HUD/UI (Heads Up Display / User Interface). Of course, these are merely a fraction of the custom gameplay elements your technical team will be implementing during the creation of a new game, but these make up the foundation of the game framework and are common to all games and, as such, require special attention.The [Getting Started: Gameplay Elements](GettingStartedGameplay.md) page details each of these elements and provides links to a reference and examples for each.

## Level Creation

Levels, or maps, are collections of items that together form the world or environment in which the game takes place. Building environments and worlds for your game is obviously a very important aspect of the production cycle. The process of creating levels involves a broad collection of topics, but at its foundation it involves placing various types of Actors into a map within Unreal Editor, the editing suite provided with Unreal Engine 3.As level design does involve a broad range of disciplines, there may be several people working on a single level at any one time. There may be one person in charge of the level as a whole while one or more people are in charge of scripting events using the Kismet visual scripting system and others may be handling animating events and cinematic sequences using Matinee. The level streaming system in Unreal Engine 3 makes this all possible as a single persistent level can contain multiple sub-levels, called streaming levels. These sub-levels can contain the Kismet scripting and Matinee sequences keeping things organized and allowing multiple people to be working on the same overall level at the same time.To learn more about how to create environments for your game, visit the [Getting Started: Level Creation](GettingStartedLevels.md) page.

## Content Creation

Unreal Engine 3 provides both custom tools within UnrealEd as well as pipelines for bringing in content from external applications. These features give artists the complete freedom to create content that will bring the game environment to life. From static meshes to create the environment, buildings, structures, and decorations to skeletal meshes used for player characters, weapons, and vehicles. From complex, dynamic materials to amazing particle effects, Unreal Engine 3 makes content creation simple and efficient.The [Getting Started: Content Creation](GettingStartedContent.md) page contains more information on each of the major content types as well as how to create, import, and edit them.

## Compiling and Testing

Numerous times throughout the development process, the engine and scripts will need to be built and compiled in order to run the game for testing. This process has been made as painless as possible through the addition of several tools to Unreal Engine 3. Building and compiling is handled by the Unreal Build System and Unreal Frontend. These automate a great deal of what used to require manual intervention.Testing and debugging can be a tedious process, but there are tools included which can help to track down bugs, performance issues, and tweak gameplay in a very efficient manner.Visit the [Getting Started: Building and Testing](GettingStartedBuilding.md) for an overview of the building and testing processes as well as information on using all of the included tools.

## Packaging and Distribution

Preparing and creating a finished version of game for distribution is the final step in the process of creating a game with Unreal Engine 3 or Unreal Development Kit. In cases where storage space is a concern, it is important to make sure that you are only including that content which is actually used by the game. You also want to make sure that you follow any license agreements that exist with any software to be included with your game or dependencies on third-party software your game may have.The [Getting Started: Deployment](GettingStartedDeployment.md) provides more information over packaging games made with Unreal Engine 3.

Important!

You are viewing documentation for the **Unreal Development Kit (UDK)**.

If you are looking for the Unreal Engine 4 documentation, please visit the [Unreal Engine 4 Documentation](https://docs.unrealengine.com) site.

Don't show me this again
