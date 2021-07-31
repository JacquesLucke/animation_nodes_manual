---
title : Mix Matrices
---

## Description

This node linearly mixes between two matrices or matrix lists based on a factor or
factor list.

## Options

- **Clamp** - A factor that is larger than 1 won't be clamped but rather multiplied to
the second matrix. That's why the node has an option to *Clamp Factor*.
So if *Clamp Factor* is enabled, any factor that is larger than 1 will
return the second matrix.

## Inputs

- **Factor(s)** - A float or float list that controls the amount of each matrix(ces) input
    to the output, where 0 means the first matrix(ces) only and 1 means the
    second matrix(ces) only.
- **A** - First matrix(ces).
- **B** - Second matrix(ces).

## Outputs

- **Result(s)** - The resultant matrix(ces) of mixing the two matrices or matrix lists by
    the input factor(s).
