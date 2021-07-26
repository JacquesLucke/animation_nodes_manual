---
title : Spline From Points
---

## Description

This node creates a new spline from input vectors, each vector will
represent the position of a handle in the output spline.

## Options

- **Bezier** - This option will create the spline as a bezier spline
    which have a left and right handle.
- **Poly** - This option will create the spline as a simple poly
    spline, a poly spline is just a linear connection between points and
    can't be smoothed or edited but it is faster to create.

## Inputs

- **Points** - A vector list that represents the position of the points of the
  output splines.
- **Left Handles** - A vector list that represent the position of the left
  handles of the spline.
- **Right Handles** - A vector list that represent the position of the right
  handles of the spline.
- **Radius** - A float list the contains the radii of each of the points of the
  spline.
- **Cyclic** - A boolean which if True will connect the first handle to the last
  handle and thus having a closed spline.
- **Material Index** - The material index of the spline.

## Outputs

- **Spline** - The output spline.
