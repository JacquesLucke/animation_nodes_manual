---
title : Mix Colors
---

## Description

This node linearly mixes between two colors or color lists based on a factor or factor list.

## Options

- **Clamp** - The way *Mix Colors* works, A factor that is larger than 1 won't be
    clamped but rather multiplied to the second color. That's why the node
    has an option to *Clamp Factor*. So if *Clamp factor* is enabled, any
    factor that is larger than 1 will return the second color.

## Inputs

- **Factor(s)** - A float or float list that controls the amount of each input color(s) to
    the output. 0 means the first color(s) only and 1 means the second color(s) only.
- **A** - First color(s).
- **B** - Second color(s).

## Outputs

- **Result(s)** - The result(s) of mixing the two colors or color lists by the factor(s).
