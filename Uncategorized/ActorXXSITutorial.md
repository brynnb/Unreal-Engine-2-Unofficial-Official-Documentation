# How to export animations using [ActorX](../Content Creation/Tools/ActorX.md) and XSI

*Document Summary: A tutorial showing how to export animations using [ActorX](../Content Creation/Tools/ActorX.md) with XSI.**Document Changelog: Created; maintained over time.*

* [How to export animations using ActorX and XSI](ActorXXSITutorial.md#How to export animations using _ActorX and XSI)
  + [Install the Plug-In](ActorXXSITutorial.md#Install the Plug-In)
  + [Usage](ActorXXSITutorial.md#Usage)
  + [Script interface](ActorXXSITutorial.md#Script interface)
  + [Downloads](ActorXXSITutorial.md#Downloads)

This document assumes that you have already created and rigged your skeletal actor or static mesh and are looking for a step-by-step tutorial on how to use the ActorX exporter to export your model and animations out of XSI and into Unreal. This also assumes that you have already read the ActorX documentation on the UDN site and understand how to use static meshes in the Unreal editor, and the relationship between .PSK files and .PSA files.

## Install the Plug-In

1. Download and unzip the ActorX addon for XSI onto your system. (Files are available on the [ActorX](../Content Creation/Tools/ActorX.md) topic.)
2. Launch XSI, choose File -> Add-On -> Install and point it to wherever you stored the '.addon' file.
3. Bring up the GUI by typing "ActorX()" (without quotes) into the script command line at the bottom of the screen, or into the Script Editor.

Version notes:

* 01/14/05 version 1.00 First Beta test version.
* 02/14/05 version 1.00e Fixed multi-UV export and GUI issues. First release candidate.
* 05/10/05 version 1.01 Fixed bug where multiple materials were ignored in .ASE exports.

## Usage

The functionality is almost exactly equivalent to that of the Maya exporter - see [ActorXMayaTutorial](ActorXMayaTutorial.md) - except that all windows can be conveniently accessed though tabs in the single GUI window activated by typing "ActorX()".

## Script interface

The ActorX exporter is fully scriptable in all available scripting languages that ship with SOFTIMAGE|XSI.
The following is a list of functions exposed by the exporter:ActorX()

* Opens up the ActorX UI panel.

ActorManager()

* Opens up the ActorX Actor Manager dialog.

ActorXAbout()

* Shows the ActorX About Box.

ActorXSaveMesh()

* Save the mesh with the current settings.

ActorXDigestAnimation()

* Digests the current animation using the current ActorX settings.

ActorXExportStaticMesh()

* Exports a static mesh using the currently set settings on the StaticMesh dialog.

ActorXSetValue( ParamName, NewValue )

* Sets a value in the ActorX UI. Here is a list of all supported parameter names:

ActorX Panel:

* outputfolder
* meshfilename
* animationfilename
* animationsequencename
* animationrange

ActorX Setup:

* persistentsettings
* persistentpaths
* allskintype
* alltextured
* allselected
* invert
* forcereferencepose
* tangentuvsplits
* bakesmoothinggroups
* cullunuseddummies
* exportanimatedscale
* fixrootnetmotion
* hardlock
* globalscalefactor
* nologfiles
* class
* base
* explicitsequencelist
* assumepcxtextures

ActorX StaticMesh Export:

* nopopups
* convertunderscores
* selectedonly
* geometrynameasfilename
* autotriangulate
* obeyhardedges
* consolidateoutputgeometry
* defaultpath

## Downloads

Here is a simple JScript files which creates a skeletal mesh, and exports it using commands as listed above.[XSI\_ExampleScripts.zip](../assets/xsi_examplescripts.zip)To run, please make sure XSI is configured to use JScript: go to File->Preferences and select Scripting in the properties tree (near the bottom) - then a "Script Language" selection drop box becomes available. Select "JScript Language" and close.
