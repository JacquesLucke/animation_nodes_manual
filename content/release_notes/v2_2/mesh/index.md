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

## Line Mesh

The *Line Mesh* node now outputs the edge and polygon indices of the mesh.

## Get Custom Attribute

The *Get Custom Attribute* node was added. The node gets the data of a custom
attribute.

## Insert Custom Attribute

The *Insert Custom Attribute* node was added. The node inserts a new custom
attribute to the mesh.

## Set Custom Attribute

The *Set Custom Attribute* node was added. The node changes the value of an
existing custom attribute.
