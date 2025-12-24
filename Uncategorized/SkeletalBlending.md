# Skeletal Animation Blending

*Document Summary: Introduction into skeletal blending features of the engine.**Document Changelog: Last updated by Michiel Hendriks, overall cleanup. Last updated by Rob Faison (ZombieEvalTeam?). Original author was Erik de Neve ([EpicGames](https://udn.epicgames.com/Main/EpicGames)).*

* [Skeletal Animation Blending](SkeletalBlending.md#Skeletal Animation Blending)
  + [Introduction](SkeletalBlending.md#Introduction)
  + [Native implementation](SkeletalBlending.md#Native implementation)
  + [Script Functions](SkeletalBlending.md#Script Functions)
  + [Script Events](SkeletalBlending.md#Script Events)
  + [Console Commands](SkeletalBlending.md#Console Commands)
  + [Futher Reading](SkeletalBlending.md#Futher Reading)

## Introduction

Skeletal meshes can blend various animations into one, this way a walking left and walking forward can be blended into a walking forward and left animation. A skeletal mesh as several animation channels (`MAXSKELANIMCHANNELS` is set to 256 in `UnSekeletalMesh.h`) that can contain an animation, these channels (sometimes called "stage") will be blended into the final animation. The base channel is `0`, the lower the number the higher the priority of the channel is.Each channel can have its own UMeshAnimation object linked to it at runtime.For networking purposes, the base channel still works as usual. Additional blended channels are not automatically replicated. Blending works fine for client-side animations, any special network requirements for blended animation are meant to be implemented at a higher level (e.g. through replicated function calls.)An example on how the channels can be used can be found on [this](https://udn.epicgames.com/Two/PawnAnimation#The_Use_of_Channels) page.

## Native implementation

As said a skeletal mesh has up to `MAXSKELANIMCHANNELS` animation channels, stored as a dynamic array (called `Blends`) of the struct type `MeshAnimChannel` in `USkeletalMeshInstance` (both are defined in the file `Engine\Inc\UnSkeletalMesh.h`).Each `MeshAnimChannel` has a lot of variables, only a few of them can be set from Unreal Script via *AnimBlendParams(...)*. These variables have been documented quite well in the source code.The actual blending happens in \_USkeletalMeshInstance::UpdateAnimation(...) \_ in the file `Engine\Src\UnSkeleralMesh.cpp`, just like pretty much the rest of the blending related code.I'm not going into detail on how this works. If you want to know the detail I suggest to take a look at those files.

## Script Functions

Pretty much all animation related UnrealScript functions have an argument `channel`, this is the animation channel the function will have an effect on. The most interesting functions are AnimBlendParams and AnimBlendToAlpha.The following blending related functions are defined in Actor:

* [PlayAnim](ActorFunctions.md#PlayAnim)
* [LoopAnim](ActorFunctions.md#LoopAnim)
* [AnimStopLooping](ActorFunctions.md#AnimStopLooping)
* [TweenAnim](ActorFunctions.md#TweenAnim)
* [IsAnimating](ActorFunctions.md#IsAnimating)
* [FinishAnim](ActorFunctions.md#FinishAnim)
* [StopAnimating](ActorFunctions.md#StopAnimating)
* [FreezeAnimAt](ActorFunctions.md#FreezeAnimAt)
* [SetAnimFrame](ActorFunctions.md#SetAnimFrame)
* [IsTweening](ActorFunctions.md#IsTweening)
* [AnimBlendParams](ActorFunctions.md#AnimBlendParams) -- This is an important function, it allows you to set up various settings of the animation channel. It should be called before animation anything on that channel. The channel argument is called "stage" in this function.
* [AnimBlendToAlpha](ActorFunctions.md#AnimBlendToAlpha)
* [GetAnimParams](ActorFunctions.md#GetAnimParams)
* [AnimIsInGroup](ActorFunctions.md#AnimIsInGroup)
* [EnableChannelNotify](ActorFunctions.md#EnableChannelNotify)
* [GetNotifyChannel](ActorFunctions.md#GetNotifyChannel)

## Script Events

Actually, there is only one skeletal blending related event and it doesn't have much to do with blending.

* [AnimEnd](ActorFunctions.md#AnimEnd)

## Console Commands

rend blend
:   This toggles the rendering of normals on meshes, for skeletal meshes, they are colored with the number of influences (green =1, red=2, pink=3, light blue=4, white for 5+ )

rend bone
:   Toggles the rendering of bones (prevents rendering the regular mesh), where each bone's origin shows the local coordinate system with a small axis system, X,Y,Z = red,green,blue. Also, a purple 'root' line is drawn from the mesh's local space origin to the the 0th/root bone.

## Futher Reading

* [PawnAnimation](https://udn.epicgames.com/Two/PawnAnimation) -- discusses most of the animation aspects
* [MyFirstPawn](MyFirstPawn.md) -- an example where blending is used
* [EditorAnimBlending](https://udn.epicgames.com/Two/EditorAnimBlending) -- an unofficial addon to add animation bleding to UnrealEd

Ofcourse you can always check the mailing lists ([1](https://udn.epicgames.com/Two/UnProg), [2](https://udn.epicgames.com/Two/UnEdit)) for extra information of this subject.
