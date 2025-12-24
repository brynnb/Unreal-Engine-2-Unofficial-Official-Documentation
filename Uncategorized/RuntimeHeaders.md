# UnrealEngine2 Runtime Native Source Code Headers

![urt_logo.jpg](../assets/urt_logo.jpg)

*Document Summary: Introduction to the native source code headers for the [UnrealEngine2Runtime](UnrealEngine2Runtime.md), including release information.*

* [UnrealEngine2 Runtime Native Source Code Headers](RuntimeHeaders.md#UnrealEngine2 Runtime Native Source Code Headers)
  + [Overview](RuntimeHeaders.md#Overview)
  + [About the Native Source Code Headers](RuntimeHeaders.md#About the Native Source Code Headers)
  + [Obtaining the Native Source Code Headers](RuntimeHeaders.md#Obtaining the Native Source Code Headers)

## Overview

The C++ native source headers for the Unreal Engine 2 Runtime allow you to create new DLLs and interfaces for your Runtime projects. Past use has included 360 degree rendering drivers for VR systems, interfaces to motion capture devices, and integration with other software systems like natural language processing, AI and VoIP tools.The C++ headers are made available under the same license as the registered version of the Unreal Engine 2 Runtime. The EULA is available here: [UnrealEngine2RuntimeRegisteredEULA](UnrealEngine2RuntimeRegisteredEULA.md). The headers are only available under non-disclosure agreement. Do not use the Runtime or the headers if you cannot agree to the terms and conditions.

## About the Native Source Code Headers

The Unreal engine is primarily designed to be extended in two ways: by the community using the publicly available script interface and by licensees with full C++ access. The idea of releasing the C++ headers without the full code was never a development path intended in the engine's architecture, so there are some limitations on the access to engine functions given by the headers. In general:All of the interesting gameplay functionality is exposed through script, which is powerful enough to do almost any platform-independent game programming. The big limitation of script is that it can't easily interface to external libraries or peripherals. This limitation was necessary because scripts and mods can run cross-platform on Windows, Linux, Mac, Xbox, etc., without even being recompiled.All the C++ headers can be counted on to do is bridge the gap between the UnrealScript gameplay code, and external libraries and peripherals. With the headers, one can expose an external library or peripheral to script fairly easily. Thus the headers can be useful for interfacing scripts with:

* External AI libraries.
* External networking libraries.
* External input devices or input libraries.
* External libraries that do anything else related to gameplay, stats, input, or otherwise examining or manipulating the state of the game.

However, the C++ headers don't expose enough of the engine's internals to go much beyond gameplay programming. For example, adding new rendering features to the engine, new sound features, new collision features, new UnrealEd functionality, and so on -- all of these tasks require access to the engine's full C++ code.

## Obtaining the Native Source Code Headers

The headers are only given to registered commercial or academic licensees of the runtime who have signed an NDA. If you do not have access to the links below, you should contact your account representative.Versions are labeled in xxxx.yy.zz fashion, where xxxx is the Unreal Engine 2 version, yy is the patch level and zz is the Runtime version.The latest version is [version 2226.20.02](https://udn.epicgames.com/Two/RuntimeHeaders22262002), corresponding to [version 2226.20.02](UnrealEngine2Runtime22262002.md) of the Unreal Engine 2 Runtime.
