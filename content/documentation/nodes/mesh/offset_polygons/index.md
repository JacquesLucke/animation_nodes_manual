---
title : Offset Polygons
weight : 70
---

## Description

This node offset the polygons of the input mesh based on one of two source:

- An input offset translation, rotation, and scale with an input falloff as a
  factor.
- A bounded action representing a transformation.

## Loc/Rot/Scale

In this offset source, the polygons are offset based on the input location,
rotation, and scale using the input falloff as a factor.

### Options

- **Location** - Enables location-based offset.
- **Rotation** - Enables rotation-based offset.
- **Scale** - Enables scale-based offset.

### Inputs

- **Mesh** - The input mesh.
- **Falloff** - A falloff to use as a factor.
- **Translation** - The offset translation vector.
- **Rotation** - The offset rotation euler.
- **Scale** - The offset scale vector.

## Action

In this offset source, the polygons are offset based on a bounded
transformation action. The action can be evaluated at a fixed frame or at
variable frames defined by a falloff. You can think of the offset action when
evaluated as the transformation of an animated empty.

### Fixed

In this mode of operation, the action is evaluated at a certain frame and the
polygons will be offset based on the transforms of the action at this frame.

#### Inputs

- **Mesh** - The input mesh.
- **Action** - A bounded transformation action.
- **Frame** - The frame to evaluate the action at.

### Falloff

In this mode of operation, the action is evaluated at the normalized frame
computed by evaluating the input falloff at the input polygons. By normalized
frame we mean relative to the bounds of the action, that is, a falloff value of
zero will evaluate the action at its very start and a falloff value of 1 will
evaluate the action at its very end. Then the input polygons will be offset
based on the transforms of the action after evaluation.

#### Inputs

- **Mesh** - The input mesh.
- **Action** - A bounded transformation action.
- **Falloff** - The normalized frame falloff.

## Outputs

- **Mesh** - The mesh.

## Advanced Node Settings

### Local Pivots

- *Default* - Use center as pivot and guess some tangent and bitangent.
- *Custom Points* - Provide custom pivots for every polygon. Tangent and
  bitangent are guessed.
- *Custom Matrices* - Provide a transformation matrix for each polygon that
  represent it. The rotation part of the matrices has to be orthogonal.

### Translation

- **Global Axis** - This option translate matrices in global space.
- **Local Axis** - This option translate matrices in local space, in
    other words, the translation vector is rotated based on the rotation
    of the transformation matrix before it get added.

### Rotations

- **Global Axis - Global Pivot** - This option rotate matrices in
    global space around the space's origin point. Use it when your
    matrix represent a vector.
- **Global Axis - Local Pivot** - This option rotate matrices in
    global space around their origin point. Use it when you matrix
    represent an object and you want to transform in around its origin.
- **Local Axis - Local Pivot** - This option rotate matrices in local
    space around their origin point. Use it when you matrix represent an
    object and you want to transform in around its origin.

### Scale

- **Local Axis** - This option scale matrices in their local space.
    Use this option if your matrices represent objects and you want to
    scale them without changing their position.
- **Global Axis** - This option scale matrices in global space. Use
    this option if your matrices represent objects and you want to scale
    them without changing their position.
- **Include Translation** - This option scale matrices in global
    space. Use this option if you want to scale them while changing
    their position.
- **Translation Only** - This option scale matrices in global space.
    Use this option if you want only location to change.
