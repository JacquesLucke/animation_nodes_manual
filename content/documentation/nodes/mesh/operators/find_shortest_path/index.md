---
title : Find Shortest Path
weight : 30
---

## Description

This node find shortest path(s) from source(s) on mesh island(s) using modified Dijkstra's algorithm.

## Options

- **Mode Type** -
    - *Path* - Find path from source vertex to other vertex.
    - *Tree* - Find paths from source vertex(ies) to other vertices.

- **Path Type** -
    - *Mesh* - It generates mesh type path(s).
        - *Join Meshes* - If enabled, will join meshes and generate a mesh for paths.
    - *Spline* - It generates spline type paths.
    - *Stroke* - It generates gp stroke type paths.

## Inputs

- **Mesh** - The mesh.
- **Source(s)** - An integer or integer list which is the index(ies) of the *start* vertex(ies).

## Outputs

- **Mesh(s)** - The mesh(es).
- **Splines** - The splines.
- **Strokes** - The GP Strokes.
