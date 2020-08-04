---
title : Chain Actions
---

## Description

This node chain two bounded actions after each other.

## Options

- **Relative** - If enabled, the second action will be superimposed over the
  last frame evaluation of the first action. The superposition is computed as
  an addition except for scale channels which are computed as a multiplication.
  For instance, if the first action represents the position of an object and
  the object position was at some point P in the last frame, the second action
  will start from this point P relative to the world origin.

## Inputs

- **A** - The first action.
- **A** - The second action.

## Output

- **Chained Action** - The output chained action.
