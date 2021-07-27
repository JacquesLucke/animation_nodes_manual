---
title : Clamp Falloff
---

## Description

This node clamps falloff value to a certain range. Any value outside of the
defined range will be clamped, that is, if it is larger than the maximum
value it will be rendered the maximum value and if it is less than the
minimum value it will be rendered the minimum value.

## Inputs

- **Falloff** - A falloff.
- **Min** - If the input falloff value is less than this value, the output
    falloff will be this value.
- **Max** - If the input falloff value is more than this value, the output
    falloff will be this value.

## Outputs

- **Falloff** - The actual falloff object.
