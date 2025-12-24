# Recommended and Required Hardware for Unreal Development

*Last updated by Chris Linder (DemiurgeStudios?) to date this document. Original author was Tim Sweeney / Vito Miliano ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).*

* [Recommended and Required Hardware for Unreal Development](RecommendedHardware.md#recommended-and-required-hardware-for-unreal-development)
  + [Guide to Buying Computers for Unreal Development](RecommendedHardware.md#guide-to-buying-computers-for-unreal-development)

## Guide to Buying Computers for Unreal Development

*NOTE: This document was written in December 2002 and as such, the hardware specs and prices reflect this. Aside from the hardware and price specifics, the general information is still quite valuable. (Mar-12-2004)*Unreal editing and compiling performance is so close between top-of-the-line Athlons and P4's that it shouldn't be a determining factor when buying computers for development.Neither the engine nor editor nor the Visual C++ compiler are multithreaded, so getting dual-CPU systems won't increase performance of compiles or map rebuilds directly. However, with dual CPU's and plenty of RAM, you can very comfortably edit code in Visual Studio or browse the web while waiting for a rebuild or recompile. Also you can test network play running a separate client and server executable on the same machine very comfortably. With a single CPU, recompiling or rebuilding takes so much CPU time that it's impractical to use your computer for anything else.All the Epic programmers use dual Athlon 1800+'s and faster as their primary work machines, except Steve who uses his Dell P4/GeForce4MX laptop. The level designers use a mix of single-processor P4's and Athlons, and most of them have more than one machine on their desk.Our reason for choosing Athlon's for our dual CPU workstations is cost: we can get top-of-the-line dual Athlon workstations for around $3200 from GamePC.com, while equivalant-performing dual-P4 workstations are around $2000 more from that vendor, or $4000 more from Dell.Here are some things to consider:

* For development (huge compiles and rebuilds, especially) having lots of RAM will give you a significant speedup. I recommend a gigabyte if buying a new computer now. A gig of DDR only costs around $250, so price shouldn't be an issue.

* Never buy SCSI hard drives. In our experience, their performance is now lower than 7200 RPM IDE drives, their prices are much higher, and their capacities are lower.

* A dual monitor, dual-CPU setup tends to give you more usability at less cost than having 2 PC's. If you want dual monitor buy a dual-head video card, don't try to mix a PCI & AGP graphics card.

* LCD monitors are much easier on the eyes than CRT's for writing code (no flicker, less blurry), but suck for all 3D work because of their slow persistence (causing a hazy motion blur effect on everything that moves). Programmers should consider a dual monitor setup with an LCD mainly for code, and a CRT mainly for playing & 3D work. *Note by Vito: Modern digital (DVI) LCDs are much less susceptible to pixel persistence than analog LCDs (ones that use a normal VGA adapter). A dual DVI LCD setup can to be vastly superior to a single DVI LCD and a CRT.*

* Look at reasonably-priced vendors like [GamePC.com](http://www.gamepc.com/). They make a lot of sense nowadays. Their prices are much lower than big-name vendors like Dell, their systems are far better configured than retail PC's, and everyone's quality is basically identical nowadays - all these companies will ship you a working PC, and they all use the same basic components so they're all equally likely to break down. Don't worry about whether these companies have comparable service to "big name" guys like Dell or IBM. Service is irrelevant now: if a clone PC dies (motherboard or CPU problem) you can just order a new component fedex and replace it yourself for a few hundred bucks at most, and have it back up and running 2 days later. If a proprietary-motherboard PC dies (like a Dell), you have to wait on hold for hours to talk to them, pack up your computer in a box, ship it, then lose the use of your computer for weeks while waiting for them to fix it.

* Windows 2000 and XP seem to perform equally well.

* Any sound card brand should be fine.

-Tim
