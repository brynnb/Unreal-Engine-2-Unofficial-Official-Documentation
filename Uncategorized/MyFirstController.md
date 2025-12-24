# My First Controller

*Created by Chris Linder (DemiurgeStudios?) on 11-18-03 for 2226 builds. Last Updated by Chris Linder (DemiurgeStudios?). Last updated by Michiel Hendriks, for fun*

* [My First Controller](MyFirstController.md#my-first-controller)
  + [Related Documents](MyFirstController.md#related-documents)
  + [Introduction](MyFirstController.md#introduction)
  + [Flying and Walking](MyFirstController.md#flying-and-walking)
  + [Dancing](MyFirstController.md#dancing)
  + [Using the Controller](MyFirstController.md#using-the-controller)

## Related Documents

[MyFirstCode](MyFirstCode.md), [MyFirstPawn](MyFirstPawn.md), [MyFirstGameInfo](MyFirstGameInfo.md), [MyFirstHUD](MyFirstHUD.md)

## Introduction

If you have not looked over the [MyFirstCode](MyFirstCode.md) document you should do that first.This document goes over how to make a simple controller class that will allow the pawn to easily fly and also play a "dance" animation. This example requires the pawn class described in [MyFirstPawn](MyFirstPawn.md) as well as the *GameInfo* described in [MyFirstGameInfo](MyFirstGameInfo.md).To use this example follow the [installation instructions](MyFirstCode.md#installing_the_example) in the *MyFirstCode* document. The *MyFirstCode* document includes the UnrealScript source code as well as the compiled \*.u file and the animation and texture packages to make everything work.This example can be used in any 2226 build of the engine including the straight code drop, UDNBuild, UDNBuildOff, and the Runtime or a 3323 (and maybe later) build of the engine.

## Flying and Walking

To easily switch between walking and flying there are three exec functions: *Fly*, *Walk*, and *ToggleFlyWalk*. These functions are the same functions that are in *RTPlayerController* in the runtime. These functions are not cheating functions because they are defined in the controller (not in *CheatManager.uc*) and can therefore be used in net games. To work in net games properly these function also need to be replicated to the server properly. The following replication block and functions show how this is done.

```

replication
{
   reliable if(Role < ROLE_Authority)
      Fly, Walk, ToggleFlyWalk;
   ...
}

exec function Fly()
{
   if ( Pawn != None )
   {
      Pawn.UnderWaterTime = Pawn.Default.UnderWaterTime;
      ClientMessage("You feel much lighter");
      Pawn.SetCollision(true, true , true);
      Pawn.bCollideWorld = true;
      GotoState('PlayerFlying');
   }
}

exec function Walk()
{
   if ( Pawn != None )
   {
      Pawn.UnderWaterTime = Pawn.Default.UnderWaterTime;
      Pawn.SetCollision(true, true , true);
      Pawn.SetPhysics(PHYS_Walking);
      Pawn.bCollideWorld = true;
      GotoState('PlayerWalking');
   }
}

exec function ToggleFlyWalk()
{
   if(IsInState('PlayerFlying'))
      Walk();
   else
      Fly();
}
```

## Dancing

The *DoDance* function illustrates how it is possible for players to make their pawns play an animation on all clients. This function uses the *SetAnimAction* function of *ExamplePawn* which deals with the replication of the animation properly if it is called on the server. This is explained in the [MyFirstPawn](MyFirstPawn.md#user_controlled_animation) document. By looking at the block of code below you can see that *SetAnimAction* is called on the server in multiplayer situations. This code also works in single player.

```

var bool DoingDance;

replication
{
   ...
   reliable if ( Role < ROLE_Authority )
      DoDance;
}

exec function DoDance()
{
   if( ExamplePawn(Pawn) != NONE && Pawn.Physics == PHYS_Walking && !DoingDance)
   {
      Pawn.SetAnimAction( ExamplePawn(Pawn).DanceAnim );
      PlayerReplicationInfo.Score += 1;
      DoingDance = true;
      SetTimer(3.0, false);
   }
}

event Timer()
{
   DoingDance = false;
}
```

To ensure that the pawns do not "dance" too fast, a *Timer* is used in conjunction with the bool *DoingDance* to limit the rate at which *SetAnimAction* is called. *DoingDance* starts initialized to `false`. In multiplayer situations the timer only exists on the server. The pawns also do not dance if they are not standing on the ground ( `Pawn.Physics == PHYS_Walking` ).

## Using the Controller

First install the example; see the [MyFirstCode](MyFirstCode.md#installing_the_example) document for instruction on how to install this example.Next you need to make sure you have a key bound to `"ToggleFlyWalk"`. By default, in the Runtime, this is the `'f'` key. If you are not using the Runtime, or have unbound the key for some reason, you need to bind it by typing:`set input f ToggleFlyWalk`at the in-game console (bring up the console by pressing the `'~'` key). Oh course you don't have to bind flying to the `'f'` key but it works out well. Now in the game you can press your flying key and the pawn will switch between flying and walking.To do make the pawn dance you need to bind a key to `"DoDance"`. You can do this by typing:`set input g DoDance`at the in-game console. Now when you press `'g'` (or some other key if you don't want to bind dancing to `'g'`) your pawn will do a little shimmy. Honestly, it isn't that much like a dance but it should get the point across.
