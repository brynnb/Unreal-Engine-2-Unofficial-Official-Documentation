# HUD Reference

*Last updated by Michiel Hendriks, major v3323 update. Previously updated by Chris Linder (DemiurgeStudios?). Original author was Chris Linder ([chris@demiurgestudios.com](mailto:chris@demiurgestudios.com)) (DemiurgeStudios?); please feel free to send suggestions or comments.*

* [HUD Reference](#hud-reference)
  + [Intro](#intro)
  + [Structs](#structs)
    - [ConsoleMessage](#consolemessage)
    - [HUDLocalizedMessage](#hudlocalizedmessage)
  + [Variables](#variables)
    - [Used Variables](#used-variables)
    - [Unused Variables](#unused-variables)
  + [Exec Functions](#exec-functions)
    - [GrowHUD](#growhud)
    - [NextStats](#nextstats)
    - [ShowHud](#showhud)
    - [ShowScores](#showscores)
    - [ShowStats](#showstats)
    - [ShowDebug](#showdebug)
    - [ShrinkHUD](#shrinkhud)
  + [Events](#events) 
    - [AnnouncementPlayed](#announcementplayed)
    - [ConnectFailure](#connectfailure)
    - [ShowUpgradeMenu](#showupgrademenu)
    - [WorldSpaceOverlays](#worldspaceoverlays)
  + [Delegates](#delegates)
    - [OnBuildMOTD](#onbuildmotd)
    - [OnPostRender](#onpostrender)
  + [Functions](#functions)
    - [AddHudOverlay](#addhudoverlay)
    - [AddTextMessage](#addtextmessage)
    - [BuildMOTD](#buildmotd)
    - [CanvasDrawActors](#canvasdrawactors)
    - [ClearMessage](#clearmessage)
    - [CopyMessage](#copymessage)
    - [CreateKeyMenus](#createkeymenus)
    - [DisplayBadConnectionAlert](#displaybadconnectionalert)
    - [DisplayHit](#displayhit)
    - [DisplayMessages](#displaymessages)
    - [DisplayProgressMessage](#displayprogressmessage)
    - [Draw3DLine](#draw3dline)
    - [DrawCanvasLine](#drawcanvasline)
    - [DrawCinematicHUD](#drawcinematichud)
    - [DrawCrosshair](#drawcrosshair)
    - [DrawCustomBeacon](#drawcustombeacon)
    - [DrawInstructionGfx](#drawinstructiongfx)
    - [DrawHUD](#drawhud)
    - [DrawLevelAction](#drawlevelaction)
    - [DrawRoute](#drawroute)
    - [DrawSpectatingHud](#drawspectatinghud)
    - [DrawTypingPrompt](#drawtypingprompt)
    - [FadeZoom](#fadezoom)
    - [GetConsoleFont](#getconsolefont)
    - [GetFontSizeIndex](#getfontsizeindex)
    - [GetLocalStatsScreen](#getlocalstatsscreen)
    - [GetMediumFont](#getmediumfont)
    - [GetMediumFontFor](#getmediumfontfor)
    - [IsInCinematic](#isincinematic)
    - [LargerFontThan](#largerfontthan)
    - [LinkActors](#linkactors)
    - [LoadFont](#loadfont)
    - [LoadFontStatic](#loadfontstatic)
    - [LoadProgressFont](#loadprogressfont)
    - [LocalizedMessage](#localizedmessage)
    - [Message](#message)
    - [PlayReceivedMessage](#playreceivedmessage)
    - [PostRender](#postrender)
    - [PrintActionMessage](#printactionmessage)
    - [RemoveHudOverlay](#removehudoverlay)
    - [SetCropping](#setcropping)
    - [SetScoreBoardClass](#setscoreboardclass)
    - [SetTargeting](#settargeting)
    - [SpawnScoreBoard](#spawnscoreboard)
    - [StaticDrawCanvasLine](#staticdrawcanvasline)
    - [UseHugeFont](#usehugefont)
    - [UseLargeFont](#uselargefont)
    - [UseMediumFont](#usemediumfont)
    - [UseSmallFont](#usesmallfont)
  + [Functions that are not implemented.](#functions-that-are-not-implemented)
    - [CheckCountdown](#checkcountdown)
  + [Functions that are not called.](#functions-that-are-not-called)
    - [ProcessKeyEvent](#processkeyevent)
  + [Functions that are neither Implemented nor Called.](#functions-that-are-neither-implemented-nor-called)
    - [PlayStartupMessage](#playstartupmessage)
    - [DisplayPortrait](#displayportrait)
    - [DrawTargeting](#drawtargeting)
    - [SetInstructionKeyText](#setinstructionkeytext)
    - [SetInstructionText](#setinstructiontext)

## Intro

Despite the size of this document, the HUD is not that complicated. You will spend most of your time working with the HUD in the [DrawHUD](#drawhud) function. Here you will uses [Canvas](CanvasReference.md) functions to draw on the HUD. Also remember that pawns have their own *DrawHud(...)* function that will be called before the normal *DrawHUD(...)* function and you can use this to add specialized things to a given pawns HUD. Other than that you might want to check out the slightly old [HeadsUpDisplayTutorial](../../Uncategorized/HeadsUpDisplayTutorial.md) which goes over the HUD on a higher level than this reference.

## Structs

### ConsoleMessage

```

struct native ConsoleMessage
{
   var string Text;
   var color TextColor;
   var float MessageLife;
   var PlayerReplicationInfo PRI;
};
```

This is the structure used to store messages queued with the [Message](#message) function.

### HUDLocalizedMessage

```

struct HUDLocalizedMessage
{
    var class<LocalMessage> Message;
    var String StringMessage;
    var int Switch;
    var PlayerReplicationInfo RelatedPRI, RelatedPRI2;
    var Object OptionalObject;
    var float EndOfLife;
    var float LifeTime;

    var Font StringFont;
    var Color DrawColor;
    var EDrawPivot DrawPivot;
    var LocalMessage.EStackMode StackMode;
    var float PosX, PosY;
    var float DX, DY;

    var bool Drawn;
};
```

This is used for localized messages. `HUD.uc` does not uses localized messages but `HUDBase.uc` does so you can look there for an example if you want to use them. Also see [CopyMessage](#copymessage) and [ClearMessage](#clearmessage).Because the HUD class doesn't use this struct it has been moved to HUDBase in v3323.

## Variables

### Used Variables

Misc:

|  |  |
| --- | --- |
| PlayerController PlayerOwner | always the actual owner |
| Pawn PawnOwner | will be set to the viewtarget of the PlayerOwner for easy reference (v3323 and up) |
| PlayerReplicationInfo PawnOwnerPRI | set to the PRI of the PawnOwner, if it doesn't have any it will be set to the PRI of the PlayerOwner (v3323) |
| Console PlayerConsole | the console of the PlayerOwner (v3323) |
| ScoreBoard Scoreboard | used for drawing the scoreboard |
| Scoreboard LocalStatsScreen | used for ingame stats (v3323) |
| Actor VoteMenu | hook for mod authors (v3323) |

Settings:

|  |  |
| --- | --- |
| globalconfig float HudCanvasScale | Specifies amount of screen-space to use (for TV's). This is only used for drawing messages; it does not scale everything. |
| globalconfig float HudScale | Global Scale for all widgets (v3323) |
| globalconfig float HudOpacity | make everything transparent (v3323) |

Flags:

|  |  |
| --- | --- |
| bool bHideHUD | when true, neither *ScoreBoard.DrawScoreboard(...)* nor *DrawHUD(...)*, nor *DrawSpectatingHud(...)* are called |
| bool bShowScoreBoard | if false, the *ScoreBoard* is not drawn, pre-v3323 this variable was called `bShowScores` |
| bool bShowLocalStats | Show the local player stats (v3323) |
| bool bShowDebugInfo | if true, debugging info is drawn. See [ShowDebug](#showdebug) for more details. |
| bool bHideCenterMessages | don't draw centered messages (screen center being used) |
| bool bBadConnectionAlert | display warning about bad connection |
| config bool bMessageBeep | when you get a message, it beeps |
| globalconfig bool bShowWeaponInfo | Show information about the current weapon (v3323) |
| globalconfig bool bShowPersonalInfo | Show personal info like armor and health (v3323) |
| globalconfig bool bShowPoints | Show the players score (v3323) |
| globalconfig bool bShowWeaponBar | Show the weapon information bar (v3323) |
| globalconfig bool bCrosshairShow | Show the crosshair (v3323) |
| globalconfig bool bShowPortrait | Show the player portrait of the chatting player. (v3323) |
| globalconfig bool bShowPortraitVC | Show portrait for voice chat. (v3323) |
| globalconfig bool bNoEnemyNames | Show enemy names (v3323) **todo: ??** |
| globalconfig bool bSmallWeaponBar | Use a smaller weapon bar (v3323) |
| bool bShowVoteMenu | Show the voting menu (for map\kick voting) (v3323) |

Progress Messages (see [DisplayProgressMessage](#displayprogressmessage)):

|  |  |
| --- | --- |
| localized string ProgressFontName | name of progress font |
| Font ProgressFontFont | font itself |
| float ProgressFadeTime | time for font fade |
| Color MOTDColor | Progress Font Color |

Action Messages (see [PrintActionMessage](#printactionmessage)):
Some of these variables have been moved (and renamed) to HudBase and others have completely been removed from the HUD class in v3323.

|  |  |
| --- | --- |
| localized string LoadingMessage | loading message |
| localized string SavingMessage | saving message |
| localized string ConnectingMessage | connecting message |
| localized string PausedMessage | pause message |
| localized string PrecachingMessage | precaching message |

Console Messages (see [Message](#message)):

|  |  |
| --- | --- |
| globalconfig int ConsoleMessageCount | The number of messages queued with the [Message](#message) function to be displayed. |
| ConsoleMessage TextMessages[8] | This is the queue of messages queued with the [Message](#message) call. |
| float ConsoleMessagePosX, ConsoleMessagePosY | These are ratios of screen size of where the messages queued with [Message](#message) will be drawn. |

Fonts:

|  |  |
| --- | --- |
| font SmallFont | Small system font (up to v3323) |
| font MedFont | Medium system font (up to v3323) |
| font BigFont | Big system font (up to v3323) |
| font LargeFont | Largest system font (up to v3323) |
| localized string FontArrayNames[9] | This is an array or font names with each larger index assumed to be smaller font. |
| Font FontArrayFonts[9] | This is the array of fonts specified by FontArrayNames. |
| globalconfig int ConsoleFontSize | The default index for the FontArrayNames if the canvas is <= 640 in width. Large indices will be used if the canvas is larger. The assumption is that larger indices have larger fonts. See [LoadFont](#loadfont) for more details. |
| int FontScreenWidthMedium[9] | This is a list you should fill in with the screen widths that are appropriate for each index of the FontArrayFonts for medium sized fonts. |
| int FontScreenWidthSmall[9] | This is a list you should fill in with the screen widths that are appropriate for each index of the FontArrayFonts for small fonts. |

Cinematics (v3323 and up):

|  |  |
| --- | --- |
| SceneSubtitles SubTitles | Used by HudBase to display subtitles during a cinematic. |
| array Overlays | Overlays that are draw when the HUD is in cinematic mode. See [DrawCinematicHUD](#drawcinematichud) |

### Unused Variables

|  |  |
| --- | --- |
| string HUDConfigWindowType | ? |
| HUD nextHUD | list of huds which render to the canvas |
| Color ConsoleColor | this looks like it does something and it is used in many cases but secretly, it does nothing because the value is always overwritten |
| globalconfig int MessageFontOffset | ? |

Voice chat (all are set natively) (v3323 and up):

|  |  |
| --- | --- |
| const float LastVoiceGain |  |
| const float LastVoiceGainTime |  |
| int LastPlayerIDTalking |  |
| const float LastPlayerIDTalkingTime |  |

## Exec Functions

### GrowHUD

`exec function GrowHUD()`Show more details on the HUD. The details have the following order (from most important to least important):

1. bShowWeaponInfo
2. bShowPersonalInfo
3. bShowPoints
4. bShowWeaponBar
5. bSmallWeaponBar

(v3323 and up).

### NextStats

`exec function NextStats()`Shows the next local stats screen. (v3323 and up)

### ShowHud

`exec function ShowHud()`Toggles `bShowHud` and saves the current configuration. (v3323 and up)

### ShowScores

`exec function ShowScores()`ShowScores toggles the showing of the *Scoreboard*.

### ShowStats

`exec function ShowStats()`Toggles the `bShowLocalStats` variable to display local stats. (v3323 and up)

### ShowDebug

`exec function ShowDebug()`ShowDebug toggles the showing of debug information. This information includes that which is displayed in the *PlayerOwner.ViewTarget.DisplayDebug(...)* function as well as that which is displayed in the *DrawRoute()* function.

### ShrinkHUD

`exec function ShrinkHUD()`Show less details. (v3323 and up)

## Events

### AnnouncementPlayed

`event AnnouncementPlayed( Name AnnouncerSound, byte Switch )`Stub. This is used by the Assault gametype in UT2004 to update\show the the next objective list. (v3323)

### ConnectFailure

`event ConnectFailure(string FailCode, string URL)`This event should be called when the client fails to connect to a server. The only problem is that the line in C++ that calls this event is commented out in 2110 with a "// @@FixMeJoe" tag. Since v2226 this event is no longer used. In v3323 the ConnectFailure event of the Console is called when the connection failed.

### ShowUpgradeMenu

`event ShowUpgradeMenu()`This event is called when the engine version is less than the *MinNetVer* of the server you are trying to connect with. This function as been removed in v3323, the upgrade notice is now properly handled through the ConnectFailure event in the console.

### WorldSpaceOverlays

`simulated event WorldSpaceOverlays()`This event is called from C++ when it is appropriate to draw overlays in world space. It is from this function that [Draw3DLine](#draw3dline) should be called. WorldSpaceOverlays calls [DrawRoute](#drawroute) if *bShowDebugInfo* is true and there is a view target.

## Delegates

Only available in v3323 and up

### OnBuildMOTD

`delegate OnBuildMOTD(HUD Sender)`Called when building the message of the day

### OnPostRender

`delegate OnPostRender(HUD Sender, Canvas C)`Called when PostRender is finished.

## Functions

### AddHudOverlay

`simulated function AddHudOverlay(HudOverlay Overlay)`Add a new *HudOverlay* to the `Overlays` list. (v3323 and up)

### AddTextMessage

`function AddTextMessage(string M, class MessageClass, PlayerReplicationInfo PRI)`This function is called by [Message](#message) to add messages to the queue that [DisplayMessages](#displaymessages) draws.

### BuildMOTD

`simulated function BuildMOTD()`Constructs the message of the day from the GameReplicationInfo and sets it to the `MOTD` array. Before the MOTD is build the *OnBuildMOTD()* delegate is called. (v3323 and up)

### CanvasDrawActors

`function CanvasDrawActors( Canvas C, bool bClearedZBuffer )`Specific function to use *Canvas.DrawActor()*. Clear Z-Buffer once, prior to rendering all actors. (v3323 and up)

### ClearMessage

`function ClearMessage(out HUDLocalizedMessage M)`This function clears out a HUDLocalizedMessage.

### CopyMessage

`function CopyMessage(out HUDLocalizedMessage M1, HUDLocalizedMessage M2)`This function copies HUDLocalizedMessage M2 into M1.

### CreateKeyMenus

`simulated function CreateKeyMenus()`Stub. This is used by HudBase to spawn the vote menu. The function is called from *PostBeginPlay*. (v3323 and up)

### DisplayBadConnectionAlert

`function DisplayBadConnectionAlert()`This function is called when the connection is bad. You are intended to implement this function; it is not yet implemented.

### DisplayHit

`function DisplayHit(vector HitDir, int Damage, class damageType)`Calls *PlayerOwner.ClientFlash(...)* , used for a visual hit notification. (v3323 and up).

### DisplayMessages

`function DisplayMessages(Canvas C)`This function does that actual work for displaying the messages created with [Message](#message). This is called from [PostRender](#postrender).

### DisplayProgressMessage

`simulated function DisplayProgressMessage(Canvas C)`This function displays the current progress messages, set in PlayerController by the SetProgressMessage(...) function. There are 4 possible lines of progress messages. These messages fade after *ProgressTimeOut* has elapsed from the start of the level or since the last time SetProgressTime(...) in PlayerController was called.

### Draw3DLine

`native final function Draw3DLine(vector Start, vector End, color LineColor)`This draws a line in 3D. This is used in the DrawRoute() function to draw paths for example. This function should be used when the engine calls the event WorldSpaceOverlays().

### DrawCanvasLine

`native final function DrawCanvasLine(float X1, float Y1, float X2, float Y2, color LineColor)`A shorthand for calling *DrawLine(...)* in the canvas of the viewport of the player owner. (v3323 and up)

### DrawCinematicHUD

`simulated function DrawCinematicHUD( Canvas C )`Called when viewing a Matinee cinematic. This render additional overlays. This is called by *PostRender()* only when `PlayerOwner.bViewingMatineeCinematic` is true. (v3323 and up)

### DrawCrosshair

`simulated function DrawCrosshair(Canvas C)`Stub. Used for drawing the weapon crosshair. In HudBase this is called from the *DrawInstructionGfx()* function. (v3323 and up.)

### DrawCustomBeacon

`function DrawCustomBeacon(Canvas C, Pawn P, float ScreenLocX, float ScreenLocY)`Draws a player beacon (player name and the texture from `PlayerOwner.TeamBeaconTexture` ) on the canvas for pawn *P* and the location *(ScreenLocX, ScreenLocY)* . (v3323 and up)

### DrawInstructionGfx

`simulated function DrawInstructionGfx( Canvas C )`Stub. Called in *PostRender* when `!bHideHud` and `PawnOwner`  None= . (v3323 and up)

### DrawHUD

`function DrawHUD(canvas Canvas);`This function is called from [PostRender](#postrender) when it is appropriate to draw the HUD. You are intended to implement this function; it is not yet implemented.

### DrawLevelAction

`function bool DrawLevelAction( canvas C )`This draws messages for level loading, saving, connecting to a server, and precaching. It also draws the pause message.

### DrawRoute

`simulated function DrawRoute()`This function is useful for debugging AIs. It will show where the AIs are focusing in red, their current path in green, and their current path segment in white.

### DrawSpectatingHud

`function DrawSpectatingHud (Canvas C)`This function is called from [PostRender](#postrender) when:

```

( (PlayerOwner == None) ||
  (P == None) ||
  (P.PlayerReplicationInfo == None) ||
  PlayerOwner.IsSpectating() )
```

and *bHideHud* is false. You are intended to implement this function; it is not yet implemented.

### DrawTypingPrompt

`simulated function DrawTypingPrompt (Canvas C, String Text, optional int Pos)`Draw a tiny console at `ConsoleMessagePosX` and `ConsoleMessagePosY`. (v3323 and up).Called by *PostRender* when `((PlayerConsole`  None) && PlayerConsole.bTyping)=

### FadeZoom

`function FadeZoom()=`Stub. To be used to create initiate a zoom effect between a weapon zoom and the normal HUD. (v3323)

### GetConsoleFont

`static function font GetConsoleFont(Canvas C)`This returns fonts with higher indices based on how large the screen is. It does this by calling LoadFontStatic. The assumption is that fonts with higher indices are larger.

### GetFontSizeIndex

`function Font GetFontSizeIndex(Canvas C, int FontSize)`Load a font with a certain size. The canvas size increases the `FontSize`. (v3323 and up)

### GetLocalStatsScreen

`function GetLocalStatsScreen()`Stub. This function should spawn and set the `LocalStatsScreen` variable when needed. (v3323 and up)

### GetMediumFont

`function Font GetMediumFont( float Size )`Just like *GetMediumFontFor()* except that Size is used instead of `Canvas.ClipX` (v3323 and up).

### GetMediumFontFor

`static function Font GetMediumFontFor(Canvas Canvas)`Much like [GetConsoleFont](#getconsolefont), this function returns higher index fonts the larger the screen is. The assumption is that fonts with higher indices are larger.

### IsInCinematic

`function bool IsInCinematic()`Stub. Should return true when a cinematic\matinee is played back. Use this to prevent certain actions while a cinemtic is being played. (v3323 and up).

### LargerFontThan

`static function Font LargerFontThan(Font aFont)`This function should return a font that is larger than the given font assuming that fonts with higher indices are larger. It does not however. It returns a font that is 4 indices smaller than the given font. If the given font is not found in the font list, this function returns font index 5.

### LinkActors

`simulated function LinkActors()`Called by *PostBeginPlay* and the beginning of *PostRender* to assign the PlayerOwner, PlayerConsole, PawnOwner, PawnOwnerPRI variables. (v3323 and up).

### LoadFont

`simulated function Font LoadFont(int i)`This loads the i th font specified by the font names in FontArrayNames if it is not already loaded. This function loads the font based on the current version of FontArrayNames into the current version of FontArrayFonts. LoadFont then returns the requested font.

### LoadFontStatic

`static function Font LoadFontStatic(int i)`This loads the i th font specified by the font names in FontArrayNames if it is not already loaded. This static function loads the font based on the default version of FontArrayNames into the default version of FontArrayFonts. LoadFontStatic then returns the requested font.

### LoadProgressFont

`simulated function font LoadProgressFont()`This function loads the font specified by *ProgressFontName* if it is not already loaded. If the font specified by *ProgressFontName* could not found, a warning is logged and the default font is loaded instead. LoadProgressFont then returns that font.

### LocalizedMessage

```

simulated function LocalizedMessage (
    class<LocalMessage> Message,
    optional int Switch,
    optional PlayerReplicationInfo RelatedPRI_1,
    optional PlayerReplicationInfo RelatedPRI_2,
    optional Object OptionalObject,
    optional string CriticalString
);
```

This function deals with a localized message and is called from ClientReceive(...) in LocalMessage.uc which is called from ReceiveLocalizedMessage(...) in PlayerController.uc. It is not implemented in HUD.uc but you can look at WarfareHUD.uc for an example.

### Message

`simulated function Message( PlayerReplicationInfo PRI, coerce string Msg, name MsgType )`Message adds a message to the displayed message queue. This message will be displayed until it times out or other messages force it out of the queue. The messages will start drawing based on *ConsoleMessagePosX* and *ConsoleMessagePosY* which are ratios of screen size. The message queue size is four and the messages will scroll up.

### PlayReceivedMessage

`simulated function PlayReceivedMessage( string S, string PName, ZoneInfo PZone )`PlayReceivedMessage ignores PName and PZone and just calls PlayerOwner.ClientMessage(S). If *bMessageBeep* is true, a beep will happen.

### PostRender

`simulated event PostRender( canvas Canvas )`PostRender is called from C++ when the HUD should be drawn. This function draws many things. First, the pawn's weapon overlays are drawn if there is a pawn and weapon. Next, *DisplayMessages(...)* is called to display the messages queued up with the *Message(...)* function. Several things are drawn for game and level state and then the pawn's *DrawHUD(...)* function is called if its `bSpecialHUD` is true and the player is not `bBehindView`. Next, if `bShowDebugInfo` is true in the HUD, *PlayerOwner.ViewTarget.DisplayDebug(...)* is called. Now, if `bHideHud` is not true, either the ScoreBoard or some sort of HUD will be drawn. In most cases *DrawHUD(...)* will be called but in some cases, if the player is spectating for example, *DrawSpectatingHud(...)* will be called. After this the player's overlays are drawn and last but not least movies are drawn on the HUD.

### PrintActionMessage

`function PrintActionMessage( Canvas C, string BigMessage )`PrintActionMessage will print a centered message on the HUD. Right now, for example, it is used by *DrawLevelAction(...)* to inform the user that he or she is loading a level or connecting to a sever.No longer available in v3323.

### RemoveHudOverlay

`simulated function RemoveHudOverlay(HudOverlay Overlay)`Remove a *HudOverlay* from the `Overlays` list. (v3323 and up)

### SetCropping

`simulated function SetCropping( bool Active )`Stub. Not used? (v3323 and up).

### SetScoreBoardClass

`simulated function SetScoreBoardClass (class ScoreBoardClass)`Destroys the current scoreboard and spawn the new scoreboard defined by `ScoreBoardClass`. This function is called by the PlayerController in the function *ClientSetHUD(...)*. This function replaces the *SpawnScoreBoard* function used in earlier version. (v3323 and up).

### SetTargeting

`simulated function SetTargeting( bool bShow, optional Vector TargetLocation, optional float Size )`Stub. Should be used to set up targetting information. For example, this is used in UT2004 to show a pass target for the ball launcher in the Bombing run gametype. (v3323 and up).

### SpawnScoreBoard

`function SpawnScoreBoard(class ScoringType)`This function spawns the *ScoreBoard* based on *ScoringType*. The *ScoreBoard* is drawn instead of the normal HUD if bShowScores is true. Obsolete and removed in v3323 see [SetScoreBoardClass](#setscoreboardclass) for the replacement function.

### StaticDrawCanvasLine

`native static final function StaticDrawCanvasLine( Canvas C, float X1, float Y1, float X2, float Y2, color LineColor )`Calls *C.DrawLine(...)* (v3323 and up)

### UseHugeFont

`function UseHugeFont(Canvas Canvas)`Sets the canvas to use *LargeFont*. Removed in v3323 and up.

### UseLargeFont

`function UseLargeFont(Canvas Canvas)`Sets the canvas to use *BigFont* if the canvas is <= 640 across or *LargeFont* otherwise. Removed in v3323 and up.

### UseMediumFont

`function UseMediumFont(Canvas Canvas)`Sets the canvas to use *MedFont* if the canvas is <= 640 across or *BigFont* otherwise. Removed in v3323 and up.

### UseSmallFont

`function UseSmallFont(Canvas Canvas)`Sets the canvas to use *SmallFont* if the canvas is <= 640 across or *MedFont* otherwise. Removed in v3323 and up.

## Functions that are not implemented.

### CheckCountdown

`function CheckCountdown(GameReplicationInfo GRI);`This is called from PostRender(...) every frame. Maybe you should check some sort of countdown here.

## Functions that are not called.

### ProcessKeyEvent

`function bool ProcessKeyEvent( int Key, int Action, FLOAT Delta )`This function is never called. It passes the ProcessKeyEvent to the *NextHUD* if there is one and if not returns false.This function no longer exists in v3323 and up.

## Functions that are neither Implemented nor Called.

### PlayStartupMessage

`function PlayStartupMessage(byte Stage)`This function is neither implemented nor called. It seems you would put some sort of startup message here. And then call it yourself. Removed in v3323 and up/

### DisplayPortrait

`function DisplayPortrait(PlayerReplicationInfo PRI)`This function is neither implemented nor called. Presumably you would want to display some sort of portrait here.

### DrawTargeting

`simulated function DrawTargeting( Canvas C )`This function is neither implemented nor called. Maybe targeting would be something worthwhile to do in this function.

### SetInstructionKeyText

`simulated function SetInstructionKeyText( string text )`Stub, never used. (v3323 and up)

### SetInstructionText

`simulated function SetInstructionText( string text )`Stub, never used. (v3323 and up)

