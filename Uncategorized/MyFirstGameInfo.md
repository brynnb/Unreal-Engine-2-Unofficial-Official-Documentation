# My First GameInfo

*Created by Chris Linder (DemiurgeStudios?) on 11-18-03 for 2226 builds. Last Updated by Chris Linder (DemiurgeStudios?). Last updated by Michiel Hendriks, because of 3323*

* [My First GameInfo](MyFirstGameInfo.md#my-first-gameinfo)
  + [Related Documents](MyFirstGameInfo.md#related-documents)
  + [Introduction](MyFirstGameInfo.md#introduction)
  + [The Class](MyFirstGameInfo.md#the-class)

## Related Documents

[MyFirstCode](MyFirstCode.md), [MyFirstPawn](MyFirstPawn.md), [MyFirstController](MyFirstController.md), [MyFirstHUD](MyFirstHUD.md)

## Introduction

If you have not looked over the [MyFirstCode](MyFirstCode.md) document you should do that first.The *GameInfo* in this example is very simple. Its only purpose is to specify the *HUDType*, the *ScoreBoardType* , the *PlayerControllerClassName*, the *DefaultPlayerName*, and the *GameName*. This game info does not create any new game type or store any new state about the current game.A bit more information about the *GameInfo* class can be found in the [GameRules](GameRules.md) document.

## The Class

As mentioned above, this *GameInfo* is very simple.

```

class ExampleGameInfo extends GameInfo;

defaultproperties
{
   HUDType="MyFirstExample.ExampleHUD"
   ScoreBoardType="MyFirstExample.ExampleScoreboard"
   PlayerControllerClassName="MyFirstExample.ExampleController"
   DefaultPlayerName="Player"
   GameName="Example Game"
}
```

Note: The [CodeDrop2226](https://udn.epicgames.com/Two/CodeDrop2226) and 3323 version of this code additionally has the line: `"bDelayedStart=false"` which starts the game with no delay or waiting for the user to click. This line is not necessary for the Runtime or the UDNBuild because they already have *bDelayedStart* set to *false* in *GameInfo.uc*.Once the simple game info that specifies these things has been created, the game INI file (*ut2004.ini* or *ue2runtime.ini* for example) must be updated to use this new *GameInfo* by default. See the [MyFirstCode](MyFirstCode.md#installing-the-example) document for more details on installing the example.
