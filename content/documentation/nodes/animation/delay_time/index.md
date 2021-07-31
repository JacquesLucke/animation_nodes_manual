---
title : Delay Time
---

## Description

This node subtracts the *delay* input from the *time* input.

The essence of this subtraction is changing the frame at which an
animation will start when using one of the animation nodes or using the
output in a custom animation node tree. That is because negative values
are clamped to zero in the animation process so subtracting 20 from the
input frame will result in zero for the first 20 frame.

## Inputs

- **Time(s)** - An input time(s).
- **Delay(s)** - A value or list to subtract from the time(s) or the frame(s) at which
    the animation will start.

## Outputs

- **Time(s)** - The delayed time(s).
