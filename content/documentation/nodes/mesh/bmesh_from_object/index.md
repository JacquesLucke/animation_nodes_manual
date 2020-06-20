---
title : Bmesh From Object
weight : 1
---

## Description

This node returns a bmesh data type for the input object.

It is not recommended to use this node if you are not going to use bmesh
operations and just want to get mesh data, because it is a lot slower to
create.(Object Mesh Data node can get the same data in about 33x the
speed of the bmesh)

![image](bmesh_from_object_node.png)

## Inputs

- **Object** - An object.
- **Use World Space** - This option allows you to choose between local
    and global coordinates space for the output vectors (vertices
    location).
- **Use Modifiers** - This option if enabled will return the data as
    modifiers were applied, that includes both the generative and
    defomative modifiers.
- **Scene** - The scene the object exist in.

## Outputs

- **Bmesh** - A bmesh data type.

## Advanced Node Settings

- N/A

## Notes

- Using Bmesh doesn't mean that the info will be updated on the fly
    when you are in edit mode editing, you will have to change to object
    mode to update the edits you applied.

## Examples of Usage

{{< video bmesh_from_object_node_example.mp4 >}}
