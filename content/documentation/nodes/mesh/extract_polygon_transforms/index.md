---
title : Extract Polygon Transforms
weight : 90
---

## Description

This node returns transformation matrices that describe the location and
orientation of the input polygons.

## Options

- **Extraction Type** -
    - *Default* - Use polygon center and first edge as basis for the transformation
        matrix of the polygon.
    - *Edge* - Use one of the edge of the polygon as basis for the transformation matrix
        of the polygon.
        - *Edge Selection Type* -
            - *Direction* - This option allows to select the edge based on the direction.
                - *X* - Return matrix oriented on the edge in the polygon that along
                        X-axis.
                - *Y* - Return matrix oriented on the edge in the polygon that along
                        Y-axis.
                - *Z* - Return matrix oriented on the edge in the polygon that along
                        Z-axis.
                - *Custom* - Return matrix oriented on the edge in the polygon that
                             along the custom axis.
            - *Distance* - This option allows to select the edge based on the distance
                           to the input center.
                - *Closest* - Return matrix oriented on the edge in the polygon closest
                              to the input center.
                - *Furthest* - Return matrix oriented on the edge in the polygon furthest
                               to the input center.

## Inputs

- **Mesh** - The mesh.
- **Vertices** - A vector list that represents the locations of the vertices of the
    polygons.
- **Polygon Indices** - The polygon indices of the polygons.
- **Direction** - A vector to specify the direction. (Available in *Direction*
    edge selection type.)
- **Center** - A vector to specify the center. (Available in *Distance* edge
    selection type.)

## Outputs

- **Transforms** - A matrix list that includes transformation matrices that describe
    the location and orientation of the polygons.
- **Inverse Transforms** - The inverse matrix of the transforms.

## Advanced Node Settings

- **Source** - This option allows to select the input source type.
    - *Mesh* - A mesh as the input source.
    - *Vertices and Polygons* - A vector list that represents the locations of the
        vertices of the polygons and polygon indices of the polygons as the input source.
- **Polygons are Flat** - Performance can be improved when you are certain that all
    polygons are flat. Enabling this can lead to artifacts when the polygons are not
    actually flat.
