---
title : Radial Falloff
---

## Description

This node creates a vector based falloff that associates a float to every
vector. The float is equal to the normalized angle between the projection of two
vectors on the plane defined by the inputs. The first vector is the positive x
axis and the second vector is the vector in question.

## Demonstration

The simplest case is when the input plane is the XY plane, in which case, the
falloff value will be the normalized angle between the 2D projection of the
vector and the positive x axis. By normalized we mean that the angle will have a
range from 0 to 1 as opposed to from 0 to two Pi. This can be conceptually
generalized to any plane in space by a 3D rotation.

## Inputs

- **Origin** - The center of the plane.
- **Normal** - The normal of the plane.
- **Phase** - Each unit of the phase corresponds to a full rotation around the
  normal of the plane. Alternatively, one can think of this input as an addition
  to the output followed by a modulo 1 operation.

## Outputs

- **Falloff** - The actual falloff object.
