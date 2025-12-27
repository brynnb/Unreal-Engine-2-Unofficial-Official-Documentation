# Runtime SVehicles

*Created by Chris Linder (DemiurgeStudios?) on 11-12-03 for the Unreal Runtime version 2226.19.03. Last Updated by Khaled Shariff (ProjectWhitecardInc?.).*

* [Runtime SVehicles](RuntimeSVehicles.md#runtime-svehicles)
  + [Related Documents](RuntimeSVehicles.md#related-documents)
  + [Introduction](RuntimeSVehicles.md#introduction)
  + [Installing SVehicle Support.](RuntimeSVehicles.md#installing-svehicle-support)
  + [Compiling new SVehicles](RuntimeSVehicles.md#compiling-new-svehicles)
  + [Recompiling - Additional Note - If running into compilation error.](RuntimeSVehicles.md#recompiling---additional-note---if-running-into-compilation-error)

## Related Documents

[SimpleSVehicleExamples](../Content%20Creation/Physics/SimpleSVehicleExamples.md),
[SVehicleCreation](SVehicleCreation.md),
[SVehicleReference](SVehicleReference.md), [SCarReference](SCarReference.md), [SCopterReference](SCopterReference.md), [HelicopterTutorial](HelicopterTutorial.md)

## Introduction

SVehicles are the most commonly used type of vehicle in the Unreal engine. SVehicles (SVehicle stands for Skeletal Vehicle) are made of skeletal meshes as opposed to static meshes. Because the meshes have skeletons, SVehicles can include things like tires and moving gun turrets in the single mesh for the vehicle.This document guides you through the process of adding vehicle support to the Unreal Runtime. Specifically this document contains a [zip file](../assets/[runtimesvehiclesupport.zip](../assets/runtimesvehiclesupport.zip)) that you can drop in the Runtime which adds the nessisary \*.u file and DLL for SVehicles to work. The zip also contains the base UnrealScript classes that one would extend to make new SVehicles. This document does not contain any example vehicles or anything you can test or play with right out of the box. See the [SimpleSVehicleExamples](../Content%20Creation/Physics/SimpleSVehicleExamples.md) document for examples the can be dropped right into the Runtime.

## Installing SVehicle Support.

Note: The zip attached to this document is designed for the Unreal Runtime version 2226.19.03. If you have a different version of the Runtime, the SVehicle Support may not work. To check the version of the Runtime open *Manifest.ini* in the System sub-directory in your Runtime directory and search for the text `"Version="`.Download the [[runtimesvehiclesupport.zip](../assets/runtimesvehiclesupport.zip)](../assets/[runtimesvehiclesupport.zip](../assets/runtimesvehiclesupport.zip)) file and extract its contents into your Unreal Runtime directory. That is it.

## Compiling new SVehicles

As mentioned above, the the [[runtimesvehiclesupport.zip](../assets/runtimesvehiclesupport.zip)](../assets/[runtimesvehiclesupport.zip](../assets/runtimesvehiclesupport.zip)) also contains the UnrealScript classes that one would extend to make new SVehicles. To make a new SVehicle the given classes should be extended, not modified. For examples of new SVehicles see the [SimpleSVehicleExamples](../Content%20Creation/Physics/SimpleSVehicleExamples.md) document which includes UnrealScript source for the new vehicles.New SVehicles must go in their own package because *Vehicles* is a native package and can not be recompiled. Once you have created a new SVehicle in UnrealScript, you will need to compile it. First you need to make sure that `"Vehicles"` is added to your *EditPackages* lists in *UE2Runtime.ini*. Next make sure that your new vehicle package (`"ExampleVehicles"` in [SimpleSVehicleExamples](../Content%20Creation/Physics/SimpleSVehicleExamples.md)) is added to the *EditPackages* lists in *UE2Runtime.ini*. Now delete the existing *ExampleVehicles.u* file in your system directory and then run `"ucc make"` from the command line in your system directory. This will compile a new *ExampleVehicles.u* file which will enable you to use your new vehicles.

## Recompiling - Additional Note - If running into compilation error.

Follow all the above.
If you are going to use the latest example vehicles, before you can create your own vehicles you will run into a problem recompiling with or without your own classes.
For example "superclass SHalfTrack not found" . This is because it seems that Vehicles.u as given when you install vehicle support is missing classes. This is a problem. You need to create an updated Vehicles class, and you are going to need headers. So:Temporarily remove `"ExampleVehicles"` from the *EditPackages* lists in *UE2Runtime.ini* ( if you have already added it) , and then create a stub file at UnrealEngine2Runtime/Vehicles/Inc/VehiclesClasses.h. It can be empty.
DELETE Vehicles.u from the System directory.
Once Vehicles is added to *EditPackages* lists in *UE2Runtime.ini* , run `"ucc make"` from the command line in your system directory (it will compile *Vehicles* ; it will create Vehicles.u and say YES to overwrite the Inc/VehiclesClasses.h (when the cmd line queries say "Y" ).
You may now compile your own vehicles. This header file has been attached to this page.
