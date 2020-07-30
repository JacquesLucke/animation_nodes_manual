---
title : Spline
---

## Spline Normals

Spline nodes now return spline normals when possible. Normals, while arbitrary,
are guaranteed to be sufficiently continues with low deviations for visually
pleasing results.

![Spline Normals](spline_normals.png)

## Spline Tilt

Splines nodes can now deals with spline tilt.

{{< video spline_tilt.mp4 >}}

## Tilt Spline

A new *Tilit Spline* node was added. The node alters the tilt of the spline and
can so in an accumulative manner.

{{< video tilt_spline.mp4 >}}

## Splines From Edges

A new *Spline Per Branch* option was added. It minimizes discontinuity by
forming splines from *branches* instead of edges. A comparison between the old
approach and the new option is shown in the following example.

![Spline Per Branch](spline_per_branch.png)

## Evaluate Spline

A new *Evaluate Range* option was added.

![Spline Evaluate Range](spline_evaluate_range.png)

## Get Spline Samples

This node was removed. Replaced by the *Evaluate Range* option of the *Evaluate
Spline* node.

## Tilt Spline

The *Tilt Spline* node vectorized, now it allows to set tilt of multiple splines.

## Change Spline Direction

A new *Change Spline Direction* node added that allows to switch the direction of a spline or a spline list.

## Spline From GP Stroke

A new *Spline From GP Stroke* node added. This allows to convert gp stroke(s) into spline(s). So with this
node one can convert a gp object into a curve object.

## Offset Spline

A new *Offset Spline* node added. This node allows to offset location, radius and tilt of a spline with the
falloff.

{{< video offset_spline.mp4 >}}

## Trim Spline

The node now returns an empty spline if the start and end are equal.
