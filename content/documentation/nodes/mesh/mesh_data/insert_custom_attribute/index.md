---
title : Insert Custom Attribute
weight : 30
---

## Description

This node inserts value(s) for a custom attribute in mesh.

## Options

- **Domain** - All attributes have a domain and type associated with them.
               Knowing the domain of an attribute is important because it defines
               which parts of the geometry the attribute can affect.
    - *Point* - This domain attributes are associated with the vertices of the mesh.
    - *Edge* - This domain attributes are associated with the edges of the mesh.
    - *Face* - This domain attributes are associated with the faces of the mesh.
    - *Corner* - This domain attributes are associated with the corners of the faces of the mesh.

- **Data Type** - The data type for the custom attribute.
    - *Integer* - The integer list.
    - *Float* - The float list.
    - *Float2* - The 2D vector list.
    - *Vector* - The 3D vector list.
    - *Color* - The color list.
    - *Byte Color* - The color list.
    - *Boolean* - The boolean list.

## Inputs

- **Mesh** - The mesh.
- **Name** - The string, name for the custom attribute.
- **Value(s)** - A value or list of values for the data of the custom attribute.

## Outputs

- **Mesh** - The mesh.
