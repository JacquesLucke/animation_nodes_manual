---
title : Spline
---

## Spline Curvatures

Spline nodes now return spline curvatures when possible. A low curvature value
means the spline is mostly straight at this point, while a high curvature value
means the spline is mostly curved or bent at this point. One can use this
information to remove points at the straight portions of the spline as they
don't provide any signification information to the shape of the spline.

{{< video spline_curvature.mp4 >}}

## Offset Spline

The *Offset Spline* node is now vectorized.

## Curve Object Output

A new *Fill Caps*, *Bevel Mode*, and *Taper Mode* inputs were added to the
*Curve Object Output* node.

## Evaluate Spline

A new *Matrix* output was added, it returns a matrix that is aligned with the
tangent and normal of the spline at the evaluation point and scaled by the
radius of the spline at the evaluation point.

A new *Wrap Parameters* option was added to the *Advanced Node Settings*. If
enabled, the input parameters will wrap around the `[0, 1]` range. For instance,
a parameter of `1.1` will be wrapped to `0.1` and a parameter of `-0.1` will be
wrapped to `0.9`. This can be used to animate points along the spline such that
they start again after reaching the end of the spline.

{{< video evaluate_spline_wrap.mp4 >}}

The *Use Range* option was removed and replaced by an *Evaluation Type* option.
The option includes a new mode of operation *Range Step*, which evaluates the
spline on a uniform range with a specified step size.

## Spline Info

A new *Material Index* output was added. It returns the material index of the
input spline.

## Spline From Points

A new *Material Index* input was added. It defines the material index of the
spline.

## Spline From Object

The *Spline From Object* node can now get splines from text objects.
Additionally, a new *Apply Modifiers* input was added.

## Transform Spline

The *Transform Spline* node was vectorized.

## Set Spline Radius

A new option to change the vectorization behavior was added. It is now possible
to set the radius per spline or per point in each spline.

## Bevel Spline

The *Bevel Spline* node was added. The node bevels the points of a poly spline.

{{< video spline_bevel.mp4 >}}
