# UnrealEngine2 Runtime UnrealScript Source Code (version 2226.19.03)

![urt_logo.jpg](../assets/urt_logo.jpg)

*Document Summary: Introduction to the [UnrealEngine2Runtime](UnrealEngine2Runtime.md) UnrealScript source code, including release information.**Document Changelog: Created and updated; maintained over time.*

* [UnrealEngine2 Runtime UnrealScript Source Code (version 2226.19.03)](RuntimeScripts22261903.md#UnrealEngine2 Runtime _UnrealScript Source Code (version 2226.19.03))
  + [Overview](RuntimeScripts22261903.md#Overview)
  + [Obtaining the UnrealScript Source Code](RuntimeScripts22261903.md#Obtaining the _UnrealScript Source Code)
    - [Downloading](RuntimeScripts22261903.md#Downloading)
  + [Installing](RuntimeScripts22261903.md#Installing)
  + [Developing with the UnrealScript Source Code](RuntimeScripts22261903.md#Developing with the _UnrealScript Source Code)
    - [Debugging](RuntimeScripts22261903.md#Debugging)

## Overview

The source code is made available under the same license as the [UnrealEngine2Runtime22261903](../Powered/UnrealEngine2Runtime22261903.md) ([also online](rsrc/Powered/UnrealEngine2Runtime22261903EULA/)). Do not use the Runtime or the source code if you cannot agree to the terms and conditions.This page provides links to download version **2226.19.03** of the UnrealEngine2 Runtime UnrealScript source code, corresponding to the same version of the [UnrealEngine2Runtime](UnrealEngine2Runtime.md).

## Obtaining the UnrealScript Source Code

### Downloading

* **Download:** [UE2RuntimeScripts-22261903.zip](http://udn.epicgames.com/Files/UE2/Runtime/UE2RuntimeScripts-22261903.zip) (508 KBytes; 516,980 bytes; October 22, 2003)

If downloading through your web browser, it will likely ask you what it should do with the file. Click *Save File* or *Save this program to disk*, note the location where you're saving it to, and click *OK*.

## Installing

**Please note:** If you **unchecked** *Runtime modification association* when you originally install the UnrealEngine2 Runtime -- that is, if you did not just simply hit *Next* several times -- you will need to manually install the UnrealScript sources by uncompressing the archive to your Runtime's System, and launching the Runtime install manually, using the command line *setup.exe install ue2uscript.urm* from within your Runtime's System directory.Otherwise, please follow the instructions below:

* Once your download completes, if the dialog provides you with the option to *Open* or *Launch File*, click that option. If not, click on *Start*, *Run...*, *Browse...* and navigate to where you saved the installation file. Double-click on the file, then click *OK*.
* Double-click on *UE2UScript.urm* to launch the Runtime installer. Click on *Next* to proceed.
* On the next screen, you can enter an alternative location to install the UnrealScript sources; the default is highly recommended, as the compiler does not immediately support other paths. Click on *Next* to continue.
* Finally, click *Next*, then *Install*.
* When the installation finishes, you can read the *Release Notes* ([also online](rsrc/Two/RuntimeScripts22261903/RuntimeScripts.txt)) or visit the *UnrealEngine2 Runtime UnrealScript Source Code web site* (this site).

## Developing with the UnrealScript Source Code

### Debugging

The UnrealEngine2 Runtime ships with a version of the UnrealScript Debugger. This application allows you to step through running UnrealScript code to more easily debug your programs. Specially compiled versions of the stock Runtime packages are provided for this purpose. Their use is unsupported. Please back up your existing packages, as the debug versions are not network compatible, are not to be redistributed with your runtime projects and will slow down your execution time.

* **Download**: [UE2RuntimeDebugU-22261903.zip](http://udn.epicgames.com/Files/UE2/Runtime/UE2RuntimeDebugU-22261903.zip) (1.2 MBytes; 1,216,331 bytes; October 27, 2003)
