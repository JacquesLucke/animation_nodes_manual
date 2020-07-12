---
title : Extract Polygon Transforms
weight : 90
---

## Description

This node returns transformation matrices that describe the location and
orientation of the input polygons.

## Options

- **Extraction Type** -
    - *Default* - Use polygon center and first edge as basis.
    - *Edge* - Use one of the edges as basis.
        - *Edge Selection Type* -
            - *Direction* - This option allows to select the direction axis.
                - *X*
                - *Y*
                - *Z*
                - *Custom*
            - *Distance* - This option allows to select the direction axis.
                - *Closest*
                - *Furthest*

## Inputs

- **Mesh** - The mesh.
- **Vertices** - A vector list that represent the the locations of the vertices of the polygons.
- **Polygon Indices** - The polygon indices of the polygons.
- **Direction** - A vector to specify the direction.
- **Center** - A vector to specify the center.

## Outputs

- **Transforms** - A matrix list that include transformation matrices that describe the location and orientation of the polygons.
- **Inverse Transforms** - The inverse matrix of the transforms.

## Advanced Node Settings

- **Source** - This option allows to select the input source type.
    - *Mesh*
    - *Vertices and Polygons*
- **Polygons are Flat** - Performance can be improved when you are certain that all polygons are flat. Enabling this can lead to artifacts when the polygons are not actually flat.
