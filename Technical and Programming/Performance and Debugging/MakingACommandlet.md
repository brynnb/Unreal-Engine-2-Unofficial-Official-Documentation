# Making a Commandlet

*Last updated by Michiel Hendriks, made a real document out of it. Created by somebody at DemiurgeStudios? .*

* [Making a Commandlet](#making-a-commandlet)
  + [Overview](#overview)
  + [How To Make a Commandlet in Script](#how-to-make-a-commandlet-in-script)
  + [Giving Users Some Help](#giving-users-some-help)
  + [How To Use a Commandlet](#how-to-use-a-commandlet)
  + [Commandlet Listing](#commandlet-listing)
    - [HelpCmd](#helpcmd)
    - [HelpOneLiner](#helponeliner)
    - [HelpUsage](#helpusage)
    - [HelpWebLink](#helpweblink)
    - [Help Parmameters and Help Description](#help-parmameters-and-help-description)
    - [Log to Standard Out](#log-to-standard-out)
    - [IsServer, IsClient, IsEditor](#isserver-isclient-iseditor)
    - [LazyLoad](#lazyload)
    - [Show Error Count](#show-error-count)
    - [Show Banner](#show-banner)
    - [Entry Point](#entry-point)
    - [Native Commandlets](#native-commandlets)

## Overview

Commandlets are (often small) programs that make use of the UnrealEngine to perform certain functions. For example the UnrealScript compiler and the dedicated server are executed via a commandlet. Commandlets can be both native and script based.

## How To Make a Commandlet in Script

Create a script class for your commandlet as seen below:

```

class HelloWorldCommandlet extends Commandlet;

event int Main( string Params )
{
   log( " hello world " );

   return 0;
}
```

## Giving Users Some Help

Built into a commandlet is the ability to show help information about it, so that users can discover what it is and what options it supports. To make help information available for your commandlet, you need to add entries into the INT file that your commandlet resides in. If you package is in Core, then you need to modify Core.int for your help information to show up. Below is a sample setting for the "hello world" commandlet residing in Core.

```

[HelloWorldCommandlet]
HelpDescription="This commandlet displays hello world" HelpUsage="gamename.exe helloworld"
HelpWebLink="https://udn.epicgames.com/bin/view/Three/MakingACommandlet"
HelpParamNames[0]="param1"
HelpParamDescriptions[0]="Ignored since helloworld doesn't need params"
```

Notice that the section name must include the *commandlet* as part of the class name. Without this, the commandlet wouldn't be found. To see how this information is used, run the following commands:

```

game.exe help help
game.exe help list
game.exe help webhelp help
```

## How To Use a Commandlet

Commandlets are executed from the `ucc.exe` command line utility, using the following syntax:

```

UCC.exe package_name.commandlet_class_name [parm=value]...
```

For example:

```

UCC.exe Core.HelloWorldCommandlet
UCC.exe Editor.MakeCommandlet
```

In addition, if you list your commandlet in the public section of your package's localized text file (see `Engine.int` for example), then your commandlet can be executed without requiring a fully qualified name, for example:

```

UCC.exe MakeCommandlet
```

Example of a commandlet declaration (from `Engine.int`):

```

[Public]
Object=(Name=Engine.ServerCommandlet,Class=Class,MetaClass=Core.Commandlet)
```

As a convenience, if a user tries to run a commandlet and the exact name he types isn't found, then `ucc.exe` appends the text "commandlet" onto the name and tries again. Therefore, the following shortcuts perform identically to the above:

```

UCC.exe Core.HelloWorld
UCC.exe Editor.Make
UCC.exe Make
```

It is also perfectly valid to call the Main method of a commandlet class directly, for example from within the body of another commandlet. Commandlets are executed in a "raw" UnrealScript environment, in which the game isn't loaded, the client code isn't loaded, no levels are loaded, and no actors exist.All commandlets are descendents of the Commandlet class that is defines as:

```

class Commandlet
   extends Object
   abstract
   transient
   noexport
   native;
```

## Commandlet Listing

Here are the general UnrealScript commandlets that are available...

### HelpCmd

`var localized string HelpCmd;`Command name to show for `ucc help`. This name can then be used to get additional information via `ucc help _name_`.

### HelpOneLiner

`var localized string HelpOneLiner;`Command description to show for `ucc help`. This will be shown in the overview of all commandlets.

### HelpUsage

`var localized string HelpUsage;`Usage template to show for `ucc help _name_`. The line will be shown after the "Usage:" in the help overview.

```

Usage:
   ucc server map.unr[?game=gametype] [-option...] [parm=value]...
```

### HelpWebLink

`var localized string HelpWebLink;`Hyperlink for more info. This will be added to the detailed commandlet help info like this:

```

For more info, see
   http://unreal.epicgames.com/servertips.htm
```

### Help Parmameters and Help Description

```

var localized string HelpParm[16];
var localized string HelpDesc[16];
```

Parameters and descriptions for `ucc help _name_`.

```

Parameters:
   Log              Specify the log file to generate
   AllAdmin         Give all players admin priveleges
```

### Log to Standard Out

`var bool LogToStdout;`Whether to redirect log output to console stdout. (Default: `true`)

### IsServer, IsClient, IsEditor

`var bool IsServer, IsClient, IsEditor;`Whether to load objects required in server, client, and editor context. (Default: `true` for all)

### LazyLoad

`var bool LazyLoad;`Whether to load objects immediately, or only on demand. (Default: `true`)

### Show Error Count

`var bool ShowErrorCount;`Whether to show standard error and warning count on exit. When this is set to `true` the following line is printed at the end of execution (in case of no errors):

```

Success - 0 error(s), 0 warning(s)
```

(Default: `false`)

### Show Banner

`var bool ShowBanner;`Whether to show Unreal banner on startup. When set to `true` the following message will be printed in the beginning:

```

=======================================
ucc.exe: UnrealOS execution environment
Copyright 2001 Epic Games Inc
=======================================
```

(Default: `true`)

### Entry Point

`native event int Main( string Parms );`Entry point. This is the commandlets' entry point. `Parms` will contain the arguments passed to the commandlet on the command-line. For example:

```

ucc server MyMap?game=mygame.gametype -alladmin
```

`Param` will have the content:

```

MyMap?game=mygame.gametype -alladmin
```

The return value of this function is the error\exit code passed back to the shell.

### Native Commandlets

Most of the native commandlets are found in the [Commandlet List](https://udn.epicgames.com/Two/CommandletList).

