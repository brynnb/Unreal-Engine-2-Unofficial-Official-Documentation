# Converting CAD data into Unreal

*Document Summary: A small guide to importing Autodesk/Discreet models into UnrealEd.**Document Changelog: Last updated by Michiel Hendriks, cleaning up. Last updated by Vito Miliano ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)), for document creation. Original author was Daniel Patton ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).*

* [Converting CAD data into Unreal](#converting-cad-data-into-unreal)
  + [Overview](#overview)
  + [Converting ...](#converting-)

## Overview

The purpose of this document is to assist you in the process of transferring 3D geometry created in one or more of the Autodesk/Discreet products into the Unreal engine:

* Autodesk Inventor 6
* Autodesk AutoCAD 2002
* Autodesk Architectural Desktop 3.3 (ADT)
* Autodesk 3D Studio VIZ R4

* Discreet 3D Studio MAX R4.26 & 5

To find this document useful, you should already be familiar with AutoCAD or one of the Autodesk "Vertical" products (such as Inventor or ADT) as well as have a basic understanding of 3D Studio MAX/VIZ. Whether or not you start by creating geometry in Inventor, AutoCAD or ADT, you will still need to translate the data through a modeling program (i.e. MAX or Maya) in order to import it into Unreal. This is primarily due to the fact that Unreal import geometry using the ASE file format and with the exception of MAX, most Autodesk products do not support exporting the ASE format directly.In the specific case of UT2003 or UnrealEngine2.5, Lightwave can also be used, as the game natively supports the LWO format as well, but this would require exporting the files from AutoCAD as a 3DS file before importing into Lightwave, and this format has some minor file name convention limitations.3D Studio MAX is the preferred application if you are coming from one of the Autodesk products as it can open the native DWG file format. It may be possible to use earlier versions of MAX, but most testing was done using 4.26 and 5.3D Studio VIZ does not export the required ASE file format, but it is a required tool when translating from ADT.And finally, even if you are not experienced with any of the Autodesk vertical products, you might still gain some valuable knowledge from the following information as a "MAX only" user.

## Converting ...

Here's a short guide of the steps to take to convert models from the various application.

* Inventor -> MAX, then [MAXtoUnreal](../../Uncategorized/MAXtoUnreal.md), then [Import Into UnrealEd](../Primitives/StaticMeshesTutorial.md#importing-a-static-mesh)

* AutoCAD 2002 -> MAX, then [MAXtoUnreal](../../Uncategorized/MAXtoUnreal.md), then [Import Into UnrealEd](../Primitives/StaticMeshesTutorial.md#importing-a-static-mesh)

* Architectural Desktop -> VIZ, then VIZ -> MAX, then [MAXtoUnreal](../../Uncategorized/MAXtoUnreal.md), then [Import Into UnrealEd](../Primitives/StaticMeshesTutorial.md#importing-a-static-mesh)

* VIZ -> MAX, then [MAXtoUnreal](../../Uncategorized/MAXtoUnreal.md), then [Import Into UnrealEd](../Primitives/StaticMeshesTutorial.md#importing-a-static-mesh)

* [MAXtoUnreal](../../Uncategorized/MAXtoUnreal.md), then [Import Into UnrealEd](../Primitives/StaticMeshesTutorial.md#importing-a-static-mesh)

