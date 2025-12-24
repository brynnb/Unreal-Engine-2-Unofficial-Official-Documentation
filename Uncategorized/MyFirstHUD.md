# My First HUD

*Created by Chris Linder (DemiurgeStudios?) on 11-18-03 for 2226 builds. Last Updated by Chris Linder (DemiurgeStudios?). Last updated by Michiel Hendriks, small v3323 update.*

* [My First HUD](MyFirstHUD.md#My First HUD)
  + [Related Documents](MyFirstHUD.md#Related Documents)
  + [Introduction](MyFirstHUD.md#Introduction)
  + [ExampleHUD](MyFirstHUD.md#ExampleHUD)
  + [ExampleScoreboard](MyFirstHUD.md#ExampleScoreboard)

## Related Documents

[MyFirstCode](MyFirstCode.md), [MyFirstPawn](MyFirstPawn.md), [MyFirstController](MyFirstController.md), [MyFirstGameInfo](MyFirstGameInfo.md), [HeadsUpDisplayReference](../Technical and Programming/User Interface/HeadsUpDisplayReference.md), [CanvasReference](../Technical and Programming/User Interface/CanvasReference.md)

## Introduction

If you have not looked over the [MyFirstCode](MyFirstCode.md) document you should do that first.This document goes over how to create a simple Heads-Up-Display the reports how many times your avatar has "danced" (see [MyFirstController](MyFirstController.md) for more details). This example uses two classes to accomplish this goal. The first class, *ExampleHUD.uc* extends *HUD.uc* and displays in the lower right corner the number of times your avatar has danced. The second class, *ExampleScoreboard.uc*, which extends *ScoreBoard.uc*, is drawn instead of the HUD when you press 'F1'. The score board shows the names and scores of everyone in the current game, or at least those that fit on the screen.

## ExampleHUD

As mentioned above, *ExampleHUD* displays in the lower right corner the number of times your avatar has danced. The number of times your avatar has danced is stored in the *Score* variable in the *PlayerReplicationInfo* for your player. (See the [MyFirstController](MyFirstController.md#Dancing) document for more details.)In older builds (2226), the first thing we need to do before we can draw the HUD is to get at the *PlayerReplicationInfo*. The code below shows how to safely get the *PlayerReplicationInfo*. In 3323 and up this is already done by the base class.

```

var PlayerController PlayerOwner;
...


simulated function PostBeginPlay()
{
   Super.PostBeginPlay();
   PlayerOwner = PlayerController(Owner);
}


function DrawHUD(canvas Canvas)
{
   local Pawn PawnOwner;
   local PlayerReplicationInfo PawnOwnerPRI;
   ...

   // Get PlayerOwner
    if (PlayerOwner.ViewTarget == PlayerOwner)
   {
      PawnOwner = PlayerOwner.Pawn;
   }
   else if (PlayerOwner.ViewTarget.IsA('Pawn') && Pawn(PlayerOwner.ViewTarget).Controller != None)
   {
      PawnOwner = Pawn(PlayerOwner.ViewTarget);
   }
   else if ( PlayerOwner.Pawn != None )
   {
      PawnOwner = PlayerOwner.Pawn;
   }
   else
   {
      PawnOwner = None;
   }

   // Get PlayerReplication
   if ((PawnOwner != None) && (PawnOwner.Controller != None))
      PawnOwnerPRI = PawnOwner.PlayerReplicationInfo;
   else
      PawnOwnerPRI = PlayerOwner.PlayerReplicationInfo;

   ...
}
```

Once we have the *PlayerReplicationInfo* we can get the score for this player by accessing *PawnOwnerPRI.Score*.The next thing we need to do before we can draw the HUD is pick a font to use. Fonts in Unreal are tricky because they don't scale and you therefore need to pick the font you want based on the resolution of the screen. See the [HeadsUpDisplayReference](../Technical and Programming/User Interface/HeadsUpDisplayReference.md) and the [FontTutorial](FontTutorial.md) for more details. The fonts specified in the *FontArrayNames* array are sorted in a descending order and so smaller numbers indices are larger fonts. Fonts are accessed with the `static function Font LoadFontStatic(int i)` function which returns the font with the given index. The block of code below shows how an appropriate font size is picked.

```

function DrawHUD(canvas Canvas)
{
   ...

   //Get Font Size - (larger numbers are smaller fonts)
   if ( Canvas.ClipX <= 640 )
      FontSize=4;
   else if ( Canvas.ClipX <= 800 )
      FontSize=3;
   else if ( Canvas.ClipX <= 1024 )
      FontSize=2;
   else if ( Canvas.ClipX <= 1280 )
      FontSize=1;
   else if ( Canvas.ClipX <= 1600 )
      FontSize=0;
   else
      FontSize=0;
   Canvas.Font = LoadFontStatic(FontSize);

   ...
}

defaultproperties
{
   ...

   FontArrayNames(0)="ExampleFonts_T.ExampleFont38"
   FontArrayNames(1)="ExampleFonts_T.ExampleFont38"
   FontArrayNames(2)="ExampleFonts_T.ExampleFont34"
   FontArrayNames(3)="ExampleFonts_T.ExampleFont30"
   FontArrayNames(4)="ExampleFonts_T.ExampleFont26"
   FontArrayNames(5)="ExampleFonts_T.ExampleFont22"
   FontArrayNames(6)="ExampleFonts_T.ExampleFont18"
   FontArrayNames(7)="ExampleFonts_T.ExampleFont14"
   FontArrayNames(8)="ExampleFonts_T.ExampleFont10"

   ...
}
```

Now that we have the *Score* and the font we are ready to actually draw things on the HUD. The block of code below draws a texture in the lower right hand corner scaled based on the current resolution and then draws the current score on top of that texture. The text of the score is manually right justified using the *StrLen* function. See the [CanvasReference](../Technical and Programming/User Interface/CanvasReference.md) document for more details about the functions used below to draw the HUD.

```

function DrawHUD(canvas Canvas)
{
   ...

   // Draw Hud

   Canvas.SetDrawColor(255,255,255);
   HUDScoreScaleX = Canvas.ClipX/800;
   HUDScoreScaleY = Canvas.ClipY/600;
   HUDScorePosX = Canvas.ClipX - 256*HUDScoreScaleX;
   HUDScorePosY = Canvas.ClipY - 128*HUDScoreScaleY;
   Canvas.SetPos(HUDScorePosX, HUDScorePosY);
   Canvas.DrawTileScaled(HUDScoreBox, HUDScoreScaleX, HUDScoreScaleY);

   Canvas.SetDrawColor(230,240,240);
   Score = PawnOwnerPRI.Score;
   ScoreString = ""$Score;
   Canvas.StrLen(ScoreString,XL,YL);
   Canvas.SetPos(HUDScorePosX + 235*HUDScoreScaleX - XL, HUDScorePosY + 70*HUDScoreScaleY);
   Canvas.DrawText(Score);
}
```

## ExampleScoreboard

The scoreboard works by accessing the *GRI.PRIArray* which is defined in *ScoreBoard.uc* like so:`var() GameReplicationInfo GRI;`The *GameReplicationInfo* class defines the *PRIArray* as follows:`var() array PRIArray;`The *PRIArray* contains the player replication information for all the players in the game. With this array we can get all the player names and scores to display on the scoreboard.The actual drawing of the scoreboard is relatively straight forward but the code is somewhat lengthy because there is a lot to draw. The code is well documented and looking at the UnrealScript file *ExampleScoreboard.uc* would be the best way to understand what is going on. See the [HeadsUpDisplayReference](../Technical and Programming/User Interface/HeadsUpDisplayReference.md) and the [CanvasReference](../Technical and Programming/User Interface/CanvasReference.md) for more details about the functions used below to draw the HUD.
