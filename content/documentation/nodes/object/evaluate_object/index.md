---
title : Evaluate Object
---

## Description

This node forces an update to the scene. Blender doesn't update the scene data
immediately after changes to the scene, this node forces Blender to update the
scene at the point of invocation. For instance, if a node tree adds a modifier
to an object then tries to read the mesh with modifiers applied, the mesh will
be returned without the modifier because Blender haven't updated the scene yet.
This node can force an update after adding the modifier to get the mesh with the
modifier applied.

Using this node is highly discouraged and might have unintended consequences.
Avoid using it when you can.

## Inputs

- **Object** - The input object.

## Outputs

- **Object** - The input object.
