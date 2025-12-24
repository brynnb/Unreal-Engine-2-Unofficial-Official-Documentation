# Exec Functions

*Last updated by Michiel Hendriks, major v3323 update. Previously updated by Chris Linder (DemiurgeStudios?). Original author was Martin Actor ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).*

* [Exec Functions](#exec-functions)
  + [Usage](#usage)
    - [Game Administration](#game-administration)
      * [AdminIni](#adminini)
    - [Cheats](#cheats)
    - [Debug commands](#debug-commands)
    - [Normal usage](#normal-usage)
      * [Console](#console)
      * [Settings](#settings)
      * [Gameplay](#gameplay)
      * [Inventory](#inventory)
      * [Chatting](#chatting)
      * [HUD](#hud)
        + [Assault HUD](#assault-hud)
        + [Onslaught HUD](#onslaught-hud)
      * [Music](#music)
    - [Miscelaneous](#miscelaneous)

## Usage

Exec functions are very similar to [ConsoleCommands](ConsoleCommands.md). You can use then by bringing up the console window by typing `~' or the console line by typing `TAB' and simply typing the command. You can also edit your User.ini file and create an Alias for the command and then map the alias to a key. Exec commands are different from [ConsoleCommands](ConsoleCommands.md) because they are created in script and are therefore easy to add and remove.

### Game Administration

The following commands allow you to administer the current game. Most commands require you to log in as administrator.
Some commands require the logged in user to have certain privileges. In the single admin system the admin has all privileges.

* Admin *command* - executes an admin command on a server where you are logged in as administrator.
* AdminGUI - stub
* AdminLogin - log in as server admin, this is required for some exec commands to work. Depending on the administration backend used the arguments are either *username* *password* or simply *password*
* AdminLogout - log out as server admin.
* AdminMenu - stub
* AdminSay - special say command to display a message in the middle of the screen of every player.
* AddBots *number* - add this number of bots
* AddNamedBot *name* - add a bot
* Kick *command users* - remove a user from the game. Command can be ommited, command can be one of the folowing: *list* (will display all players and IDs), *ban* (kickban the user), *session* (ban the user for this game only). You can enter multiple users to kick, seperated by a space. A user can either be their ID (as shown by *kick list*) or a name ('\*' can be used as wildcard).
* KickBan - the same as *kick ban users ...*
* KillBots *number* - remove bots from the game
* Map *command* - Switches the current map. Command can be: map name (same as *switch map*), *next* (the next map in the list), *restart* (restart the current map), *list* (display the current maplist)
* Maplist *command params* - Modify the maplist.
  + list - display all available maps for this gametype
  + used - display the maps in the maplist
  + switch -
  + add - comma seperated list of maps to add
  + del - comma seperated list of maps to remove
* NextMap - switch to the next map
* PlayerList - display all player names and their ping
* RestartMap - restart the current map
* Switch *map* - tells the server to change levels based on the string parameter, which is parsed as a URL (see commandline parameters)

#### AdminIni

Commands available when using the multi admin system. Allows some basic ingame editing, using the webadmin is prefered.

* Bots *cmd params* - modify bot settings
  + add - add new bots, can be a number or a bot name
  + kill - remove a bot, can be a number or the name of a bot
  + set *number* - set the minimum number of players
* Game - edit a certain gametype
  + changeto - set the next gametype (use *switch map* to switch the game)
  + edit *name* - start editing the settings of a certain gametype (can be acronym or classname), or edit the current game
  + endedit - save the changes made
  + canceledit - cancel the changes made
  + get *variable* - get the value of a variable in the game configuration
  + set *variable value* - set a new value for this game type
* maplist - Additional commands are available when using AdminIni and editing a game
  + list *id* - if name is empty show all maplist for the edited game type, otherwise display the map list
  + edit *id* - edit the maplist with said ID (defaults to the current maplist)
  + endedit - save the current maplist
  + new *name* - create a new maplist
  + remove - remove this maplist
  + add *maps* - add these maps to the list
  + del *maps* - remove these maps from the list
  + find *match* - search for available maps
* Mutators - edit mutator usage (need to switch/restart for changes to take effect)
  + used - display mutators used
  + unused - display mutators not used
  + add - add a mutator to the list
  + del - remove a mutator
* User - stub

### Cheats

Cheat codes. Only work offline.

* AllAmmo - gives the user full ammo
* AllWeapons - gives the user all weapons in the retail game
* Amphibious - unlimited breath
* DisableNextObjective - disables the next game objective
* EnableCheats - disable the cheat warning displayed for single player games.
* Fly - fly, use 'walk' to stop flying
* FreezeAll - toggle Players Only
* Ghost - flying and noclipping
* God - god mode
* Invisible *true|false* - toggle player's visibility
* JumpMatch *id* - Jump to a specific match in the ladders. Combine the ladder/rung into one number, i.e., 54 = ladder 5, rung 4.
* KillAll *class* - kill all actors of type *class*
* KillPawns - kill all pawns
* KillViewedActor - kill the current viewtarget
* Loaded - give all weapons and full ammo
* Phil - *phil == god*
* PlayersOnly - toggle players only
* ruler - touch all ONSPowerCore classes
* SetCameraDist *float* - SetCameraDist
* SetGravity *float* - set the gravity of the current volume
* SetJumpZ *float* - set the jumpZ of the pawn
* SetSpeed *float* - set the ground and water speed
* SkipMatch - skip the current ladder match
* SloMo *float* - set the gamespeed
* summon *class* - summon this class
* Teleport - Teleport to surface player is looking at
* walk - go back to normal walking
* WeakObjectives - remove the protection from the gameobjectives
* WinMatch - win the current match

### Debug commands

Most of the following commands only work offline

* AdminDebug \_command\_- execute a direct console command
* Avatar *classname* - changes the controller's avatar
* CauseEvent *event* - triggers an event
* ChangeSize *float* - changes the player size
* ChatDebug - enables chat debugging
* CheatView *class bool* - *viewclass(class, bool, true)*
* check - dumps *Decoration* information
* CheckPriority - dumps weapon priority
* ClearAllDebugLines - clears all staying debug lines
* ClearProgressMessages - removes all progress messages
* CreateCameraEffect *class* - add a new camera effect class
* DebugTabOrder - dumps information about the taborder settings in the current active page
* DLO - DynamicLoadObject
* DumpLoadingHints - dump all loading hints for the current class to the log file
* DumpMaplists - dump all map lists to the log file (only works from the WebAdmin console)
* DumpPlayInfo - dump PlayInfo details to the log
* DumpRecords - dump the cache records to the log file
* EndPath - stub
* FreeCamera *true|false* - set freecamera (Camera rotation doesn't control pawn rotation) and behindview.
* FreezeFrame *float* - pauze the game in *float* seconds
* GetWeaponStats - enables logging of weapon statistics
* L33TPhrase *number* - no it's not
* ListDynamicActors - list dynamic actors in the log
* LockCamera - lock the camera to the current position
* LogScriptedSequences - Toggles logging of scripted sequences on and off
* NetDebugBot - Debug bot when a net client
* RememberSpot - remember spot for path testing (display path using ShowDebug)
* ReviewJumpSpots *name* - Used for correlating game situation with log file
* SetFlashScaling *float* - sets flashscaling
* SetFlash - sets the flash scale to the string parameter (interpreted as a float value). Only available if cheating is enabled
* SetFogB - sets the blue color component of FlashFog variable to the string parameter (interpreted as a float value).
* SetFogG - sets the green color component of FlashFog variable to the string parameter (interpreted as a float value).
* SetFogR - sets the red color component of FlashFog variable to the string parameter (interpreted as a float value).
* SetProgressMessage *index message color* - sets a progress message
* SetProgressTime *float* - set the timeout for the progress messages
* ShowAI - show AI debug info on the HUd
* ShowDebug - toggles the displaying of debug information on the HUD
* SoakBots - set bSoaking to true for all bots
* streamdebug - music player debug meta command
* ViewActor *name* - view actor with said name
* ViewBot - view the first bot
* ViewClass *class quiet cheat* - set the viewport to the first *class*
* ViewFlag - view the first flag carrier
* ViewPlayer *playername* - change the view port to the player with that name
* ViewSelf - set the viewtarget to the controllers pawn
* ViewTurret - view the first turrent
* WriteToLog *param* - write *param* to the log file

### Normal usage

Various commands that can be used from the PlayerController

* AddCurrentToFavorites - add the current server to your favorite list
* DemoViewNextPlayer - view next player (during demo playback)
* LocalTravel *url* - travels the client to the URL
* MusicMenu - opens the music player
* Mutate *command* - meta command to pass commands through the mutator list
* PlayWaitingGame - open the `WaitingGameClassName` menu
* QuickLoad - save the current game in slot 9
* QuickSave - loads the game in slot 9
* RestartLevel - restarts the current level
* ServerInfo - opens the Server Info menu
* ShowMenu - opens the mid game menu
* ShowScores - toggles the displaying of the score spread of players in the game on the HUD
* ShowVoteMenu - opens the voting menu
* SpecViewGoal - change the view target to the goal
* SwitchLevel *url* - switches to the new URL

#### Console

* CLS - clears the console
* ConsoleClose - open the console
* ConsoleOpen - open the console
* ConsoleToggle - toggle the console
* Talk - open a tiny console with "say " as prefix
* TeamTalk - open a tiny console with "teamsay " as prefix
* Type - open a tiny console

#### Settings

* BehindView *true|false* - sets the status of the camera view behind the player
* ChangeCharacter *pawn class* - changes character on the fly (for next respawn)
* ChangeTeam *number* - changes the current team
* FOV *number* - sets the Field Of View for the player to the string parameter (interpreted as a float). FOV is clamped between 1 and 170, and if the game is a network game, FOV will not accept values below 80.0
* InvertLook - inverts looking (XBox only)
* InvertMouse - toggles inverted mouse
* SetAutoTaunt *true|false* - set auto taunt
* SetMouseAccel *float* - sets the mouse acceleration
* SetMouseSmoothing *float* - sets the mouse input smoothing
* SetName *string* - changes the player's name
* SetSensitivity *float* - sets the sensitivity of the mouse for the player
* SetSmoothingMode *number* - sets the mouse smoothing method (1 = enabled; 0 = disabled)
* SetSmoothingStrength *float* - sets the mouse smoothing strength
* SetSpectateSpeed *float* - set the movement speed in spectator mode
* SetVoice *voice class* - sets the players voice class
* SetWeaponHand *left|right|center|hidden* - sets the weapon side
* ShowAliases - sends all aliases to the security class
* ShowBindings - sends all binds to the security class
* ShowGun - toggle the gun
* ToggleBehindView - toggles behindview
* ToggleScreenShotMode - toggles screen shot mode (no hud\weapon\crosshair)

#### Gameplay

Some gamplay related commands, also see the [inventory](#inventorycommands) commands

* BasePath - show the path to the base\next objective
* Jump - tells the player code to jump
* NewRound - start a new round (Assault gametype)
* Pause - pauses the game
* PlayVehicleHorn *number* - sound a horn of the current vehicle
* RandomTaunt - play a random taunt
* Speech *type index callsign* - sends a sound message from the player's voice pack to another player
* Suicide - commit suicide
* Taunt *animation* - play a taunt animation

#### Inventory

Commands that affect the player's inventory (including weapons).

* ActivateInventoryItem *class* - activates the inventory item of the class
* ActivateItem - activates the player's currently selected item
* AltFire - alternate fires the player's currently selected weapon with an optional accuracy modifier of string parameter (interpreted as a float)
* DropFlag - drop the flag\ball\...
* Fire - fires the player's currently selected weapon with an optional accuracy modifier of string parameter (interpreted as a float)
* ForceReload - stub
* GetWeapon *class* -gives the player a weapon
* NextItem - switches to the next item in the player's inventory
* NextWeapon - switches the player's weapon to the next weapon in the player's inventory
* PipedSwitchWeapon *number* - just like SwitchWeapon except that it won't be executed when a weapon is pending to be switched
* PrevItem - switches the player's item to the previous item in the player's inventory
* PrevWeapon - switches the player's weapon to the previous weapon in the player's inventory
* SwitchToBestWeapon - attempts to change the player's weapon to the best one in the player's inventory
* SwitchToLastWeapon - switch to the previous selected weapon
* SwitchWeapon *number* - switches the player's weapon to the specific weapon group
* ThrowWeapon - throws the currently selected weapon out of the player inventory and selects another
* updaterelative - for inventory items, updates the relative rotation of the item to the player
* Use - make the player attempt to use any level objects the player is touching

#### Chatting

Voice chat and text chat commands

* command *string* - voice recognision command (as if it was recognised)
* DisableVoiceChat - disabled voice chat completely
* EnableVoiceChat - enable voice chat
* InGameChat - open the in-game chat menu
* Join *channel* - join this voice chat channel
* Leave *channel* - leave this voice chat channel
* Say - sends a message to everyone connected to the server, message is all text following the command
* SetChatPassword *password* - Change the password for your personal chatroom
* Speak *channel* - Set a voice chatroom to your active channel
* SpeakDefault - Set your active channel to the default channel
* SpeakLast - Set your active channel to the last active channel
* SpeechMenuToggle - show the speech menu to issue commands to bots
* TeamChatOnly - only show team messages
* TeamSay - sends a message to everyone on the same team as you on the server, message is all text following the command

#### HUD

* GrowHUD - show more information
* NextStats - display stats for the next player
* ShowHud - toggle the hud
* ShowScores - toggle the scores
* ShowStats - toggle the stats
* ShrinkHUD - show less information

##### Assault HUD

* ShowObjectiveBoard - toggle the Assault objectives
* ShowSpawnAreas - debug to show current valid playerstarts

##### Onslaught HUD

* CopyLinkSetup - copy the current link setup to the clipboard
* LinkDesigner - open the link designer
* ToggleRadarMap - toggle the game radar

#### Music

Commands that control the music player (not the ingame music)

* GetCurrentStream - return the current song
* NextSong - play the next song in the play list
* PauseSong - pause the playback
* PlaySong *name initial-time* - play the song *name*, start at the position *initial time*
* PrevSong - play the previous song
* SeekStream *float* - seek in the current song
* SetMusicVolume *float* - set the music volume
* StopSong - stop music playback

### Miscelaneous

Other things

* StartRollingDemo - start loading demo levels
* StopRollingDemo - stop the demo cycle
* utvsay *message* - only valid for a UTV controller

