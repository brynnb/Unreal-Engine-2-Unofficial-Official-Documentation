# UnrealScript Startup Code Flow

*Created by Chris Linder (DemiurgeStudios?) on 12-12-03 for 2226 builds. Last Updated by Chris Linder (DemiurgeStudios?).*

* [UnrealScript Startup Code Flow](#unrealscript-startup-code-flow)
  + [Related Documents](#related-documents)
  + [Introduction](#introduction)
  + [Startup Code Flow](#startup-code-flow)

## Related Documents

[UnrealScriptReference](UnrealScriptReference.md), [MyFirstCode](../../Uncategorized/MyFirstCode.md), [GameAndAIHandout](../../Uncategorized/GameAndAIHandout.md)

## Introduction

The following code is used for starting the UnrealScript scripting part of the engine. This code is called when loading a map so all the actors in that map get the proper events and notifications. The code is presented because it seems useful to know what order in which the UnrealScript functions are called when starting a map.

## Startup Code Flow

The following is C++ code that in some form exists in all builds of the Unreal Engine. This code is specifically from UT2004 and was brought to you by Steve Polge, the number '5', and the letter 'fun'.

```

// Init the game.
if( Info->Game )
{
   Info->Game->eventInitGame( Options, Error );
   Info->Game->eventSetGrammar();
}

// Send PreBeginPlay.
for( INT i=0; i<GLevel->Actors.Num(); i++ )
   if( GLevel->Actors(i) && !GLevel->Actors(i)->bScriptInitialized )
      GLevel->Actors(i)->eventPreBeginPlay();

// Set BeginPlay.
for( INT i=0; i<GLevel->Actors.Num(); i++ )
   if( GLevel->Actors(i) && !GLevel->Actors(i)->bScriptInitialized )
      GLevel->Actors(i)->eventBeginPlay();

// Set zones.
for( INT i=0; i<GLevel->Actors.Num(); i++ )
   if( GLevel->Actors(i) && !GLevel->Actors(i)->bScriptInitialized )
      GLevel->Actors(i)->SetZone( 1, 1 );

// set appropriate volumes for each actor
for( INT i=0; i<GLevel->Actors.Num(); i++ )
   if( GLevel->Actors(i) && !GLevel->Actors(i)->bScriptInitialized )
      GLevel->Actors(i)->SetVolumes();

// Post begin play.
for( INT i=0; i<GLevel->Actors.Num(); i++ )
   if( GLevel->Actors(i) && !GLevel->Actors(i)->bScriptInitialized )
   {
      GLevel->Actors(i)->eventPostBeginPlay();

      if(GLevel->Actors(i))
         GLevel->Actors(i)->PostBeginPlay();
   }

// Post net begin play.
for( INT i=0; i<GLevel->Actors.Num(); i++ )
   if( GLevel->Actors(i) && !GLevel->Actors(i)->bScriptInitialized )
      GLevel->Actors(i)->eventPostNetBeginPlay();

// Begin scripting.
for( INT i=0; i<GLevel->Actors.Num(); i++ )
   if( GLevel->Actors(i) && !GLevel->Actors(i)->bScriptInitialized )
      GLevel->Actors(i)->eventSetInitialState();

// Find bases
for( INT i=0; i<GLevel->Actors.Num(); i++ )
{
   if( GLevel->Actors(i) )
   {
      if ( GLevel->Actors(i)->AttachTag != NAME_None )
      {
         //find actor to attach self onto
         for( INT j=0; j<GLevel->Actors.Num(); j++ )
         {
            if( GLevel->Actors(j)
               && ((GLevel->Actors(j)->Tag == GLevel->Actors(i)->AttachTag)
                   || (GLevel->Actors(j)->GetFName() == GLevel->Actors(i)->AttachTag))  )
            {
               GLevel->Actors(i)->SetBase(GLevel->Actors(j), FVector(0,0,1), 0);
               break;
            }
         }
      }
      else if( GLevel->Actors(i)->bCollideWorld && GLevel->Actors(i)->bShouldBaseAtStartup
         &&   ((GLevel->Actors(i)->Physics == PHYS_None) || (GLevel->Actors(i)->Physics == PHYS_Rotating)) )
      {
            GLevel->Actors(i)->FindBase();
      }
   }
}
```

