# My First Pawn

*Created by Chris Linder (DemiurgeStudios?) on 11-7-03 for the 2226 builds. Updated by Chris Linder (DemiurgeStudios?). Last updated by Michiel Hendriks, changed animation code for 3323.*

* [My First Pawn](MyFirstPawn.md#my-first-pawn)
  + [Related Documents](MyFirstPawn.md#related-documents)
  + [Introduction](MyFirstPawn.md#introduction)
  + [Class Setup](MyFirstPawn.md#class-setup)
  + [A New Model](MyFirstPawn.md#a-new-model)
  + [PointOfView](MyFirstPawn.md#pointofview)
  + [Pawn Movement and Animation](MyFirstPawn.md#pawn-movement-and-animation)
    - [Movement Animation](MyFirstPawn.md#movement-animation)
    - [Jumping, Landing, and Falling](MyFirstPawn.md#jumping-landing-and-falling)
    - [Idling](MyFirstPawn.md#idling)
    - [User Controlled Animation](MyFirstPawn.md#user-controlled-animation)
  + [Scripting Physics](MyFirstPawn.md#scripting-physics)
  + [Installing the Example](MyFirstPawn.md#installing-the-example)
    - [Unreal Runtime](MyFirstPawn.md#unreal-runtime)
    - [Code Drop, UDNBuild, UDNBuildOff](MyFirstPawn.md#code-drop-udnbuild-udnbuildoff)
  + [Using these Pawns in Net-Play](MyFirstPawn.md#using-these-pawns-in-net-play)
  + [Making Changes to the Example - Using the Example in UnrealEd](MyFirstPawn.md#making-changes-to-the-example---using-the-example-in-unrealed)

## Related Documents

[MyFirstCode](MyFirstCode.md), [MyFirstController](MyFirstController.md), [MyFirstGameInfo](MyFirstGameInfo.md), [MyFirstHUD](MyFirstHUD.md)

## Introduction

If you have not looked over the [MyFirstCode](MyFirstCode.md) document you should do that first.This document goes over how to make a simple pawn class that will move around in the world and animate properly. Animating properly includes walking, running, crouch walking, swimming, flying, jumping, falling, landing, and idling. Animating properly also include functionality for playing arbitrary animations not based on movement. All these animations will work properly in a net game. This document includes not only the class to make pawns animate properly but two subclasses, *ExampleBoy* and *ExampleGirl*, that illustrate how to use the animation code with different models. The guy and the girl are very lightweight classes that only adjust defaultproperties.This document includes the UnrealScript source code as well as the compiled \*.u file and the animation and texture packages to make everything work. See [Installing the Example](MyFirstPawn.md#installing-the-example) below for details on seeing this pawn example in action.This example can be used in any 2226 build of the engine including the straight code drop, UDNBuild, UDNBuildOff, and the Runtime or a 3323 (and maybe later) build of the engine.

## Class Setup

This example is composed of three classes, *ExamplePawn.uc*, *ExampleGirl.uc*, and *ExampleBoy.uc*. *ExamplePawn* contains the main functionality for animation and movement. *ExampleGirl* and *ExampleBoy* both extend *ExamplePawn* and do nothing more than specify their own models, set of animations, and collision cylinder in defaultproperties.

## A New Model

Probably the biggest part of making a new pawn is making a new model for that pawn. For more information on how to create a character model see the [ModelingTableOfContents](ModelingTableOfContents.md) document.Once you have a model in a UKX file you can use that model for your pawn by specifying the *Mesh* variable in defaultproperties like so:

```

Mesh=SkeletalMesh'UDN_CharacterModels_K.GenericMale'
- or -
Mesh=SkeletalMesh'UDN_CharacterModels_K.GenericFemale'
```

In some cases the imported model will not be the right size or orientated properly. You can alter the scale, location, and orientation of the modeling in the Animation Browser as described in the [AnimBrowserReference](../Content%20Creation/Animation/AnimBrowserReference.md#mesh).You also need to adjust the *CollisionRadius* and *CollisionHeight* of the collision cylinder for the model in defaultproperties of the class.

## PointOfView

There is a function, `simulated function bool PointOfView()` which is called when the pawn is possessed by the controller. This return value of this function determines if the camera will be third person (true) or first person (false). *ExamplePawn* adds the *bStartBehindView* variable so pawns can just set this variable in defaultproperties as opposed to overriding *PointOfView* to change how the camera starts.

## Pawn Movement and Animation

Most of the animation for *ExamplePawn* is done using physics based animation. Physics based animation means that the motion of the pawn determines what animation the pawn is playing. This is the method with which animation is generally done in the Unreal engine. Not only does it work in single player but it is very good for multiplayer situations because each client just looks at the motion of a given pawn to see what animation should be playing; no extra information needs to be transmitted. To enable physics based animation, *bPhysicsAnimUpdate* is set to `true` in defaultproperties.For more information on physics based animation, see the [PhysicsBasedAnim](https://udn.epicgames.com/Two/PhysicsBasedAnim) document. This document is based on the 2226 code drop but it should still be helpful.For v3323 and up you can ignore the next sections up to [User Controlled Animation](MyFirstPawn.md#user-controlled-animation), it's not completely relevant because the physics based animation has changed. Read the [PhysicsBasedAnim](https://udn.epicgames.com/Two/PhysicsBasedAnim) document for more information about this. In v3323 the below UnrealScript isn't needed, you just have to set the correct variables.

### Movement Animation

To do movement physics based animation uses six animation names to play animation based on how the pawn is moving. These animation names are:

```

MovementAnims[0]      //Forward
MovementAnims[1]      //Back
MovementAnims[2]      //Left
MovementAnims[3]      //Right
TurnLeftAnim
TurnRightAnim
```

When the pawn is moving forward the animation specified by *MovementAnims[0]* is looped. When the pawn is moving left the animation specified by *MovementAnims[2]* is looped. If the pawn is moving forward and left, the forward and left animations are blended together using animation channels and then looped. When the pawn is standing still and rotating either *TurnLeftAnim* or *TurnRightAnim* is looped. The faster the pawn rotates the faster the turning animation is played.You might be wondering how six animations account for all the different type of animation such as walking, running, crouching, swimming, etc... The answer involves the function `simulated function PlayMoving()` which is called whenever a player changes their movement type. This means the player changed from running to walking or falling to walking, or flying to falling. *PlayeMoving* calls other functions based on the type of movement the pawn is currently doing which reset the *MovenmentAnims* and also the turn animations in some cases. For example if *PlayMoving* is called and `(Physics == PHYS_Flying)`, then *AnimateFlying()* is called. *AnimateFlying()* is as follows:

```

// Play appropriate flying animations
simulated function AnimateFlying()
{
   MovementAnims[0]=FlyingAnims[0];
   MovementAnims[1]=FlyingAnims[1];
   MovementAnims[2]=FlyingAnims[2];
   MovementAnims[3]=FlyingAnims[3];
}
```

Flying does not use the turn animations so those are not reset. Crouching does use turn animations and *AnimateCrouchWalking()* is as follows:

```

// Play appropriate crouching animations
simulated function AnimateCrouchWalking()
{
   MovementAnims[0]=CrouchAnims[0];
   MovementAnims[1]=CrouchAnims[1];
   MovementAnims[2]=CrouchAnims[2];
   MovementAnims[3]=CrouchAnims[3];
   TurnLeftAnim=CrouchTurnAnims[0];
   TurnRightAnim=CrouchTurnAnims[1];
}
```

*PlayeMoving* and the *Animate...()* functions account for all movement animation except for jumping, landing, and falling which are covered below.

### Jumping, Landing, and Falling

Jumping, landing, and falling are handled by the *PlayJump*, *PlayLandingAnimation*, and *PlayFalling* which are all functions the engine calls when it the pawn is doing those respective things. *PlayJump* and *PlayFalling* are very simple and are listed below:

```

simulated event PlayJump()
{
   AnimBlendToAlpha(LANDINGCHANNEL,0,0.0);
   if ( (Acceleration.X != 0) || (Acceleration.Y != 0) )
      PlayAnim(JumpMovingAnim, 1.0, 0.1);
   else
      PlayAnim(JumpStandingAnim, 1.0, 0.1);
}

simulated event PlayFalling()
{
   LoopAnim(FallingAnim, 1.0, 0.5);
}
```

In *PlayJump*, *AnimBlendToAlpha* is called at the beginning because the landing channel described below was interfering with jumping multiple times in quick succession.In the case of landing, I needed to specify an animation channel because if I played it on the default (channel 0), the movement animations would overwrite the landing animation. Because I used a channel higher than all the movement animations, I needed to blend the alpha of that channel back to 0.0 after the land animation was done playing or else no movement animations would be seen. This is done in *AnimEnd*. The functions below illustrate how this is done:

```

simulated event PlayLandingAnimation(float ImpactVel)
{
   AnimBlendParams(LANDINGCHANNEL, 1.0, 2.0, 2.0);
   PlayAnim(LandAnim, 0.4, 0.0, LANDINGCHANNEL);
}

simulated event AnimEnd(int Channel)
{
   Super.AnimEnd(Channel);

   ...
   if(Channel == LANDINGCHANNEL)
   {
      AnimBlendToAlpha(LANDINGCHANNEL,0,0.5);
   }
}
```

### Idling

Idling is very simple. When the engine detects that the pawn is just standing there, `simulated function PlayWaiting()` is called. This function just calls *LoopAnim* with the appropriate animation based on the state of the pawn (see the function below). When *LoopAnim* is called, it specifies a rate, `"1.0"`, and a tween time, `"0.2"`. This causes the animation to play at the normal rate and tween from existing animations in 0.2 seconds. Since no channel is specified (one of the optional parameters of *LoopAnim*), the animation is played on channel 0 and affects the whole skeleton. Movement animations are played on higher channels so when the character starts to move, the idle will be blended over and not be seen.

```

// Play appropriate idle animations
simulated function PlayWaiting()
{
   if(Physics == PHYS_Falling)
      LoopAnim(FallingAnim, 1.0, 0.2);
   else if(Physics == PHYS_Flying)
      LoopAnim(FlyIdle, 1.0, 0.2);
   else if(Physics == PHYS_Swimming)
      LoopAnim(SwimIdle, 1.0, 0.2);
   else
   {
      if(bIsCrouched)
         LoopAnim(CrouchIdle, 1.0, 0.2);
      else
         LoopAnim(StandIdle, 1.0, 0.2);
   }
}
```

### User Controlled Animation

User controlled animations are when the user presses a button or executes a command and the pawn plays an animation, like taunting in UT2004 for example. This is fairly easy in a single player situation. It unfortunately gets much harder in a net game because as mentioned [above](MyFirstPawn.md#pawn-movement-and-animation), animation is not sent over the network.This is why the function `simulated event SetAnimAction(name NewAction)` and the variable `var name AnimAction` exist. They are designed to work together to send animation data from the server to all clients. If *SetAnimAction* is called on the server, it changes *AnimAction* which is replicated from the server to all clients. When the clients receive the new *AnimAction*, code in C++ detects if the *AnimAction* is new and then calls *SetAnimAction* on that client with the new animation which is then played by *SetAnimAction*. Once the animation is done playing, *AnimAction* is set to '' on both the client and the server so that the next time *SetAnimAction* is called, everything will work again. The code for this is as follows:

```

//Called to have all clients play a single animation in the idle animation channel
simulated event SetAnimAction(name NewAction)
{
   AnimAction = NewAction;
   PlayAnim(NewAction); //Play on base channel, which is the idle channel
   bPlayedAnimAction = true;
}

simulated event AnimEnd(int Channel)
{
   Super.AnimEnd(Channel);

   if(Channel == 0 && bPlayedAnimAction) //idle channel
   {
      PlayWaiting(); //reset to normal idle
      bPlayedAnimAction = false;
      AnimAction = '';
   }
   ...
}
```

## Scripting Physics

When you are using scripted sequences to control pawns, the *ScriptedController* expects the function *SetMovementPhysics()* to be implemented. *SetMovementPhysics* is defined in *Pawn.uc* but it has no body. If you do not have your own implementation, the pawn you are trying to script will just hang in the air with its physics equal to "PHYS\_None". The following implementation of *SetMovementPhysics* is simple and works well.

```

// Sets up Physics correctly for Scripted Sequences
function SetMovementPhysics()
{
   if (Physics == PHYS_Falling)
      return;
   if ( PhysicsVolume.bWaterVolume )
      SetPhysics(PHYS_Swimming);
   else
      SetPhysics(PHYS_Walking);
}
```

## Installing the Example

### Unreal Runtime

If you are using the Runtime, simply download the [examplepawns.zip](../assets/examplepawns.zip)), unzip it and run *ExamplePawns.urm*. If you can not simply run *ExamplePawns.urm* this probably means you unchecked the "Runtime modification association" box when installing the Runtime. In that case you will have to follow the steps below:

1. Open [examplepawns.zip](../assets/examplepawns.zip) and extract *ExamplePawns.urm* to the `"System"` directory of the Runtime.
2. Open a command prompt in the `"System"` directory of the Runtime.
3. Type `"setup install ExamplePawns.urm"`

In either case, follow the instructions presented in the install window and this will install the example pawns for the Runtime.Once the pawns are installed you can use them in several ways. You can alter your *User.ini* to specify the type of pawn to. In the `[DefaultPlayer]` section of *User.ini* set *Class* as follows:

```

Class=MyFirstExample.ExampleBoy
- or -
Class=MyFirstExample.ExampleGirl
```

You can also run the game from the command prompt with either of the following lines. This method will alter *User.ini* as well.`UE2Runtime EM_Runtime?Class=MyFirstExample.ExampleBoy`
  
- or -  
`UE2Runtime EM_Runtime?Class=MyFirstExample.ExampleGirl`Another way is to type one of the following lines in the console in-game. This method will also alter *User.ini*.`Open EM_Runtime?Class=MyFirstExample.ExampleBoy`
  
- or -  
`Open EM_Runtime?Class=MyFirstExample.ExampleGirl`

### Code Drop, UDNBuild, UDNBuildOff

If you are using the UDNBuild or UDNBuildOff, download [myfirstpawn_udnbuild.zip](../assets/myfirstpawn_udnbuild.zip) and unzip it in your build of the engine.If you are using the 2226 code drop, download [myfirstpawn_codedrop.zip](../assets/myfirstpawn_codedrop.zip) and unzip it in your build of the engine. For 3323 and up use download [myfirstexample_codedrop3323.zip](../assets/myfirstexample_codedrop3323.zip)At this point you can play with the new pawn by altering your *User.ini* to specify the type of pawn. In the `[DefaultPlayer]` section of *User.ini* set *Class* as follows:

```

Class=MyFirstExample.ExampleBoy
- or -
Class=MyFirstExample.ExampleGirl
```

You can also run the game from the command line with these arguments. This method will alter *User.ini* as well.`UT2004 <YourMap>?Class=MyFirstExample.ExampleBoy`
  
- or -  
`UT2004 <YourMap>?Class=MyFirstExample.ExampleGirl`Another way is to type one of the above lines in the console in-game except replacing "UT2004" with "Open". This method will also alter *User.ini*.

## Using these Pawns in Net-Play

If you would like to use these pawns in net play you have to do a few things on the computer hosting the game.First edit *<YourGame.ini>* (*UE2Runtime.ini* or *UT2004.ini* for example) and include `"MyFirstExample"` in your *ServerPackages* list. The *ServerPackages* list is in the `[Engine.GameEngine]` section of the INI file and you can just add the following line to that section:`ServerPackages=MyFirstExample`Next you must rebuild the MD5 database. Do this by opening a command prompt in the "System" directory of your build of the engine and then type:

```

UCC MASTERMD5 -c *.U
```

Now you can host a game and other people can connect to it and you can all run/fly/swim around together. You can host a game by typing the following at a command prompt in the system directory:`UE2Runtime <YourMap> -server`
  
- or -  
`UW <YourMap> -server`You can connect to server as described above in the [Installing the Example](MyFirstPawn.md#installing-the-example) section but instead of the map name, use the IP address of the server. For example, from the command line one might type:`UE2Runtime 192.168.1.112?Class=MyFirstExample.ExampleGirl`

## Making Changes to the Example - Using the Example in UnrealEd

If you wish to make changes to the given code or you want to place *ExamplePawns* in UnrealEd, you will have to add "MyFirstExample" to the *EditPackages* lists in *<your\_game>.ini* (*UW.ini* or *UE2Runtime.ini* for example). Do this by opening your INI file and doing a text search for "EditPackages" and then add the line "EditPackages=MyFirstExample" to the bottom of the list. There are two lists so make sure to add the line to both lists. If you are making changes to the code you can recompile the changes you made by deleting the existing *MyFirstExample.u* file in the system directory and typing `"ucc make"` at the command line.
