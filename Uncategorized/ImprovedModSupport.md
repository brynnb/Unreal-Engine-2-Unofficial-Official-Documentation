# Improved Mod Support

*Document Summary: An overview of the improved mod support in the latest UT2004 patches.**Document Changelog: Created by [Joe Wilcox](https://udn.epicgames.com/Main/JoeWilcox). Updated by Michiel Hendriks. Maintained by Richard Nalezynski?.*

* [Improved Mod Support](ImprovedModSupport.md#improved-mod-support)
  + [Overview](ImprovedModSupport.md#overview)
  + [Running a Mod](ImprovedModSupport.md#running-a-mod)
    - [The (Magic) Commandline Switch](ImprovedModSupport.md#the-magic-commandline-switch) Commandline Switch)
  + [Setting Up a Mod Project](ImprovedModSupport.md#setting-up-a-mod-project)
    - [Getting the Resources](ImprovedModSupport.md#getting-the-resources)
      * [Essential files](ImprovedModSupport.md#essential-files)
      * [Other useful files](ImprovedModSupport.md#other-useful-files)
    - [Directory Structure](ImprovedModSupport.md#directory-structure)
    - [Script Packages](ImprovedModSupport.md#script-packages)
    - [Content Packages](ImprovedModSupport.md#content-packages)
    - [Karma Asset Files (.ka)](ImprovedModSupport.md#karma-asset-files-ka))
  + [Configuration Files](ImprovedModSupport.md#configuration-files)
    - [Mod Configuration](ImprovedModSupport.md#mod-configuration)
      * [UT2004Mod.ini File](ImprovedModSupport.md#ut2004modini-file)
      * [UT2004User.ini File](ImprovedModSupport.md#ut2004userini-file)
    - [Alternate Class Configuration Files](ImprovedModSupport.md#alternate-class-configuration-files)
  + [System Files](ImprovedModSupport.md#system-files)
    - [Log Files](ImprovedModSupport.md#log-files)
    - [Localization Files](ImprovedModSupport.md#localization-files)
    - [Cache Record Files](ImprovedModSupport.md#cache-record-files)
    - [Player Settings Files (.upl)](ImprovedModSupport.md#player-settings-files-upl))
  + [Splash Screen](ImprovedModSupport.md#splash-screen)
  + [Installation and Distribution](ImprovedModSupport.md#installation-and-distribution)
  + [Example Mod](ImprovedModSupport.md#example-mod)

## Overview

**NOTE**: *This document pertains to the latest revision of UT2004 and mods built to these specifications will require that level as well!*This document will cover the features in UT2004 designed to help mod authors full and partial conversions. It will outline how to isolate your mod using the **-mod=** command-line switch as well as how to get your mod to show in the *User Mods* tab of the in-game *Community* menu.This document is intended for creators of larger mods (like Total Conversions); smaller mods (like mutators or gametypes) that only enhance or alter the current game rules don't have to use the improved mod support.

## Running a Mod

### The (Magic) Commandline Switch

To load the game and editor for your mod you will have to use the mod commandline switch. The syntax for this switch is:

```

ut2004.exe -mod=MyMod
```

Where `MyMod` is the (directory) name of your mod.You simply have to add the above commandline switch to the normal commandline you use to start various elements. For example:

```

// start the game:
ut2004.exe -mod=MyMod

// start the game with a diffirent user ini:
ut2004.exe -USERINI=MyUser.ini -mod=MyMod

// join a server running your mod:
ut2004.exe 1.2.3.4:7777 -mod=MyMod

// start UnrealEd for your mod
unrealed.exe -mod=MyMod

// running the UnrealScript compiler
ucc.exe make -mod=MyMod
```

The mod switch is just like any of the other command line options?.**Note:** for the rest of the document it is assumed that your mod is called *MyMod*.

## Setting Up a Mod Project

### Getting the Resources

In addtition to the game, itself, you will need the following essential files. It may be helpful to download some of the other useful files, as well.

#### Essential files

* [Latest UT2004 Patch](http://unreal.epicgames.com/files/ut2004-winpatch3369.exe)
* [UT2004 UnrealScript source files](USCRIPTDownload.md) - All the .UC files needed to start creating mods.

#### Other useful files

* [UT2004 Debug package files](UDEBUGDownload.md) - Debug version of the game's Unreal Script packages.
* [UDE 3.0 (UnrealScript Development Environment)](UDEDownload.md) - UDE is a full featured editing environment similar to Visual Studio from Microsoft.
* [Maya Complete Plugins](MayaCompletePlugins.md) - The Maya Complete versions of the user-friendly PLE plugin that shipped with UT2004.
* [ActorX](../Content%20Creation/Tools/ActorX.md) - Animation Export Tools

### Directory Structure

One of the goals of UT2004's improved mod support is to give authors the ability to isolate their mod content from the rest of the game.The following structure is based on the root directory (default is *c:\ut2004*). The content structure is as follows:

```

c:\ut2004
   +- Animations
   +- Help
   +- KarmaData
   +- Maps
   +- Music
   +- Sounds
   +- System
   +- Textures
   +- Web
```

All of the game's content and script packages are nicely seperated in various folders.The isolated directory of your mod should be created in the same root directory. Therefore, create a directory called `MyMod` in the root directory. The name of this directory is important because that's the name you will have to use for the **-mod=** commandline switch. So, now you should have a directory called *c:\ut2004\MyMod*. This directory will be the root directory of your mod that will contain your mod's content and scripts.How you further organise the content in the *MyMod* directory is up to you, with one exception: a sub-directory called `System` has to exist. The rest of the directories is up to your [configuration](ImprovedModSupport.md#defaultini).

### Script Packages

The *c:\ut2004\MyMod* directory will be used as the root directory of your mod (when the programs are started with the **-mod=MyMod** switch). Even though you can include content from UT2004's root directory (with the right [configuration](ImprovedModSupport.md#defaultini)), it doesn't apply to the UnrealScript packages. The UnrealScript packages you create should be set up just like you would do with a normal package for UT2004 except it should be within your mod directory.Your mod directory would look like this:

```

c:\ut2004
   ...
   +- MyMod
   |  +- MyModCode    &lt;-- an UnrealScript package for your mod
   |  |  +- Classes   &lt;-- put you UnrealScript source code here (.uc)
   |  +- MyModGUI     &lt;-- another UnrealScript Package
   |  |  +- Classes
   |  +- System     &lt;-- configuration files (.ini), localization files (.int), and compiled UnrealScript packages (.u)
   ...
```

### Content Packages

Content packages go in their respective folders...

```

c:\ut2004
   ...
   +- MyMod
   |  +- Animations     &lt;-- Skeletal Mesh animation packages (.ukx)
   |  +- Help     &lt;-- elements such as a splash screen (.bmp) and ReadMe (.txt)
   |  +- Maps     &lt;-- Level packages (.ut2)
   |  +- Music     &lt;-- Music files (.ogg)
   |  +- Sounds     &lt;-- Sound packages (.usx)
   |  +- Textures     &lt;-- Texture packages (.utx)
   ...
```

### Karma Asset Files (.ka)

If your project has Karma Assets stored in `.ka` files, you will need to have a *KarmaData* directory in your mod's root directory. This directory will automatically be used if it exists.

## Configuration Files

For general information, see the [Configuration Files](ConfigurationFiles.md) page.

### Mod Configuration

When the game is started with the **-mod=** command-line switch it will load (and/or create) your mod's configuration files. All mods have their own configuration files that get constructed at first start. These files use the mod's root directory for their name and is auto-assigned. So using the MyMod example, we will end up with **MyMod.ini** and **MyModUser.ini** configuration files in the mod's System directory. These files are constructed by combining the configuration files of UT2004 (`UT2004.ini` and `User.ini`) with your mod's default configuration.
The files `Default.ini` and `DefUser.in` have to exist in your mod's `System` directory. When the game starts (with your mod) the following is done:If `UT2004.ini` exists in the game's System directory, it will be used to merge it with the mod's `Default.ini`; otherwise it will use the game's `Default.ini` and merge it with the mod's `Default.ini` . The same goes for the `user.ini` files.It's important to understand how the merging of the files works as well as how the Mod's configuration file modifiers available to your mod's default configuration files. Let's take a look at an example Default.ini configuration file for MyMod.

```

[Core.System]
+Paths=../MyMod/System/*.u
+Paths=../MyMod/Textures/*.utx
+Paths=../MyMod/StaticMeshes/*.usx
+Paths=../MyMod/Maps/*.ut2

[Editor.EditorEngine]
+EditPackages=MyModCode
+EditPackages=MyModGUI

[Engine.GameEngine]
MainMenuClass=MyMod.MyModMainMenu
```

It looks fairly similar to the original Default.ini configuration file. Your mod's default configuration files should only contain the changes required, nothing more.Note the **+** prefix in front of the `Paths` and `EditPackages` lines. There are two prefixes you can use: **+** for addition, and **-** for removal of entries. This is only usefull for dynamic array configuration entries (like `Paths`, `EditPackages`, `ServerPackages`, `ServerActors`, etc.).For example, adding the following entry:

```

-Paths=../Maps/*.ut2
```

Will remove the default path to the Maps directory from the generated configuration file. This way the maps for the normal game can't be accessed from your mod.If no prefix is used the line will simply set the values, old values will be overwritten.Keys get processed in the order they appear, so the following is possible:

```

-CacheRecordPath=../System/*.ucl
+CacheRecordPath=../MyMod/System/*.ucl
+CacheRecordPath=../System/*.ucl
```

This basically inserts the reference to you mod's ucl files before looking in the default game location. Be careful with ordering of some of the entries the order often is important.

#### UT2004Mod.ini File

Two important things happen when you use the **-mod=** switch. First, UT2004 will look for the existence of the UT2K4Mod.ini configuration file in the mod's root directory (*c:\ut2004\MyMod*) you specify and then (if found) it will proceed to load custom configuration files and then the game's configuration files.In truth, the contents of this file is only referenced by the *User Mods* tab of the *Community* menu in the game. Think of it as the definition file for you mod. It contains the the various sections of key-value pairs that represent the options needed to fill out that menu. This file is only required for your mod to show up in the *User Mods* tab; it doesn't have any other meaning for the rest of the game.Here is an example of a mod configuration file:

```

[MOD]
ModTitle=Test Mod
ModLogo=TestModTex.TestModLogo
ModDesc=This is a test of the mod system.  This is only a test.
ModCmdLine=
ModURL=https://udn.epicgames.com/Two/ImprovedModSupport
```

* `ModTitle`: This is the title of the mod and will be displayed in the select list of the *User Mods* tab.
* `ModLogo`: This is the full name (i.e. `Package.texture`) of the image to be displayed on the *User Mods* tab of the *Community* menu when someone selects your mod. It should be 512x128. It's assumed that the package is in *c:\ut2004\MyMod\Textures*.
* `ModDesc`: This options sets the description that will show in the box on the *User Mods* tab. You can use the pipe character ("|") to add carriage returns/line feeds to the display.
* `ModCmdLine`: This is the command line that will be used to launch your mod. You do not need to include the **-mod=** as it will be auto-appended. The resulting commandline would be something like: **ut2004.exe -mod=MyMod <ModCmdLine>**.
* `ModURL`: This is a hyperlink to a web site for your mod.

#### UT2004User.ini File

### Alternate Class Configuration Files

The Unreal engine supports alternate individual configuration files for a given class (using the `config(SomeName)` class modifier). Unfortunately at this time, this feature is not supported.

## System Files

### Log Files

When running with mod support, the main .log files will be placed in your mod's System directory by default and be called `<ModName>.Log` (i.e. MyMod.log). All other secondary log files (such as ucc.log) will still be created in the game's System directory.

### Localization Files

Starting with the latest patch, UT2004 can correctly locate and use localized text (.int) files stored in your mod's System directory. This requires some work on your part.

1. `DUMPINT` will always create the new .int files in the game's System directory. This is an unfortunate outcome; but changing it would have proven difficult at this time.

### Cache Record Files

Starting with the latest patch, UT2004 can correctly locate and use cache record (.ucl) files stored in your mod's System directory (or in the case of cache record files, whichever directory is specified by the `CacheRecordPath` array). This requires some work on your part.

1. `EXPORTCACHE` will create the .ucl files in the first directory found in the `CacheRecordPath` array. Using the trick above, you can force it to use your directory, but that's unsupported.

As a general rule, you will have to hand copy these files in to their proper place - from the game's System directory to your mod's System directory.

### Player Settings Files (.upl)

There is special logic built in to the latest patch to make UPL files mod friendly. It works as follows...When the Cache Manager searches for .UPL files, it traverses the `Paths` array in reverse (bottom to top) and it checks each directory for .UPL files, adding any that it finds to the cache. When it reaches the game's System directory, the following occurs:

1. If you are not running with a mod, it will scan the directory as normal.
2. If you are running a mod, and no .upl files have been found already, it will scan the directory as normal.
3. If you are running a mod, and the game has already found even a single .upl file, it will skip the default System directory.

In a nutshell, this means that if you have a mod that uses both your own custom .upl files and you want to allow them to use the default characters, you will need to include a copy of the original .upl files with your mod.

## Splash Screen

If you want to have a custom splash screen that appears when you first start the game, you will need to create a support directory named *Help* in your mod's root directory and add a 256 color bitmap (.bmp) file. You must name the .bmp file the same as your mod's root directory <ModName> Logo.bmp. So in our example it is MyModLogo.bmp.

## Installation and Distribution

See the [.umod game installer](UmodInstaller.md) page for information on packaging up your mod for distribution, allowing users to easily install everything to work with other games.

## Example Mod

Click [here](../assets/[drsins-testmod.zip](../assets/drsins-testmod.zip)) to download an example mod called TestMod.
