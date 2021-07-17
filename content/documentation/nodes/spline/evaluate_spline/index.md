---
title : Evaluate Spline
---

## Description

This node will return information a point on the spline at some normalized
distance from the starting point where this distance is defined by the input
*Parameter*.

## Options

- **Parameter Type** - The method of evaluation. Can be *Uniform* or
  *Resolution*. A uniform type would result in equally spaced evaluated points
  for equally spaced parameters. On the other hand, a resolution type would
  evaluated points depending on the density of the spline, so they may not be
  equally spaced.
- **Evaluate Range** - If enabled, the node will evaluated multiple points with
  equally spaced parameters in a specific range.

## Inputs

- **Spline** - A spline to evaluate.

### Evaluate Range Disabled

- **Parameter** - The position of the point to be evaluated in the
    normalized distance of the spline. (0 is the start of the spline and
    1 is the end of the spline)

### Evaluate Range Enabled

- **Count** - The number of points to evaluate.
- **Start** - The start parameter to start evaluating from.
- **End** - The end parameter to end evaluating at.

## Outputs

- **Location** - A vector that represents the position of the point in
    the curve that correspond to the input parameter.
- **Tangent** - A vector that is aligned with the tangent line to the
    evaluated point.
- **Normal** - A vector that is perpendicular to the tangent and some other
  vector. The other vector is chosen such that it guarantee minimal change in
  the normal as the parameter change.
- **Radius** - The radius of the spline at the point.
- **Tilt** - The tilt of the spline at the point.
- **Curvature** - The curvature of the spline at the point.

## Advanced Node Settings

- **Resolution** - It is the quality of the evaluated spline, in other words,
  it is the number of point in the spline used in evaluation.
