---
title : Mesh Object Output
weight : 240
---

## Description

This node edits the input object's data based on a new input data.

## Options

- **Mesh** - This option lets you write a mesh to the input
    object. Since the mesh carries only the vertices
    locations, edge, indices, polygons indices info, uv maps and vertex colors,
    those will be the only data in the output object. (A bmesh data carries more
    information than the mesh like vertices normals.)
- **Bmesh** - This option lets you write a bmesh data to the input
    object. A bmesh data carry much more information than the mesh,
    such extra information like *Vertex Normals*, *Vertex group weights*
    and *Material indices*.
- **Vertices** - This option will only edit the vertices locations,
    that is, the input object should already have some data and you are
    just editing the vertices locations of this data. This option is
    much faster than the **Mesh** option assuming all you do is
    edit the vertices.

## Inputs

- **Object** - An object to edit. The plus button let you add a new
    object and write to it.
- **Mesh** - Mesh to write to the input object. (Only for
    the Mesh option)
- **Bmesh** - Bmesh to write to the input object. (Only for the Bmesh
    option)
- **Vertices** - Vector list that represents the new locations for the
    vertices. (Only for the vertices option)

## Outputs

- **Object** - The input object.

## Advanced Node Settings

- **Ensure Animation Data** - Make sure that the mesh has animation data so that
    it will be exported as animation by exporters (mainly Alembic).
- **Validate Mesh** - If enabled, animation nodes will check if the
    mesh is valid and if not, it will try to correct it as much as
    possible. This option should always be enabled to avoid blender
    crashes. However, if you are absolutely sure that your mesh is
    valid, you should disable it because it slows down execution.
- **Print Validation Info** - If enabled and **Validate Mesh** is
    enabled, animation nodes will print the procedures taken to fix the
    input mesh.
- **Calculate Loose Edges** - If enabled, the node will compute the loose edge
  status of edges. This useful for drawing the mesh in the view-port.
