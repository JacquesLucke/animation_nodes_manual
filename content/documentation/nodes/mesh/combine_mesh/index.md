---
title : Combine Mesh
weight : 40
---

## Description

This node combines individual mesh data into a mesh.

## Inputs

- **Vertex Locations** - A vector list that contains the locations of the
  vertices for the output mesh.
- **Edges Indices** - An edge indices list that contains the edge information
  for the output mesh.
- **Polygons Indices** - A polygon indices list that contains the polygon
  information for the output mesh.
- **Polygons Indices** - An integer list that contains the material indices for
  the output mesh. This input is disabled by default and can be enabled by
  enabling the *Is Used* button. If disabled, material indices will not be
  stored in the mesh and will be considered all zero.

## Outputs

- **Mesh Data** - A mesh.

## Advanced Node Settings

- **Skip Validation** - Skipping validation might cause Blender to crash
    when the data is not valid.
