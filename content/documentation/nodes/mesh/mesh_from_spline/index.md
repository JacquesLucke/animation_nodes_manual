---
title : Mesh From Spline
weight : 50
---

## Description

This node generates a mesh from a spline.

## Options

- **Use Custom Shape** - This option allows to choose custom shape for bevel.

## Inputs

- **Spline** - A spline.
- **Size** - A float value that controls the radius of the output mesh.
- **Spline Resolution** - A integer value that controls the resolution for sampling the input spline.
- **Bevel Resolution** - A integer value that controls the bevel resolution of the output mesh.
- **Shape Border** - A vector list that for bevel shape of the output mesh.
- **Closed Shape** - A boolean value that close the bevel shape of the output mesh.
- **Cap Ends** - A boolean value that close the ends of the output mesh.


## Outputs

- **Mesh** - The mesh.

## Advanced Node Settings

- **Parameter Type** -
    - *Uniform* - This option allows to uniformly sample the input spline with custom resolution.
    - *Resolution* - This option allows to sample the input spline based on the resolution of the spline.
