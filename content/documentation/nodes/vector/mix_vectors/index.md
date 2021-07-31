---
title : Mix Vectors
---

## Description

This node linearly mixes between two vectors or two vector lists based on a factor or factor list.

## Options

- **Clamp** - If enabled, a factor that is larger than one will be rendered one
    and a factor that is negative will be rendered zero.  Subsequently, the
    output will be in the range of the input floats.  If disabled, the result is
    computed based on the equation `A(1-F)+B\*F` (Where `F` is the factor, `A`,
    and `B` are the first and second floats) which accordingly may result in
    strange results for negative factors or factors that are larger than one.

## Inputs

- **Factor(s)** - A float or float list that controls the amount of each vector(s) input to the
    output, where 0 means the first vector(s) only and 1 means the second vector(s) only.
- **A** - First vector(s).
- **B** - Second vector(s).

## Outputs

- **Result(s)** - The result vector(s) of mixing the two vectors or vector lists by the input factor(s).
