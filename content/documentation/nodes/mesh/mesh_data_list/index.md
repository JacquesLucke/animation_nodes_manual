---
title : Mesh Data List
weight : 1
---

## Description

This node is used to create an arbitrary list of mesh data. A new mesh
data can be added with the *New Input* button. A new mesh data can also
be added by plugging it into the transparent socket.

![image](mesh_data_list_node.png)

## Inputs

  - **Element** - A mesh data at the index 0.
  - **Element** - A mesh data at the index 1.
  - **Element** - ...

## Outputs

  - **Mesh Data list** - A list that contains all the input mesh data.

## Advanced Node Settings

  - **Change type** - Changes the type of the mesh data list to another
    list type.
  - **Hide Inputs** - Hides all the inputs in the node.
  - **Remove Unlinked Inputs** - Removes all the inputs that are not
    connected to another node.

## Caution

A warning will pop up when you use the *Remove Unlinked Inputs* button
in the node, while if you used the the *Remove Unlinked Inputs* button
in the *Advanced Node Settings* the inputs will be removed without a
warning.

## Examples of Usage

{{< video join_mesh_data_list_node_example.mp4 >}}
