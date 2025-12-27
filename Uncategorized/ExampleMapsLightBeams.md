# Light Beams Example Map

*Document Summary: A simple map that demonstrates how to simulate beams of light. Requires limited knowledge of emitters and projectors. Novices should be able to follow without much difficulty.**Document Changelog: Last updated by Tom Lin (DemiurgeStudios?), for document summary. Original author was Lode Vandevenne ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).*

* [Light Beams Example Map](ExampleMapsLightBeams.md#light-beams-example-map)
  + [Introduction](ExampleMapsLightBeams.md#introduction)
  + [Downloads](ExampleMapsLightBeams.md#downloads)

## Introduction

This map, submitted by a licensee for the 927 build and then updated for 2110, shows a way to create close to realistic light beams with a SpriteEmitter and a Projector.

![lightbeam.jpg](../assets/![lightbeam.jpg](../assets/lightbeam.jpg))

There's a window in a dusty room, the sun shines through the window, creating light beams in the dust, and shining on the wall. The dust is created with an emitter. Then, the effect of light beams is done with a projector with the texture of the window that shines on the particles. To get this to work, set in the options of the emitter in Rendering: AcceptsProjectors to True AND in the options of the Projector in Projector set bProjectParticles to True. Then the effect should work, and the projector should also shine on the wall.How good the effect looks depends on what ProjectionNormal setting (in Sprite) you set the dust emitter: PTDU\_Up looks quite good, and with PTDY\_None it looks great as well, but then it may look a little unrealistic from certain angles.Note that there are also some small dust motes in the map, this is done with another SpriteEmitter, this one is set to AcceptsProjectors as well to make sure they'll only be visible inside the light beams.

## Downloads

Below you can download a compressed archive that contains the content for this example:

* [[lightbeam.zip](../assets/lightbeam.zip)](../assets/[lightbeam.zip](../assets/lightbeam.zip))
* [EM2110\_LightBeam.zip](../assets/[em2110_lightbeam.zip](../assets/em2110_lightbeam.zip)) (for Unreal Engine 2 build 2110)
* [EM2226\_LightBearm.zip](../assets/[em2226_lightbearm.zip](../assets/em2226_lightbearm.zip)) (for Unreal Engine 2 build 2226)
