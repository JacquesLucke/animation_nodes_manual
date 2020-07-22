---
title : Get Bounding Box
weight : 30
---

## Description

This node returns mesh data of a cuboid that represents the bounding box
of the input object.

A bounding box is a box that bounds the object, that is, each face of
the box is a least upper bound or greatest lower bound of a specific
vertex coordinate.

## Inputs

- **Object** - An object.

## Outputs

- **Vertices** - A vector list that includes vertices locations of the
    bounding box.
- **Edges** - A list of edge indices that includes all the edges of
    the bounding box.
- **Polygons** - A list of polygon indices that includes all the
    polygons of the bounding box.

## Advanced Node Settings

- **Use World Space** - This option allows you to choose between local
    and global coordinate space for the bounding box.
