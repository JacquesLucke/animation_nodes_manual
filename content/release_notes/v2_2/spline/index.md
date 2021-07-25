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
