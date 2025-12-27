# Console Commands

*Last updated by Michiel Hendriks, more toys for v3323. Previously updated by Chris Linder to include additional information. Original author was Martin Actor ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).*

* [Console Commands](#console-commands) 
  + [Overview](#overview)
  + [Command List](#command-list)
    - [General Purpose](#general-purpose)
    - [Debugging](#debugging)
    - [Display](#display)
    - [Rendering](#rendering)
    - [Karma](#karma)
    - [Movie\Demo recording](#moviedemo-recording)
    - [Sounds](#sounds)
    - [Networking](#networking)
    - [Miscelaneous](#miscelaneous)

## Overview

To use console commands, bring up the console and type them in. Console commands may be executed from within the game, from within the editor, or if the game has been started using the -server switch, from the server's console. They can do various things from resetting the engine to setting particular actor's variables.Lists of commands can also be stored in text files in the system directory and executed by typing "exec *filename* " at the console.

## Command List

The following is a list of engine supported console commands

### General Purpose

* CANCEL - tells the engine to cancel an in progress connection attempt
* DISCONNECT - disconnects the client from the current game/server
* EXIT - tells the engine to shutdown and close the application
* MAP - alias for `START`
* OPEN - tells the engine to open a map by the name of the string that comes immediately after
* QUIT - same as EXIT
* RECONNECT - reconnects the client to the current game/server
* SERVERTRAVEL - travels the client to the server by the name/address of the string that comes immediately after
* START - similar to OPEN, difference is it does a TRAVEL\_Absolute instead of TRAVEL\_Partial

### Debugging

* CONFIGHASH - displays configuration information
* DEBUG - is used to simulate various errors with the following parameters identifying which
  + CRASH - tells the engine to simulate a fatal crash
  + EATMEM - tells the engine to simulate eating up all available system memory
  + GPF - tells the engine to simulate a general protection fault
  + RECURSE - tells the engine to simulate a runaway recursion or loop
  + SLEEP - sleep for a couple seconds
* DIR - displays all used directories and files
* DUMPCACHE - displays objects in cache and their cache attribute
* DUMPNATIVES - displays all native functions
* FLUSH - tells the engine to flush all engine caches
* MEM - displays allocated memory information
* MEMSTAT - displays memory usage information
* NAMECOUNT - return the number of registered names
* OBJ - is used in conjunction with the following parameters
  + CLASSES - displays a list of all loaded classes
  + DEPENDENCIES - displays a list of dpendencies upon a specific package as passed by a string parameter
    - PACKAGE=
  + DUMP - Dump all variable values for the specified object, supports specifying categories to hide or show (hide=movement,collision)
    - [class] - plain name or CLASS= or NAME=
    - HIDE=
    - SHOW= - comma seperated list
  + GARBAGE - forces a garbage collection sweep
  + HASH - displays a count of how many objects have hashes
  + LINKERS - iterates through GObjLoaders and displays info about their linkers
  + LIST - displays a list of objects of a class, from a package, or inside a package. The following parameters can be given in any combination
    - CLASS= - the string value is the class of object to find
    - INSIDE= - the string value is the name of the package to look in for objects
    - PACKAGE= - the string value is the name of the package to list objects which have an outer of
  + MARK - tells the engine to iterate through all objects and set their marked flag
  + MARKCHECK - displays a list of objects that aren't marked
  + REFMAP - show a reference map for the given class
    - [class] - plain name or CLASS= or NAME=
    - DEPTH= - optional depth
  + REFS - takes two parameters which identify a class and name of an object, then displays all objects that reference it
    - CLASS=
    - NAME=
  + VFHASH - lists how many hashes are in each object's VfHash table
* REPORT - prints a little report about the current game
* RESETPROFILE - resets internal stat counter variables (ticks, calls, and cycles)
* STAT - is used in conjunction with the following parameters to toggle on/off statistic displaying
  + ALL - toggles on all statistics display
  + ANIM - toggles on/off animation statistics display
  + AUDIO - toggles on/off audio statistics display
  + DEFAULT - resets most statistic display flags to not display anything
  + FPS - toggles on/off frames per second display
  + GAME - toggles on/off game statistics display
  + HARDWARE - toggles on/off hardware statistics display
  + HISTOGRAPH -
  + HISTOGRAPH - toggles on/off histograph statistics display
  + LIGHT -
  + MATINEE - toggles on/off matinee statistics display
  + NET - toggles on/off (inter)net(work) statistics display
  + NONE - toggles off all statistics display
  + RENDER - toggles on/off rendering statistics display
  + RESET - same as DEFAULT
  + XBOXMEM - toggles on/off XBox memory statistics display
* SUPPRESS [tag] - suppress messages
* UNSUPPRESS [tag] - unsuppress messages

### Display

* BRIGHTNESS - modifies the screen brightness. Takes a parameter value for setting the brightness or can take a parameter of '+' to increase it. If no parameters are passed, brightness is set to 0.5
* CONTRAST - works the same as BRIGHTNESS, only affects the contrast level
* ENDFULLSCREEN - end fullscreen mode
* GAMMA - works the same as BRIGHTNESS, only affects the gamma level
* GETCOLORDEPTHS - returns 32
* GETCURRENTCOLORDEPTH - return color depth
* GETCURRENTRENDERDEVICE - returns the current render device
* GETCURRENTRES - return the current resolution
* ISFULLSCREEN - return `true` or `false`
* SETRES [height]x[width]x[depth][w|f] - changes the resolution (w = windowed; f = fullscreen) for example: 800x600x32f
* SUPPORTEDRESOLUTION - return 1 if this mode is supported (all parameters are required)
  + BITDEPTH=
  + HEIGHT=
  + WIDTH=
* TEMPSETRES - same as `setres` but the change is not saved
* TOGGLEFULLSCREEN - toggle fullscreen

### Rendering

* CINEMATICS - toggle cinematics mode (black bars)
* CINEMATICSRATIO [value] - set the size of the black bars
* D3DRESOURCES - show d3d resources summary
  + ALL - show more detailed information
* DUMPRESOURCEHASH - dumps D3D resource hash table
* FIRSTCOLOREDMIP [value] - sets the first colored mip or 255 if none provided (D3D)
* FIXEDFPS [value] - sets a fixed FPS
* FIXEDVISIBILITY - toggle fixed visiblity, with fixed visibility the visibility will no longer be updated when moving around
* HIDEACTORS - hide all actors
* NEARCLIP [value] - sets the near clipping plane
* REND - render various items (only for clients)
  + BLEND
  + BONE
  + BOUND
  + COLLISION
  + DEFAULT
  + NORMALS
  + RESET
  + SKIN
* RENDEREMULATE - rendering emulation
  + GF1
  + GF2
  + XBOX
* RMODE [value] - set the render mode
* SHOW - toggle display of various items (only for clients)
  + ACTORINFO
  + ACTORS
  + BSP
  + COLLISION
  + CORONAS
  + FALLBACKMATERIALS
  + FLUID
  + FOG
  + PARTICLES
  + RADII
  + SKY
  + STATICMESHES
  + TERRAIN
  + VOLUMES
* SHOWACTORS - show all actors
* SHOWALL - show all actors (set bhidden to false)
* TEXSTATS - dump texture stats
* TOGGLEREFRAST - toggle software rasterizer

### Karma

* KDEBUGCONTACTS - toggle logging of karma contacts
* KDRAW - toggle drawing of various Karma elements
  + COLLISION - karma collision geometry in green wireframe.
  + COM - the centre of mass of Karma-simulated Actors
  + CONTACTS - active contacts indicating position, penetration and normal.
  + JOINTS - joints including limits
  + ORIGIN
  + REPULSORS
  + SAFETIME
  + TRIANGLES - all terrain/bsp triangles being considered by Karma collision
  + WHEEL
* KNOTRICOLL - toggle triangle collision calculation with the level
* KSAFETIME [0/1] - sets the usage of Karma Safe-Time
* KSTEP -
* KSTOP - stop karma evolution

### Movie\Demo recording

More information about this can be found in the [DemoRecording](https://udn.epicgames.com/Two/DemoRecording) document.

* DEMOPLAY - play a demo
* DEMOREC - record a demo
* DUMPFRAMES - create a screenshot for every frame
  + START
  + STOP
* RECORDMOVIE - record a movie of the current game
  + START
  + STOP
* SHOT - create a screenshot
* STOPDEMO - stop demo playback\recording

### Sounds

* AUDIO FLUSH TRUE - flush all sound buffers
* CHECKSOUNDPLAYING - returns 1 if a sound is playing, otherwise 0
* GETDURATION [handle] - returns the duration of the sound with said [handle]
* PAUSESOUNDS - iterates through all sound sources and sets their paused flag
* ROLLOFF - sets the sound RollOff value to the value of the string parameter
* SETTEMPMUSICVOLUME - set the music volume (but don't save it)
* SOUND\_REBOOT - restart the sound driver
* STOPSOUNDS - stop all non-streaming sounds
* UNPAUSESOUNDS - iterates through all sound sources and unsets their paused flag
* WEAPONRADIUS - sets a default sound radius to the value of the string parameter

### Networking

* CRACKURL - breaks down passed URL to the engine for the map/game and displays all parameters
* GETCURRENTTICKRATE - displays the current tick rate
* GETLOSS - current packet loss
* GETMAXTICKRATE - displays the max allowed tick rate
* GETPING - get the current ping
* INJECT [cmd] - inject [cmd] to the server, [cmd] has special meanings
* NETSPEED - set the netspeed

### Miscelaneous

* GET [class] [property] - returns the default value of a class property
* GETALL [class] [property] - returns the value property for all instantiated classes
* GETSYSTEMLANGUAGE - return the system language
* GSPYLITE - tells the engine to run GameSpy Lite executable
* GTIME - displays the value of GTime
* POKE [class] [object] [property] [value] - poke class property
* PREFERENCES - show preferences window
* RELAUNCH - flushes the engine and then relaunchs the executable
* SAVEGAME - tells the engine to save the current game state. See [SavingAndLoadingGames](https://udn.epicgames.com/Two/SavingAndLoadingGames) for more info.
* SAY - GUI server only
* SET - this one is the most powerful of them all. It takes as the first parameter string a class name, the second string a variable name, and the third string, a value. All objects of the given class (including subclasses) will have the given variable set to the given value. For example "set Pawn CollisionRadius 200" will make all pawns have a collision radius of 200. (See [PawnTricksAndTips](../../Uncategorized/PawnTricksAndTips.md#the-set-command) for more details). In v3323 the `set` command has limited functionality when using online, this is to limit cheating.
* SETMOUSE x y - warp mouse to X,Y
* TTS [text] - feed [text] to the Text To Speech engine

