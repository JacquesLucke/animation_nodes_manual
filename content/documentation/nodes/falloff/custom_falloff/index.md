---
title : Custom Falloff
---

## Description

This node creates an index based falloff that associates the first
element from the float list to the first object, second element to the
second object and so on.

## Inputs

- **Strengths** - A float list the represents the floats of the
    objects. If the number of object is greater than the length of this
    list, extra object will have a floats equal to the input fallback
    value.
- **Fallback** - The fallback value.

## Outputs

- **Falloff** - The actual falloff object.
