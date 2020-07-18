---
title : Offset Polygons
weight : 70
---

## Description

This node offset *location, rotation* and *scale* the polygons of a mesh.

## Options

- **Transformation Source** -
    - *Loc/Rot/Scale* - This option allows to offset the location, rotation and scale of the polygons.
        - *Loc* - Enabling this option will offset the location of polygons.
        - *Rot* - Enabling this option will offset the rotation of polygons.
        - *Scale* - Enabling this option will offset the scale of polygons.
    - *Action* - This option allows to offset *(loc, rot and scale)* the polygons based on the action.
        - *Evaluation Time Mode* -
            - *Fixed* - Evaluate all actions at the same frame.
            - *Falloff* - Use falloff to determine the frame to evaluate (only works with bounded actions).

## Inputs

- **Mesh** - The mesh.
- **Translation** - A vector or a vector list to offset the location of the polygons of the input mesh.
- **Rotation** - An euler or an euler list to offset the rotation of the polygons of the input mesh.
- **Scale** - A vector or a vector list to offset the scale of the polygons of the input mesh.
- **Action** - An action to offset the polygons of the input mesh.
- **Falloff** - A falloff to controls the offset of the polygons of the input mesh.

## Outputs

- **Mesh** - The mesh.

## Advanced Node Settings

- **Local Pivots** - Determines the pivot and rotation axis for each polygon.
    - *Default* - Use center as pivot and guess some tangent and bitangent.
    - *Custom Points* - Provide custom pivots for every polygon. Tangent and bitangent are guessed.
    - *Custom Matrices* - Provide a transformation matrix for each polygon that represent it. The rotation part of the matrices has to be orthogonal.

- **Translation** -
    - *Local Axis* - Translation of polygon along the local axis of polygon.
    - *Global Axis* - Translation of polygon along the global axis.
- **Rotation** -
    - *Local Axis - Local Pivot* - Rotation about the local axis at the local pivot of the polygon.
    - *Global Axis - Local Pivot* - Rotation about the global axis at the local pivot of the polygon.
    - *Global Axis - Global Pivot* - Rotation about the global axis at the global pivot of the polygon.
- **Scale** -
    - *Local Axis* - Scale the polygon along the local axis of the polygon.
    - *Global Axis* - Scale the polygon along the global axis of the polygon.
    - *Include Translation* - Scale the polygon as well as the translation.
    - *Translation Only* - Only scale the translation of the polygon.
