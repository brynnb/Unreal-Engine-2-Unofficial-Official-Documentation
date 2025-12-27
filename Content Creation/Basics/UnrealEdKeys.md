# UnrealEd Key Combinations Cheat Sheet

*Document Summary: A reference for all of the keyboard shortcuts for Unreal Ed.**Document Changelog: Last updated by Jason Lentz (DemiurgeStudios?), to update for the 2110 build. Original author was Mike Lambert ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).*

* [UnrealEd Key Combinations Cheat Sheet](#unrealed-key-combinations-cheat-sheet)
  + [Movement](#movement)
    - [Movement Usage](#movement-usage)
    - [Axial Movement](#axial-movement)
    - [Free Movement](#free-movement)
    - [Axial Rotation](#axial-rotation)
  + [Clicking on...](#clicking-on)
    - [the backdrop](#the-backdrop)
    - [a surface/polygon in the 3D view](#a-surfacepolygon-in-the-3d-view)
    - [an actor](#an-actor)
    - [the vertex of a brush](#the-vertex-of-a-brush)
  + [Render Options](#render-options)
    - [Render Modes](#render-modes)
    - [Toggle Rendering](#toggle-rendering)
  + [Brush Manipulation](#brush-manipulation)
  + [Actor Manipulation](#actor-manipulation)
  + [The Usual](#the-usual)
    - [File](#file)
    - [Edit](#edit)
    - [Find/Replace](#findreplace)
  + [Polygon Selection](#polygon-selection)
    - [Select Adjacent...](#select-adjacent)
    - [Complex Selection Modes](#complex-selection-modes)
    - [Memorization](#memorization)
    - [Miscellaneous](#miscellaneous)
  + [Editing Modes](#editing-modes)
    - [Brush Clipping Mode](#brush-clipping-mode)
    - [Vertex Editing Mode](#vertex-editing-mode)
    - [Polygon (Face) Dragging Mode](#polygon-face-dragging-mode) Dragging Mode)
    - [Brush Rotate Mode](#brush-rotate-mode)
    - [Brush Scale Mode](#brush-scale-mode)
    - [Freehand Polygon Drawing Tool](#freehand-polygon-drawing-tool)
    - [Texture Panning Mode](#texture-panning-mode)
    - [Texture Rotate Mode](#texture-rotate-mode)
    - [Terrain Editing Mode](#terrain-editing-mode)
    - [Regular Viewport Mode](#regular-viewport-mode)
  + [UnrealEd Bugs (found while creating the above document)](#unrealed-bugs-found-while-creating-the-above-document))

One can find the below key shortcuts in the following files, since this file will become out of date as new features are added:

* UnEdCam's UEditorEngine::Key
* UnEdCam's UEditorEngine:: MouseDelta
* UnEdCam's CalcFreeMoveRot and CalcAxialMoveRot
* UnEdClick's HBackdrop::Click and FEditorHitObserver::Click

## Movement

There are two 'modes' for mouse movement.

### Movement Usage

Free movement is used for:

* moving the camera
* moving actors in an orthographic view
* face dragging
* vertex dragging

Axial movement is used for:

* moving actors in an non-orthographic view
* scaling brushes
* snapping brushes

Axial rotation is used for:

* brush rotation

### Axial Movement

If orthographic viewport (XY,YZ,XZ views)

|  |  |
| --- | --- |
| ![m.gif](../../assets/m.gif) ![y.gif](../../assets/y.gif) | Zoom In/Out |
| ![l.gif](../../assets/l.gif) ![x.gif](../../assets/x.gif) | Move Left/Right (horizontal) |
| ![r.gif](../../assets/r.gif) ![y.gif](../../assets/y.gif) | Move Up/Down (vertical) |

If non-orthographic viewport (3D view)

|  |  |
| --- | --- |
| ![l.gif](../../assets/l.gif) ![x.gif](../../assets/x.gif) | Move along X axis |
| ![r.gif](../../assets/r.gif) ![x.gif](../../assets/x.gif) | Move along Y axis |
| ![l.gif](../../assets/l.gif) ![r.gif](../../assets/r.gif) ![y.gif](../../assets/y.gif) | Move along Z axis |

### Free Movement

If orthographic viewport (XY,YZ,XZ views)

|  |  |
| --- | --- |
| ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Move left/right and up/down |
| ![l.gif](../../assets/l.gif) ![r.gif](../../assets/r.gif) ![y.gif](../../assets/y.gif) | Zoom in/out |
| ![r.gif](../../assets/r.gif) ![x.gif](../../assets/x.gif) | Rotate in plane of current viewpoint |

If non-orthographic viewport (3D view)

|  |  |
| --- | --- |
| ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Yaw and Move forwards/backwards and yaw |
| ![l.gif](../../assets/l.gif) ![r.gif](../../assets/r.gif) ![xy.gif](../../assets/xy.gif) | Move left/right and up/down |
| ![r.gif](../../assets/r.gif) ![xy.gif](../../assets/xy.gif) | Yaw and Pitch |

### Axial Rotation

|  |  |
| --- | --- |
| ![l.gif](../../assets/l.gif) ![x.gif](../../assets/x.gif) | Pitch |
| ![r.gif](../../assets/r.gif) ![x.gif](../../assets/x.gif) | Yaw |
| ![l.gif](../../assets/l.gif) ![r.gif](../../assets/r.gif) ![y.gif](../../assets/y.gif) | Roll |

## Clicking on...

### the backdrop

|  |  |
| --- | --- |
| ![ctrl.gif](../../assets/ctrl.gif) ![m.gif](../../assets/m.gif) | Center Camera at Clicked Point |
| A ![l.gif](../../assets/l.gif) | Add Current Actor |
| L ![l.gif](../../assets/l.gif) | Add Light |
| ![r.gif](../../assets/![r.gif](../../assets/r.gif)) | Context Menu |
| No- ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) | Select None |
| ![ctrl.gif](../../assets/ctrl.gif) ![r.gif](../../assets/r.gif) | Add Clip Marker |
| ![shift.gif](../../assets/shift.gif) ![alt.gif](../../assets/alt.gif) ![m.gif](../../assets/m.gif) | Dragging the mouse extends a ruler that will give you the distance between any two points |

### a surface/polygon in the 3D view

|  |  |
| --- | --- |
| ![shift.gif](../../assets/shift.gif) ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) | Select Brush associated with surface |
| ![shift.gif](../../assets/shift.gif) ![l.gif](../../assets/l.gif) | Apply current texture to surface |
| ![alt.gif](../../assets/alt.gif) ![r.gif](../../assets/r.gif) | Grab texture from surface |
| ![alt.gif](../../assets/alt.gif) ![l.gif](../../assets/l.gif) | Apply current texture to surface |
| ![alt.gif](../../assets/alt.gif) ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) | Apply current texture and texture coordinates (from last grabbed surface) to surface |

### an actor

|  |  |
| --- | --- |
| ![ctrl.gif](../../assets/ctrl.gif) ![r.gif](../../assets/r.gif) | Add Clip Marker |
| ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) | Toggle selection of Actor |
| ![l.gif](../../assets/![l.gif](../../assets/l.gif)) | Select this |
| ![r.gif](../../assets/![r.gif](../../assets/r.gif)) | Context Menu |
| ![l.gif](../../assets/l.gif) ![l.gif](../../assets/l.gif) | Properties Window |

### the vertex of a brush

|  |  |
| --- | --- |
| ![ctrl.gif](../../assets/ctrl.gif) ![r.gif](../../assets/r.gif) | Add Clip Marker |
| ![r.gif](../../assets/![r.gif](../../assets/r.gif)) | Set vertex as pivot |

## Render Options

### Render Modes

|  |  |
| --- | --- |
| ![alt.gif](../../assets/alt.gif) 1 | RMODE 1 (Wireframe) |
| ![alt.gif](../../assets/alt.gif) 2 | RMODE 2 (Zones and zone portals) |
| ![alt.gif](../../assets/alt.gif) 3 | RMODE 3 (Flat-shaded) |
| ![alt.gif](../../assets/alt.gif) 4 | RMODE 4 (Flad-shaded with normals) |
| ![alt.gif](../../assets/alt.gif) 5 | RMODE 5 (Illuminated texture mapping) |
| ![alt.gif](../../assets/alt.gif) 6 | RMODE 6 (Plain texture mapping) |
| ![alt.gif](../../assets/alt.gif) 7 | RMODE 13 (XY view) |
| ![alt.gif](../../assets/alt.gif) 8 | RMODE 14 (YZ view) |
| ![alt.gif](../../assets/alt.gif) 9 | RMODE 15 (YZ view) |

### Toggle Rendering

|  |  |
| --- | --- |
| B | Toggle Show-Brushes |
| H | Toggle Show-Actors |
| K | Toggle Show-Backdrop |
| P | Toggle Show-Player-Control (Realtime Preview) |
| W | Toggle Show-Hardware-Brushes |

## Brush Manipulation

|  |  |
| --- | --- |
| ![ctrl.gif](../../assets/ctrl.gif) A | Add Brush |
| ![ctrl.gif](../../assets/ctrl.gif) D | Deintersect Brush |
| ![ctrl.gif](../../assets/ctrl.gif) I | Intersect Brush |
| ![ctrl.gif](../../assets/ctrl.gif) S | Subtract Brush |

## Actor Manipulation

|  |  |
| --- | --- |
| ![shift.gif](../../assets/shift.gif) A | Select All Actors |
| ![alt.gif](../../assets/alt.gif) ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Add selected actors (supports shift.gif for multiple-selection) |
| Delete | Delete Selected Actors |
| F4 | View Actor Properties |
| F5 | View Surface Properties |
| F6 | View Level Properties |
| F7 | Compile Changed Scripts |

## The Usual

### File

|  |  |
| --- | --- |
| ![ctrl.gif](../../assets/ctrl.gif) O | Open |
| ![ctrl.gif](../../assets/ctrl.gif) L | Save |
| ![ctrl.gif](../../assets/ctrl.gif) E | Save As... |
| ![ctrl.gif](../../assets/ctrl.gif) P | Play Level |

### Edit

|  |  |
| --- | --- |
| ![ctrl.gif](../../assets/ctrl.gif) X | Cut |
| ![ctrl.gif](../../assets/ctrl.gif) C | Copy |
| ![ctrl.gif](../../assets/ctrl.gif) V | Paste |
| ![shift.gif](../../assets/shift.gif) D   ![ctrl.gif](../../assets/ctrl.gif) W | Duplicate (important when using Static Meshes/Hardware Brushes) |
| ![ctrl.gif](../../assets/ctrl.gif) Y | Redo |
| ![ctrl.gif](../../assets/ctrl.gif) Z | Undo |

### Find/Replace

|  |  |
| --- | --- |
| ![ctrl.gif](../../assets/ctrl.gif) F | Find |
| ![ctrl.gif](../../assets/ctrl.gif) H | Replace |

## Polygon Selection

### Select Adjacent...

|  |  |
| --- | --- |
| ![shift.gif](../../assets/shift.gif) J | Select All Adjacent Polys |
| ![shift.gif](../../assets/shift.gif) C | Select Adjacent Coplanar Polys |
| ![shift.gif](../../assets/shift.gif) F | Select Adjacent Floor Polys |
| ![shift.gif](../../assets/shift.gif) Y | Select Adjacent Polys With Slanted Slope |
| ![shift.gif](../../assets/shift.gif) W | Select Adjacent Walls |

### Complex Selection Modes

|  |  |
| --- | --- |
| ![shift.gif](../../assets/shift.gif) G | Select Matching Group Polys |
| ![shift.gif](../../assets/shift.gif) B | Select All Polygons on Brushes which have a polygon currently selected |
| ![shift.gif](../../assets/shift.gif) I | Select Polys on Brush with Same ItemNames |

### Memorization

|  |  |
| --- | --- |
| ![shift.gif](../../assets/shift.gif) M | Memorize Selected Polys |
| ![shift.gif](../../assets/shift.gif) R | Select Memorized Polys |
| ![shift.gif](../../assets/shift.gif) O | Select Memorized Polys and Currently Selected Polys (Selected OR Memorized) |
| ![shift.gif](../../assets/shift.gif) U | Select Memorized Selected Polys (Selected AND Memorized) |
| ![shift.gif](../../assets/shift.gif) X | Select Memorized Non-Selected Polys and Non-Memorized Selected Polys (Selected XOR Memorized) |

### Miscellaneous

|  |  |
| --- | --- |
| ![shift.gif](../../assets/shift.gif) S | Select All Surfaces in Level |
| ![shift.gif](../../assets/shift.gif) Q | Select Unselected Polys on Brush (Brush MINUS Selected) |
| ![shift.gif](../../assets/shift.gif) T | Select Matching-Texture Polys |
| ![shift.gif](../../assets/shift.gif) N | Select None |

## Editing Modes

*(choose a mode by selecting an icon on the upper portion of the left toolbar)*

### Brush Clipping Mode

|  |  |
| --- | --- |
| ![r.gif](../../assets/![r.gif](../../assets/r.gif)) | Add vertex (up to three) |

### Vertex Editing Mode

|  |  |
| --- | --- |
| ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Regular Camera Movement |
| ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Move vertices |
| ![alt.gif](../../assets/alt.gif) ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Add selected vertices (supports shift.gif for multiple-selection) |
| ![l.gif](../../assets/![l.gif](../../assets/l.gif)) | Add vertex to selection |

### Polygon (Face) Dragging Mode

|  |  |
| --- | --- |
| ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Regular Camera Movement |
| ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Move faces |
| ![l.gif](../../assets/![l.gif](../../assets/l.gif)) | Add polgyons visible to point clicked (as if it is on the 0 plane) |

### Brush Rotate Mode

|  |  |
| --- | --- |
| ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Regular Camera Movement |
| ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Axial Rotation |

### Brush Scale Mode

|  |  |
| --- | --- |
| ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Regular Camera Movement |
| ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Snap to grid |
| ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Scaling on Brush in Given Direction |

*(Deprecated? Broken?)*

|  |  |
| --- | --- |
| ![alt.gif](../../assets/alt.gif) ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Scaling on Each Brush, Retaining Relative Positioning |

### Freehand Polygon Drawing Tool

|  |  |
| --- | --- |
| ![r.gif](../../assets/![r.gif](../../assets/r.gif)) | Add vertex to list |
| ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Regular Camera Movement |
| ![r.gif](../../assets/![r.gif](../../assets/r.gif)) | Options which allow one to "Create Brush" |

### Texture Panning Mode

|  |  |
| --- | --- |
| ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Regular Camera Movement |
| ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![r.gif](../../assets/r.gif) ![y.gif](../../assets/y.gif) | Uniform Texture Scaling |
| ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![x.gif](../../assets/x.gif) | U Panning |
| ![ctrl.gif](../../assets/ctrl.gif) ![r.gif](../../assets/r.gif) ![y.gif](../../assets/y.gif) | V Panning |

### Texture Rotate Mode

|  |  |
| --- | --- |
| ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Regular Camera Movement |
| ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Rotate Textures on Selected Faces |

### Terrain Editing Mode

*(rough and unfinished. changes expected)*

|  |  |
| --- | --- |
| ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Regular Camera Movement |
| ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![r.gif](../../assets/r.gif) ![y.gif](../../assets/y.gif) | Raise/Lower Terrain Vertices |
| ![l.gif](../../assets/![l.gif](../../assets/l.gif)) | Select Vertex |
| ![shift.gif](../../assets/shift.gif) ![l.gif](../../assets/l.gif) | Select Additional Vertex |

### Regular Viewport Mode

|  |  |
| --- | --- |
| ![alt.gif](../../assets/alt.gif) ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Add selected vertices (supports shift.gif for multiple-selection) |
| ![l.gif](../../assets/![l.gif](../../assets/l.gif)) | Select brush, or Select vertex on brush |
| ![alt.gif](../../assets/alt.gif) ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Move selected vertices |
| ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Move |
| ![l.gif](../../assets/l.gif) ![xy.gif](../../assets/xy.gif) | Move Actors |
| ![ctrl.gif](../../assets/ctrl.gif) ![l.gif](../../assets/l.gif) ![x.gif](../../assets/x.gif) ![alt.gif](../../assets/alt.gif) ![r.gif](../../assets/r.gif) ![y.gif](../../assets/y.gif) ![shift.gif](../../assets/shift.gif) Delete | Eliminate all BSP errors |

## UnrealEd Bugs (found while creating the above document)

![ctrl.gif](../../assets/![ctrl.gif](../../assets/ctrl.gif))

N assigned to both "New" and "Intersect"

![shift.gif](../../assets/![shift.gif](../../assets/shift.gif))

S assigned to both "Select all surfaces" and "select adj. slants""Select None" mislabelled as

![shift.gif](../../assets/![shift.gif](../../assets/shift.gif))

Z, should be

![shift.gif](../../assets/![shift.gif](../../assets/shift.gif))

N"Select Adj. Slanted" should be

![shift.gif](../../assets/![shift.gif](../../assets/shift.gif))

Y, not

![shift.gif](../../assets/![shift.gif](../../assets/shift.gif))

S"Intersect" should be

![ctrl.gif](../../assets/![ctrl.gif](../../assets/ctrl.gif))

I, not

![ctrl.gif](../../assets/![ctrl.gif](../../assets/ctrl.gif))

N"Save As" should have "Ctrl-E" listed in the menu

