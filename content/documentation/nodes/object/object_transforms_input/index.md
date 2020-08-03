---
title : Object Transforms Input
---

## Description

This node returns the current location, rotation, and scale of the input
object.

## Inputs

- **Object** - An object.

## Outputs

- **Location** - A vector that contains the current location of the
    input object.
- **Rotation** - An Euler that contains the current rotation of the
    input object.
- **Scale** - A vector that contains the current scale of the input
    object.
- **Quaternion** - A quaternion that contains the current rotation of
    the input object.

## Notes

- To be able to use the quaternion output the rotation mode of the object have
  to be set to quaternion. The same for other rotation models.
