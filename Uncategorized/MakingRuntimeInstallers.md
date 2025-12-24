# Making Runtime Installers

* [Making Runtime Installers](MakingRuntimeInstallers.md#making-runtime-installers)
  + [Overview](MakingRuntimeInstallers.md#overview)
  + [Mastering](MakingRuntimeInstallers.md#mastering)
    - [Step 1: Setup](MakingRuntimeInstallers.md#step-1-setup)
    - [Step 2: Making Your First Installer](MakingRuntimeInstallers.md#step-2-making-your-first-installer)
    - [Step 3: Changing Essential Fields](MakingRuntimeInstallers.md#step-3-changing-essential-fields)
      * [SetupYourProject.INT](MakingRuntimeInstallers.md#setupyourprojectint)
      * [SetupYourProject.INI](MakingRuntimeInstallers.md#setupyourprojectini)
      * [SetupStrings.INT](MakingRuntimeInstallers.md#setupstringsint)

## Overview

This document will explain start to finish, how to pack up the runtime with whatever additions you have made for release. The Unreal Engine includes a tool for creating installers which is relatively easy to customize to suit your project's needs. The same tool described in this document was used to create the installer that installed the Runtime on your computer in the first place.Following the instructions contained in here, you ought to be able to make a functional installer in about half an hour.

## Mastering

Mastering a build is done via the `ucc master` command, which generates the installer for your project. This tool needs two files, a configuration file (.ini) and a localization file (.int) that specify, among other things, what files need to be installed on the end-user's machine in order to run, as well as the strings used for the setup. They are simple text files but they include lots of information.

### Step 1: Setup

First, **back up your Manifest.ini file**! This gets overwritten during the setup creation process, making it impossible to uninstall the Runtime later. You must back up and restore this file after you're done creating your installers!Copy [SetupYourProject.ini](rsrc/Two/MakingRuntimeInstallers/SetupYourProject.ini) and [SetupYourProject.int](rsrc/Two/MakingRuntimeInstallers/SetupYourProject.int) into the System folder in your runtime installation. Rename these two files to reflect the name of your project. Throughout this tutorial, however, they will continue to be referred to as SetupYourProject.ini and SetupYourProject.int.You will also need [SetupStrings.int](rsrc/Two/MakingRuntimeInstallers/SetupStrings.int); put it in the System folder of your project.

### Step 2: Making Your First Installer

Without filling in any of your project's specifics it's possible to generate an installer that will basically install a dummy version of the Unreal Engine 2 Runtime. To do that type the following from the command-line in the System folder of you runtime installation:

```

ucc master SetupYourProject.ini
```

A bunch of information will scroll by as the installer is generated. The dummy installer will be placed in a newly created folder called **YourProductNameCodeTODO-1** in the directory where the runtime is installed.To test out the installer go into YourProductNameCodeTODO-1/System and run the Setup.exe located there.Please note, in order to uninstall this "YourProductNameCodeTODO-1 " build and executable,
you need to make sure you have copied the following into the installed and new program file directory,
by default, C:/YourProductNameCodeTODO-1You need a copy of PixoDrv.dll and pixomatic.dll
(COPY from UT2004/System or download them)Copy into [runtimedir]/System/
(1)PixoDrv.dll
(2)pixomatic.dllThese two files:
(3) /System/SetupStrings.int
(4) /Help/InstallerLogo.bmp--++Note:
This should be a clue, in the steps that follow, that you need to properly include these above two files in your SetupYourProject.ini , in addition to the below tasks.That's it! Obviously there's a bit of work to do to customize the installer to suit your needs. Some of the important stuff is covered next...

### Step 3: Changing Essential Fields

The [SetupYourProject.ini](rsrc/Two/MakingRuntimeInstallers/SetupYourProject.ini), [SetupYourProject.int](rsrc/Two/MakingRuntimeInstallers/SetupYourProject.int) and [SetupStrings.int](rsrc/Two/MakingRuntimeInstallers/SetupStrings.int) files have "TODO" written on every line you'll want to eventually change.

#### SetupYourProject.INT

Update the following lines in [SetupYourProject.int](rsrc/Two/MakingRuntimeInstallers/SetupYourProject.int) to reflect your project's name and other information:

|  |  |
| --- | --- |
| LocalProduct= | A nice readable name for your product |
| DefaultFolder= | The default folder to install to. If your project is installed to a folder name with a space, end-users will likely have trouble running UnrealEd |
| SetupWindowTitle= | The text to be displaced in the title bar of the setup window |
| Developer= | Your name or your company's name |
| DeveloperURL= | You or your company's website |
| Logo= | A .bmp file to place at the top of the installer. This image should be 343x82 pixels, and 8-bit (256 colors). |
| PlayLevelCommand= | A string describing a button that starts your product |
| OpenLinkCommand= | A string describing a button that opens your product's website |
| Caption= | There are a number of captions for the icons placed in the start menu. Update all of these according to the supplied .INT file's descriptions |

#### SetupYourProject.INI

**Setup**

|  |  |
| --- | --- |
| Product= | A code without spaces that describes your project. It will be used as a unique identifier for your project so that installing/uninstalling doesn't interact incorrectly with other Unreal Engine 2 projects. |

**HelpGroup**There are a number of *File=* lines in SetupYourProject.ini. Create the appropriate files and update the lines by changing the names of the files and removing the ";" from the beginning of the line.

|  |  |
| --- | --- |
| YourProductReadme.txt | This file is the "readme" file for your project. It can be opened from the installer. |
| YourProductLogo.bmp | A splash-screen for your project |
| YourProductInstallerLogo.bmp | A bitmap that will go in the installer. This image should be 343x82 pixels, and 8-bit (256 colors). |
| YourProduct.url | A file containing a link to your project. See UDN.url in the runtime distribution for the format of this file |

**ProjectGroup**This section contains a list of files that make up the core of your project. Content should not go here, but things that are required to launch the project even without a map, such as fonts belong here. Also include any new .dll's, .u's, or other system files.**ContentGroup**This section contains a list of files that make up your project's content such as maps, static meshes and textures.**Other Sections**There are a few other "TODO"s in the .ini file, they're all self-explanitory.

#### SetupStrings.INT

Feel free to alter any of these strings. Not all are used, but there are two mandatory ones:

|  |  |
| --- | --- |
| IDC\_Play= | A string describing a button that launches your project. |
| IDC\_Web= | A string describing a button that opens your project's website. |
