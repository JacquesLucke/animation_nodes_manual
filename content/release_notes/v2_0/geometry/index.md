---
title : Geometry
weight : 1
---



## Point in Camera Frustrum

This node returns four outputs: Image U, Image V, Z Depth and a Visible
boolean. **Image U and V** represent the point position in a UV
coordinate based on the active camera view, while **Z Depth** tells you
how far the vector is away.

![image](camera_frustrum_explain.png)

{{< video point_in_camera_frustrum_example.mp4 >}}

Note: the object input must be a Camera object.

## Triangulate Polygons

Triangulate Polygons has been removed because it is nearly never used
and hard to maintain. However, it may be rewritten in a better form in
the future.

## Intersect Polyline Plane

Intersect Polyline Plane was removed because it is nearly never used and
hard to maintain
