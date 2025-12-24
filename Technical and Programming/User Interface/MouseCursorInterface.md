# Mouse Cursor Interface Example

*Last updated by Martin Actor ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)), because to not to would be a crime against coolness. Original author was Martin Actor ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).*

* [Mouse Cursor Interface Example](#mouse-cursor-interface-example)
  + [Introduction](#introduction)
  + [Preparation](#preparation)
  + [Execution](#execution)
    - [PlayerController](#playercontroller)
    - [HUD](#hud)
  + [Genesis](#genesis)

## Introduction

This document is to demonstrate how to add a mouse cursor interface to your project, wholly in UnrealScript. While there may be room for optimization (moving some UnrealScript to native, for example), the purpose of this document is to show just how simple the task can be made to be.So, if you're looking for a way to have a player interface using the mouse as a mouse (yet still within the normal 3d world), this document will surely interest you.It is worthy to note that the code presented in this document was written with the runtime build (2226).Also, if you aren't starting a new project from scratch and are just interested in the implemention, feel free to skip to the next section.

## Preparation

The following are classes that we will be subclassing (extending). Provided with each class listed is a short explanation of what the class does and why we'll be subclassing it.`PlayerController` - this class is where the logic for player control resides. Equally as important, because it's good to know how our code will work over a network, it houses the network handling for player movement commands. What makes this important is that our code will be entirely client side, meaning that in a network game, the server knows nothing about what the local player is doing in regards to the mouse cursor interface. The player movement control code is segregated into a number of different states, depending on the physics mode the player's Pawn is in. Our subclass will have a new state to encompass the new interface method.`HUD` - this class is where all manual screen rendering is done in-game (for things like health displays, ammo, objectives, inventory, etc.). We'll be subclassing this class in order to handle rendering of a mouse cursor as well as telling our custom PlayerController class the size of the screen.

## Execution

Though it may seem like the following would work by itself, the code below is intended to be either added to (to fill out other project implementation requirements) or to be added to your current (and relevant) custom classes.

### PlayerController

This is the more heavy duty class (as opposed to the HUD class), code-wise. If you're starting from scratch, in your custom package directory, under the Classes directory, create an UnrealScript file (call it CustomPlayer.uc if you want an example). It should look something like this :

```

class CustomPlayer extends PlayerController;

defaultproperties
{
}
```

This is as basic as a class gets. At this stage, you could rebuild your custom package and have no warnings nor errors, but also no additional functionality. So, we need to get this showboat going.We need to know where our mouse cursor currently is on the screen, so we add the follow below the class declaration :

```

var vector PlayerMouse;
```

This vector represents the 2d (we will be ignoring the Z component of the vector with this implementation, but if you want to z-order the mouse cursor, or even scale the cursor or whatever, the Z component is available to you) position of the mouse cursor on the screen, with the origin at the center of the screen.We also need to know the size of the screen currently (this will become more apparent later on). To that end, we add the following after the previous variable declaration :

```

var float LastHUDSizeX;
var float LastHUDSizeY;
```

We don't want the player to be doing anything else, control-wise, while they're in mouse control mode, so we need a custom state (added before the defaultproperties line) :

```

state PlayerMousing
{
}
```

Our custom state doesn't do anything for us yet, so let's fix that. The following block of code is our entire PlayerMousing state :

```

state PlayerMousing
{
   exec function Fire(float f)
   {
      // do stuff here for when players click their fire/select button

      return;
   }

   simulated function PlayerMove(float DeltaTime)
   {
      local vector MouseV, ScreenV;

      // get the new mouse position offset
      MouseV.X = DeltaTime * aMouseX / (InputClass.default.MouseSensitivity * DesiredFOV * 0.01111);
      MouseV.Y = DeltaTime * aMouseY / (InputClass.default.MouseSensitivity * DesiredFOV * -0.01111);

      // update mouse position
      PlayerMouse += MouseV;

      // convert mouse position to screen coords, but only if we have good screen sizes
      if ((LastHUDSizeX > 0) && (LastHUDSizeY > 0))
      {
         ScreenV.X = PlayerMouse.X + LastHUDSizeX * 0.5;
         ScreenV.Y = PlayerMouse.Y + LastHUDSizeY * 0.5;
         // here is where you would use the screen coords to do a trace or check HUD elements
      }

      return;
   }
}
```

There are, immediately, two things worthy of note - the Fire exec function does nothing for you, nor has any supporting code, and that the PlayerMove looks woefully sparse, in comparison to other versions found in the other states in PlayerController. The Fire function is there as a placeholder and helper to show where code for "the user has clicked the mouse" needs to go. The PlayerMove function, however, completely removes all player movement control while the player is in the PlayerMousing state. The reason for this is, if you do not clear everything out, the player will be able to either move or rotate the camera while in the mousing mode. If this is desirable, you will have to also take a look at the PlayerInput class, as it uses the mouse variables aMouseX and aMouseY to modify player rotation and/or movement (which you will want to disallow while in the PlayerMousing state).The key work is done with the MouseV assignment lines. We take the mouse input vars (which are offset values, i.e. how far the mouse has moved in arbitrary mouse coord units since the last Tick or input poll), scale them by the time taken for the last engine loop (to produce consistant mouse moving feel regardless of framerate), and further scale them by the mouse sensitivity, player Field Of View, and the magic values pulled from PlayerInput, which all results in the mouse moving consistantly across the player's screen, regardless of screen size and player FOV.After the mouse position updating is done, the last block of code converts the mouse position to screen coordinates, for use with a ScreenToWorld call or whatever you might need.With the PlayerMousing state done, our custom PlayerController class has the necessary code for allowing the player to control a mouse cursor. However, we can't see anything! It's time to work on the HUD.

### HUD

The HUD class we'll be working on will be very basic. If you're starting from scratch, create a new UnrealScript file in your package's classes directory (CustomHUD, for example). It should look something like this :

```

class CustomHUD extends HUD;

var Texture MouseCursorTexture;

defaultproperties
{
   //MouseCursorTexture=Texture'CustomTexturePackage.MouseCursorTexture'
}
```

We've added more than the base requirements this time. In the defaultproperties, the commented out line (when uncommented) sets the texture reference you would use for the mouse cursor texture. Now, we need to override the most important event function in the class :

```

simulated event PostRender(Canvas C)
{
   Super.PostRender(Canvas C);

   return;
}
```

PostRender is the event function that the engine calls to tell the HUD class to render to screen what it wants to render. What we've done is override PostRender and told it to do whatever the parent class does (via the Super.PostRender call). We need to add a bit more in order to see where our mouse cursor lays :

```

simulated event PostRender(Canvas C)
{
   Super.PostRender(Canvas C);

   CustomPlayer(PlayerOwner).LastHUDSizeX = C.SizeX;
   CustomPlayer(PlayerOwner).LastHUDSizeY = C.SizeY;

   if (PlayerOwner.IsInState('PlayerMousing')) DrawMouseCursor(C);

   return;
}
```

We've added calls to set the screen size variables in CustomPlayer, and we make a call to a new function, DrawMouseCursor :

```

simulated function DrawMouseCursor(Canvas C)
{
   local float XPos, YPos;

   C.SetDrawColor(255, 255, 255);
   C.Style = ERenderStyle.STY_Alpha;

   // find position of cursor, and clamp it to screen
   XPos = CustomPlayer(PlayerOwner).PlayerMouse.X + C.SizeX / 2.0;
   if (XPos < 0)
   {
      CustomPlayer(PlayerOwner).PlayerMouse.X -= XPos;
      XPos = 0;
   }
   else if (XPos >= C.SizeX)
   {
      CustomPlayer(PlayerOwner).PlayerMouse.X -= (XPos - C.SizeX);
      XPos = C.SizeX - 1;
   }
   YPos = CustomPlayer(PlayerOwner).PlayerMouse.Y + C.SizeY / 2.0;
   if (YPos < 0)
   {
      CustomPlayer(PlayerOwner).PlayerMouse.Y -= YPos;
      YPos = 0;
   }
   else if (YPos >= C.SizeY)
   {
      CustomPlayer(PlayerOwner).PlayerMouse.Y -= (YPos - C.SizeY);
      YPos = C.SizeY - 1;
   }

   // render mouse cursor
   C.SetPos(XPos, YPos);
   C.DrawIcon(MouseCursorTexture);

   return;
}
```

The DrawMouseCursor function is pretty simple. We make sure our rendering settings are how we want, and then we clamp the mouse cursor position to the screen area limits. After that, it's a simple matter of setting the drawing location for the canvas, and then rendering our mouse cursor texture (which is undefined in this example).

## Genesis

The above is all that's needed to get a mouse cursor interface started for your project. However, only a basis for expansion is provided here; your project's needs will determine just how you modify and add functionality (multiple cursors? selecting objects in 3d space? managing 2d windows?). Another consideration might be switching between mouse cursor control and normal player control. There aren't many games (nor mods for games) using the Unreal engine that present an interface dominated by mouse cursor control, and it always adds to the interest in the project when it does.

