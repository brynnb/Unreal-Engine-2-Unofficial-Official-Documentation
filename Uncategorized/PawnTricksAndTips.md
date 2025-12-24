# Pawn Tricks and Tips

*Created by Chris Linder (DemiurgeStudios?) on 12-05-03 for 2226 builds. Last Updated by Chris Linder (DemiurgeStudios?).*

* [Pawn Tricks and Tips](PawnTricksAndTips.md#Pawn Tricks and Tips)
  + [Related Documents](PawnTricksAndTips.md#Related Documents)
  + [Introduction](PawnTricksAndTips.md#Introduction)
  + [Walking and Running](PawnTricksAndTips.md#Walking and Running)
  + [Pawn Scale](PawnTricksAndTips.md#Pawn Scale)
    - [Using the Scaling Code](PawnTricksAndTips.md#Using the Scaling Code)
    - [Net Play](PawnTricksAndTips.md#Net Play)
    - [Runtime Install](PawnTricksAndTips.md#Runtime Install)
  + [Camera and View](PawnTricksAndTips.md#Camera and View)
    - [Simple Third-Person Camera](PawnTricksAndTips.md#Simple Third-Person Camera)
    - ["Special" Camera](PawnTricksAndTips.md#"Special" Camera)
    - [PlayerController Camera Functions](PawnTricksAndTips.md#PlayerController Camera Functions)
      * [PlayerCalcView](PawnTricksAndTips.md#PlayerCalcView)
    - [CalcFirstPersonView](PawnTricksAndTips.md#CalcFirstPersonView)
      * [CalcBehindView](PawnTricksAndTips.md#CalcBehindView)
  + [The "Set" Command](PawnTricksAndTips.md#The "Set" Command)

## Related Documents

[MyFirstPawn](MyFirstPawn.md), [MyFirstCode](MyFirstCode.md), [GameAndAIHandout](GameAndAIHandout.md)

## Introduction

This document is a collection of little odds and ends that are helpful. For example, this document includes a small code change that allows you to change the default behavior of pawns from running to walking.

## Walking and Running

By default in the Unreal Engine, pawns run and when you hold shift they switch to walking. This tip shows you how to make it so that pawns walk by default and run you hold shift. Changing this behavior could be useful in many situations, for example in a less fast paced game, or a game that has some consequence of running like making more noise. This change could also be used to make characters run and sprint instead of walk and run.In *PlayerController.uc* there is a function *HandleWalking()*. This function is called to set the walking status of the pawn. Normally the function reads:

```

function HandleWalking()
{
   if ( Pawn != None )
      Pawn.SetWalking( (bRun != 0) && !Region.Zone.IsA('WarpZoneInfo') );
}
```

To change the walking/running behavior all you need to do is change `"(bRun != 0)"` to `"(bRun == 0)"`. You can either make this change in *PlayerController.uc* or override *HandleWalking* in your own subclass of *PlayerController*. Note: If you are using a build like the Runtime or UT2003 (you don't have an engine license) then you cannot rebuild *Engine.u* (where *PlayerController.uc* is) so you will have to subclass *PlayerController*. The changed version of *HandleWalking()* will look like this:

```

function HandleWalking()
{
   if ( Pawn != None )
      Pawn.SetWalking( (bRun == 0) && !Region.Zone.IsA('WarpZoneInfo') );
}
```

## Pawn Scale

Quite frequently it is a tricky problem to get the size of the player to feel right in comparison to the size of the world. The *SetPawnScale* function below allows you to easily change the size of the pawn. It changes the draw scale, the collision cylinder size, the eye height, the movement speed, and several other variables.The code presented below is not a perfect solution but this will give you a good idea of how to scale the pawn. The main problem is that un-crouching sets the collision cylinder back to its default size. Also, the maximum height of steps that pawns can walk up is a const defined in *Actor.uc* as "35.0" which means if you scale the size of the pawn up, it can still be blocked by walls that now look like tiny little obstacles. Another thing that feels a little odd is that the gravity of the world is not changing as you change size. So, for example, when your pawn is very large, you will hang in the air a longer time when you jump. You will still jump the same relative height though.The following code can be placed in any subclass of class *Pawn*.

```

replication
{
   reliable if ( Role < ROLE_Authority )
      ServerSetPawnScale;
}

...

simulated function SetPawnScale(float NewScale)
{
   Local PlayerController PC;

   if(NewScale == 0)
   {
      log("Can't set scale to 0.");
      return;
   }

   //DrawScale
   SetDrawScale(NewScale);

   //Movement Speeds
   GroundSpeed      = Default.GroundSpeed * NewScale;      // maximum
                                                            ground speed
   WaterSpeed       = Default.WaterSpeed * NewScale;       // maximum
                                                          swimming speed
   AirSpeed         = Default.AirSpeed * NewScale;         // maximum
                                                            flying speed
   LadderSpeed      = Default.LadderSpeed * NewScale;      // ladder
                                                          climbing speed
   AccelRate        = Default.AccelRate * NewScale;        // max
                                                       acceleration rate
   JumpZ            = Default.JumpZ * Sqrt(NewScale);      // vertical
                                                           jump velocity
   MaxFallSpeed     = Default.MaxFallSpeed * NewScale;     // speed pawn
                                              can land w/o taking damage
   BaseMovementRate = Default.BaseMovementRate * NewScale; // used to
                                          scale movement animation speed

   //Camera
   BaseEyeHeight   = Default.BaseEyeHeight * NewScale;   // base eye
                                          height above collision center.
   if(Controller != NONE)
      PC = PlayerController(Controller);
   if(PC != NONE)
      PC.CameraDist = PC.Default.CameraDist * NewScale; // behind view
                                                         camera distance

   //Collision - Note: un-crouching messes up the collision size
   CrouchHeight   = Default.CrouchHeight * NewScale;  // CollisionHeight
                                                          when crouching
   CrouchRadius   = Default.CrouchRadius * NewScale;  // CollisionRadius
                                                          when crouching
   SetCollisionSize(Default.CollisionRadius * NewScale,
                                    Default.CollisionHeight * NewScale);
}

function ServerSetPawnScale(float NewScale)
{
   SetPawnScale(NewScale);
}

exec function ScalePawn(float NewScale)
{
   if(Role < ROLE_Authority)
      ServerSetPawnScale(NewScale);
   SetPawnScale(NewScale);
}

exec function GetBigger()
{
   if(Role < ROLE_Authority)
      ServerSetPawnScale(DrawScale * 1.25);
   SetPawnScale(DrawScale * 1.25);
}

exec function GetSmaller()
{
   if(Role < ROLE_Authority)
      ServerSetPawnScale(DrawScale * 0.8);
   SetPawnScale(DrawScale * 0.8);
}
```

### Using the Scaling Code

To scale your pawn in-game, simply use one of the three exec function, *ScalePawn*, *GetBigger*, or *GetSmaller*. For example, you can bring up the console (hit `"~"`) and type `"ScalePawn x"` where "x" is the new scale, for example 0.5. You could also bind keys to the *GetBigger* and *GetSmaller* functions and just press those keys to get bigger and smaller. To do this, bring up the console and type:

```

set input g getsmaller
set input h getbigger
```

Once you have found a good scale for your pawn, you can actually redefine the variables in defaultproperties that *SetPawnScale* temporarily adjusts. Make sure you remember to adjust *DrawScale* and *CollisionRadius* and *CollisionHeight* as well. Also, do not change *CameraDist* in *PlayerController*, it will scale correctly when you change *CollisionRadius*.

### Net Play

The scaling code works in net play as well as single player. For more details on setting up and connecting to a server see the [MyFirstCode](MyFirstCode.md) document.

### Runtime Install

If you are using the Runtime, you can simply download [ScalePawns.zip](rsrc/Two/PawnTricksAndTips/ScalePawns.zip) and install the contained UMOD. If you have trouble installing the UMOD see the [MyFirstCode](MyFirstCode.md) document. Once the UMOD is installed you can then start the Runtime, bring up the console by pressing `"~"`, and type:`Open EM_Runtime?Class=ScalePawns.ScaleBoy`
  
- or -  
`Open EM_Runtime?Class=ScalePawns.ScaleGirl`This will put you in a map with the new scalable pawns.

## Camera and View

Often people wish to change the camera in Unreal. There are many ways to do this; the section below will cover a few.

### Simple Third-Person Camera

The easiest way to get a third person camera is to type `"behindview 1"` at the console when you are in the game. This will switch the camera to a third-person camera behind the pawn. To switch back to a first-person view type `"behindview 0"` at the console. Some builds of the engine (2226 code-drop and builds based on 2226) have an additional function *ToggleBehindView* which is bound to `'b'`, so all you have to do to switch between first-person and third-person is to press the `'b'` key.If you want to start with a third-person camera, the easiest way is to override the *PointOfView* function in *Pawn.uc*. This function, `simulated function bool PointOfView()`, is called when the pawn is possessed by the controller. The return value of this function determines if the camera will be third person (true) or first person (false). Be default this function returns *false* but you can override it to return true like follows:

```

/* PointOfView()
called by controller when possessing this pawn
false = 1st person, true = 3rd person
*/
simulated function bool PointOfView()
{
   return true;
}
```

### "Special" Camera

If you want a camera that is different from the basic first-person and third-person cameras mentioned above, you might want to override function *SpecialCalcView* in *Pawn.uc*. This function will be called when *bSpecialCalcView* is *true*. *SpecialCalcView* allows you to change the actor the camera is looking at, the location of the camera, and the rotation of the camera. The function is defined as follows:

```

// If returns false, do normal calview anyway
function bool SpecialCalcView(out actor ViewActor,
                              out vector CameraLocation,
                              out rotator CameraRotation );
```

* *ViewActor* -- comes in as the *Viewport.Actor* (which is the *PlayerController*). In most cases you will ignore this "in" value. You should set *ViewActor* to the pawn relevant for this camera. In a first-person camera, that will be the pawn whose eyes the world is seen though; in a third-person camera, that will be the pawn on which the camera is focused.
* *CameraLocation* -- comes in as the location of the *Viewport.Actor* (which is the *PlayerController*). The location of the *PlayerController* is almost always that of the *Pawn*. In most cases you will ignore this "in" value. You should set *CameraLocation* to the location you want the camera.
* *CameraRotation* -- comes in as the rotation of the *Viewport.Actor* (which is the *PlayerController*). This "in" value is very useful because it indicates which way the player has moved his or her mouse to look. In most cases you will not change *CameraRotation* but you can set it to the direction the camera should be pointing.

The code below is an example implementation of *SpecialCalcView* that points the camera at the pawns face. The camera is closer than the normal third person view and focused on the head of the pawn instead of the center of the pawn. There is also an exec function (*ToggleSV*) for toggling the *SpecialCalcView*.

```

simulated function bool SpecialCalcView(out actor ViewActor,
                                        out vector CameraLocation,
                                        out rotator CameraRotation )
{
   local vector CamLookAt, HitLocation, HitNormal, OffsetVector;
   local PlayerController pc;

   pc = PlayerController(Controller);

   pc.bBehindView = true;

   // Only do this mode we have a playercontroller viewing this pawn
   if(pc == None || pc.ViewTarget != self)
      return false;

   ViewActor = self;
   CamLookAt = Location;
   CamLookAt.Z += EyeHeight;

   OffsetVector = vect(0, 0, 0);
   OffsetVector.X = -0.5 * pc.CameraDist * Default.CollisionRadius;

   // look at Pawn's face
   CameraRotation.Yaw += 32768;

   CameraLocation = CamLookAt + (OffsetVector >> CameraRotation);

   if( Trace( HitLocation, HitNormal, CameraLocation, CamLookAt, false,
                                            vect(10, 10, 10) ) != None )
   {
      CameraLocation = HitLocation;
   }

   return true;
}

exec function ToggleSV()
{
   bSpecialCalcView = !bSpecialCalcView;
}
```

### PlayerController Camera Functions

If you really want to overhaul the camera or completely change it, you probably want to override the camera functions in *PlayerController.uc*. There are three important functions; *PlayerCalcView*, *CalcBehindView*, and *CalcFirstPersonView*. *PlayerCalcView* is the entry point for calculating the camera. This function calls *SpecialCalcView* described above if *Pawn.bSpecialCalcView* is **true**. If a special camera is not used, *PlayerCalcView* does some trickery based *ViewTarget* and *bBehindView* and ends up calling *CalcFirstPersonView* or *CalcBehindView*.Each of these functions is discussed in detail below. The discussion revolves around not what these functions do already but when they are called and what their parameters are.

#### PlayerCalcView

```

event PlayerCalcView(out actor ViewActor,
                     out vector CameraLocation,
                     out rotator CameraRotation )
```

This is the entry point into the calculating the camera and is called every fame.

* *ViewActor* -- comes in as the *Viewport.Actor* (which is the *PlayerController*). In most cases you will ignore this "in" value. You should set *ViewActor* to the pawn relevant for this camera. In a first-person camera, that will be the pawn whose eyes the world is seen though; in a third-person camera, that will be the pawn on which the camera is focused.
* *CameraLocation* -- comes in as the location of the *Viewport.Actor* (which is the *PlayerController*). The location of the *PlayerController* is almost always that of the *Pawn*. In most cases you will ignore this "in" value. You should set *CameraLocation* to the location you want the camera.
* *CameraRotation* -- comes in as the rotation of the *Viewport.Actor* (which is the *PlayerController*). This "in" value is very useful because it indicates which way the player has moved his or her mouse to look. In most cases you will not change *CameraRotation* but you can set it to the direction the camera should be pointing.

### CalcFirstPersonView

```

function CalcFirstPersonView(out vector CameraLocation,
                             out rotator CameraRotation )
```

This function calculates a first-person camera. The only function that calls *CalcBehindView* is *CalcBehindView*. *CalcFirstPersonView* is useful for adding things like eye-height, view shake, and stair smoothing.

* CameraLocation -- comes in as the location of the *Viewport.Actor* (which is the *PlayerController*). The location of the *PlayerController* is almost always that of the *Pawn*. In most cases you will add things like eye-height and view shake to *CameraLocation* and then return the modified *CameraLocation*.
* *CameraRotation* -- comes in as the rotation of the *Viewport.Actor* (which is the *PlayerController*). This "in" value is very useful because it indicates which way the player has moved his or her mouse to look. In most cases you will not change *CameraRotation* but you can set it to the direction the camera should be pointing.

#### CalcBehindView

```

function CalcBehindView(out vector CameraLocation,
                        out rotator CameraRotation,
                        float Dist)
```

This function calculates a third-person camera. The only function that calls *CalcBehindView* is *CalcBehindView*. *CalcBehindView* is only called when *bBehindView* is true. It is worth noting that *bBehindView* does not make the camera a third person camera, it only makes it so the player's own pawn is drawn.

* CameraLocation -- this is the location from which the camera should be slid back. Once the camera has been slid back, the new slide back location is returned in *CameraLocation*.
* CameraRotation -- comes in as the rotation the *PlayerController*. This "in" value is very useful because it indicates which way the player has moved his or her mouse to look. In most cases you will not change *CameraRotation* but you can set it to the direction the camera should be pointing.
* Dist -- this is the distance the camera should be slide back starting at *CameraLocation* and moved in the direction opposite to *CameraRotation*.

## The "Set" Command

The "Set" command is a general and very useful debugging tool that works for all actors, not just pawns. The idea is that you can change variables of actors mid-game simply by typing something at the console. The format of the "Set" command is as follows:`SET <ClassName> <VariableName> <NewValue>`The first parameter string a class name, the second string a variable name, and the third string is a value. All objects of the given class (including subclasses) will have the given variable set to the given value. For example `"SET PAWN JUMPZ 4000"` will set the jump velocity of all pawns, including your character, to 4000. Below are some more examples of the "Set" in use. (Note: Capitalization does not matter.)`set Pawn CollsionRadius 10` -- sets the collision radius of all pawns to 10.`set ZoneInfo bDistanceFog false` -- turns off distance fog for all zones.`set Pawn Mesh SkeletalMesh'UDN_CharacterModels_K.GenericFemale'` -- sets the mesh of all pawns to the UDN example girl model.`set Pawn ConstantAcceleration (X=0,Y=0,Z=1300)` -- sets the additional falling acceleration of all pawns. This is added on top of gravity. 1300 is still less than normal gravity so pawns will still fall, just much more slowly.All values are entered in to the form they are entered in for defaultproperties for the given variable type.
