# Sound Reference

*Created on 7/11/03 by Chris Linder (DemiurgeStudios?) for v2226.*
  
*Updated on 7/21/03 by Chris Linder (DemiurgeStudios?), to separate C++ Audio Subsystem code into its own doc.*
  
*Updated on 7/22/03 by Chris Linder (DemiurgeStudios?), for first public release.*
  
*Updated on 11/10/03 by Jan Svarovsky (KujuEntertainment?), for sound volume/radius clarification.*
  
*Updated on 2005-04-03 by Michiel Hendriks, v3323 update.*

* [Sound Reference](SoundReference.md#Sound Reference)
  + [Related Documents](SoundReference.md#Related Documents)
  + [Intro](SoundReference.md#Intro)
  + [Importing Sounds in UnrealEd](SoundReference.md#Importing Sounds in _UnrealEd)
  + [Script Sound Functions](SoundReference.md#Script Sound Functions)
    - [PlaySound](SoundReference.md#PlaySound)
      * [Single vs. Multiplayer Use of PlaySound](SoundReference.md#Single vs. Multiplayer Use of _PlaySound)
    - [PlayOwnedSound](SoundReference.md#PlayOwnedSound)
      * [Summary of PlayOwnedSound](SoundReference.md#Summary of _PlayOwnedSound)
      * [Details](SoundReference.md#Details)
    - [DemoPlaySound](SoundReference.md#DemoPlaySound)
    - [GetSoundDuration](SoundReference.md#GetSoundDuration)
    - [PlayMusic](SoundReference.md#PlayMusic)
    - [StopMusic](SoundReference.md#StopMusic)
    - [StopAllMusic](SoundReference.md#StopAllMusic)
    - [Music streams](SoundReference.md#Music streams)
      * [PlayStream](SoundReference.md#PlayStream)
      * [StopStream](SoundReference.md#StopStream)
      * [SeekStream](SoundReference.md#SeekStream)
      * [AdjustVolume](SoundReference.md#AdjustVolume)
      * [PauseStream](SoundReference.md#PauseStream)
  + [Variables](SoundReference.md#Variables) 
    - [TransientSoundVolume](SoundReference.md#TransientSoundVolume)
    - [TransientSoundRadius](SoundReference.md#TransientSoundRadius)
    - [SoundOcclusion](SoundReference.md#SoundOcclusion)
    - [AmbientSound](SoundReference.md#AmbientSound)
    - [SoundRadius](SoundReference.md#SoundRadius)
    - [SoundVolume](SoundReference.md#SoundVolume)
    - [SoundPitch](SoundReference.md#SoundPitch)
    - [bFullVolume](SoundReference.md#b_FullVolume)

## Related Documents

[AudioSubsystemReference](https://udn.epicgames.com/Two/AudioSubsystemReference), [ExampleMapsSounds](ExampleMapsSounds.md)

## Intro

This document will go over the script functions and variables relating to sound and music. All the functions and variables are described in great detail as well as how and when to use them. Also covered are replication and the implications of using different sound functions in both single and multi player situations. While this document is mainly aimed at a technical audience, importing sounds as well as the variables relating to ambient sound should be useful for a non-technical audience as well.

## Importing Sounds in UnrealEd

You can import just about any WAV file into Unrealed. Sounds can be mono or stereo, they can be 8-bit or 16-bit, and they can have different sampling rates from 8,000 to 44,100 Hz and beyond. If you want a sound to play in 3D, it must be mono however. (See [PlaySound](SoundReference.md#PlaySound) for more details.) To import sounds simply open to the sound browser in Unrealed and go to **File->Import** and import the sounds into whatever package you want. Note that sounds must be in a path that does not contain spaces or the import will not work.By default stereo sounds can not be used. Daniel Vogel [said the following](https://udn.epicgames.com/lists/showpost/php?list=unedit&id=10934&lessthan=&show=20) about this:

```

> How can I play a stereo sound?

You can't. If you really want to, have a programmer remove the code in
ALAudioSubsystem that will disregard stereo sounds and make sure they are
played with SF_No3D. The reason I removed support for stereo sounds is
because they don't attenuate and artists tend to import stereo for sound
effects which will then cause all sorts of issues.

-- Daniel, Epic Games Inc.
```

## Script Sound Functions

The following sound functions are in Actor.uc.

### PlaySound

```

native simulated final function PlaySound(
   sound                 Sound,
   optional ESoundSlot   Slot,
   optional float        Volume,
   optional bool         bNoOverride,
   optional float        Radius,
   optional float        Pitch,
   optional bool         Attenuate
)
```

*PlaySound* plays a sound attached to the location of the actor that calls *PlaySound*. The parameters to this function are described below.

| [Parameter](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=1;up=0#sorted_table "Sort by this column") | [Description](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=1;up=0#sorted_table "Sort by this column") | [Default](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=1;up=0#sorted_table "Sort by this column") |
| --- | --- | --- |
| sound Sound | This is the sound to play. This must be a mono sound to be heard in 3D. If the sound is stereo, it will not play in 3D. Because the sound is not played in 3D, it will not attenuate with distance nor will there be any stereo separation based on the direction of the sound. The stereo sound will play at full volume when you are inside the *SoundRadius* and will not play at all outside the radius. | no default |
| optional ESoundSlot Slot | This is the slot in which to play the sound. There are 8 slots. The first slot, SLOT\_None=0, represents no slot and any sounds played here will be played and mixed into whatever is playing already. In all the other slots (SLOT\_Misc, SLOT\_Pain, SLOT\_Interact, SLOT\_Ambient, SLOT\_Talk, SLOT\_Interface), only one sound can be played per actor. If a new sound is played in a slot that already has a sound playing and *bNoOverride* (described below) has not been set, the playing sound will be cut off and then new sound will be played. Note that slots work on a per actor basis; if there are many actors all playing sounds on the same slot, many sounds will be heard, just one sound per actor. | SLOT\_Misc |
| optional float Volume | Volume is a scale from 0.0, which is silent, to 1.0, which is full volume. 0.5 is half volume (-6dB), 0.25 is quarter (-12dB) and so on. Sounds are played at full volume in the sound browser in Unrealed. You cannot make sounds louder, only softer. The Volume that is passed into *PlaySound* is scaled by one or two values. *SoundVolume* is a property of ALAudioSubsystem which is set in *<your\_game>.ini*. All sound volumes are multiplied by this value which has a range between 0.0 and 1.0. The default value of *SoundVolume* is 1.0. When *PlaySound* is called from a *Pawn*, *Volume* is also multiplied by *SoundDampening* which is an attribute of *Pawn*. *SoundDampening* initially defaults to 1.0. The last thing that happens to *Volume* is that it is clamped between 0.0 and 1.0. | [TransientSoundVolume](SoundReference.md#TransientSoundVolume) |
| optional bool bNoOverride | This option is only useful for sounds that are played on a slot other than SLOT\_None (see *Slot* above). If *bNoOverride* is set to true and another sound tries to play on this slot in this actor, it will not play. This will happen even if both calls to *PlaySound* have *bNoOverride* set to true. This prevents the sounds called with *bNoOverride* from being interrupted. By default this option is false and if another sound is played on the same slot by the same actor, the new sound will interrupt the old one. Note that slots work on a per actor basis; if there are many actors all playing sounds on the same slot, many sounds will be heard, just one sound per actor. | false |
| optional float Radius | *Radius*, in Unreal units, is the radius at which the sound begins to drop in volume. Between 0 and *Radius*, the sound is played at a constant volume of *Volume*. From then on outwards, the sound drops in volume by a scaled version of the way it works in the real world. At *Radius* times 100, the sound is completely cut off. In the real world, doubling the radius halves the volume. In Unreal the rate of falloff is affected by RollOff which is a global in the sound library. To be exact, equation is **volume\_drop\_in\_db = 20 \* log10(1 + RollOff \* (current\_radius - *Radius*) / *Radius*)**. The transition at the edge of the outer radius (100 \* *Radius*) is a little tricky. If you are inside the outer radius when *PlaySound* is called and move out of it, you will continue to hear the sound and it will continue to drop in volume. If you are outside the outer radius when the sound plays and move in, you will not hear the sound at all. | [TransientSoundRadius](SoundReference.md#TransientSoundRadius) |
| optional float Pitch | *Pitch* is clamped between 0.5 and 2.0. At 0.5 the sound is played at half the speed of the original sound, will take twice as long to play, and will sound one octave lower. At 2.0 the sound will be played at twice the speed, will take half as long to play, and will sound like it is one octave higher. This is ignoring Doppler shift which will additionally raise and lower the pitch of the sound. | 1.0 |
| optional bool Attenuate | This parameter should only be used by actors that are "owned" by the local player. "Owners" are determined by the *SpawnOwner* parameter of the *Spawn* function or the *SetOwner* function. Weapons in CodeDrop 2226 are "owned" by the local player for example. If *Attenuate* is true, which is its default, the sound will play in 3D originating at the location of the actor calling *PlaySound*. If *Attenuate* is false the sound will not play in 3D. Because the sound is not played in 3D, it will not attenuate with distance nor will there be any stereo separation based on the direction of the sound. | true |

#### Single vs. Multiplayer Use of PlaySound

In a single player game, *PlaySound* will send a hear sound event (either *AIHearSound* or *ClientHearSound*) to all controllers in the level that have *bIsPlayer* set to true. The local player, remote online players, and Bots all have *bIsPlayer* set to true in UT2003 for example. *ClientHearSound*, which is called for the local player, will cause the actual sound to play on the sound card. *AIHearSound* is a script event that AI controllers can listen for and can override in script to handle the hearing of sounds.In a multiplayer game if you are a client (NetMode == Client) the sound will only be played on that client via *ClientHearSound*. If a sound is played on a client, it is not propagated to the server and does not effect any other players either AI or human.If *PlaySound* is played on the server from a "simulated" function, nothing will happen.If *PlaySound* is played on the server (not from a "simulated" function), hear sound events will be sent to all the controlers but these events will be on the server and will not cause any client to hear sound though the sound card. This is not a problem for AIs because the logic for AIs exists on the server and does not need to get to any clients. In most cases a simulated event is used to cause a sound to be heard though the sound card on all clients because it allows *PlaySound* to be called independently on all the clients and also on the server.In the case of a ListenServer the sound will be played through the sound card of the computer running the ListenServer and all the events will also be called just like a normal server.

### PlayOwnedSound

```

native simulated final function PlayOwnedSound(
   sound                 Sound,
   optional ESoundSlot   Slot,
   optional float        Volume,
   optional bool         bNoOverride,
   optional float        Radius,
   optional float        Pitch,
   optional bool         Attenuate
)
```

The parameters of *PlayOwnedSound* are the same as [PlaySound](SoundReference.md#PlaySound) which you should refer to for a complete explanation. The only difference is that *Attenuate* defaults to false.

#### Summary of \_PlayOwnedSound

If you are a pawn or anything a pawn "owns" and you don't want your controller to receive events about the sound you are about to play, call *PlayOwnedSound* instead of *PlaySound*. This is useful for example with AIs that respond to the script event *AIHearSound* because you are saved the trouble of checking that it is you or anything you own that is making the sound. Clearly you do not want your AI to go "Who? What? Where? Why?" every time it fires its own gun.

#### Details

The details of *PlayOwnedSound* are slightly trickier than the summary. There is a special case for the *PlayedController* of the local player. *ClientHearSound* is called on this *PlayedController* because this is how the player actually hears the sound even if the maker of the sound is owned by that *PlayerController*.Additionally all sound playing gets harder to think about in a multiplayer situation. If NetMode==Client *PlayOwnedSound* works just like *PlaySound* when NetMode==Client. *PlayedOwnedSound* does not however, care if the function calling it is "simulated" while *PlaySound* does.*PlayOwnedSound* behaves notably different from *PlaySound* in a single player game or on the server of a multiplayer game. It is in these cases that *PlaySound* calls hear sound events on ALL controls while *PlayOwnedSound* avoids calling hear sound events on the controller that "owns" the sound.

### DemoPlaySound

```

native simulated final function DemoPlaySound(
   sound                 Sound,
   optional ESoundSlot   Slot,
   optional float        Volume,
   optional bool         bNoOverride,
   optional float        Radius,
   optional float        Pitch,
   optional bool         Attenuate
)
```

*DemoPlaySound* is called from C++ by *PlaySound* and *PlayOwnedSound* when you doing Demo Recording. This function is called on the server and replicated to the client to play a sound. Presumably you would not want to call this function directly from either script or C++

### GetSoundDuration

`native final function float GetSoundDuration( sound Sound )`*GetSoundDuration* returns the length of the sound in seconds. This is the real world duration of the sound, thus is has not be "corrected" with the game speed. When sound duration is of importance for certain events, for example when a player has to wait for the sound to be finished, be sure to correct the duration with the gamespeed (`Level.TimeDilation`). By default in the UnrealEngine2.5 10% faster than expected, with game speed set to 1 a real world second takes 1.1 seconds in game (see *SetGameSpeed()* in GameInfo, e.g. the requested speed is always multiplied with 1.1).

### PlayMusic

`native final function int PlayMusic( string Song, float FadeInTime )`Music in Unreal games in no longer handled with "tracked" songs. Instead, Ogg Vorbis ( <http://www.vorbis.com/> ), a "completely open, patent-free, professional audio encoding and streaming technology", is used to encode sound files. OGG files are sort of like MP3s in that both are encoding standards that compress normal wav files.This function starts playing an OGG file as music for the game. *Song* is the name of the OGG file without the .OGG extention. OGG files are stored in the "Music" directory. So for example, if you had a song "MySong.ogg" in your Music directory, you would play it my calling: `PlayMusic("MySong", 2.0);`. *FadeInTime* is the time it takes for the song to fade in to full volume which in the previous example is 2 seconds. This function returns the handle to the song which can be later used to stop the sound with [StopMusic](SoundReference.md#StopMusic). If 0 is returned, *PlayMusic* failed.Unlike sounds, which are loaded then played, music is streamed. There are many advantages to streaming but one disadvantage is that only 8 streams can be played at the same time.

### StopMusic

`native final function StopMusic( int SongHandle, float FadeOutTime )`*StopMusic* will stop the song with the given *SongHandle*. *SongHandle* is from the [PlayMusic](SoundReference.md#PlayMusic) function. *FadeOutTime* is the time from when this function is called to when the song will be silent, unregistered, and stop using a music stream.

### StopAllMusic

`native final function StopAllMusic( float FadeOutTime )`This will stop all songs played with [PlayMusic](SoundReference.md#PlayMusic). *FadeOutTime* is the time from when this function is called to when all the songs will be silent, unregistered, and all the music streams will be free.

### Music streams

In UnrealEngine25 and additional music playback system was added to support custom music to be played back. This allows players to play their own music from their system. For this the following support functions have been added. The music played back via this interface is not stopped during level transitions.

#### PlayStream

```

native final function int PlayStream( string Song, optional bool  UseMusicVolume, optional float Volume,
    optional float FadeInTime, optional float SeekTime );
```

| [Parameter](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Description](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Default](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=2;up=0#sorted_table "Sort by this column") |
| --- | --- | --- |
| song | The full path to the file to play back, this includes extention. For example `"D:\\alongtheway.mp3"` . |  |
| UseMusicVolume | If true the `MusicVolume` is used for playback, otherwise `InVolume` argument is used. | true |
| InVolume | The playback volume, only used if `UseMusicVolume` is false. | 1 |
| FadeInTime | Fade in duration. | 0 |
| SeekTime | Offset to start playing from, in seconds | 0 |

The return value is a handle that can be used in the other "stream" functions.

#### StopStream

`native final function StopStream(   int Handle,  optional float FadeOutTime );`Stops the stream with the given handle. `FadeOutTime` is time to fade out the music, if set to 0 the music stops instantly.

#### SeekStream

`native final function int  SeekStream( int Handle, float Seconds );`Sets the current playback position of the song identified by `handle` to `Seconds`.

#### AdjustVolume

`native final function bool AdjustVolume( int Handle, float NewVolume )`Change the playback volume of the given stream.

#### PauseStream

`native final function bool PauseStream(  int Handle )`Toggles playback of the given stream.

## Variables

The following sound variables are defined in Actor.uc. These variables are defined in script but are also accessible through C++.

### TransientSoundVolume

`var(Sound) float TransientSoundVolume`This is the default sound volume for sounds played with [PlaySound](SoundReference.md#PlaySound) or [PlayOwnedSound](SoundReference.md#PlayOwnedSound). This volume can be overridden in both these functions.

### TransientSoundRadius

`var(Sound) float TransientSoundRadius`This is the default sound radius for sounds played with [PlaySound](SoundReference.md#PlaySound) or [PlayOwnedSound](SoundReference.md#PlayOwnedSound). This radius can be overridden in both these functions.

### SoundOcclusion

`var(Sound) ESoundOcclusion SoundOcclusion`This is how sounds played with [PlaySound](SoundReference.md#PlaySound) or [PlayOwnedSound](SoundReference.md#PlayOwnedSound) as well as Ambient Sounds for this actor will be occluded. This setting applies to all sound playing for this actor. You cannot, for example, have an ambient sound occluded in one manner and have sounds played with [PlaySound](SoundReference.md#PlaySound) occluded in another. There are four settings for this variable explained in the chart below:

| [Occlusion Type](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Description](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=3;up=0#sorted_table "Sort by this column") |
| --- | --- |
| OCCLUSION\_Default | This is the default. It behaves like *OCCLUSION\_BSP* described below. |
| OCCLUSION\_None | Sounds will not be occluded at all. |
| OCCLUSION\_BSP | Sounds will be occluded by BSP but not by blocking volumes. (does a *FastLineCheck* from the location of the sound to the listener.) |
| OCCLUSION\_StaticMeshes | Sounds will be occluded by static meshes and BSP but not by blocking volumes. (does a *SingleLineCheck* from the location of the sound to the listener.) |

Occlusion works by dropping the radius by 65% when the actor making the sound is occluded based on the settings described in the table above. Because the radius of the sounds is reduced the sound will be quieter. Occlusion does not always take place instantly. The radius change is interpolated over time to make the transition smooth.

### AmbientSound

`var(Sound) sound AmbientSound`This is the ambient looping sound effect of this actor. AmbientSound can be set on any *Actor*; it does not need to be a *class AmbientSound*. The sound must be mono to be heard in 3D. If the sound is stereo it will not play in 3D. Because the sound is not played in 3D, it will not attenuate with distance nor will there be any stereo separation based on the direction of the sound. The stereo sound will play at full volume when you are inside the [SoundRadius](SoundReference.md#SoundRadius) and will not play at all outside the radius.

### SoundRadius

`var(Sound) float SoundRadius`This is the radius of the ambient sound. Like [PlaySound](SoundReference.md#PlaySound), the radius is 1/100 of the radius of the sound in Unreal Units. The transition at the edge of the radius is handled differently from *PlaySound* however. The transition at the edge of the radius is not perfectly smooth. Once you step inside the sound radius you will suddenly be able to hear it though it will be faint. If you step outside the radius the sound will suddenly be cutoff. The cutoff will be faint but there is still a sharp discernible transition if you look for it.

### SoundVolume

`var(Sound) byte SoundVolume`*SoundVolume* is a scale from 0, which is silent, to 255, which is the volume the sound plays at the sound browser in Unrealed. You cannot make sounds louder, only softer. It is possibly to enter a value greater than 255, but it will only loop the volume values so that a setting of 256=0, 257=1, and so on... If [bFullVolume](SoundReference.md#bFullVolume) is set to false (which is its default), *SoundVolume* is scaled by *AmbientVolume* which is a 0.0 to 1.0 multiplier for all ambient sounds. *AmbientVolume* is defined in *<your\_game>.ini*.

### SoundPitch

`var(Sound) byte SoundPitch`SoundPitch is a scale clamped between 32 to 128. 64 is the default value which means the sound will play at the normal pitch/speed. At 32 the sound is played at half the speed of the original sound, will take twice as long to play, and will sound one octave lower. At 128 the sound will be played at twice the speed, will take half as long to play, and will sound like it is one octave higher. This is ignoring Doppler shift which will additionally raise and lower the pitch of the sound.

### bFullVolume

`var(Sound) bool bFullVolume`If this is set to true, the ambient sound of this actor will ignore the *AmbientVolume* settings in *<your\_game>.ini*. See [SoundVolume](SoundReference.md#SoundVolume) above for more details about volume.
