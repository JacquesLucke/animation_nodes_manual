---
title : Create Mesh List
weight : 180
---

## Description

This node is used to create an arbitrary list of mesh. A new mesh
data can be added with the *New Input* button. A new mesh can also
be added by plugging it into the transparent socket.

## Inputs

- **Element** - A mesh at the index 0.
- **Element** - A mesh at the index 1.
- **Element** - ...

## Outputs

- **Mesh Data list** - A list that contains all the input mesh.

## Advanced Node Settings

- **Change type** - Changes the type of the mesh list to another
    list type.
- **Hide Inputs** - Hides all the inputs in the node.
- **Remove Unlinked Inputs** - Removes all the inputs that are not
    connected to another node.

## Caution

A warning will pop up when you use the *Remove Unlinked Inputs* button in the
node, while if you used the *Remove Unlinked Inputs* button in the *Advanced
Node Settings* the inputs will be removed without a warning.
