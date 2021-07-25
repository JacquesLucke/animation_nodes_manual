---
title : Mix Quaternions
---

## Description

This node mixes between two quaternions based on a factor. The mixing is done
using a spherical interpolation which ensures a linear angular rate of change of
rotation.

## Inputs

- **Factor** - A float that controls the amount of each quaternion
    input to the output, where 0 means the first quaternion only and 1
    means the second quaternion only.

## Outputs

- **Result** - The resultant quaternion of mixing the two quaternions
    by the input factor.

## Note

The way *Mix Quaternions* works, a factor that is larger than 1 won't be
clamped but rather multiplied to the second quaternion. That's why the
node has an option to *Clamp Factor*. So if *Clamp factor* is enabled,
Any factor that is larger than 1 will return the second quaternion.
