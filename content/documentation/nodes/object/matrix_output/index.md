---
title : Object Matrix Output
---

## Description

This node sets the transformations of the input object to the input
transformation matrix.

## Inputs

- **Object** - An object.
- **Matrix** - An input transformation matrix.

## Outputs

- **Object** - The input object.

## Advanced Node Settings

- **Type** - This option lets you set the transformation matrix as:
  - **World** - World space transformation matrix.
  - **Basis** - World space transformation matrix but without constraints and
    parenting.
  - **Local** - Local space transformation matrix.
  - **Parent Inverse** - Inverse of object’s parent matrix at time of
    parenting.
