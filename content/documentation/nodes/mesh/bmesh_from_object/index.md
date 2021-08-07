---
title : Bmesh From Object
weight : 220
---

## Description

This node returns a bmesh type for the input object.

## Inputs

- **Object** - An object.
- **Use World Space** - This option allows you to choose between local and
  global coordinates space for the output vectors (vertices location).

## Outputs

- **Bmesh** - A bmesh type.

## Notes

- It is not recommended to use this node if you are not going to use Bmesh
  operations and just want to get mesh data, because it is a lot slower to
  create. (The *Object Mesh Data* node can get the same data 33x faster)
- Using Bmesh doesn't mean that the info will be updated on the fly when you are
  in edit mode editing, you will have to change to object mode to update the
  edits you applied.
