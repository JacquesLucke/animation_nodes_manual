---
title : Set Spline Radius
---

## Description

This node set the radius of individual spline points.

## Options

- **Radius Per Point** - If both inputs are a list, the first radius will be set
  to the first point in all splines, and so on.
- **Radius Per Spline** - If both inputs are a list, the first radius will be
  set to the first spline, and so on.

## Inputs

- **Splines** - A spline(s) to set their radius.
- **Radius** - A float list that include the radii of each point in the input
  spline. (Has to has a length equal to the amount of points the spline(s) has)

## Outputs

- **Spline** - The output splines.
