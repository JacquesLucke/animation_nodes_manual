---
title : GP Stroke Info
weight : 40
---

## Description

This node returns some information about the gp stroke like its points, strengths, and vertex colors, etc.

## Inputs

- **Stroke** - A gp stroke.

## Outputs

- **Points** - A vector list of location of all vertices of the input gp stroke.
- **Strengths** - A float list of strength of all vertices of the input gp stroke.
- **Pressures** - A float list of pressurre of all vertices of the input gp stroke.
- **UV-Rotations** - A float list of uv-rotation of all vertices of the input gp stroke.
- **Vertex Colors** - A color list of vertex color of all vertices of the input gp stroke.
- **Line Width** - The line width of the input gp stroke.
- **Hardness** - A value that controls the softness of edges of the input gp stroke.
- **Cyclic** - A boolean value. True when the input gp stroke is cyclic.
- **Start Cap Mode** - The start-shape of the input gp stroke, e.g., FLAT, ROUND.
- **End Cap Mode** - The end-shape of the input gp stroke, e.g., FLAT, ROUND.
- **Material Index** - This is the 'Color Index' pass of the input gp stroke.
- **Display Mode** - This is the display mode of the input gp stroke, e.g., 3DSPACE, SCREEN, etc.
