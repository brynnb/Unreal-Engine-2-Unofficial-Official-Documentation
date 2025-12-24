# Search .UC files in Windows XP

*Last updated by Vito Miliano ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)) to prepare for public release.*

* [Search .UC files in Windows XP](#search-uc-files-in-windows-xp)
  + [Overview](#overview)
  + [Usage](#usage)
  + [Fin](#fin)

## Overview

If you're like me, not a programmer but you still have to often search through UnrealScript Class (.uc) files, and you use Windows XP, you may have run into a frustrating bug with Explorer's search in that it won't look for keywords inside .uc files, even though they're really just plain text. Here's a registry key for WinXP that will create a new file type called "UnrealScript" and tell Explorer's search to search 'em. The file type only has one option, "edit," which puts the .uc file in Notepad.Programmers might not want to install it, as they have more sophisticated techniques at hand for searching files and this might break 'em! ;D

## Usage

Just extract the attached Zip file and merge in the registry key. You'll need to close and re-open any open windows for it to take effect. Also note I've only tested it with WinXP.

## Fin

Many thanks to the author of this Web page, whose info helped me solve the problem! <http://www.dougknox.com/xp/tips/xp_bad_search.htm>Enjoy!DP

