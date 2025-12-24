# Unreal Cache Lists Tutorial

*Document Summary: Tutorial which briefly describes how to use the UT2004 caching system.**Document Changelog: Original revision.*

* [Unreal Cache Lists Tutorial](UnrealCacheLists.md#unreal-cache-lists-tutorial)
  + [Overview](UnrealCacheLists.md#overview)
  + [Preparation](UnrealCacheLists.md#preparation)
  + [Exporting](UnrealCacheLists.md#exporting)

## Overview

Loading an unreal package, like anything else, takes time. The caching system for UT2004 was introduced for 2 reasons:

* Speed - accessing values for properties in a class requires that the class first be loaded into memory (for obvious reasons).If this is the first time (during the current gaming session) that the class is being referenced, the engine must first loadthe package containing the class into memory. When this happens, you might experience a slight pause in gameplay, or hitch, whilethe package is loaded from disk. Many times, the class is no longer needed once the value of the property is read.  
    
  The caching system helps reduce the number of hitches during the game by eliminating unnecessary loading of packages for caseswhere the properties being referenced are static - that is, their values do not change at runtime. Gametype acronyms, map names, andmutator descriptions are perfect examples of these types of properties.

* Simplification - provides a centralized location for storing and retrieving static property values for supported classes. Theformat of the caching system allows for additional properties to be made cacheable without changing any existing code.

## Preparation

In addition to maps, the following class types are supported by the caching system:

* Gametypes (subclasses of GameInfo?)
* Mutators (subclasses of Engine.Mutator)
* Weapons (subclasses of Engine.Weapon)
* Custom crosshairs (subclasses of CrosshairPack?)
* Vehicles (subclasses of Engine.Vehicle)
* Custom announcers (subclasses of AnnouncerVoice?)

Only classes of the above types will be exported by the caching system. Some types have certain requirements in order to be imported from the caching file into the game correctly. They are as follows:

|  |  |
| --- | --- |
| Maps | Must have Acronym set in LevelInfo |
| Game Types | Must have Acronym and MaplistClassname set in defaultproperties |
| Crosshairs | Must be able to load the crosshair texture |
| Announcers | If bEnglishOnly is true, will not be available when game is running in other languages |

If a class fails to meet one of the above criteria, you have the option of seeing a warning written to the game's log file (UT2004.log). By default, this option is disabled. In order to see these messages, remove (or disable using a semi-colon) the line in the UT2004.ini file that reads `Suppress=RecordCache`.

## Exporting

To have your custom content appear in the game, it must have an associated cache entry. Cache entries are stored in unreal cache list files. These files have a .ucl extension, and can be generated automatically using the 'exportcache' commandlet. The syntax for the exportcache commandlet is as follows:`ucc exportcache [-a][ -y][ -v][ -nocreate][ -mod=<foldername>] <file.ext> [file.ext file.ext] [DestFile.ucl]`Options:

|  |  |
| --- | --- |
| -a (or -append) | Cache entries should be appended to the end of the cache list file, replacing any existing matching entries. |
| -y (or -yes) | Automatically overwrite read-only files. |
| -v (or -verbose) | Enables detailed logging of cache activities (for debugging). |
| -nocreate | Indicates that no new cache list files should be created; existing cache list files may be updated. |
| -mod=<modname> | Mod directory support. |
| file.ext | File that should be exported. Only .u and .ut2 files may be exported. You may specify files individually, seperating filenames with spaces. The \* wildcard is supported. |
| DestFile.ucl | By default, each package receives its own .ucl file. You may group multiple package's cache entries into a single file, however, by specifying a destination filename on the command-line. You must include the .ucl part in order for this parameter to be recognized. Keep in mind that even if you change the extension for cache list files by altering the CacheRecordPath, this parameter must still contain .ucl (the file would be written using the correct extension, however). |

Cache files should never be modified manually. If changes need to be made to a .ucl file, the corresponding property should be first be changed in the class or map file, and the .ucl file should be regenerated using the exportcache commandlet.In order to make the transition from the old .int based system to the new cache entry based system, the game will automatically create ucl entries for any gameinfo, mutator, or weapon entries that are found in the [Public] section of .int files. Cache entries will also be created automatically for any new maps which are found. Folders are scanned at each mapchange for new packages and cache list files. When packages are deleted or otherwise removed from their respective directories, any existing cache entries for content from those packages will be removed from the cache list file. When the last cache entry is removed from a cache list file, the cache list file will be deleted.
