---
title : Mesh
---

## Unity Triangle

A new *Unity Triangle* node was added. The node returns a mesh composed of a
single triangle whose area is 1, whose center is 0, and whose orientation is
such that if an object was instanced on it, the instance orientation will be 0.

This node is extremely useful if one wans to instance many meshes with specific
transformations. Using the *Object Instancer* node would be very inefficient.
A more efficient approach would be to transform many unity triangles based on
the target transformations and then use Blender's face instating to instance
the target objects on that mesh. The following example illustrates this
approach.

![Unity Triangle Example](unity_triangle.png)

## Compose Matrix

A new *Compose Matrix* node was added. The node allows the user to construct a
matrix or a list of matrices from locations, rotations, and scales. The
*Translation Matrix*, *Scale Matrix*, and *Rotation Matrix* nodes were removed
to be replaced by this node.
