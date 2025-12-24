# Why Hardware Brushes Have No LOD

*Document Summary: A fairly technical discussion of the limitations of LOD on static meshes. Good for intermediate to advanced users.**Document Changelog: Last updated by Tom Lin (DemiurgeStudios?), for document summary. Original author was Vito Miliano ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)). Based on an [ongoing January 29 thread](https://udn.epicgames.com/lists/showpost/php?list=unedit&id=7845&lessthan=7854&show=20) on [UnEdit](https://udn.epicgames.com/Two/UnEdit).*

* [Why Hardware Brushes Have No LOD](NoLodOnHardwareBrushes.md#Why Hardware Brushes Have No LOD)
  + [Overview](NoLodOnHardwareBrushes.md#Overview)
  + [Triangle throughput](NoLodOnHardwareBrushes.md#Triangle throughput)
  + [Good LOD is Hard to Do](NoLodOnHardwareBrushes.md#Good LOD is Hard to Do)
  + [Vertex Throughput](NoLodOnHardwareBrushes.md#Vertex Throughput)

## Overview

Hardware brushes have no LOD (level of detail). This is by design. For the same reasons that BSP brushes [don't convert optimally](ConvertingBspBrushesIsSuboptimal.md) to hardware brushes, implementing your own discrete or dynamic LOD for hardware brushes isn't recommended.

## Triangle throughput

Triangle throughput of static meshes is already extremely fast. The significant slowdowns are per-object and per-state-change overhead, which a LOD system won't improve at all. Therefore, reducing polygon counts based on distance won't gain you much performance.The benchmark specifics: Dan Vogel ([EpicGames](https://udn.epicgames.com/Main/EpicGames)) clocked 85fps in an untextured (rmode 7, lighting only) room with 21 ~16k poly spheres (~340,000 triangles in view) at 1280x1024 on a 1GHz Athlon and Radeon 8500. The framerate gets cut in half if you enable texturing and it gets worse if you use multiple layers and/or cubemaps.

## Good LOD is Hard to Do

It's hard to do this well for typical static meshes. LOD works well on characters because they're curvy and contain a lot of high-frequency detail that can be eliminated without changing topology/volume significantly. But on regular objects like architectural building blocks, LOD tends to change the shape of objects significantly, which looks bad.

## Vertex Throughput

It's really hard to create a level where you are vertex throughput bound. Most of the time you'll end up being fillrate or texture memory bandwidth bound. The first one scales nicely with resolution and the second one with texture resolution. Those approachs are much easier to use to ensure a steady framerate than using an LOD scheme.
