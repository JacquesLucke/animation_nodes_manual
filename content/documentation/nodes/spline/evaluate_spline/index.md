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
- **Evaluation Type** -
  - **Parameter** - The spline will be evaluated at the input parameter(s) using
    the evaluation method outlined above.
  - **Range Count** - The spline will be uniformly evaluated giving a specific
    number of points.
  - **Range Step** - The spline will be uniformly evaluated every specific step
    size.

## Inputs

- **Spline** - A spline to evaluate.

### Parameter Evaluation Type

- **Parameter** - The position of the point to be evaluated in the
    normalized distance of the spline. (0 is the start of the spline and
    1 is the end of the spline)

### Range Count Evaluation Type

- **Count** - The number of points to evaluate.
- **Start** - The start parameter to start evaluating from.
- **End** - The end parameter to end evaluating at.

### Range Step Evaluation Type

- **Step** - The step size to evaluate the spline at.
- **Start** - The start parameter to start evaluating from.
- **End** - The end parameter to end evaluating at.

## Outputs

- **Location** - A vector that represents the position of the point in the curve
  that correspond to the input parameter.
- **Tangent** - A vector that is aligned with the tangent line to the evaluated
  point.
- **Normal** - A vector that is perpendicular to the tangent and some other
  vector. The other vector is chosen such that it guarantee minimal change in
  the normal as the parameter change.
- **Radius** - The radius of the spline at the point.
- **Tilt** - The tilt of the spline at the point.
- **Curvature** - The curvature of the spline at the point.
- **Matrix** - A matrix that is aligned with tangent and normal of the spline at
  the point and scaled by the radius of the spline at the point.

## Advanced Node Settings

- **Resolution** - It is the quality of the evaluated spline, in other words, it
  is the number of point in the spline used in evaluation.
- **Wrap Parameters** - If enabled, the input parameters will wrap around the
  `[0, 1]` range. For instance, a parameter of `1.1` will be wrapped to `0.1`
  and a parameter of `-0.1` will be wrapped to `0.9`.
