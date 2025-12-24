# Core UnrealScript Objects

*Last updated by Michiel Hendriks, update for v3223. Previously updated by Michael Breen (DemiurgeStudios?)*.   
*Original author was Michael Breen (DemiurgeStudios?) 02.13.2004.*

* [Core UnrealScript Objects](#core-unrealscript-objects)
  + [Related Documents](#related-documents)
  + [Base Object](#base-object)
  + [UObject variables](#uobject-variables)
  + [Object flags](#object-flags)
  + [Structures](#structures)
    - [GUID](#guid)
    - [Units of rotation in UnrealScript](#units-of-rotation-in-unrealscript)
    - [Vector](#vector)
    - [Plane](#plane)
    - [Rotator](#rotator)
    - [Coordinates](#coordinates)
    - [Quaternions](#quaternions)
    - [Range](#range)
    - [Range Vector](#range-vector)
    - [Scale and sheering](#scale-and-sheering)
    - [Camera orientations for Matinee](#camera-orientations-for-matinee)
    - [Generic axis enum.](#generic-axis-enum)
    - [RGB Color](#rgb-color)
    - [Bounding Box](#bounding-box)
    - [Bounding Volume](#bounding-volume)
    - [Matrix (4x4)](#matrix-4x4))
    - [Interpolated functions](#interpolated-functions)
      * [Interpolated function point](#interpolated-function-point)
      * [Interpolated function point](#interpolated-function-point)
    - [Compressed position](#compressed-position)
  + [Constants](#constants)
  + [Basic native operators and functions](#basic-native-operators-and-functions)
    - [Boolean operators](#boolean-operators)
      * [A](#a)
      * [A = B](#a-code-b)
      * [A = B](#a-b)
      * [A && B](#a-b)
      * [A ^^ B](#a-b)
      * [A || B](#a-b)
    - [Byte operators](#byte-operators)
      * [A \*= B](#a-b)
      * [A /= B](#a-b)
      * [A += B](#a-b)
      * [A -= B](#a-b)
      * [++A](#a)
      * [A--](#a-)
      * [A++](#a)
      * [A--](#a-)
    - [Bit Manipulation](#bit-manipulation)
    - [Integer operators](#integer-operators)
    - [Integer functions](#integer-functions)
    - [Float operators](#float-operators)
    - [Float functions](#float-functions)
    - [Vector operators](#vector-operators)
    - [Vector functions](#vector-functions)
    - [Rotator operators and functions](#rotator-operators-and-functions)
    - [String operators and functions](#string-operators-and-functions)
    - [Object operators](#object-operators)
    - [Name operators](#name-operators)
    - [Interpolated Curve functions](#interpolated-curve-functions)
    - [Quaternion functions](#quaternion-functions)
  + [General functions](#general-functions)
    - [Logging](#logging)
    - [Goto state and label](#goto-state-and-label)
    - [Objects](#objects)
    - [Probe messages](#probe-messages)
    - [Properties](#properties)
    - [Configuration](#configuration)
    - [Random number within a range](#random-number-within-a-range)
  + [Engine notification functions](#engine-notification-functions)
    - [Begin State](#begin-state)
    - [End State](#end-state)

## Related Documents

[UnrealScriptReference](UnrealScriptReference.md)[StringsInUnrealScript](../../Uncategorized/StringsInUnrealScript.md)These are the base classes, functions and structures on which all UnrealScript objects are built.

## Base Object

This is the Object class, corresponding to UObject in code.

```

//=============================================================================
// Object: The base class all objects.
// This is a built-in Unreal class and it shouldn't be modified.
//=============================================================================
class Object
   native
   noexport;
```

## UObject variables

These are internal variables for the object. You shouldn't have to touch these. Although, [ObjectFlags](#object-flags) are laid out below.

```

//=============================================================================
// UObject variables.

// Internal variables.
var native private const pointer ObjectInternal[6];
var native const object Outer;
var native const int ObjectFlags;
var(Object) native const editconst noexport name Name;
var native const editconst class Class;
```

## Object flags

This is for internal use. You probably won't have to use this.
These are the flags that can be set for each object to specify certain properties.They are used when creating an object. You can simply add the flags together. The following example returns a new MaterialClass object.Example:

```

return New(Outer, Name, RF_Public+RF_Standalone) MaterialClass;
```

It's interesting that the Object Flags below are, in fact, a subset of the actual flags in the Unreal Engine. RF\_Standalone is not define below, so it is defined for convenience in MaterialFactory.uc:

```

const RF_Standalone = 0x00080000;
```

Standalone means you should keep this object around for editing even if unreferenced.

```

//=============================================================================
// Unreal base structures.

// Object flags.
const RF_Transactional  = 0x00000001; // Supports editor undo/redo.
const RF_Public         = 0x00000004; // Can be referenced by external package files.
const RF_Transient      = 0x00004000; // Can't be saved or loaded.
const RF_Standalone     = 0x00080000; // Keep object around for editing even if unreferenced.
const RF_NotForClient   = 0x00100000; // Don't load for game client.
const RF_NotForServer   = 0x00200000; // Don't load for game server.
const RF_NotForEdit     = 0x00400000; // Don't load for editor.
```

## Structures

### GUID

A globally unique identifier, represented as four integers. Usually a GUID is represented as a hexidecimal string. This is an internal structure. You probably won't have to use this.

```

// A globally unique identifier.
struct Guid
{
   var int A, B, C, D;
};
```

### Units of rotation in UnrealScript

In UnrealScript, rotations are neither expressed in degrees nor radians. They are expressed in Unreal Units (URUs), which run from 0 to 65536 (2^16).

* 45� : 8192 URUs
* 90� : 16384 URUs
* 180� : 32768 URUs
* 270� : 49152 URUs
* 360� : 65536 URUs

To convert degrees to URUs multiply by 8192/45.   
To convert URUs to degrees multiply by 45/8192.

### Vector

When used as a direction vector, the vector begins at the origin and extends to the point represented by X, Y and Z. Vectors are used all over UnrealScript, since every actor must have a 3D position, and we are constantly checking if an actor is near something, etc.Warning: UnrealScript does not use degrees or radians for rotation. Instead of running from 0 to 360, units run from 0 to 65536. See [Units of rotation in UnrealScript](#units-of-rotation-in-unrealscript) for more informationSee also: [Vector operators](#vector-operators) and [Vector functions](#vector-functions)Example:

```

simulated final function bool TouchingActor(Actor A)
{
   local vector Dir;

   Dir = Location - A.Location;

   if ( abs(Dir.Z) > CollisionHeight + A.CollisionHeight )
      return false;

   Dir.Z = 0;
   return ( VSize(Dir) <= CollisionRadius + A.CollisionRadius );
}
```

Here you can see

* The actors location (*Location*) as well as *A.Location* are both vectors.
* You can perform a subtraction of vectors (representing 3D points in space) and yield a relative direction vector *Dir* which is a vector from actor A to the current actor.
* Individual components of the vector can be accessed in the standard way (e.g. Dir.Z = 0);

```

// A point or direction vector in 3d space.
struct Vector
{
   var() config float X, Y, Z;
};
```

### Plane

Plane contains X, Y, Z **and** W. (Note that Plane extends Vector).   
Imagine a vector beginning at the origin and extending to a point in space (X, Y, Z). Now travel from the origin, along this vector a distance W. The plane in this structure is defined as the one perpendicular to the vector at that point W. The vector defined by (0,0,0) -> (X, Y, Z) probably should be normalized.Also of note is that this structure can be used as a sphere. See [Bounding Volume](#bounding-volume) for an example of this. For a sphere imagine a point in space, (X, Y, Z) and the sphere is defined as every point a distance W away.

```

// A plane definition in 3d space.
struct Plane extends Vector
{
   var() config float W;
};
```

### Rotator

Euler angle rotators are used all over UnrealScript as both an absolute and relative rotation expressed with Roll, Pitch and Yaw. See [Rotator operators and functions](#rotator-operators-and-functions) for the many ways to use rotators. To avoid gimbel lock, you may want to convert your rotator to a [quaternion](#quaternions) before applying it to a vector. There's a really fun java apply [here](http://gamemath.com/Euler.htm) and shows rotations graphically as both Euler angle vectors and quaternions.Warning: UnrealScript does not use degrees or radians for rotation. Instead of running from 0 to 360, units run from 0 to 65536. See [Units of rotation in UnrealScript](#units-of-rotation-in-unrealscript) for more information

```

// An orthogonal rotation in 3d space.
struct Rotator
{
   var() config int Pitch, Yaw, Roll;
};
```

### Coordinates

I know we're all tired of using the same old boring coordinate system we normally use in Unreal with the origin at (0,0,0) and with the X-axis extending in front of you (into the screen), the Y-axis heading off to your right, and Z going straight up. Let's say we wanted a totally different coordinate system. We can specify it in terms of the old system with an origin of (Origin.X, Origin.Y, Origin.Z), which is a point in space defined in terms of the old coordinate system. Then we've got three (hopefully orthogonal, normalized) vectors, creating our axes from the *Origin*. This can be used to represent a transform from one coordinate system (not just the standard one) to another. By *standard*, I mean the origin of the map our level is using.

```

// An arbitrary coordinate system in 3d space.
struct Coords
{
   var() config vector Origin, XAxis, YAxis, ZAxis;
};
```

### Quaternions

Quaternions are a way to represent and apply rotations which avoid gimbel lock. For an introduction to quaternions see [Using Quaternions to Represent Rotation](http://www.cs.berkeley.edu/~laura/cs184/quat/quaternion.html). There are many functions available to translate a vector of Euler angles (rotator) to quaternions and back, as well as apply quaternion rotations to a object in [Quaternion functions](#quaternion-functions). There's a really fun java applet [here](http://gamemath.com/Euler.htm) that shows rotations graphically as both Euler angle vectors, matrices and quaternions.Some advantages of quaternions over axis-angle rotations:

* Avoids gimbel lock
* composing quaternion rotations is trivial and computationally cheaper
* dividing rotations (interpolation) is computationally cheaper

```

// Quaternion
struct Quat
{
   var() config float X, Y, Z, W;
};
```

### Range

There are many variables (e.g. CollisionSoundProbability) which require specification in terms of range. Sometimes the game AI (guided by circumstances) may use a value within that range for an action or effect. In some circumstances it may pick a value at random within that range, in other circumstances it may just enforce that a value is within this range. Whether or not (Max >= Min) is true is unknown.

```

// Used to generate random values between Min and Max
struct Range
{
   var() config float Min;
   var() config float Max;
};
```

### Range Vector

Range vectors, in general can specify any 3D rectangle, having an Min and Max for X, Y and Z. They're usually used to define an area in the map where something is or is not happening, such as an area where it is raining or where you can hear music. They are also used in the [particle systems](../../Content Creation/Effects/ParticleSystems.md) as a randomly chosen value in this range for the number/velocity of particles moving in each direction. [Bounding Boxes](#bounding-box) are similar.Examples:

```

ParticleEmitter.uc(168):var (Collision)      rangevector               DampingFactorRange;
ParticleEmitter.uc(175):var (Collision)      rangevector               SpawnedVelocityScaleRange;
ParticleEmitter.uc(181):var (Color)      rangevector               ColorMultiplierRange;
ParticleEmitter.uc(207):var (Location)      rangevector               StartLocationRange;
ParticleEmitter.uc(211):var (Location)      rangevector               StartLocationPolarRange;
ParticleEmitter.uc(218):var (MeshSpawning)   rangevector               VelocityScaleRange;
ParticleEmitter.uc(219):var (MeshSpawning)   rangevector               MeshScaleRange;
ParticleEmitter.uc(234):var (Revolution)      rangevector               RevolutionCenterOffsetRange;
ParticleEmitter.uc(235):var (Revolution)      rangevector               RevolutionsPerSecondRange;
ParticleEmitter.uc(244):var (Rotation)      rangevector               SpinsPerSecondRange;
ParticleEmitter.uc(245):var (Rotation)      rangevector               StartSpinRange;
ParticleEmitter.uc(247):var (Rotation)      rangevector               RotationDampingFactorRange;
ParticleEmitter.uc(254):var (Size)         rangevector               StartSizeRange;
ParticleEmitter.uc(297):var (Velocity)      rangevector               StartVelocityRange;
ParticleEmitter.uc(300):var (Velocity)      rangevector               VelocityLossRange;
ParticleEmitter.uc(302):var (Velocity)      rangevector               AddVelocityMultiplierRange;
```

```

// Vector of Ranges
struct RangeVector
{
   var() config range X;
   var() config range Y;
   var() config range Z;
};
```

### Scale and sheering

Used inside the editor to scale or sheer a solid object. Scaling will change the size of an object, sheering will streach an object in a certain direction (along a certain axis) whilst keeping it's "mass" the same. Picture pulling on one side of a square until it's a parrallelogram of the same area.

```

// A scale and sheering.
struct Scale
{
   var() config vector Scale;
   var() config float SheerRate;
   var() config enum ESheerAxis
   {
      SHEER_None,
      SHEER_XY,
      SHEER_XZ,
      SHEER_YX,
      SHEER_YZ,
      SHEER_ZX,
      SHEER_ZY,
   } SheerAxis;
};
```

### Camera orientations for Matinee

This is used in [Matinee](../../Uncategorized/MatineeTopics.md) to specify the desired orientation of the camera and how to get there.

```

// Camera orientations for Matinee
enum ECamOrientation
{
   CAMORIENT_None,
   CAMORIENT_LookAtActor,
   CAMORIENT_FacePath,
   CAMORIENT_Interpolate,
   CAMORIENT_Dolly,
};
```

### Generic axis enum.

Used to find "Support Bone Axis", the axis about which a bone will pivot in SVehicles. Also used in the editor to rotate the builder brush to match the axis requested.

```

// Generic axis enum.
enum EAxis
{
   AXIS_X,
   AXIS_Y,
   AXIS_Z
};
```

### RGB Color

A color, specified as Red/Green/Blue and Alpha (opacity).

```

// A color, Red, Green, Blue and Alpha
struct Color
{
   var() config byte B, G, R, A;
};
```

### Bounding Box

This is a 3D Box to contain something, like a system of particles, for example. See: [Particle Systems](../../Content Creation/Effects/ParticleSystems.md).This is similar to a [Range Vector](#range-vector).

```

// A bounding box.
struct Box
{
   var vector Min, Max;
   var byte IsValid;
};
```

### Bounding Volume

This is a box and a sphere. The sphere is implement with the same data structure as a plane, just consider (X,Y,Z) to be a point in space and W to be a distance.

```

// A bounding box sphere together.
struct BoundingVolume extends Box
{
   var plane Sphere;
};
```

### Matrix (4x4)

Matrices are used to transform from the global reference frame to a local reference frame. (e.g. RenderWorldToCamera contains the transform from the "Render World" (the global frame) to the "Camera World" (a local frame)). You could invert this matrix to get the "Camera to Render World" transform.

```

// a 4x4 matrix
struct Matrix
{
   var() Plane XPlane;
   var() Plane YPlane;
   var() Plane ZPlane;
   var() Plane WPlane;
};
```

### Interpolated functions

#### Interpolated function point

A point on a interpolated curve. (InVal, OutVal) is an ordered pair similar to (x,y). This is used internally.See also: [Interpolated curve functions](#interpolated-curve-functions) below.

```

// A interpolated function point.
struct InterpCurvePoint
{
   var() float InVal;
   var() float OutVal;
};
```

#### Interpolated function point

Just an array of points, which can be used to interpolate a function. This is used in SVehicleWheel.uc to approximate [Pacejka's Magic Formula](http://www.racer.nl/reference/pacejka.htm).

```

struct InterpCurve
{
   var() array<InterpCurvePoint>   Points;
};
```

### Compressed position

Just location, rotation and velocity. Heisenberg would be proud.
Pawn position is stored as a CompressedPosition for network replication.

```

struct CompressedPosition
{
   var vector Location;
   var rotator Rotation;
   var vector Velocity;
};
```

## Constants

MaxInt is the maximum positive integer.   
Pi is an [excellent film](http://www.imdb.com/title/tt0138704/) by Darren Aronofsky

```

//=============================================================================
// Constants.

const MaxInt = 0x7fffffff;
const Pi     = 3.1415926535897932;
```

## Basic native operators and functions

```

//=============================================================================
// Basic native operators and functions.
```

### Boolean operators

```

// Bool operators.
```

Boolean operaters usually operate on expressions inside 'if' statements that *evaluate* to be boolean, as opposed to actual booleans {true, false}. You won't see: if (true == (false && (true ^^ false))) you'll see if (i>5 && name=="John"). In this sense A and B are merely placeholders for boolean expressions.Below are a set of tables that will give you, given A and B, the result of each particular boolean expression.

#### A

"Not A" simply returns the opposite of A

| [A](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=1;up=0#sorted_table "Sort by this column") | [!A](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=1;up=0#sorted_table "Sort by this column") |
| --- | --- |
| false | true |
| true | false |

```

// !A     : Not A
native(129) static final preoperator  bool  !  ( bool A );
```

#### A = B

A == B returns whether or not two Booleans are the same:

| [A](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [B](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [A == B](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=2;up=0#sorted_table "Sort by this column") |
| --- | --- | --- |
| false | false | true |
| false | true | false |
| true | false | false |
| true | true | true |

```

// A == B : A equals B
native(242) static final operator(24) bool  == ( bool A, bool B );
```

#### A = B

A is not equal to B

| [A](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [B](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [A = B](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=3;up=0#sorted_table "Sort by this column") |
| --- | --- | --- |
| false | false | false |
| false | true | true |
| true | false | true |
| true | true | false |

```

// A != B : A is not equal to B
native(243) static final operator(26) bool  != ( bool A, bool B );
```

#### A && B

Both A and B must be true

| [A](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=4;up=0#sorted_table "Sort by this column") | [B](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=4;up=0#sorted_table "Sort by this column") | [A && B](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=4;up=0#sorted_table "Sort by this column") |
| --- | --- | --- |
| false | false | false |
| false | true | false |
| true | false | false |
| true | true | true |

```

// A && B : Both A and B must be true.
native(130) static final operator(30) bool  && ( bool A, skip bool B );
```

#### A ^^ B

A exclusive-or B, Either A or B can be true, but not both.

| [A](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=5;up=0#sorted_table "Sort by this column") | [B](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=5;up=0#sorted_table "Sort by this column") | [A ^^ B](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=5;up=0#sorted_table "Sort by this column") |
| --- | --- | --- |
| false | false | false |
| false | true | true |
| true | false | true |
| true | true | false |

```

// A ^^ B : Either A or B must be true, but not both
native(131) static final operator(30) bool  ^^ ( bool A, bool B );
```

#### A || B

True if either A or B (or both) are true.

| [A](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=0;table=6;up=0#sorted_table "Sort by this column") | [B](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=1;table=6;up=0#sorted_table "Sort by this column") | [A | | B](https://udn.epicgames.com/bin/publish/WebHome?webs=Main%2CTwo%2CThree%2CPowered&amp;inclusions=%2A&amp;exclusions=&amp;filter=&amp;inclfilter=%5C%25META%5C%3AFIELD%5C%7Bname%5C%3D%5C%22Documentavailability%5C%22.%2Avalue%5C%3D%5C%22General%20public%5C%22&amp;filterbymeta=yes&amp;skin=static_udn3&amp;restrictedclass=restricted&amp;format=&amp;sortcol=2;table=6;up=0#sorted_table "Sort by this column") |
| --- | --- | --- |
| false | false | false |
| false | true | true |
| true | false | true |
| true | true | true |

```

// A || B : Either A or B must be true.
native(132) static final operator(32) bool  || ( bool A, skip bool B );
```

### Byte operators

Multiply A by B and set A to the result.  
For example:

```

A = 5;
A *= 2;

A == 10
```

#### A \*= B

```

// A *= B : Multiply A by B and set A as the result.
native(133) static final operator(34) byte *= ( out byte A, byte B );
```

#### A /= B

```

// A /= B : Divide A by B and set A as the result.
native(134) static final operator(34) byte /= ( out byte A, byte B );
```

#### A += B

```

// A += B : Add A to B and set A as the result.
native(135) static final operator(34) byte += ( out byte A, byte B );
```

#### A -= B

```

// A -= B : Subtract B from A and set A as the result.
native(136) static final operator(34) byte -= ( out byte A, byte B );
```

#### ++A

```

// ++A    : Add one to A.  This is incremented *before* it is evaluated, so it will evaluate to A+1
native(137) static final preoperator  byte ++ ( out byte A );
```

#### A--

```

// --A    : Subtract one from A. This is decremented *before it is evaluated, so it will evaluate to A-1
native(138) static final preoperator  byte -- ( out byte A );
```

#### A++

```

// A++    : Add one to A.  This is incremented *after* it is evaluated, so it will evaluate to A
native(139) static final postoperator byte ++ ( out byte A );
```

#### A--

```

// A--    : Subtract one from A. This is decremented *after* it is evaluated, so it will evaluate to A
native(140) static final postoperator byte -- ( out byte A );
```

### Bit Manipulation

An introduction in bit manipulation can be found on [the WikiPedia](http://en.wikipedia.org/wiki/Bitwise_operation).

```

// ~A : bit flip A (one's complement)
// ~11001010 = 00110101
native(141) static final preoperator  int  ~  ( int A );
```

```

// A << B : Shift A left by B bits, fill bits on right with zeros
// 11001010 << 2 = 00101000
native(148) static final operator(22) int  << ( int A, int B );
```

```

// A >> B : Shift A right by B bits, fill bits on left with zeros
// 11001010 >> 2 = 00110010
native(149) static final operator(22) int  >> ( int A, int B );
```

```

// A >>> B : Same as right shift, as far as I know.
// 11001010 >> 2 = 00110010
native(196) static final operator(22) int  >>>( int A, int B );
```

```

// A & B : bitwise AND of A and B
// 11001010 & 11110000 = 11000000
native(156) static final operator(28) int  &  ( int A, int B );
```

```

// A ^ B : bitwise exclusive-OR of A and B
// 11001010 & 11110000 = 00111010
native(157) static final operator(28) int  ^  ( int A, int B );
```

```

// A | B : bitwise OR of A and B
// 11001010 & 11110000 = 11111010
native(158) static final operator(28) int  |  ( int A, int B );
```

### Integer operators

```

// Integer operators.

// make negative
native(143) static final preoperator  int  -  ( int A );

// A * B : multiply A by B
native(144) static final operator(16) int  *  ( int A, int B );

// A / B : divide A by B
native(145) static final operator(16) int  /  ( int A, int B );

// A + B : add A to B
native(146) static final operator(20) int  +  ( int A, int B );

// A - B : subtract B from A
native(147) static final operator(20) int  -  ( int A, int B );

// A < B : A less than B
native(150) static final operator(24) bool <  ( int A, int B );

// A > B : A greater than B
native(151) static final operator(24) bool >  ( int A, int B );

// A <= B : A less than or equal to B
native(152) static final operator(24) bool <= ( int A, int B );

// A >= B : A greater than or equal to B
native(153) static final operator(24) bool >= ( int A, int B );

// A == B : A is equal to B
native(154) static final operator(24) bool == ( int A, int B );

// A != B : A is not equal to B
native(155) static final operator(26) bool != ( int A, int B );

// A *= B : Multiply A by B and set A to the result
native(159) static final operator(34) int  *= ( out int A, float B );

// A /= B : Divide A by B and set A to the result
native(160) static final operator(34) int  /= ( out int A, float B );

// A += B : Add A to B and set A to the result
native(161) static final operator(34) int  += ( out int A, int B );

// A -= B : Subtract B from A and set A to the result
native(162) static final operator(34) int  -= ( out int A, int B );

// ++A : Add one to A.  This is incremented *before* it is evaluated, so it will evaluate to A+1
native(163) static final preoperator  int  ++ ( out int A );

// --A    : Subtract one from A. This is decremented *before it is evaluated, so it will evaluate to A-1
native(164) static final preoperator  int  -- ( out int A );

// A++    : Add one to A.  This is incremented *after* it is evaluated, so it will evaluate to A
native(165) static final postoperator int  ++ ( out int A );

// A--    : Subtract one from A. This is decremented *after* it is evaluated, so it will evaluate to A
native(166) static final postoperator int  -- ( out int A );
```

### Integer functions

```

// Integer functions.

// return a random number between 0 and (Max-1)
// Max should be a positive number, otherwise Rand consistently returns 0
native(167) static final Function     int  Rand  ( int Max );

// return A or B, whichever is smaller
native(249) static final function     int  Min   ( int A, int B );

// return A or B, whichever is larger
native(250) static final function     int  Max   ( int A, int B );

// Clamp V between A and B.  If V is between A and B, return V,
// if smaller, return the lower limit (either A or B)
// if larger, return the upper limit (either A or B)
native(251) static final function     int  Clamp ( int V, int A, int B );
```

### Float operators

```

// Float operators.

// negate A.
native(169) static final preoperator  float -  ( float A );

// raise A to the power of B, or multiply A by itself, B times.
native(170) static final operator(12) float ** ( float A, float B );

// multiply A by B
native(171) static final operator(16) float *  ( float A, float B );

// divide A by B
native(172) static final operator(16) float /  ( float A, float B );

// return A modulo B, the remainder when you divide A by B
native(173) static final operator(18) float %  ( float A, float B );

// Add A and B
native(174) static final operator(20) float +  ( float A, float B );

// Subtract B from A
native(175) static final operator(20) float -  ( float A, float B );

// return whether A is less than B
native(176) static final operator(24) bool  <  ( float A, float B );

// return whether A is greater than B
native(177) static final operator(24) bool  >  ( float A, float B );

// return whether A is less than or equal to B
native(178) static final operator(24) bool  <= ( float A, float B );

// return whether A is greater than or equal to B
native(179) static final operator(24) bool  >= ( float A, float B );

// return whether A is equal to B
native(180) static final operator(24) bool  == ( float A, float B );

// return whether A is approximately (within 0.0001) equal to B
native(210) static final operator(24) bool  ~= ( float A, float B );

// return whether A is not equal B
native(181) static final operator(26) bool  != ( float A, float B );

// multiply A and B, set A to the result
native(182) static final operator(34) float *= ( out float A, float B );

// divide A by B, set A to the result
native(183) static final operator(34) float /= ( out float A, float B );

// Add A to B, set A to the result
native(184) static final operator(34) float += ( out float A, float B );

// Subtract B from A, set A to the result
native(185) static final operator(34) float -= ( out float A, float B );
```

### Float functions

```

// Float functions.
// Absolute value of A
native(186) static final function     float Abs   ( float A );

// sin(A) : Sine of A, expressed in radians.
native(187) static final function     float Sin   ( float A );

// Asin(A) : inverse sine of A expressed in radians.
native      static final function     float Asin  ( float A );

// cos(A) : cosine of A expressed in radians.
native(188) static final function     float Cos   ( float A );

// Acos(A) : inverse cosine of A expressed in radians.
native      static final function     float Acos  ( float A );

// tan(A) : tangent of A expressed in radians.
native(189) static final function     float Tan   ( float A );

// Atan(A) : inverse tangent of A/B expressed in radians.
native(190) static final function     float Atan  ( float A, float B );

// exp(A) : raise e to the A power
native(191) static final function     float Exp   ( float A );

// ln(A) : compute the natural log of A
native(192) static final function     float Loge  ( float A );

// sqrt(A): compute the square root of A
native(193) static final function     float Sqrt  ( float A );

// A*A, compute A multiplied by itself
native(194) static final function     float Square( float A );

// return a random number between 0 and 1
native(195) static final function     float FRand ();

// return either A or B, whichever is smaller
native(244) static final function     float FMin  ( float A, float B );

// return either A or B, whichever is larger
native(245) static final function     float FMax  ( float A, float B );

// Clamp V between A and B.  If V is between A and B, return V,
// if smaller, return the lower limit (either A or B)
// if larger, return the upper limit (either A or B)
native(246) static final function     float FClamp( float V, float A, float B );

// give a linear interpolation of Alpha between A and B
native(247) static final function     float Lerp  ( float Alpha, float A, float B );

// Returns an Alpha-smooth nonlinear interpolation between A and B.
native(248) static final function     float Smerp ( float Alpha, float A, float B );
```

### Vector operators

```

// Vector operators.

// negate the vector (multiply by -1)
native(211) static final preoperator  vector -     ( vector A );

// right-multiply a vector by a number
native(212) static final operator(16) vector *     ( vector A, float B );

// left-multiply a number by a vector
native(213) static final operator(16) vector *     ( float A, vector B );

// multiply two vectors
native(296) static final operator(16) vector *     ( vector A, vector B );

// divide a vector by a number
native(214) static final operator(16) vector /     ( vector A, float B );

// add two vectors
native(215) static final operator(20) vector +     ( vector A, vector B );

// subtract two vectors
native(216) static final operator(20) vector -     ( vector A, vector B );

// Forward vector transformation.  Rotate vector A forward by a rotator B (yaw, pitch, roll)
native(275) static final operator(22) vector <<    ( vector A, rotator B );

// Backward vector transformation.  Rotate vector A by backward a rotator B (yaw, pitch, roll)
native(276) static final operator(22) vector >>    ( vector A, rotator B );

// test for vector equality
native(217) static final operator(24) bool   ==    ( vector A, vector B );

// test for vector inequality
native(218) static final operator(26) bool   !=    ( vector A, vector B );

// compute dot product of two vectors
native(219) static final operator(16) float  Dot   ( vector A, vector B );

// compute cross product of two vectors
native(220) static final operator(16) vector Cross ( vector A, vector B );

// set A to result of right-multiply vector A by number B
native(221) static final operator(34) vector *=    ( out vector A, float B );

// set A to result of multiplying vectors A and B
native(297) static final operator(34) vector *=    ( out vector A, vector B );

// set A to result of dividing vector A by B
native(222) static final operator(34) vector /=    ( out vector A, float B );

// set A to result of adding vectors A and B
native(223) static final operator(34) vector +=    ( out vector A, vector B );

// set A to result of subtracting B from A
native(224) static final operator(34) vector -=    ( out vector A, vector B );

```

### Vector functions

```

// Vector functions.

// Returns the euclidean size of the vector (the square root of the sum of the components squared).
native(225) static final function float  VSize  ( vector A );

// Returns a vector of size 1.0, facing in the direction of the specified vector.
native(226) static final function vector Normal ( vector A );

// Inverts a coordinate system specified by three axis vectors.
// Vectors X, Y, and Z specify an arbitrary coordinate system.  X, Y and Z are specified in terms of the "root" or "Euclidian"
// coordinate system.  Create a coordinate system that would map a point in the X,Y,Z system back into the "root" system.
native(227) static final function        Invert ( out vector X, out vector Y, out vector Z );

// Returns a uniformly distributed random vector.
native(252) static final function vector VRand  ( );

// Mirrors a vector about a specified normal vector.
native(300) static final function vector MirrorVectorByNormal( vector Vect, vector Normal );
```

### Rotator operators and functions

A rotator is just a vector representing yaw, pitch and roll.

```

// Rotator operators and functions.

// Tests for rotator equality
native(142) static final operator(24) bool ==     ( rotator A, rotator B );

// Tests for rotator inequality
native(203) static final operator(26) bool !=     ( rotator A, rotator B );

// right-multiply a rotator by a number
native(287) static final operator(16) rotator *   ( rotator A, float    B );

// left-multiply a rotator by a number
native(288) static final operator(16) rotator *   ( float    A, rotator B );

// divide a rotator by a number
native(289) static final operator(16) rotator /   ( rotator A, float    B );

// set A to the result of mutiplying a rotator A by B
native(290) static final operator(34) rotator *=  ( out rotator A, float B  );

// set B to the result of dividing a rotator A by B
native(291) static final operator(34) rotator /=  ( out rotator A, float B  );

// Add rotators A and B
native(316) static final operator(20) rotator +   ( rotator A, rotator B );

// Subtract rotator B from A
native(317) static final operator(20) rotator -   ( rotator A, rotator B );

// Set A to the result of adding rotators A and B
native(318) static final operator(34) rotator +=  ( out rotator A, rotator B );

// Set A to the result of subtracting B from A
native(319) static final operator(34) rotator -=  ( out rotator A, rotator B );

// ??
native(229) static final function GetAxes         ( rotator A, out vector X, out vector Y, out vector Z );

// ??
native(230) static final function GetUnAxes       ( rotator A, out vector X, out vector Y, out vector Z );

// Get a random rotator
native(320) static final function rotator RotRand ( optional bool bRoll );

// Return the orthogonal rotation based on the input vectors
native      static final function rotator OrthoRotation( vector X, vector Y, vector Z );

// return a normalized rotation
native      static final function rotator Normalize( rotator Rot );

// returns true if B is clockwise from A, rotators wrap around at 32768.
// this function can be used to determine if B is clockwise from A or not.
native      static final operator(24) bool ClockwiseFrom( int A, int B );

```

### String operators and functions

Extensive documentation on string operators and functions is available here:  [StringsInUnrealScript](../../Uncategorized/StringsInUnrealScript.md)

```

// String operators.

// concat A and B, result would be "AB"
native(112) static final operator(40) string $  ( coerce string A, coerce string B );

// concat A , " " and B, the result would be "A B"
native(168) static final operator(40) string @  ( coerce string A, coerce string B );

// string comparision
native(115) static final operator(24) bool   <  ( string A, string B );
native(120) static final operator(24) bool   <= ( string A, string B );
native(121) static final operator(24) bool   >= ( string A, string B );

// strings are equal
native(122) static final operator(24) bool   == ( string A, string B );

// case insensitive string compare
native(123) static final operator(26) bool   != ( string A, string B );

// strings are not equal (case insensitive)
native(124) static final operator(24) bool   ~= ( string A, string B );

// concat and assign: A $=B results in A = "AB"
native(322) static final operator(44) string $= ( out    string A, coerce string B );
native(323) static final operator(44) string @= ( out    string A, coerce string B );

// remove the B from A and assign it to A
native(324) static final operator(45) string -= ( out    string A, coerce string B );

// String functions.
// string length
native(125) static final function int    Len    ( coerce string S );

// returns the position of T in S, -1 if not found
native(126) static final function int    InStr  ( coerce string S, coerce string t );
native(127) static final function string Mid    ( coerce string S, int i, optional int j );
native(128) static final function string Left   ( coerce string S, int i );
native(234) static final function string Right  ( coerce string S, int i );

// byte to char
native(236) static final function string Chr    ( int i );
native(237) static final function int    Asc    ( string S );

// change the case of a string
native(235) static final function string Caps   ( coerce string S );
native(238) static final function string Locs   ( coerce string S);

// device("key=value", "=", "key", "value")
native(239) static final function bool   Divide ( coerce string Src, string Divider, out string LeftPart, out string RightPart);
// splits a string on divider, returns the number of elements
native(240) static final function int    Split  ( coerce string Src, string Divider, out array<string> Parts );

// compare two strings, count is the nubber of characters to compare (if count = 0 this is the same as the == operator)
native(200)  static final function int    StrCmp ( coerce string S, coerce string T, optional int Count, optional bool bCaseSensitive );

// replace substrings
native(201)  static final function string Repl   ( coerce string Src, coerce string Match, coerce string With, optional bool bCaseSensitive );

// if condition is true return ResultIfTrue otherwise ResultIfFalse
native(202)  static final function string Eval   ( bool Condition, coerce string ResultIfTrue, coerce string ResultIfFalse );
```

### Object operators

```

// Object operators.

// Generic equality operator for objects.
native(114) static final operator(24) bool == ( Object A, Object B );

// Generic inequality operator for objects
native(119) static final operator(26) bool != ( Object A, Object B );

```

### Name operators

```

// Name operators.
// Returns whether the names are equal
native(254) static final operator(24) bool == ( name A, name B );

// Returns whether the names are different
native(255) static final operator(26) bool != ( name A, name B );

```

### Interpolated Curve functions

To be used with [Interpolated Curves](#interpolated-curve-functions)

```

// InterpCurve operator

// returns the output value for the given input
native      static final function float InterpCurveEval( InterpCurve curve, float input );

// get the min and max output value
native      static final function InterpCurveGetOutputRange( InterpCurve curve, out float min, out float max );

// get the min and max input value that can be used
native      static final function InterpCurveGetInputDomain( InterpCurve curve, out float min, out float max );
```

### Quaternion functions

```

// Quaternion functions

// Returns the product of two quaternions.
native      static final function Quat QuatProduct( Quat A, Quat B );

// Inverts the quaternion
native      static final function Quat QuatInvert( Quat A );

// Applies quaternion A to vector B, return resulting vector
native      static final function vector QuatRotateVector( Quat A, vector B );

// Computes the quaternion that will rotate vector A to vector B
native      static final function Quat QuatFindBetween( Vector A, Vector B );

// Convert an axis and angle to a quaternion
native      static final function Quat QuatFromAxisAndAngle( Vector Axis, Float Angle );

// Convert a rotator to a quaternion
native      static final function Quat QuatFromRotator( rotator A );

// Convert a quaternion to a rotator
native      static final function rotator QuatToRotator( Quat A );

```

## General functions

```

//=============================================================================
// General functions.
```

### Logging

```

// Logging.
// Logs the string S, using debugf, prepended by the tag _Tag_
native(231) final static function Log( coerce string S, optional name Tag );

// Creates a warning in the log file. A warning message contains the Class name and line where the warning was issued.
native(232) final static function Warn( coerce string S );

// Looks up the localized version of a string (translated into the local language)
native static function string Localize( string SectionName, string KeyName, string PackageName );
```

### Goto state and label

```

// Goto state and label.
// Redirects code flow to the new state
native(113) final function GotoState( optional name NewState, optional name Label );

// returns whether the code is in a certain state.
native(281) final function bool IsInState( name TestState );

// return the name of the state UnrealScript is currently in.
native(284) final function name GetStateName();

```

### Objects

```

// Objects.

// Return whether _TestClass_ inherits from _ParentClass_
native(258) static final function bool ClassIsChildOf( class TestClass, class ParentClass );

// Return whether this object inherits from _ClassName_
// This function will bubble up the class tree (parent classes) of the this object add check if
// ClassName matches the (parent) classname. ClassName will never be instantiated.
native(303) final function bool IsA( name ClassName );
```

### Probe messages

```

// Probe messages.

// Allow a type of message to be passed into UnrealScript, (e.g. Enable( 'Tick' );)
native(117) final function Enable( name ProbeFunc );

// Filter out type of message to be passed into UnrealScript, (e.g. Enable( 'Tick' );)
native(118) final function Disable( name ProbeFunc );

```

### Properties

```

// Properties.

// Finds _PropName_ amoungst the packages, and returns it's value
native final function string GetPropertyText( string PropName );

// Find _PropName_ amoungst the packages, set it's value to _PropValue_
native final function SetPropertyText( string PropName, string PropValue );

// Returns the name of the enum value
// GetEnum(enum'EDetailMode', 1) will return 'DM_High'
native static final function name GetEnum( object E, int i );

// Load an object: (e.g. HudClass = class<HUD>(DynamicLoadObject(HUDType, class'Class')); )
native static final function object DynamicLoadObject( string ObjectName, class ObjectClass, optional bool MayFail );

// Finds _ObjectName_ amoungst the packages.
native static final function object FindObject( string ObjectName, class ObjectClass );

```

### Configuration

See  [SaveConfiguration](../../Uncategorized/SaveConfiguration.md)

```

// Configuration.
// Saves object configurations to .ini files.
native(536) final function SaveConfig();

// Saves object configurations to .ini files.
// StaticSaveConfig() on a class variable will write the objects _default_ values to the ini file.
native static final function StaticSaveConfig();

// Remove the configuration entries for this class (or only this property) from the ini file.
// If the resulting ini is empty it will be deleted.
native(537) final function ClearConfig( optional string PropName );
native static final function StaticClearConfig( optional string PropName );

// Reloads a previously saved configuration
native static final function ResetConfig( optional string PropName );

// return the names of PerObject configurations
native static final function array<string> GetPerObjectNames( string ININame, optional string ObjectClass,
    optional int MaxResults /*1024 if unspecified*/ );
```

### Random number within a range

```

// Return a random number within the given range.
final function float RandRange( float Min, float Max )
{
    return Min + (Max - Min) * FRand();
}
```

## Engine notification functions

```

//=============================================================================
// Engine notification functions.
```

### Begin State

```

//
// Called immediately when entering a state, while within
// the GotoState call that caused the state change.
//
event BeginState();
```

### End State

```

//
// Called immediately before going out of the current state,
// while within the GotoState call that caused the state change.
//
event EndState();
```

```

defaultproperties
{
}
```

