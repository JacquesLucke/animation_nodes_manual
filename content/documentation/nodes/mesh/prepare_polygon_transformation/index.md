---
title : Prepare Polygon Transformation
weight : 1
---

## Description

This node separate input polygons and return them in their unity
position, that is, they are located at the center of the world and lie
on the xy plane.

It also return a list of transformation matrices that if used to
transformed the output polygons, the result will be the polygons in
their initial position and orientation.

![image](prepare_polygon_transformation_node.png)

## Inputs

  - **Vertices** - A vector list that represent the vertices locations
    of the polygons.
  - **Polygon Indices** - A polygon indices that define the polygons.

## Outputs

  - **Vertices** - The vector list that represent the vertices locations
    of the separated polygons at their unity position.
  - **Polygon Indices** - A polygon indices list that define the
    separated polygons.
  - **Transformations** - A matrix list that include the transformation
    matrices that describe polygons original locations and orientations.

## Advanced Node Settings

  - N/A

## Examples of Usage

{{< video prepare_polygon_transformation_node_example.mp4 >}}
