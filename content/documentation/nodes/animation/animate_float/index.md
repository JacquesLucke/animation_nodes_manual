---
title : Animate Float
---

## Description

This node mixes between two floats or two float lists where the factor for mixing is the
time mapped to an input interval *Duration*.

## Inputs

- **Time(s)** - A time(s) or the factor(s) for mixing.
- **Start Time(s)** - A factor(s) to offset the starting time *(default is 0)*
  of animation.
- **Start(s)** - A value or list to start the animation with or the first input
    for mixing.
- **End(s)** - A value or list to end the animation with or the second input for
    mixing.
- **Interpolation** - An Interpolation(Function) to evaluate the time
    at (Linear will just use the input time).
- **Duration(s)** - The duration(s) of the animation or the interval to map
    the time to or the value the time is divided by.

## Outputs

- **Result(s)** - The value(s) of the animation evaluated at the input time
    or the result of mixing.
- **Time(s)** - The difference between the input time(s) and the duration(s)
    (Isn't affected by the input interpolation).
