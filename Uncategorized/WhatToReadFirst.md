# What To Read First for the Unreal Engine 2

* [What To Read First](WhatToReadFirst.md#What To Read First)
  + [Getting the Engine](WhatToReadFirst.md#Getting the Engine)
  + [Engine Support](WhatToReadFirst.md#Engine Support)
    - [Documentation](WhatToReadFirst.md#Documentation)
      * [Navigating the Web Sites](WhatToReadFirst.md#Navigating the Web Sites)
      * [A Caveat on UDN Documentation](WhatToReadFirst.md#A Caveat on UDN Documentation)
      * [Reading the Documentation](WhatToReadFirst.md#Reading the Documentation)
      * [For programmers and other technical people](WhatToReadFirst.md#For programmers and other technical people)
      * [For Texture Artists](WhatToReadFirst.md#For Texture Artists)
      * [For Modelers](WhatToReadFirst.md#For Modelers)
      * [For Level Designers](WhatToReadFirst.md#For Level Designers)
    - [Mailing Lists - Subscribing to UnProg, UnEdit](WhatToReadFirst.md#Mailing Lists - Subscribing to _UnProg, _UnEdit)
    - [IRC: Joining the Party](WhatToReadFirst.md#IRC: Joining the Party)
    - [If You Find a Problem](WhatToReadFirst.md#If You Find a Problem)
    - [If You Have a Problem](WhatToReadFirst.md#If You Have a Problem)

This page is designed to introduce both technical and artistic developers to the Unreal Engine 2 and provide the resources for getting started. Please use this page as a roadmap of steps to follow and processes to take when developing a project using the Unreal Engine 2.

## Getting UE2

UE2 is no longer provided by Epic Games. Please visit [www.unrealengine.com](https://www.unrealengine.com/) for the latest Unreal Engine version.

## Documentation

UE2 documentation can be found [here](SiteMap.md).

#### A Caveat on UE2 Documentation

Documentation is focused on practicality and pragmatism. We try to get you up and running as fast as possible, as easily as possible. To do this, we encourage doing things "the Unreal way," which is however the engine prefers to have things done. In some instances, this may seem backwards, or roundabout, or may require *what appears to be* some semblance of tomfoolery.However, please remember that the engine is an established system, and for the most part there practical reasons why something has to be a done a certain way in a certain instance, and the solutions that we provide are usually the best and most practical *within the context of the Unreal engine.* As has been stated in the past, a system designed in isolation could easily be more advanced, easier to work with, or more efficient than Unreal's, but it would also probably cause countless headaches when making it work with the rest of the codebase and making it run at a decent frame rate.We therefore encourage you to use the solutions we provide in an effort to minimize your manipulation of the core engine, as it will save you innumerable hours of time and effort working with and merging future builds. As with all projects using licensed technology, you have to weigh the time and effort to merge updated code with the theoretical improvement your changes (or wholesale subsystem replacement) will make.

#### Reading the Documentation

After getting yourself set up with the [RecommendedHardware](RecommendedHardware.md), and then check out the latest CodeDropXYZ page, at the top of the *Codedrop-Specific Support* list in the table of contents. That will be the latest official codedrop release, and provide download links and errata, including bug fixes and known issues.

#### For programmers and other technical people

Once you have the drop, the [NewProjectPreparation](https://udn.epicgames.com/Two/NewProjectPreparation) page should be your first stop. It will walk you through stripping the codebase down and re-integrating it with all your own code and components. It is currently a work-in-progress.The *Toolchain Support* area of the table of contents lists several documents which may be useful. From setting up Visual SourceSafe to working with VTune, we try to make working with the engine easier here.From there, the main body of the table of contents is sorted by feature, for you to reference as you need to know about certain functionality. Some tutorials are provided, such as working with the skeletal system and with the HUD, and we're always working on more.Nearer the bottom of the list, is the [LicenseeCodePool](https://udn.epicgames.com/Two/LicenseeCodePool) page; consider contributing some of your more general functionality back to the site. When you start actively working with the engine, make sure you add your project's file extensions and Gamespy ID to the [LicenseeFileExtensions](https://udn.epicgames.com/Main/FileExtensions) list. And if you have any documentation requests, please don't hesitate to add it to the [UdnStaff](https://udn.epicgames.com/Main/UdnStaff) page.

#### For Texture Artists

For 2D artists, [TextureSpecifications](../Content Creation/Lighting and Textures/TextureSpecifications.md) and [TextureComparison](../Content Creation/Lighting and Textures/TextureComparison.md) are good starting points, followed by [MaterialTutorial](../Content Creation/Lighting and Textures/MaterialTutorial.md), since level designers aren't going to be using your raw textures directly; they're going to be using them in materials (like shaders).

#### For Modelers

Modelers can head straight for the bottom of the page, in the Tools area, where most of the skeletal animation documentation currently resides.

#### For Level Designers

Level designers and level artists get the rest. I'd suggest beginning with [UnrealEdInterface](../Content Creation/Basics/UnrealEdInterface.md), and then starting to work through the docs in *Primitives*, in order. Then go back up and review the rest of the docs in the *Basics* section, because they make more sense if you already know how to build basic brushes and things. Also if you haven't already checked it out, take a look at the [IntroToUnrealEd](../Content Creation/Basics/IntroToUnrealEd.md) document.
