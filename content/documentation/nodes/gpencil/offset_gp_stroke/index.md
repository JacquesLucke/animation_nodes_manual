---
title : Offset GP Stroke
weight : 120
---

## Description

This node offsets the properties *(e.g., Location, Strength, Vertex Color, etc.)* of points of the input gp stroke.

## Options

- **Offset Type** -
    - *Location* - This option allows to offset the location of points of the input gp stroke.
    - *Strength* - This option allows to offset the strength of points of the input gp stroke.
    - *Pressure* - This option allows to offset the pressure of points of the input gp stroke.
    - *UVRotation* - This option allows to offset the uv-rotation of points of the input gp stroke.
    - *Vertex Color* - This option allows to offset the vertex color of points of the input gp stroke.

## Inputs

- **Stroke** - A gp stroke.
- **Falloff** - A falloff that can be used to fade between two values.
- **Location** - A vector or a vector list to offset the location of points of the input gp stroke.
- **Strength** - A float or a float list to offset the strength of points of the input gp stroke.
- **Pressure** - A float or a float list to offset the pressure of points of the input gp stroke.
- **UV-Rotation** - A float or a float list to offset the uv-rotation of points of the input gp stroke.
- **Color** - A vector or a vector list to offset the vertex-color of points of the input gp stroke.

## Outputs

- **Stroke** - A gp stroke.

## Advanced Node Settings

- **Blend Type** - These options available for *Vertex Color* offset.
  - *Mix* - This option mix the vertex colors of points of the input gp stroke.
  - *Add* - This option add the vertex colors of points of the input gp stroke.
  - *Subtract* - This option subtract the vertex colors of points of the input gp stroke.
  - *Multiply* - This option multiply the vertex colors of points of the input gp stroke.
  - *Divide* - This option divide the vertex colors of points of the input gp stroke.
