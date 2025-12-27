# Static Mesh Collision Reference

Document Summary: This document goes over static mesh collision.Document Changelog: Created by Chris Linder (DemiurgeStudios?) on 10-28-03 for 2226 based builds.

* [Static Mesh Collision Reference](StaticMeshCollisionReference.md#static-mesh-collision-reference)
  + [Related Documents](StaticMeshCollisionReference.md#related-documents)
  + [Introduction](StaticMeshCollisionReference.md#introduction)
  + [Step 1: Actor Collision Properties](StaticMeshCollisionReference.md#step-1-actor-collision-properties)
    - [Collision Variables](StaticMeshCollisionReference.md#collision-variables)
      * [An Important Note on "Collision" vs. "Blocking"](StaticMeshCollisionReference.md#an-important-note-on-collision-vs-blocking)
      * [Variable Description for bWorldGeometry TRUE](StaticMeshCollisionReference.md#variable-description-for-bworldgeometry-true)
      * [Variable Description for bWorldGeometry FALSE](StaticMeshCollisionReference.md#variable-description-for-bworldgeometry-false)
  + [Step 2: Static Mesh Collision Properties](StaticMeshCollisionReference.md#step-2-static-mesh-collision-properties)
    - [No Collision Models](StaticMeshCollisionReference.md#no-collision-models)
    - [Type 1](StaticMeshCollisionReference.md#type-1)
    - [Type 2](StaticMeshCollisionReference.md#type-2)
  + [Step 3: Material Collision](StaticMeshCollisionReference.md#step-3-material-collision)
    - [Memory Concerns](StaticMeshCollisionReference.md#memory-concerns)
  + [Moving Static Meshes](StaticMeshCollisionReference.md#moving-static-meshes)
    - [Mover Collision](StaticMeshCollisionReference.md#mover-collision)
    - [Karma Collision](StaticMeshCollisionReference.md#karma-collision)
    - [Pawn Collision](StaticMeshCollisionReference.md#pawn-collision)

## Related Documents

[CollisionTutorial](../Content%20Creation/Physics/CollisionTutorial.md),
[KarmaReference](../Content%20Creation/Physics/KarmaReference.md),
[StaticMeshesTutorial](../Content%20Creation/Primitives/StaticMeshesTutorial.md),
[ActorVariables](ActorVariables.md)

## Introduction

Collision is a very tricky thing in the Unreal Engine. It is fraught with many complexities and nuances and is the subject of lengthy documents already. This document narrows the scope of collision to focus primarily on static meshes with *Physics* set to *PHYS\_None* or [Movers](../Content%20Creation/Primitives/MoversTutorial.md). By "static mesh" I mean any object with *DrawType* set to *DT\_StaticMesh*. This include static meshes you place in the world by right clicking and selecting `Add Static Mesh: '....'` as well as *Actors* from the Actor Browser that are drawn with static meshes. The physics of the static meshes is also important because static meshes collide best when they just sit there and other things bump into them or when they are *Movers*. Static meshes that move (but are not *Movers*) can also collide and this document can be helpful in these cases as well. For more details see the [Moving Static Meshes](StaticMeshCollisionReference.md#moving-static-meshes) section.Even within the narrow scope described above there are many complexities. This document attempts to provide a thorough reference for how and what static meshes will collide with given their settings. The first important thing to realize about collision is that there are many-many collision variables to set and they all interrelate. There is no single field you can check to make something collide. Some checks for collision occur before other checks and therefore have priority. Due to the priority of certain collision checks, this document is organized as a step-by-step process to guide you through making your static mesh collide. At any step, you can make an object not collide. To ensure that an object does collide you must continue thought all the other steps.

## Step 1: Actor Collision Properties

If you have the actor collision properties (the "Collision" category in properties) set to not collide, no amount of changing the static mesh collision (the properties in the static mesh browser) will ever make it collide. The actor collision properties say if the actor should try to collide, and then the static mesh collision properties say if and how it should collide.For example if you want a mesh to block a *KActor* but you have *bBlockKarma* set to FALSE, it will never collide. If you have *bBlockKarma* set to TRUE (and leave all the other collision properties at their default for a static mesh), it might collide. If you set *UseSimpleKarmaCollision*, *UseSimpleBoxCollision*, and *UseSimpleLineCollision* to FALSE and you set *EnableCollision* to TRUE for all the materials, it will definitely collide.

### Collision Variables

![collision.gif](../assets/![collision.gif](../assets/collision.gif))

This section explains the actor collision variables for static meshes. What makes this tricky is that based on if *bWorldGeometry* is TRUE or FALSE, the collision variables behave differently. When you place a static mesh in the level in UnrealEd by right clicking and selecting `Add Static Mesh: '....'` this type of static has *bWorldGeometry* TRUE. Other types of Actors that have a *DrawType* of *DT\_StaticMesh* might have *bWorldGeometry* FALSE. The value of *bWorldGeometry* cannot be changed or even viewed in UnrealEd; it can only be seen and changed in UnrealScript. In general if something is world geometry in that it doesn't ever move or change, it is probably *bWorldGeometry* TRUE. If an Actor which is drawn with a static mesh ever moves or changes, it is probably *bWorldGeometry* FALSE.It is also worth noting that some actors change some of their collision variables in code overwriting that values specified in UnrealEd so watch out for that. This is the case with *Triggers*, *Teleporters*, and *WarfareStationaryWeapons* for example.

#### An Important Note on "Collision" vs. "Blocking"

"Collision" (in the case of *bCollideActors* for example) is when the engine calculates weather two objects are touching. "Blocking" (in the case of *bBlockKarma* for example) is when one thing will stop another. Triggers, for example, collide but do not block. This is how the engine knows you are touching a trigger but you can still walk through the trigger.

#### Variable Description for *bWorldGeometry* TRUE

Below are descriptions of the actor collision variables as they apply to those actors that have *bWorldGeometry* set to TRUE. This is the case with the *StaticMeshActor* class which is what is generated when you right click and select `Add Static Mesh: '....'`. The defaults provided at those of *StaticMeshActor*.

| Setting | Description | default |
| --- | --- | --- |
| bCollideActors | This is the most important collision variable. If *bCollideActors* is FALSE, this static mesh will not collide with anything. This is because it will not be in the collision hash. If this is TRUE, the static mesh might collide or block based on the other settings below. | True |
| bBlockZeroExtentTraces | *bBlockZeroExtentTraces* determines if this static mesh will try to block zero extent traces. Most weapon fire uses zero extent traces for example. Whether or not the mesh will actually block is determined by cylinder collision if *bUseCylinderCollision* is TRUE, or if it is FALSE, the [static mesh collision properties](StaticMeshCollisionReference.md#step-2-static-mesh-collision-properties) explained below. | True |
| bBlockNonZeroExtentTraces | *bBlockNonZeroExtentTraces* determines if this static mesh will try to block non-zero extent traces. Player movement uses non-zero extent traces for example. Whether or not the mesh will actually block is determined by cylinder collision if *bUseCylinderCollision* is TRUE, or if it is FALSE, the [static mesh collision properties](StaticMeshCollisionReference.md#step-2-static-mesh-collision-properties) explained below. | True |
| bBlockKarma | Setting this to TRUE will make this static mesh try to block karma. Whether or not the mesh will actually block is determined by the [static mesh collision properties](StaticMeshCollisionReference.md#step-2-static-mesh-collision-properties) explained below. Note: this is not affected by *bUseCylinderCollision*. | True |
| bUseCylinderCollision | If this is TRUE, the engine will use cylinder collision (defined by *CollisionRadius* and *CollisionHeight*) for all collision EXCEPT karma collision. The settings in the static mesh collision properties will be ignored except for karma collision. | False |
| bPathColliding | If *bBlockActors* and *bCollideActors* are TRUE, and *bStatic* is FALSE, if you set *bPathColliding* to FALSE, this actor will not collide during path building. This means that AI's will think that they can move through this actor even if they can not. Settings *bPathColliding* to TRUE will not prevent AI's from finding paths through this actor if it is possible for those AI's to move through this actor. This settings is useful for movers or any actor that will move out of the way when an AI attempts to move through it. In most cases *bPathColliding* is not relevant for static meshes because *bStatic* is TRUE for *StaticMeshActors*. | False |
| bCollideWorld | Does not affect how *bWorldGeometry* = TRUE static meshes collide. | False |
| bBlockActors | Does not affect how *bWorldGeometry* = TRUE static meshes collide. | False |
| bBlockPlayers | Does not affect how *bWorldGeometry* = TRUE static meshes collide. | False |
| bProjTarget | Does not affect how *bWorldGeometry* = TRUE static meshes collide. | False |

#### Variable Description for *bWorldGeometry* FALSE

Below are additional descriptions of the actor collision variables as they apply to those actors that have *bWorldGeometry* set to FALSE. Static meshes of this type behave just like the static meshes described above except that they have an additional chance to not block things. First use the chart above to see if the static mesh in question would block things. If it will not, change those settings. If according to the descriptions above your static mesh will block, now you can apply the additional checks below to see if it will really block.

| Setting | Description |
| --- | --- |
| bCollideWorld | This is not relevant for either static meshes with *PHYS\_None* or for Movers. If your static meshes is moving, however, you most likely was to set this to TRUE. |
| bBlockActors | Tries to blocks other nonplayer actors. Must have *bBlockNonZeroExtentTraces* set to TRUE to work. Whether or not the mesh will actually block is determined by cylinder collision if *bUseCylinderCollision* is TRUE, or if it is FALSE, the [static mesh collision properties](StaticMeshCollisionReference.md#step-2-static-mesh-collision-properties) explained below. |
| bBlockPlayers | Blocks other player actors. Must have *bBlockNonZeroExtentTraces* set to TRUE to work. Whether or not the mesh will actually block is determined by cylinder collision if *bUseCylinderCollision* is TRUE, or if it is FALSE, the [static mesh collision properties](StaticMeshCollisionReference.md#step-2-static-mesh-collision-properties) explained below. |
| bProjTarget | Blocks projectiles such as rockets and even instant hit bullets. Must have *bBlockZeroExtentTraces* set to TRUE to work. Whether or not the mesh will actually block is determined by cylinder collision if *bUseCylinderCollision* is TRUE, or if it is FALSE, the [static mesh collision properties](StaticMeshCollisionReference.md#step-2-static-mesh-collision-properties) explained below. |

## Step 2: Static Mesh Collision Properties

The static mesh collision properties discussed in this section will not be used if the object is not set to collide based on the actor collision properties described in [Step 1](StaticMeshCollisionReference.md#step-1-actor-collision-properties).This section discussed some of the properties that are in the Static Mesh Browser window. It uses charts to illustrate the relation between [collision models](../Content%20Creation/Physics/CollisionTutorial.md#collision-models) and the "UseSimple" properties in the Static Mesh Browser, which can be seen in the image below.

![staticmeshcollisionprops.gif](../assets/![staticmeshcollisionprops.gif](../assets/staticmeshcollisionprops.gif))

There is a different chart for each of the collision model types; [None](StaticMeshCollisionReference.md#no-collision-models), [Type 1](StaticMeshCollisionReference.md#type-1), and [Type 2](StaticMeshCollisionReference.md#type-2). In each chart, all possible settings of *UseSimpleKarmaCollision*, *UseSimpleBoxCollision*, and *UseSimpleLineCollision*, are represented in the **Karma**, **Box**, and **Line** columns respectively.The **Karma Objects** column indicates what the mesh will use to block Karma objects. The **Non-Zero Extent Traces (ie Pawn Movement)** column indicates what the mesh will use to block non-zero extent traces which are used by things such as pawn movement and cylinder collision. The **Zero Extent Traces (ie Weapon Fire)** column indicates what the mesh will use to block zero extent traces which are used by things like weapon fire.

### No Collision Models

This chart goes over how a static mesh will collide if it does not have a [collision model](../Content%20Creation/Physics/CollisionTutorial.md#collision-models).

| default | Karma | Box | Line | Karma Objects | Non-Zero Extent Traces (ie Pawn Movement) | Zero Extent Traces (ie Weapon Fire) |
| --- | --- | --- | --- | --- | --- | --- |
|  | **False** | **False** | **False** | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **False** | **False** | **True** | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **False** | **True** | **False** | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **False** | **True** | **True** | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **True** | **False** | **False** | will not collide | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **True** | **False** | **True** | will not collide | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
| **\*** | **True** | **True** | **False** | will not collide | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **True** | **True** | **True** | will not collide | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |

### Type 1

This chart goes over how a static mesh will collide if it has a **Type 1** [collision model](../Content%20Creation/Physics/CollisionTutorial.md#collision-models). A **Type 1** collision model is created using [Save Brush As Collision](../Content%20Creation/Physics/CollisionTutorial.md#save-brush-as-collision), or [K-DOP](../Content%20Creation/Physics/CollisionTutorial.md#k-dop). This type of collision also includes collision shapes [created in a modeling program](../Content%20Creation/Physics/CollisionTutorial.md#create_in_a_modeling_program_3d_) with the *MCDCX* tag.

| default | Karma | Box | Line | Karma Objects | Non-Zero Extent Traces (ie Pawn Movement) | Zero Extent Traces (ie Weapon Fire) |
| --- | --- | --- | --- | --- | --- | --- |
|  | **False** | **False** | **False** | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **False** | **False** | **True** | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | Collide w/ Collision Model |
|  | **False** | **True** | **False** | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | collide w/ Collision Model | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **False** | **True** | **True** | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | collide w/ Collision Model | collide w/ Collision Model |
|  | **True** | **False** | **False** | collide w/ Collision Model | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **True** | **False** | **True** | collide w/ Collision Model | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | collide w/ Collision Model |
| **\*** | **True** | **True** | **False** | collide w/ Collision Model | collide w/ Collision Model | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **True** | **True** | **True** | collide w/ Collision Model | collide w/ Collision Model | collide w/ Collision Model |

### Type 2

This chart goes over how a static mesh will collide if it has a **Type 2** [collision model](../Content%20Creation/Physics/CollisionTutorial.md#collision-models). **Type 2** collision models are created with [Fit Karma Primitive](../Content%20Creation/Physics/CollisionTutorial.md#fit-karma-primitive) or collision shapes [created in a modeling program](../Content%20Creation/Physics/CollisionTutorial.md#create_in_a_modeling_program_3d_) with the *MCDBX*, *MCDSP*, or *MCDCY* tags.

| default | Karma | Box | Line | Karma Objects | Non-Zero Extent Traces (ie Pawn Movement) | Zero Extent Traces (ie Weapon Fire) |
| --- | --- | --- | --- | --- | --- | --- |
|  | **False** | **False** | **False** | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **False** | **False** | **True** | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **False** | **True** | **False** | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **False** | **True** | **True** | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **True** | **False** | **False** | collide w/ Collision Model | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **True** | **False** | **True** | collide w/ Collision Model | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
| **\*** | **True** | **True** | **False** | collide w/ Collision Model | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |
|  | **True** | **True** | **True** | collide w/ Collision Model | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) | [Material Collision](StaticMeshCollisionReference.md#step-3-material-collision) |

## Step 3: Material Collision

Material collision is only used when no collision model is being used. See the above charts from [Step 2](StaticMeshCollisionReference.md#step-2-static-mesh-collision-properties) to determine if material collision is relevant to your static mesh.Collision can be set per material in the Static Mesh Browser. Sometimes it is very useful to only make some of the materials in the mesh collide. Setting the material collision is done by expanding the *Materials* array and setting *EnableCollision* for each material as shown in the image below.

![staticmeshcollisionpropsmat.gif](../assets/![staticmeshcollisionpropsmat.gif](../assets/staticmeshcollisionpropsmat.gif))

When *EnableCollision* is True for a material, all the triangles of the mesh that are textured with that material will be used for collision calculations. This means that the collision calculations will be based on exactly the triangles you see. This will sometimes be the same speed as but in most cases slower than using simplified [collision models](../Content%20Creation/Physics/CollisionTutorial.md#collision-models) because there will be more triangles to calculate collision for.

### Memory Concerns

Other than speed, there is a memory gain to be had by using collision models and not material collision. Even if the material collision is not being used, if *EnableCollision* is TRUE, collision data for the material is stored in the static mesh. With a large number of static meshes this can lead to a great deal of wasted memory. This [Xbox memory optimization document](https://udn.epicgames.com/Two/MemoryOptimization#staticmeshes) talks about the memory savings associated with static mesh material collision. While the document focuses on Xbox, the memory savings are true for all platforms. In general, if you are using collision models for all types of collision (see [Step 2](StaticMeshCollisionReference.md#step-2-static-mesh-collision-properties) for more details), make sure you turn off material collision for all materials.

## Moving Static Meshes

As mentioned above, this document does not really cover arbitrary movement physics for static meshes. This section will give a brief summary how movement affects static meshes and what you might want to do to get it to work correctly. First off, if you want a static mesh to move around, it should probably be either a Mover, a Karma object, or pawn which uses cylinder collision.Interestingly enough, even if your static mesh is none of these things, it can still move and collide. The problem is that the contact between the static mesh and other moving objects is calculated when the other object moves. So if the static mesh moves into the other object, be it a player or a karma object, the static mesh will often pass right through the other object. But if players or karma objects move into the static mesh, they will be blocked. The other problem is that even if *bUseCylinderCollision* is FALSE for the static mesh, as it moves, the engine will use cylinder collision for the movement. For example, if you have a static mesh in *PHYS\_Falling*, it will stop falling when the collision cylinder is obstructed but it will ignore all other parts of the mesh. Other moving objects will still collide with the mesh but with the problems of moving through described above.

### Mover Collision

Because [Movers](../Content%20Creation/Primitives/MoversTutorial.md) are designed to move, they do not have the problem of only calculating collision as other *Actors* move. Collision is always calculated and therefore movers work with all the charts in this document.

### Karma Collision

If you want your static mesh to collide and react in to the work in a realistic manner you should make it a Karma actor. The collision described in this document is not very relevant because Karma has its own collision calculations. See the documents below for more information on Karma.[IntroToKarma](../Content%20Creation/Physics/IntroToKarma.md),
[KarmaReference](../Content%20Creation/Physics/KarmaReference.md),
[ImportingKarmaActors](ImportingKarmaActors.md),
[UsingKarmaActors](UsingKarmaActors.md),
[ExampleMapsKarmaColosseum](ExampleMapsKarmaColosseum.md),
[KarmaAuthoringTool](KarmaAuthoringTool.md)

### Pawn Collision

If you are using a static mesh for a pawn it works best to use cylinder collision by setting *bUseCylinderCollision* to TRUE as described [above](StaticMeshCollisionReference.md#collision-variables). The static mesh will just be used for appearance and will not be involved with collision except for Karma. If the static mesh has been configured to collide with Karma based on all the settings described above, then the pawn will push Karma objects around as it moves.
