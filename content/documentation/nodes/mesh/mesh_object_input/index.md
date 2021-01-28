---
title : Mesh Object Input
weight : 10
---

## Description

This node returns some information about the mesh of the input mesh object,
including its vertices locations, edge indices, polygon indices, and more.

Changes in edit mode will not take effect until you change into object mode.

## Inputs

- **Object** - An object.
- **Use World Space** - This option lets you choose between local and global
  coordinate space for the outputs.
- **Use Modifiers** - If enabled, the output mesh will have modifiers applied.
  It should be noted that only modifiers that are evaluated by Blender will be
  applied. Blender only evaluates modifiers for objects visible in the active
  view layer, meaning objects in other scenes and object that are hidden in the
  view layer will not have evaluated modifiers and consequently the output will
  not have modifiers applied even if this option is enabled.
- **Load UVs** - If enabled, will load UV maps in mesh.
- **Load Vertex Colors** - If enabled, will load vertex color layers in mesh.
- **Scene** - The scene the object belong to.

## Outputs

- **Mesh** - The mesh.
- **Vertex Locations** - A vector list that includes vertices locations of the
  input object.
- **Vertex Normals** - A vector list that contain unit vectors that represent
  the vertices normals of the input object.
- **Polygon Centers** - A vector list that contain the locations of the centers
  of the polygons of the input object. It is computed as the average of
  vertices of the polygon.
- **Polygon Normals** - A vector list that contain unit vectors that represent
  the normals of the polygons of the input object.
- **Edge Indices** - A list of edge indices that includes all the edges of the
  input object.
- **Polygon Indices** - A list of polygon indices that includes all the
  polygons of the input object.
- **Local Polygon Area** - A float list that contain the areas of the polygons
  of the input object.
- **Material Indices** - An integer list that contains the material index for
  each polygon, where the first integer represent the index of the material
  assigned to the first polygon, ...
- **Mesh Name** - A string that contains the name of the mesh.

## Notes

- **Mesh Name** output is not the object name! It is the name of mesh data
  block that define the geometry of the object. In Blender you can find that
  name in the *Data Panel*.
