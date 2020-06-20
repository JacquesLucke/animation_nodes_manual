---
title : Spline Falloff
weight : 1
---

## Description

This node creates a vector based falloff that associates to every object
a float that is equal to inverse the distance from it to some spline.
This float is always in `[0,1]` range, So some distances will be clamped
to `1` or `0`. We conclude that objects that are closer to the spline
will have a large float that doesn't exceed `1` and as object gets away,
their floats starts to fade till it becomes zero at some point.

![image](spline_falloff_node.png)

## Inputs

- **Distance** - This float is added to the float of every object
    which result in an offset for the distance.
- **Width** - The distance between the ones and the zeroes, can be
    though of as the slop as well.
- **Interpolation** - Floats are evaluated at this interpolation.

## Outputs

- **Falloff** - The actual falloff object.

## Advanced Node Settings

- N/A

## Examples of Usage

{{< video spline_falloff_node_example.mp4 >}}
