---
title : GP Stroke Info
weight : 40
---

## Description

This node returns information about the input gp stroke *e.g., Points, Strengths, and Vertex Colors, Hardness, etc*.

## Inputs

- **Stroke** - A gp stroke.

## Outputs

- **Points** - A vector list of location of points of the input gp stroke.
- **Strengths** - A float list of strength of points of the input gp stroke.
- **Pressures** - A float list of pressure of points of the input gp stroke.
- **UV-Rotations** - A float list of uv-rotation of points of the input gp stroke.
- **Vertex Colors** - A color list of vertex color of points of the input gp stroke.
- **Line Width** - The line width of the input gp stroke.
- **Hardness** - A value that controls the softness of edges of the input gp stroke.
- **Cyclic** - A boolean value. True when the input gp stroke is cyclic.
- **Start Cap Mode** - The start-shape of the input gp stroke, *e.g., FLAT, ROUND*.
- **End Cap Mode** - The end-shape of the input gp stroke, *e.g., FLAT, ROUND*.
- **Material Index** - This is the 'Color Index' pass of the input gp stroke.
- **Display Mode** - This is the display mode of the input gp stroke, *e.g., 3DSPACE, SCREEN, etc*.
