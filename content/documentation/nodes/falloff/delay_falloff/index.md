---
title : Delay Falloff
---

## Description

This node creates an index based falloff that associates a float that
increases as the time increases where objects at indices that are
closer to zero starts increasing before those that are farther away from
zero. User can control the rate of increasing relative to time and
indices.

## Inputs

- **Time** - The current time.
- **Delay** - Time span between the animation start of two successive
    objects.
- **Duration** - Time it takes for an object to reach its maximum
    value (1).
- **Interpolation** - The output is evaluated at this input
    interpolation or the velocity function of the animation.
- **Offsets** - When given, it specifies how much each object is
    offset in time.

## Outputs

- **Falloff** - The actual falloff object.
