---
title : Mesh Info
weight : 20
---

## Description

This node returns information about the input mesh like its
vertices locations and polygon edge indices.

## Inputs

- **Mesh** - The mesh.

## Outputs

- **Vertex Locations** - A vector list that includes vertices
    locations of the input mesh.
- **Edge Indices** - A list of edge indices that includes all the
    edges of the input mesh.
- **Polygon Indices** - A list of polygon indices that includes all
    the polygons of the input mesh.
- **Vertex Normals** - A vector list that contain unit vectors that
    represent the vertices normals of the input mesh.
- **Polygon Normals** - A vector list that contain unit vectors that
    represent the normals of the polygons of the input mesh.
- **Polygon Centers** - A vector list that contain the locations of
    the centers of the polygons of the input mesh. It is computed as
    the average of vertices of the polygon.
- **UV Map Names** - A string list that contains names of the uv map of the input mesh.
- **Vertex Color Layers** - A string list that contains names of the vertex color layer of the input mesh.
