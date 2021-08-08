---
title : Mesh
---

## Mesh Object Output

The *Material Indices* input was removed. Material indices are now part of the
mesh structure, stored as a built-in attribute. Use the new *Material Indices*
input in the *Combine Mesh* node instead.

## Regular Polygons

Menu and search entries were added to regular polygons, including Pentagon,
Hexagon, Heptagon, and Octagon. Those entries add a Circle node with the
appropriate number of points.

## BMesh Mesh Data

A new *Material Indices* output was added.

## Polygon List Socket

Polygon Lists can now be implicitly converted into Integer Lists.

## Mesh Info

A new *Material Indices* output was added.

## Bmesh From Object

The *Apply Modifiers* and *Scene* inputs were removed. This was done in response
to an API change which removed the corresponding options from Blender.

## Shade Object Smooth

The *Shade Object Smooth* node now allows smoothing curve objects.
