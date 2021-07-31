---
title : Mix Eulers
---

## Description

This node mixes between two eulers or euler lists based on a factor or factor list.

## Options

- **Clamp** - The way *Mix Eulers* works, a factor that is larger than 1 won't be
    clamped but rather multiplied to the second euler. That's why the node
    has an option to *Clamp Factor*. So if *Clamp factor* is enabled, Any
    factor that is larger than 1 will return the second euler.

## Inputs

- **Factor(s)** - A float or float list that controls the amount of each euler(s) input to
    the output, Where 0 means the first euler(s) only and 1 means the
    second euler(s) only.
- **A** - First euler(s).
- **B** - Second euler(s).

## Outputs

- **Result(s)** - The result euler(s) of mixing the two eulers or euler lists by the input
    factor(s).
