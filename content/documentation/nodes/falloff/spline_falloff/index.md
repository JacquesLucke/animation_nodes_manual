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

## Options

- **Mix List Type** - This option is only available for spline list. It allows
    to mix the falloff of each spline.
    - *Max* - This option mix the falloffs by considering the maximum value.
    - *Add* - This option mix the falloffs by adding them.

## Inputs

- **Spline(s)** - A spline or a spline list.
- **Use Radius for Distance** - This boolean input allows to use the spline's
    radius to offset distance.
- **Distance** - This float is added to the float of every object
    which result in an offset for the distance.
- **Use Radius for Width** - This boolean input allows to use the spline's
    radius to offset width.
- **Width** - The distance between the ones and the zeroes, can be
    though of as the slop as well.
- **Interpolation** - Floats are evaluated at this interpolation.

## Outputs

- **Falloff** - The actual falloff object.

## Advanced Node Settings

- **Resolution** - An integer value to specify the poly spline segments per bezier
    spline segments for input spline(s).
