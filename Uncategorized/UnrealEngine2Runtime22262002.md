# UnrealEngine2 Runtime 2226.20.02

![urt_logo.jpg](../assets/![urt_logo.jpg](../assets/urt_logo.jpg))

*Document Summary: Introduction to version 2226.20.02 of the UnrealEngine2 Runtime edition of the second-generation Unreal engine, including release information.**Document Changelog: Created; maintained over time.*

* [UnrealEngine2 Runtime 2226.20.02](UnrealEngine2Runtime22262002.md#unrealengine2-runtime-22262002)
  + [Overview](UnrealEngine2Runtime22262002.md#overview)
  + [Introduction](UnrealEngine2Runtime22262002.md#introduction)
  + [System Requirements](UnrealEngine2Runtime22262002.md#system-requirements)
    - [Windows 98/Me/2000/XP Minimum](UnrealEngine2Runtime22262002.md#windows-98me2000xp-minimum)
    - [Windows 98/Me/2000/XP Recommended](UnrealEngine2Runtime22262002.md#windows-98me2000xp-recommended)
    - [GNU/Linux x86, Macintosh OS X](UnrealEngine2Runtime22262002.md#gnulinux-x86-macintosh-os-x)
  + [Obtaining the Runtime](UnrealEngine2Runtime22262002.md#obtaining-the-runtime)
    - [Downloading](UnrealEngine2Runtime22262002.md#downloading)
    - [Installing](UnrealEngine2Runtime22262002.md#installing)
  + [Using the Runtime](UnrealEngine2Runtime22262002.md#using-the-runtime)
    - [Configuring](UnrealEngine2Runtime22262002.md#configuring)
  + [Developing for the Runtime](UnrealEngine2Runtime22262002.md#developing-for-the-runtime)
    - [Programming the Runtime](UnrealEngine2Runtime22262002.md#programming-the-runtime)
    - [Creating your own Runtime Content](UnrealEngine2Runtime22262002.md#creating-your-own-runtime-content)
  + [Reporting Bugs](UnrealEngine2Runtime22262002.md#reporting-bugs)
  + [Known Issues](UnrealEngine2Runtime22262002.md#known-issues)
  + [Errata](UnrealEngine2Runtime22262002.md#errata)

## Overview

This page provides links to download version **2226.20.02** of the UnrealEngine2 Runtime software, its documentation, release notes and errata.

## Introduction

The **UnrealEngine2 Runtime** software is the state of the art in cross-platform, real-time 3D rendering solutions for the desktop. Taking advantage of the latest advances in hardware-accelerated 3D, the Runtime provides a stable, robust platform for interactive walkthroughs and simulations.**NOTE**: The Unreal Engine 2 Runtime is not supported in any way other than the documentation available and recommended support channels below.

* For informal discussion and support, check out the BeyondUnreal forums for the UnrealEngine2 Runtime, at <http://forums.beyondunreal.com/forumdisplay.php?f=438>
* Commercial licensing of the Unreal Engine Runtime is available. More information on licensing terms is available at <http://www.unrealtechnology.com>.
* For a table of contents of runtime-specific support documents, see [RuntimeTopics](RuntimeTopics.md).
* The demo version of the UnrealEngine2 Runtime is licensed for non-commercial and educational use only. Development of games for distribution is not permitted. Please read and understand the license agreement before downloading: [UnrealEngine2RuntimeEULA](UnrealEngine2RuntimeEULA.md).
* For technical features and capabilities, please see our UnrealEngine2Features? document.

## System Requirements

Please note that regardless of Runtime client and server availability, the content production software, including the UnrealEngine2 Editor and the UnrealScript gameplay scripting language compiler are available for PCs running Windows only.

### Windows 98/Me/2000/XP Minimum

* **Processor:** Intel Pentium III or AMD Athlon 733 MHz CPU
* **Memory:** 128 MByte RAM
* **Hard Disk Space:** 65 MByte free HD space
* **Video:** 16 MB NVIDIA TNT2-class or other DirectX version 8-compliant video card[1](UnrealEngine2Runtime22262002.md#sysreqvideo)
* **Sound:** Windows-compatible sound card[2](UnrealEngine2Runtime22262002.md#sysreqsound)
* **DirectX:** DirectX version 8.1b[3](UnrealEngine2Runtime22262002.md#sysreqdx)
* **Modem:** 33.3 Kbps[4](UnrealEngine2Runtime22262002.md#sysreqnet)

### Windows 98/Me/2000/XP Recommended

* **Processor:** Intel Pentium III or AMD Athlon 733 MHz CPU
* **Memory:** 256 MByte RAM
* **Hard Disk Space:** 65 MByte free HD space
* **Video:** 32 to 128 MB NVIDIA GeForce2 or ATI Radeon[1](UnrealEngine2Runtime22262002.md#sysreqvideo)
* **Sound:** Sound Blaster Audigy series sound card[2](UnrealEngine2Runtime22262002.md#sysreqsound)
* **DirectX:** DirectX version 8.1b[3](UnrealEngine2Runtime22262002.md#sysreqdx)
* **Modem:** 56.7 Kbps[4](UnrealEngine2Runtime22262002.md#sysreqnet)

 1 Indicates device should be compatible with DirectX, version 8.1 or higher. 2 NVIDIA nForce or other motherboards/soundcards containing the Dolby Digital Interactive Content Encoder required for Dolby Digital audio. 3 DirectX 8.1b is not provided with the Runtime installation, and must already be present on your system or downloaded from Microsoft. See EndUserDirectX81bInstallation? for details. 4 Modem only required for modem-based Internet multi-user networking. Internet (TCP/IP) and LAN (TCP/IP) multi-user networking is also supported.

### GNU/Linux x86, Macintosh OS X

The Runtime software is not available for these platforms. If support for these platforms is required, consider using [Unreal Engine 2](https://udn.epicgames.com/Two/UnrealEngine2). Licensing information can be found on the [Unreal Technology site](http://www.unrealtechnology.com).

## Obtaining the Runtime

### Downloading

The latest freely-available demo version of the UE2 Runtime is:

* **Download:** [UE2Runtime-22262002\_Demo.exe](http://udn.epicgames.com/Files/UE2/Runtime/UE2Runtime-22262002_Demo.exe)
* The EULA was updated November 23, 2004 and is available here: [UnrealEngine2RuntimeEULA](UnrealEngine2RuntimeEULA.md)

The most recent registered (commercial) version of the UE2 Runtime is:

* **Download:** [UE2Runtime-22262002\_Registered.exe](https://udn.epicgames.com/Files/RuntimeDev/UE2Runtime-22262002_Registered/exe)
* The Registered EULA was updated November 23, 2004 and is available here: [UnrealEngine2RuntimeRegisteredEULA](UnrealEngine2RuntimeRegisteredEULA.md)

To obtain the UE2 Unreal Script Source Code, please visit [RuntimeScripts22261903](RuntimeScripts22261903.md).To reach the most recent version of the UE2 Runtime Headers, please visit [RuntimeHeaders22262002](https://udn.epicgames.com/Two/RuntimeHeaders22262002). Note that the UE2 Runtime Headers are only available to commercial licensees who have a signed NDA on file.If downloading through your web browser, it will likely ask you what it should do with the file. Click *Save File* or *Save this program to disk*, note the location where you're saving it to, and click *OK*.

### Installing

* Once your download completes, if the dialog provides you with the option to *Open* or *Launch File*, click that option. If not, click on *Start*, *Run...*, *Browse...* and navigate to where you saved the installation file. Double-click on the file, then click *OK*.
* Click on *Setup* to begin the installation.
* Once the installation files have uncompressed, you'll be presented with the UnrealEngine2 Runtime installation dialog. Click on *Next* to view the software licensing agreement. You must agree to the terms to use the Runtime. If you agree, click on *I Agree* to proceed.
* On the next screen, you can enter an alternative location to install the Runtime; the default is recommended. Click on *Next* to continue.
* If you are installing more than one copy of the stock Runtime software, you should read the notes for the two Runtime association checkboxes. You may want to change one or both of the options.
* Finally, click *Next*, then *Install*.
* When the installation finishes, you can *Launch* the UnrealEngine2 Runtime, read the *Release Notes* or visit this website.

## Using the Runtime

* To use the Runtime, launch it by either selecting *Launch UnrealEngine2 Runtime* from the final installer screen, or by selecting *Start*, *Programs*, *UnrealEngine2 Runtime* and clicking on *Launch UnrealEngine2 Runtime*.
* The Runtime splash screen will appear, followed by the main menu. The Runtime comes with a simple example map for you to wander around and familiarize yourself with the Runtime's controls and view some of the most basic effects possible with the software.
* Click on *Load Map* to open the level. Your mouse controls your viewpoint; this is called *mouselook*. Your keyboard controls your movement independent of your viewpoint, just as you are able to walk while also turning your head to look around. Use the up and down arrow keys or *W* and *S* to move forward and backward. Use the left and right arrow keys or *A* and *D* to step left and right (not turn left and right, but rather move laterally; sidestep). Additionally, the *F* key toggles between flying mode and walking mode.
* Pressing *Esc* brings up a menu where you can close the level and return to the main screen, access your settings, or quit the program entirely.

See [Getting Started](https://udn.epicgames.com/Two/GettingStartedWith2Runtime) (UE2 Runtime) for more information.

### Configuring

* Based on your PC's hardware, the runtime will select a basic video and audio configuration. The various tabs on the Runtime menu screen allow you to modify these settings to adjust the tradeoff between rendering quality and speed. For an examination of these options, please read EndUserEngineConfiguration?.
* Additional rendering options are available by manually editing the Runtime's configuration files, such as OpenGL support, software rendering for PCs with fast CPUs but slow video cards, video refresh synchronization, and more. For an examination of these options, please read EndUserVideoConfiguration?.

## Developing for the Runtime

### Programming the Runtime

To begin writing your own functionality for the Runtime, you will need the [UnrealScript Source Code](RuntimeScripts22261903.md) (version 2226.19.03). There is also a debugger available.If you would like to create new DLLs and interfaces for your Runtime projects, the C++ [native source code headers](RuntimeHeaders.md) for the Unreal Engine 2 Runtime are available for registered users.

### Creating your own Runtime Content

* You can launch the UnrealEngine2 Editor (UnrealEd) by selecting *Start*, *Programs*, *UnrealEngine2 Runtime* and clicking on *UnrealEngine2 Editor*.
* The [UnrealEngine2](WebHome.md) area of UDN contains full documentation on the level design process. [WhatToReadFirst](WhatToReadFirst.md) is an excellent place to start.
  + Additionally, the UDN [ExampleMaps](../Content%20Creation/Techniques/ExampleMaps.md) list many small, sample levels you can download to see how certain features and functions are implemented. Make sure to download the "Runtime" versions of each one.
* Technical documentation on customizing the Runtime's interface, creating new UnrealScript code and more is underway.
  + Learn about creating your own menus at [RuntimeExampleRestrictedMenu](RuntimeExampleRestrictedMenu.md).
  + Package up your Runtime project as a standalone application by reading [MakingRuntimeInstallers](MakingRuntimeInstallers.md).
* Community Sites
  + Visit the unofficial BeyondUnreal forums for the Runtime, at <http://forums.beyondunreal.com/forumdisplay.php?f=438>

## Reporting Bugs

* As with any cutting-edge technology, there may be instances that cause the Runtime software to crash. In these corner cases, a dialog will present itself with a *Submit Bug Report* button. We would like to encourage you to report these errors using this button. Once is enough.
* If you possess a copy of the Windows PC version of the video game *Unreal Tournament 2003*, we would sincerely appreciate you attempting to repeat the actions that cause your Runtime software to crash, using UT2003, to help us determine if it is a Runtime-specific, or general engine issue.

## Known Issues

* None

## Errata

* While the extensive network capabilities of the Runtime are not exposed in the menus, they are fully functional. You can run a server from the command line using the "ucc.exe server " syntax. You can use standard console commands to open a connection to a server. To try this, run a server, then run the runtime client. In the runtime client, press *`* (backquote) to drop down the console, and type in "open " to connect to one of the servers. Once you connect, you will be able to move around and see any other visitors (all represented by cubes). You can press *T* and enter text to speak to others in the world.
