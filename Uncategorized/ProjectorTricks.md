# Projector Tricks

Revision history:

1. Written by Nathaniel Brown 12/21/01.
2. Updated to fix some code issues.
3. Updated to add another example class.
4. Updated by Michiel Hendriks, little note about the existing DynamicProjector?.

* [Projector Tricks](ProjectorTricks.md#Projector Tricks)
  + [Introduction](ProjectorTricks.md#Introduction)
  + [Projectors at a glance](ProjectorTricks.md#Projectors at a glance)
  + [Dynamic Projector](ProjectorTricks.md#Dynamic Projector)
  + [Expanding Projector](ProjectorTricks.md#Expanding Projector)
  + [Triggered Projector](ProjectorTricks.md#Triggered Projector)
  + [Summary](ProjectorTricks.md#Summary)

## Introduction

Here I'll be going over a few projector tricks that will hopefully be useful to you. These are basically `dynamic projectors' you can use. The two-example classes I provide here are DynamicProjector, and ExpandingProjector. I'll get into these in more detail below.

## Projectors at a glance

For those of you who are unfamiliar with projectors, they basically allow you to project a texture onto any BSP, Staticmesh, Vertmesh, Skeletalmesh, or terrain surface (and soon hopefully particles also). They are useful for faking lighting effects, and decals, amongst other things.The projector functions I use here are pretty self explanatory, but I'll give a brief description anyway.**AttachProjector():** This function allows you to attach a projector to a surface. It will trace forward a number of units equal to the MaxTraceDistance variable, in a direction based on its rotation.**DetachProjector():** This functional removes the projector from a surface, which is highly useful if you need to update a projector's properties incase they have been modified since last calling AttachProjector().**AbandonProjector():** While I don't use this function in this article, I think its worth noting. It allows you to turn off the projector after the amount of time passed into it elapses, basically leaving the texture attached to the surface while disconnect the Projector (actor) from it (for performance).**Note:** It is a lot more expensive to move a projector than it is to actualy render it, although it is less so than UT's decals.

## Dynamic Projector

DynamicProjector is useful for instances inwhich you want to have a projector move (for laser scopes, or if based on an object). This relatively simple class just does a check to see if its location or rotation has changed since last tick (OldLocation/OldRotation). If so, it detaches itself from the surface (DetachProjector()) and then reattaches (AttachProjector()), so it correctly updates to the new surface. This is especially beneficial if you want a projector to fully rotate (i.e phys\_rotating + bFixedRotationDir + valid RotationRate), because a normal projector can only rotate about its Roll.There already exists a DynamicProjector class in the current code base. The difference between the implementation below and the class in the codedrop is that this one checks for changes in the location and rotation. The DynamicProjector in the codedrop always performs an detach and attach.

```

//=====================================================================
// DynamicProjector.
//=====================================================================
class DynamicProjector extends Projector;

var vector  OldLocation;
var rotator OldRotation;

simulated function Tick(float DeltaTime)
{
  if ((Location != OldLocation) || (OldRotation != Rotation))
  {
    DetachProjector(True);
    AttachProjector();
  }
  OldLocation = Location;
  OldRotation = Rotation;
}
```

## Expanding Projector

This little class allows you to make a projector that expands outward. This is best used as a sort of decal, and is really good for things like an expanding pool of blood or water. Essentially, this class will increase the size of the projector until it reaches EndScale plus the original DrawScale based on GrowRate.**GrowRate:** This determines the speed at which the Projector scale increases.**EndScale:** This is an offset from the initial DrawScale, which is used to determine the Projectors end size.**Note:** It's highly recommended that the material used by this Projector has its UClampMode and VClampMode set to TC\_Clamp. Also for most decals-like effects you will probably want to have an FOV of 0.

```

//=============================================================================
// ExpandingProjector.
//=============================================================================
class ExpandingProjector extends Projector;

var() float  GrowRate,
             EndScale;

simulated function Tick(float DeltaTime)
{
  local vector HitNormal,
               HitLocation,
               Dir;
  local float  Distance;

  if (DrawScale < (EndScale + Default.DrawScale)
  {
    DetachProjector(True);

    Dir    = Location;
    Dir.Z -= 70 * 10;
    Trace(HitLocation,HitNormal,Dir,Location);

    SetLocation(HitLocation);
    SetRotation(rotator(-HitNormal));

    Distance = Drawscale + (GrowRate * DeltaTime);

    SetDrawScale(Distance);
    AttachProjector();
  }
}
```

## Triggered Projector

This class can potentially be extremely useful. It could be used for blinking lights, or lightning flashes through a window, or many other similar things.
The basis is that it simply attaches and detaches when triggered (a toggled effect).**bInitiallyOn:** This property allows a Level Designer to specify whether this should be on from the start. Otherwise it doesn't become visible until triggered.**bIsOn:** bIsOn serves the simple puprose of indicating whether the projector is currently triggered on or off.

```

//===================================================================
// TriggeredProjector.
//===================================================================
class TriggeredProjector extends Projector;

var() bool bInitialyOn;
var   bool bIsOn;

function PostBeginPlay()
{
  AttachProjector();
  if (bProjectActor)
      SetCollision(True,False,False);
  bIsOn = bInitialyOn;
  if (!bIsOn)
  {
    DetachProjector(True);
    DetachAllActors();
  }
}


function Trigger(actor Other,pawn Instigator)
{
  bIsOn = !bIsOn;
  if (bIsOn)
  {
    AttachProjector();
    ReattachAllActors();
  }
  else
  {
    DetachProjector(True);
    DetachAllActors();
  }
}

simulated function DetachAllActors()
{
  local actor A;

  foreach TouchingActors(Class'Actor',A)
  {
    DetachActor(A);
  }
}

simulated function ReattachAllActors()
{
  local actor A;

  foreach TouchingActors(Class'Actor',A)
  {
    AttachActor(A);
  }
}

event Touch(Actor Other)
{
  if (bIsOn)
      AttachActor(Other);
}

event Untouch(Actor Other)
{
  DetachActor(Other);
}
```

## Summary

Here I have outlined some sample classes that allow you to do a few interesting tricks with Projectors. Hopefully this helps your understanding of how to do more dynamic things with them, or gives you some ideas of your own.
