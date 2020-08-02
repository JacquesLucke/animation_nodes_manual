---
title : Mix Matrices
---

## Description

This node linearly mixes between two matrices based on a factor.

## Inputs

- **Factor** - A float that controls the amount of each matrix input
    to the output, where 0 means the first matrix only and 1 means the
    second matrix only.

## Outputs

- **Result** - The resultant matrix of mixing the two matrices by the
    input factor.

## Note

A factor that is larger than 1 won't be clamped but rather multiplied to
the second matrix. That's why the node has an option to *Clamp Factor*.
So if *Clamp Factor* is enabled, any factor that is larger than 1 will
return the second matrix.
