---
title : Edge To Tube
weight : 20
---

## Description

This node returns the mesh composed of cylinders in
places of the input edges.

## Inputs

- **Points** - The locations of the vertices of the edges.
- **Edge Indices List** - The edge indices list of the edges.
- **Radius** - Radius of the cylinders.
- **Resolution** - The number of vertices per loop that forms the
    cylinder.
- **Caps** - If true, cylinders' starts and ends will be closed using
    an Ngon.

## Outputs

- **Mesh** - The mesh.
