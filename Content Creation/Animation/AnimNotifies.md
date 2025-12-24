# Animation notifies

Last updated by Chris Linder (DemiurgeStudios?) for adding how multiple events are processed in close proximity to one another. Original author was Nathaniel Brown (KungFuTheatreTeam?).

* [Animation notifies](#animation-notifies) 
  + [Introduction](#introduction)
  + [Overview](#overview)
  + [Adding a notify](#adding-a-notify)
  + [Notify types](#notify-types)
    - [AnimNotify\_Effect](#animnotify-effect)
    - [AnimNotify\_Destroyeffect](#animnotify-destroyeffect)
    - [AnimNotify\_Sound](#animnotify-sound)
    - [AnimNotify\_Script](#animnotify-script)
    - [AnimNotify\_Scripted](#animnotify-scripted)
    - [AnimNotify\_MatSubAction](#animnotify-matsubaction)
    - [AnimNotify\_Trigger](#animnotify-trigger)
  + [Making new notifies, technical overview](#making-new-notifies-technical-overview)

## Introduction

Animation notifies are one of the most useful abilities of the Unreal Engine's animation system. Especially post-829, since their functionality has been expanded a great deal. They allow you to insert callbacks into an animation at a given frame in the sequence, which can perform a variety of tasks. Some examples are, but not limited to the following, AnimNotify\_Script (calls a uscript function), AnimNotify\_Sound (plays a sound), and AnimNotify\_Effect (spawns an effect, with options for attaching it to a bone).In this article I'll try to go over how they work, how to use them, what the different types do, and how to add new ones. Also I'll provide an example class, which should ease you into how to create new types.Note: This article should be useful for both artists, and programmers.

## Overview

The animation code (UnSkeletalMesh.cpp) checks for a notify in each frame for each sequence (in case of skeletal blended animation). If you want to disable a notify, a native function is provided; EnableChannelNotify() (this is pretty useful for instances of blended animation where you may not want the notify to be called). Each AnimNotify\_\* object has a Notify() function, this is where the magic is done. Each type just overrides this to add its unique functionality.

## Adding a notify

This is a relatively painless process; just go into the AnimationBrowser and select your mesh, and then the sequence you want to add a notify to. You'll see a box appear on the right panel of the browser window. It should say Animation. LOD, Mesh, Redigest, and Skin. Above that is a list of tabs, click on Notify. The item list should now just say Notify. If you click add and then new (not the button, just the text) you should be able to drop down a list of notify types you want to insert. You may have to adjust the box's size to fully see this. Once you have added your new notify type, then you need to type in the frame it should occur one (**Note:**. This is now displayed in frame numbers instead of time).The major limitation with animation notifies is that you can not add two notifies at the same time. You should also never put a notify on the very last frame because this will interfere with the *AnimEnd* event. You can put notifies very very close to each other if you want then to occur at the "same" time. For example, one notify can be at frame `20.0` and the next one can be at frame `20.001`. These two notifies will almost always be executed in the same tick but you can not guaranty it. If you **must** have two things happen at the same time, use an [AnimNotify\_Script](#animnotify-script) and write a function to do what you want. One more thing to watch out for is that the engine can only execute four animation notifies in a single tick. If there are still more to process, they will be processed the next tick. Once again, if you are really packing in many many notifies, you should probably just write a function and use [AnimNotify\_Script](#animnotify-script) .

## Notify types

Below is a list of the various default notify types and what they do.

### AnimNotify\_Effect

This notify generates an effect at the specified point in the animation, which can be either attached to a bone, spawned at a bone location, or spawned at the actors location, all of which can be offset by location and rotation.

| [Variable](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=1;up=0#sorted_table-sort-by-this-column) | [Description](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=1;up=0#sorted_table-sort-by-this-column) | [DataType](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=1;up=0#sorted_table-sort-by-this-column) |
| --- | --- | --- |
| EffectClass | Effect class type to spawn | Class (Actor) |
| Bone | Name of the bone to attach to, or spawn at (if any) | Name |
| OffsetLocation | Offset from the actor's location (or bone) | Vector |
| OffsetRotation | Offset from the actor's rotation (or bone) | Rotator |
| Attach | Whether or not to attach to the bone | Bool |
| Tag | Tag to use on the effect (for later destroying) | Name |
| DrawScale | Scale of the effect | Float |
| DrawScale3D | Axis scale of the effect | Vector |

### AnimNotify\_Destroyeffect

DestroyEffect kills an effect created by AnimNotify\_Effect.
If an emitter is used you can opt to tell it to wait till all of the particles have died before being destroyed via bExpireParticles.

| [Variable](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=2;up=0#sorted_table-sort-by-this-column) | [Description](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=2;up=0#sorted_table-sort-by-this-column) | [DataType](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=2;up=0#sorted_table-sort-by-this-column) |
| --- | --- | --- |
| DestroyTag | Tag of the effect to destroy (set by AnimNotify\_Effect) | Name |
| bExpireParticles | If effect is an emitter let all particle die before destroying | Bool |

### AnimNotify\_Sound

A simple notify that plays a sound at the specified frame.

| [Variable](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=3;up=0#sorted_table-sort-by-this-column) | [Description](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=3;up=0#sorted_table-sort-by-this-column) | [DataType](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=3;up=0#sorted_table-sort-by-this-column) |
| --- | --- | --- |
| Sound | Name of the sound to be played | Sound |
| Volume | Volume of the sound | Float |
| Radius | Radius of the sound | Int |

### AnimNotify\_Script

The classic AnimNotify, this calls an UnrealScript function at the specified frame.

| [Variable](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=4;up=0#sorted_table-sort-by-this-column) | [Description](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=4;up=0#sorted_table-sort-by-this-column) | [DataType](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=4;up=0#sorted_table-sort-by-this-column) |
| --- | --- | --- |
| NotifyName | Name of the script function to call | Name |

### AnimNotify\_Scripted

This useful notify is for easy creation of new notifies that don't require c++ code.
It has an Unrealscript event that gets fired at the appropriate frame, this allows for easy extensions. AnimNotify\_Trigger is a good example of this.

| [Variable](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=5;up=0#sorted_table-sort-by-this-column) | [Description](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=5;up=0#sorted_table-sort-by-this-column) | [DataType](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=5;up=0#sorted_table-sort-by-this-column) |
| --- | --- | --- |
| N/A | N/A | N/A |

### AnimNotify\_MatSubAction

MatSubAction allows you to add a matinee subaction at a specific point in an animation.
This could be extremely useful for triggering camera positions by gestures, or adding specific CameraEffects such as motion blur at a key point.

| [Variable](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=6;up=0#sorted_table-sort-by-this-column) | [Description](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=6;up=0#sorted_table-sort-by-this-column) | [DataType](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=6;up=0#sorted_table-sort-by-this-column) |
| --- | --- | --- |
| SubAction | Matinee subaction to perform | MatSubAction (editinline) |

### AnimNotify\_Trigger

This notify simply calls the Trigger() method of an actor whose Tag matches EventName.

| [Variable](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=7;up=0#sorted_table-sort-by-this-column) | [Description](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=7;up=0#sorted_table-sort-by-this-column) | [DataType](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=7;up=0#sorted_table-sort-by-this-column) |
| --- | --- | --- |
| EventName | Name of the actor's tag that you wish to trigger | Name |

## Making new notifies, technical overview

Found in [MakingNewAnimNotifies](https://udn.epicgames.com/Two/MakingNewAnimNotifies), for licensees only!

