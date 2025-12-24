# Exporting Static Meshes from Maya

*Document Summary: How to set up and export static meshes using Maya and the [ActorX](ActorX.md) plugin.**Document Changelog: Created and maintained by Erik de Neve?.*

* [Exporting Static Meshes from Maya](#exporting-static-meshes-from-maya)
  + [Overview](#overview)
  + [Maya plugin commands for static mesh export](#maya-plugin-commands-for-static-mesh-export)
  + [Troubleshooting](#troubleshooting)

## Overview

The pipeline for creating static, textured geometry for levels or objects in Unreal engine games involves creating the meshes in a 3rd party modeling tool like 3DS Max or Maya, and exporting them to the .ASE file format. Max can export these natively, and for Maya users there is special functionality in the [ActorX](ActorX.md) exporter plugin.

## Maya plugin commands for static mesh export

Activate the static mesh exporter by typing `axmesh` at the command prompt. The window that pops up is largely self-explanatory.Maya-style 'hard edges' are automatically converted to smoothing groups in the ASE file, and you can export your mesh with multiple simplified-collision-geometry primitives just like with 3DS Max, by using the MCD\*\*\_name naming convention as documented in e.g. the [CollisionTutorial](../Physics/CollisionTutorial.md).For any single mesh object in the scene, vertex colors and multiple UV channel mapping data are automatically exported whenever they have been applied to them. For details on using shaders with vertex coloring(alpha) and multiple UV channels, consult the [VertexBlendingTutorial](../Techniques/VertexBlendingTutorial.md).

## Troubleshooting

If UnrealEd? shows error messages or corrupted UVs after reading a Maya exported ASE file, specifically one with multi-UV and/or vertex colors on a subset of meshes in a multi-mesh scene, consider consolidating your mesh into a single piece before exporting.Update 9/15/04: Using version 2.35 or later of [ActorX](ActorX.md) for Maya, you can avoid most UV/normals/vertexcolor issues by using the optional "consolidate" option whenever your scene contains multiple geometry objects to export.

