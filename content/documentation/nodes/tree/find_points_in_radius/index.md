---
title : Find Points In Radius
---

## Description

This node finds the points that lie inside a sphere with a given center
and radius in the input KD Tree.

## Inputs

- **KD Tree** - A KD tree that contain your points.
- **Radius** - The radius of the search sphere.
- **Vector** - A vector that represent the center of the search
    sphere.

## Outputs

- **Vectors** - The locations of the points that lies inside the
    sphere defined by the input vector and radius.
- **Distances** - The distances between the output points and the
    input point.
- **Index** - The indices of the nearest points to the input point in
    the list used to construct the KD tree.
