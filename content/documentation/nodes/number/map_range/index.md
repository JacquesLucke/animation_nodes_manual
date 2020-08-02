---
title : Map Range
---

## Description

This node remaps a value from an interval to a new interval.

## Options

- **Clamp** - If enabled, values will be clamped to the interval
    `[0,1]`.
- **Interpolation** - If enabled, values will be evaluated at the
    input interpolation before being output. (Only available when clamp
    is enabled, as interpolations work on normalized intervals only)

## Inputs

- **Value** - A float that should be remapped.
- **Input Min** - The start of the original interval.
- **Input Max** - The end of the original interval.
- **Output Min** - The start of the new interval.
- **Output Max** - The end of the new interval.
- **Interpolation** - If *Interpolation* is enabled, the output value
    will be evaluated based on this input interpolation.

## Outputs

- **Value** - The value after remapping
