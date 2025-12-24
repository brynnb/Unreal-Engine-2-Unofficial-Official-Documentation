# My First Code

*Created by Chris Linder (DemiurgeStudios?) on 11-18-03 for 2226 builds. Last Updated by Michiel Hendriks, UT2003 -> UT2004.*

* [My First Code](MyFirstCode.md#My First Code)
  + [Related Documents](MyFirstCode.md#Related Documents)
  + [Introduction](MyFirstCode.md#Introduction)
  + [Parts of the Example](MyFirstCode.md#Parts of the Example)
    - [Pawns](MyFirstCode.md#Pawns)
    - [Player Controllers](MyFirstCode.md#Player Controllers)
    - [GameInfos](MyFirstCode.md#GameInfos)
    - [HUDs](MyFirstCode.md#HUDs)
  + [Installing the Example](MyFirstCode.md#Installing the Example)
    - [Unreal Runtime](MyFirstCode.md#Unreal Runtime)
    - [Code Drop, UDNBuild, UDNBuildOff](MyFirstCode.md#Code Drop, UDNBuild, _UDNBuildOff)
  + [Using this Example in Net-Play](MyFirstCode.md#Using this Example in Net-Play)
  + [Making Changes to the Example - Using the Example in UnrealEd](MyFirstCode.md#Making Changes to the Example - Using the Example in _UnrealEd)

## Related Documents

[MyFirstPawn](MyFirstPawn.md), [MyFirstController](MyFirstController.md), [MyFirstGameInfo](MyFirstGameInfo.md), [MyFirstHUD](MyFirstHUD.md), [NewProjectPreparation](https://udn.epicgames.com/Two/NewProjectPreparation), [GameAndAIHandout](GameAndAIHandout.md)

## Introduction

This document will go over the basics of what is involved with creating your own [pawn class](MyFirstPawn.md), [player controller class](MyFirstController.md), [HUD](MyFirstHUD.md), and [game type](MyFirstGameInfo.md). This document is only an overview and describes how the different classes interrelate; for more info on each class see their respective documents.This example tries to be fairly basic but it still assumes some knowledge of UnrealScript and how networking "replication" is handled in the Unreal Engine. You should be able to jump right into this example and understand most of it but further reading would help. For more details on UnrealScript see the [UnrealScriptReference](../Technical and Programming/UnrealScript/UnrealScriptReference.md). For more details on replication consider the [NetworkingTome](https://udn.epicgames.com/Two/NetworkingTome) and the [PlayerReplicationHandout](https://udn.epicgames.com/Two/PlayerReplicationHandout).

## Parts of the Example

### Pawns

*Pawns* (any class that extends *Pawn.uc*) are *Actors* in the Unreal engine that move around on there own and are either controlled by a player, an AI, or an AI script (see [Player Controllers](MyFirstCode.md#Player_Controllers) below for more info). The avatar you control when you play UT2004 is a *Pawn* as are all the other players you see in the game be they bots or other people in a net-game. Non-Player Characters (NPCs) such as those in any single player game are also *Pawns*. Movers and rockets are examples of things that move around and are not *Pawns*. This document will focus on the *Pawn* you control as you play the game.The pawn you control when you play can be specified in *User.ini* or at the command line (see the [MyFirstPawn](MyFirstPawn.md#Installing_the_Example) document for more details). The pawn can be changed without altering any part of the engine or even changing any code. Any pawn can be used with the given [player controller](MyFirstCode.md#Player_Controllers) but it may not work quite right; it should still move around the world though. If there are a set of pawns designed to work with the given player controller then these pawns can be swapped and substituted with no problem at all. The [MyFirstPawn](MyFirstPawn.md) document has two pawns, a girl and a guy, that can both be used with the default player controller.

### Player Controllers

Controllers (any class that extends *Controller.uc*) control *Pawns* in the Unreal engine. Controllers can be AIs, like *Bots* in UT2004, or controllers can be an interface to a human player that allow a person to control a pawn. Controllers can control any pawn which is useful because it makes it very easy to use a single pawn as a Bot or as player's avatar.Player controllers (any class that extends *PlayerController.uc*) are the controllers that serve as the interface from a human player to a pawn. The player controller to use is specified in the [GameInfo](MyFirstCode.md#GameInfos). You therefore need to change code to use a new player controller.See the [MyFirstController](MyFirstController.md) example for more details.

### GameInfos

GameInfos (any class the extends *GameInfo.uc*) are how game types are created. DeathMatch and CTF are both examples of game types. The game info is accessible from most classes so those classes can query about the state of the current game. Along with creating functions and variables that define a game, the game info defines how players enter the game, restart the game, logout, etc...GameInfos also specify what the [player controller](MyFirstCode.md#Player_Controllers) class is and what the [HUD](MyFirstCode.md#HUD) class is. Specifying the controller and HUD is the primary use of the game info in the [MyFirstGameInfo](MyFirstGameInfo.md) example. The game info in the example does not create any new game type at all.

### HUDs

HUDs (any class the extends *HUD.uc*) draw the Heads Up Display to the screen. See the [HeadsUpDisplayReference](../Technical and Programming/User Interface/HeadsUpDisplayReference.md) and the [HeadsUpDisplayTutorial](HeadsUpDisplayTutorial.md) for more information on what HUDs can do. HUDs are specified in the [GameInfo](MyFirstCode.md#GameInfos) by class name. Also specified in the *GameInfo* is the *ScoreBoard* which shows the names and scores of everyone in the current game. The *ScoreBoard* is displayed instead of the HUD when you press `'F1'`. The *ScoreBoard* is closely related to the HUD but it is its own class which extends *ScoreBoard.uc*.See the [MyFirstHUD](MyFirstHUD.md) example for more details on *HUDs* and *ScoreBoards*.

## Installing the Example

There are two installs for the MyFirstCode example. The pawns in [MyFirstPawn](MyFirstPawn.md) can be installed independently without any other code. See the [MyFirstPawn](MyFirstPawn.md) document if you just want to install the pawns. The other examples such as [player controller](MyFirstController.md), [HUD](MyFirstHUD.md), and [game type](MyFirstGameInfo.md) all inter-depend on each other as well as depending on the pawn example and therefore must be installed as a block. The rest of this section will go over how to install the block of examples which includes the pawn classes, the player controller, the HUD, and the game type.

### Unreal Runtime

If you are using the Runtime, simply download the [MyFirstExample.zip](../assets/myfirstexample.zip), unzip it and run *MyFirstExample.urm*. If you can not simply run *MyFirstExample.urm* this probably means you unchecked the "Runtime modification association" box when installing the Runtime. In that case you will have to follow the steps below:

1. Open MyFirstExample.zip and extract *MyFirstExample.urm* to the `"System"` directory of the Runtime.
2. Open a command prompt in the `"System"` directory of the Runtime.
3. Type `"setup install MyFirstExample.urm"`

In either case, follow the instructions presented in the install window and this will install this example for the Runtime.Once the example is installed you must edit INI files to use the example. First edit *User.ini* to specify the type of pawn to use. In the `[DefaultPlayer]` section of *User.ini* set *Class* as follows:

```

Class=MyFirstExample.ExampleBoy
- or -
Class=MyFirstExample.ExampleGirl
```

Next you need to edit *UE2Runtime.ini*. In the `[Engine.Engine]` section change *DefaultGame* and *DefaultServerGame* as follows:

```

DefaultGame=MyFirstExample.ExampleGameInfo
DefaultServerGame=MyFirstExample.ExampleGameInfo
```

You don't need to change *DefaultServerGame* if you are only using single player but then again if you are only using single player, changing *DefaultServerGame* doesn't matter.Now just start the Runtime and pick and map and you are good to go. The pawn, controller, HUD, and GameInfo will all be used

### Code Drop, UDNBuild, UDNBuildOff

If you are using the UDNBuild or UDNBuildOff, download [MyFirstExample\_UDNBuild.zip](../assets/myfirstexample_udnbuild.zip) and unzip it in your build of the engine.If you are using the 2226 code drop, download [MyFirstExample\_CodeDrop.zip](../assets/myfirstexample_codedrop.zip) and unzip it in your build of the engine, or the [MyFirstExample\_CodeDrop3323.zip](../assets/myfirstexample_codedrop3323.zip) for newer builds.Once the example is unzipped you must edit INI files to use the example. First edit *User.ini* to specify the type of pawn to use. In the `[DefaultPlayer]` section of *User.ini* set *Class* as follows:

```

Class=MyFirstExample.ExampleBoy
- or -
Class=MyFirstExample.ExampleGirl
```

Next you need to edit *<YourGame.ini>* (*UT2004.ini* for example). In the `[Engine.Engine]` section change *DefaultGame* and *DefaultServerGame* as follows:

```

DefaultGame=MyFirstExample.ExampleGameInfo
DefaultServerGame=MyFirstExample.ExampleGameInfo
```

You don't need to change *DefaultServerGame* if you are only using single player but then again if you are only using single player, changing *DefaultServerGame* doesn't matter.Now just start the game and pick and map and you are good to go. The pawn, controller, HUD, and GameInfo will all be used

## Using this Example in Net-Play

If you would like to use this example in net play you have to do a few things on the computer hosting the game.First edit *<YourGame.ini>* (*UE2Runtime.ini* or *UW.ini* for example) and include `"MyFirstExample"` in your *ServerPackages* list. The *ServerPackages* list is in the `[Engine.GameEngine]` section of the INI file and you can just add the following line to that section:`ServerPackages=MyFirstExample`Next you must rebuild the MD5 database. Do this by opening a command prompt in the "System" directory of your build of the engine and then type:

```

UCC MASTERMD5 -c *.U
```

Now you can host a game and other people can connect to it and you can all run/fly/swim/dance around together. You can host a game by typing the following at a command prompt in the system directory:`UE2Runtime <YourMap> -server`
  
- or -  
`UW <YourMap> -server`To connect to a server running this example you must have installed the example as described above in the [Installing the Example](MyFirstCode.md#Installing_the_Example) section. Then just run the game and bring up the console (press the '~' key) and type: `"open <IP Address of Server>"`, for example `"open 192.168.1.112"`.

## Making Changes to the Example - Using the Example in UnrealEd

If you wish to make changes to the given code or you want to place *ExamplePawns* in UnrealEd, you will have to add "MyFirstExample" to the *EditPackages* lists in *<your\_game>.ini* (*UW.ini* or *UE2Runtime.ini* for example). Do this by opening your INI file and doing a text search for "EditPackages" and then add the line "EditPackages=MyFirstExample" to the bottom of the list. There are two lists so make sure to add the line to both lists. If you are making changes to the code you can recompile the changes you made by deleting the existing *MyFirstExample.u* file in the system directory and typing `"ucc make"` at the command line.
