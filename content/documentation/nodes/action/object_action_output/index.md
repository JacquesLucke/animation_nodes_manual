---
title : Object Action Output
---

## Description

This node evaluates the input action and writes its evaluated data into the
input object treating the action channel paths as object RNA paths.

## Options

- **Mode** - If set to *Transforms*, an *Offset* matrix input will be available
  to offset the transforms of the object on top of the evaluated action
  transforms data.

## Inputs

- **Object** - The input object.
- **Action** - The input action.
- **Frame** - The frame to evaluate the action at.
- **Offset** - The offset to add to the action evaluated transforms. Only
  available in the *Transforms* mode.
- **Index** - The index to evaluate the action at.

## Outputs

- **Object** - The input object.
