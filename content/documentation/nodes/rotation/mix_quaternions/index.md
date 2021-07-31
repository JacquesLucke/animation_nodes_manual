---
title : Mix Quaternions
---

## Description

This node mixes between two quaternions or quaternion lists based on a factor or
factor list. The mixing is done using a spherical interpolation which ensures a
linear angular rate of change of rotation.

## Options

- **Clamp** - The way *Mix Quaternions* works, a factor that is larger than 1 won't be
    clamped but rather multiplied to the second quaternion. That's why the
    node has an option to *Clamp Factor*. So if *Clamp factor* is enabled,
    Any factor that is larger than 1 will return the second quaternion.

## Inputs

- **Factor(s)** - A float or float list that controls the amount of each quaternion(s)
    input to the output, where 0 means the first quaternion(s) only and 1
    means the second quaternion(s) only.
- **A** - First quaternion(s).
- **B** - Second quaternion(s).

## Outputs

- **Result(s)** - The resultant quaternion(s) of mixing the two quaternions or
    quaternion lists by the input factor(s).
