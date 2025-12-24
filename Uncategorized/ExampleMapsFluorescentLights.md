# Fluorescent Lights Example Map

*Last updated by Jason Lentz (DemiurgeStudios?), to separate from the main [ExampleMaps](../Content Creation/Techniques/ExampleMaps.md) doc. Original author was Lode Vandevenne ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).*

* [Fluorescent Lights Example Map](ExampleMapsFluorescentLights.md#Fluorescent Lights Example Map)
  + [Introduction](ExampleMapsFluorescentLights.md#Introduction)
  + [Downloads](ExampleMapsFluorescentLights.md#Downloads)

## Introduction

This map, for the 927 build, has 8 realistic TL lights: if you turn them on, they'll first blink for a while before eventually going on.If you give it a sound, the sound will go on and off too. You may have to increase your volume to hear the sound. You can adjust a lot:

* bInitiallyOff: choose if the TL light will be on or off in the beginning.
* FlickerTime: how long it will flicker before it goes on.
* OnChance: while it flickers, how often the light will be on or off, 0.5 means 50/50.
* Period: the length of 1 flicker.
* TriggerAction: if the light should ignore events, go on after an event, go off after an event, or toggle on/off after an event.

NOTE: if you use TriggerToggle, please set the ReTriggerDelay of the trigger to 0.5, otherwise the light may go out again if the trigger touch accidently gets detected twice. This seems to happen quite often.This TL light is just an example of a scripted light: to make a scripted light, the light must have bStatic = False and bDynamicLight = True in its properties, otherwise it'll ignore its script. Once you did that, you can change almost anything, including the radius, color, corona, lighttype, sound... with a script.This is UNTESTED in multiplayer, the TL lights should have bStatic = False in the Default Properties (but the setting is hidden), and the behavior on the clients and the server is untested.

## Downloads

Below you can download a compressed archive that contains the content for this example:

* [TL.zip](../assets/TL.zip)
