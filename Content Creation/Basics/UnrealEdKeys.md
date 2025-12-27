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
    - [Polygon (Face) Dragging Mode](#polygon-face) Dragging Mode)
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
| m.gif y.gif | Zoom In/Out |
| l.gif x.gif | Move Left/Right (horizontal) |
| r.gif y.gif | Move Up/Down (vertical) |

If non-orthographic viewport (3D view)

|  |  |
| --- | --- |
| l.gif x.gif | Move along X axis |
| r.gif x.gif | Move along Y axis |
| l.gif r.gif y.gif | Move along Z axis |

### Free Movement

If orthographic viewport (XY,YZ,XZ views)

|  |  |
| --- | --- |
| l.gif xy.gif | Move left/right and up/down |
| l.gif r.gif y.gif | Zoom in/out |
| r.gif x.gif | Rotate in plane of current viewpoint |

If non-orthographic viewport (3D view)

|  |  |
| --- | --- |
| l.gif xy.gif | Yaw and Move forwards/backwards and yaw |
| l.gif r.gif xy.gif | Move left/right and up/down |
| r.gif xy.gif | Yaw and Pitch |

### Axial Rotation

|  |  |
| --- | --- |
| l.gif x.gif | Pitch |
| r.gif x.gif | Yaw |
| l.gif r.gif y.gif | Roll |

## Clicking on...

### the backdrop

|  |  |
| --- | --- |
| ctrl.gif m.gif | Center Camera at Clicked Point |
| A l.gif | Add Current Actor |
| L l.gif | Add Light |
| ![r.gif](../../assets/r.gif) | Context Menu |
| No- ctrl.gif l.gif | Select None |
| ctrl.gif r.gif | Add Clip Marker |
| shift.gif alt.gif m.gif | Dragging the mouse extends a ruler that will give you the distance between any two points |

### a surface/polygon in the 3D view

|  |  |
| --- | --- |
| shift.gif ctrl.gif l.gif | Select Brush associated with surface |
| shift.gif l.gif | Apply current texture to surface |
| alt.gif r.gif | Grab texture from surface |
| alt.gif l.gif | Apply current texture to surface |
| alt.gif ctrl.gif l.gif | Apply current texture and texture coordinates (from last grabbed surface) to surface |

### an actor

|  |  |
| --- | --- |
| ctrl.gif r.gif | Add Clip Marker |
| ctrl.gif l.gif | Toggle selection of Actor |
| ![l.gif](../../assets/l.gif) | Select this |
| ![r.gif](../../assets/r.gif) | Context Menu |
| l.gif l.gif | Properties Window |

### the vertex of a brush

|  |  |
| --- | --- |
| ctrl.gif r.gif | Add Clip Marker |
| ![r.gif](../../assets/r.gif) | Set vertex as pivot |

## Render Options

### Render Modes

|  |  |
| --- | --- |
| alt.gif 1 | RMODE 1 (Wireframe) |
| alt.gif 2 | RMODE 2 (Zones and zone portals) |
| alt.gif 3 | RMODE 3 (Flat-shaded) |
| alt.gif 4 | RMODE 4 (Flad-shaded with normals) |
| alt.gif 5 | RMODE 5 (Illuminated texture mapping) |
| alt.gif 6 | RMODE 6 (Plain texture mapping) |
| alt.gif 7 | RMODE 13 (XY view) |
| alt.gif 8 | RMODE 14 (YZ view) |
| alt.gif 9 | RMODE 15 (YZ view) |

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
| ctrl.gif A | Add Brush |
| ctrl.gif D | Deintersect Brush |
| ctrl.gif I | Intersect Brush |
| ctrl.gif S | Subtract Brush |

## Actor Manipulation

|  |  |
| --- | --- |
| shift.gif A | Select All Actors |
| alt.gif ctrl.gif l.gif xy.gif | Add selected actors (supports shift.gif for multiple-selection) |
| Delete | Delete Selected Actors |
| F4 | View Actor Properties |
| F5 | View Surface Properties |
| F6 | View Level Properties |
| F7 | Compile Changed Scripts |

## The Usual

### File

|  |  |
| --- | --- |
| ctrl.gif O | Open |
| ctrl.gif L | Save |
| ctrl.gif E | Save As... |
| ctrl.gif P | Play Level |

### Edit

|  |  |
| --- | --- |
| ctrl.gif X | Cut |
| ctrl.gif C | Copy |
| ctrl.gif V | Paste |
| shift.gif D   ctrl.gif W | Duplicate (important when using Static Meshes/Hardware Brushes) |
| ctrl.gif Y | Redo |
| ctrl.gif Z | Undo |

### Find/Replace

|  |  |
| --- | --- |
| ctrl.gif F | Find |
| ctrl.gif H | Replace |

## Polygon Selection

### Select Adjacent...

|  |  |
| --- | --- |
| shift.gif J | Select All Adjacent Polys |
| shift.gif C | Select Adjacent Coplanar Polys |
| shift.gif F | Select Adjacent Floor Polys |
| shift.gif Y | Select Adjacent Polys With Slanted Slope |
| shift.gif W | Select Adjacent Walls |

### Complex Selection Modes

|  |  |
| --- | --- |
| shift.gif G | Select Matching Group Polys |
| shift.gif B | Select All Polygons on Brushes which have a polygon currently selected |
| shift.gif I | Select Polys on Brush with Same ItemNames |

### Memorization

|  |  |
| --- | --- |
| shift.gif M | Memorize Selected Polys |
| shift.gif R | Select Memorized Polys |
| shift.gif O | Select Memorized Polys and Currently Selected Polys (Selected OR Memorized) |
| shift.gif U | Select Memorized Selected Polys (Selected AND Memorized) |
| shift.gif X | Select Memorized Non-Selected Polys and Non-Memorized Selected Polys (Selected XOR Memorized) |

### Miscellaneous

|  |  |
| --- | --- |
| shift.gif S | Select All Surfaces in Level |
| shift.gif Q | Select Unselected Polys on Brush (Brush MINUS Selected) |
| shift.gif T | Select Matching-Texture Polys |
| shift.gif N | Select None |

## Editing Modes

*(choose a mode by selecting an icon on the upper portion of the left toolbar)*

### Brush Clipping Mode

|  |  |
| --- | --- |
| ![r.gif](../../assets/r.gif) | Add vertex (up to three) |

### Vertex Editing Mode

|  |  |
| --- | --- |
| l.gif xy.gif | Regular Camera Movement |
| ctrl.gif l.gif xy.gif | Move vertices |
| alt.gif ctrl.gif l.gif xy.gif | Add selected vertices (supports shift.gif for multiple-selection) |
| ![l.gif](../../assets/l.gif) | Add vertex to selection |

### Polygon (Face) Dragging Mode

|  |  |
| --- | --- |
| l.gif xy.gif | Regular Camera Movement |
| ctrl.gif l.gif xy.gif | Move faces |
| ![l.gif](../../assets/l.gif) | Add polgyons visible to point clicked (as if it is on the 0 plane) |

### Brush Rotate Mode

|  |  |
| --- | --- |
| l.gif xy.gif | Regular Camera Movement |
| ctrl.gif l.gif xy.gif | Axial Rotation |

### Brush Scale Mode

|  |  |
| --- | --- |
| l.gif xy.gif | Regular Camera Movement |
| ctrl.gif l.gif xy.gif | Snap to grid |
| ctrl.gif l.gif xy.gif | Scaling on Brush in Given Direction |

*(Deprecated? Broken?)*

|  |  |
| --- | --- |
| alt.gif ctrl.gif l.gif xy.gif | Scaling on Each Brush, Retaining Relative Positioning |

### Freehand Polygon Drawing Tool

|  |  |
| --- | --- |
| ![r.gif](../../assets/r.gif) | Add vertex to list |
| l.gif xy.gif | Regular Camera Movement |
| ![r.gif](../../assets/r.gif) | Options which allow one to "Create Brush" |

### Texture Panning Mode

|  |  |
| --- | --- |
| l.gif xy.gif | Regular Camera Movement |
| ctrl.gif l.gif r.gif y.gif | Uniform Texture Scaling |
| ctrl.gif l.gif x.gif | U Panning |
| ctrl.gif r.gif y.gif | V Panning |

### Texture Rotate Mode

|  |  |
| --- | --- |
| l.gif xy.gif | Regular Camera Movement |
| ctrl.gif l.gif xy.gif | Rotate Textures on Selected Faces |

### Terrain Editing Mode

*(rough and unfinished. changes expected)*

|  |  |
| --- | --- |
| l.gif xy.gif | Regular Camera Movement |
| ctrl.gif l.gif r.gif y.gif | Raise/Lower Terrain Vertices |
| ![l.gif](../../assets/l.gif) | Select Vertex |
| shift.gif l.gif | Select Additional Vertex |

### Regular Viewport Mode

|  |  |
| --- | --- |
| alt.gif ctrl.gif l.gif xy.gif | Add selected vertices (supports shift.gif for multiple-selection) |
| ![l.gif](../../assets/l.gif) | Select brush, or Select vertex on brush |
| alt.gif l.gif xy.gif | Move selected vertices |
| l.gif xy.gif | Move |
| l.gif xy.gif | Move Actors |
| ctrl.gif l.gif x.gif alt.gif r.gif y.gif shift.gif Delete | Eliminate all BSP errors |

## UnrealEd Bugs (found while creating the above document)

![ctrl.gif](../../assets/ctrl.gif)

N assigned to both "New" and "Intersect"

![shift.gif](../../assets/shift.gif)

S assigned to both "Select all surfaces" and "select adj. slants""Select None" mislabelled as

![shift.gif](../../assets/shift.gif)

Z, should be

![shift.gif](../../assets/shift.gif)

N"Select Adj. Slanted" should be

![shift.gif](../../assets/shift.gif)

Y, not

![shift.gif](../../assets/shift.gif)

S"Intersect" should be

![ctrl.gif](../../assets/ctrl.gif)

I, not

![ctrl.gif](../../assets/ctrl.gif)

N"Save As" should have "Ctrl-E" listed in the menu

