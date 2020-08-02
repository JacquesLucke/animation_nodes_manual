---
title : Noise Falloff
---

## Description

This node constructs a position-based falloff where the falloff value of the
element is the target noise evaluated at the element's position. The node
supports many types of noises including *Perlin*, *Simplex*, *Value*, *Cubic*,
*Cellcular (Voronoi)*, and *White Noise*. The node also supports fractal
versions of the noises as well as distorted versions.

## Inputs

- **Seed** - A seed value.
- **Amplitude** - The maximum value of the noise.
- **Frequency** - The frequency of the noise.
- **Axis Scale** - A vector controlling the frequency of the noise along each
  axis individually.
- **Offset** - An offset that is added to the input elements before evaluation.
  The offset can be used as a continues seed or for animating the noise.
- **Octaves** - The number of octaves to be added. Higher values corresponds to
  more detailed noises but increases the execution time.
- **Jitter** - The amount of randomness in the cellular noise. A lower value
  corresponds to a more uniform pattern.

## Outputs

- **Falloff** - The output falloff.

## Advanced Node Settings

- **Fractal Type** - The method used to add the octaves of the noise.
- **Pertube Type** - The method used to distort the noises.
- **Distance** - The distance metric used to compute the cellular noise.
