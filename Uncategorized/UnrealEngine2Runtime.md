# UnrealEngine2 Runtime

![urt_logo.jpg](../assets/urt_logo.jpg)

*Document Summary: Introduction to the UnrealEngine2 Runtime edition of the second-generation Unreal engine, including release information.**Document Changelog: Created and updated; maintained over time.*

* [UnrealEngine2 Runtime](UnrealEngine2Runtime.md#UnrealEngine2 Runtime)
  + [Overview](UnrealEngine2Runtime.md#Overview)
  + [Introduction](UnrealEngine2Runtime.md#Introduction)
  + [System Requirements](UnrealEngine2Runtime.md#System Requirements)
    - [Windows 98/Me/2000/XP Minimum](UnrealEngine2Runtime.md#Windows 98/Me/2000/XP Minimum)
    - [Windows 98/Me/2000/XP Recommended](UnrealEngine2Runtime.md#Windows 98/Me/2000/XP Recommended)
    - [GNU/Linux x86, Macintosh OS X](UnrealEngine2Runtime.md#GNU/Linux x86, Macintosh OS X)
  + [Obtaining the Runtime](UnrealEngine2Runtime.md#Obtaining the Runtime)
  + [Reporting Bugs](UnrealEngine2Runtime.md#Reporting Bugs)
  + [Known Issues](UnrealEngine2Runtime.md#Known Issues)
  + [Errata](UnrealEngine2Runtime.md#Errata)

## Overview

This page provides information about the UnrealEngine2 Runtime software, its documentation, release notes and errata.

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
* **Video:** 16 MB NVIDIA TNT2-class or other DirectX version 8-compliant video card[1](UnrealEngine2Runtime.md#SysReqVideo)
* **Sound:** Windows-compatible sound card[2](UnrealEngine2Runtime.md#SysReqSound)
* **DirectX:** DirectX version 8.1b[3](UnrealEngine2Runtime.md#SysReqDX)
* **Modem:** 33.3 Kbps[4](UnrealEngine2Runtime.md#SysReqNet)

### Windows 98/Me/2000/XP Recommended

* **Processor:** Intel Pentium III or AMD Athlon 733 MHz CPU
* **Memory:** 256 MByte RAM
* **Hard Disk Space:** 65 MByte free HD space
* **Video:** 32 to 128 MB NVIDIA GeForce2 or ATI Radeon[1](UnrealEngine2Runtime.md#SysReqVideo)
* **Sound:** Sound Blaster Audigy series sound card[2](UnrealEngine2Runtime.md#SysReqSound)
* **DirectX:** DirectX version 8.1b[3](UnrealEngine2Runtime.md#SysReqDX)
* **Modem:** 56.7 Kbps[4](UnrealEngine2Runtime.md#SysReqNet)

 1 Indicates device should be compatible with DirectX, version 8.1 or higher. 2 NVIDIA nForce or other motherboards/soundcards containing the Dolby Digital Interactive Content Encoder required for Dolby Digital audio. 3 DirectX 8.1b is not provided with the Runtime installation, and must already be present on your system or downloaded from Microsoft. See EndUserDirectX81bInstallation? for details. 4 Modem only required for modem-based Internet multi-user networking. Internet (TCP/IP) and LAN (TCP/IP) multi-user networking is also supported.

### GNU/Linux x86, Macintosh OS X

The Runtime software is not available for these platforms. If support for these platforms is required, consider using [Unreal Engine 2](https://udn.epicgames.com/Two/UnrealEngine2). Licensing information can be found on the [Unreal Technology site](http://www.unrealtechnology.com).

## Obtaining the Runtime

Versions are labeled in *xxxx.yy.zz* fashion, where *xxxx* is the UnrealEngine2 version, *yy* is the patch level and *zz* is the Runtime version.The latest version of the UE2 Runtime is **2226.20.02**. You can reach demo and registered versions of the Runtime here:

* [UnrealEngine2 Runtime 2226.20.02](UnrealEngine2Runtime22262002.md)
* The EULA was updated November 23, 2004 and is available here: [UnrealEngine2RuntimeEULA](UnrealEngine2RuntimeEULA.md)
* The Registered EULA was updated November 23, 2004 and is available here: [UnrealEngine2RuntimeRegisteredEULA](UnrealEngine2RuntimeRegisteredEULA.md)

See [Getting Started](https://udn.epicgames.com/Two/GettingStartedWith2Runtime) (UE2 Runtime) for more information.

## Reporting Bugs

* As with any cutting-edge technology, there may be instances that cause the Runtime software to crash. In these corner cases, a dialog will present itself with a *Submit Bug Report* button. We would like to encourage you to report these errors using this button. Once is enough.
* If you possess a copy of the Windows PC version of the video game *Unreal Tournament 2003*, we would sincerely appreciate you attempting to repeat the actions that cause your Runtime software to crash, using UT2003, to help us determine if it is a Runtime-specific, or general engine issue.

## Known Issues

* None

## Errata

* While the extensive network capabilities of the Runtime are not exposed in the menus, they are fully functional. You can run a server from the command line using the "ucc.exe server " syntax. You can use standard console commands to open a connection to a server. To try this, run a server, then run the runtime client. In the runtime client, press *`* (backquote) to drop down the console, and type in "open " to connect to one of the servers. Once you connect, you will be able to move around and see any other visitors (all represented by cubes). You can press *T* and enter text to speak to others in the world.
