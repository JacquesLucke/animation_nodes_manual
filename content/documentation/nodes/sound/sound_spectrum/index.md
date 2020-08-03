---
title : Sound Spectrum
---

## Description

This node spectrally analyse the input sound and return the spectral
intensities. The node have multiple modes of operations. All mode of operations
have a number of common inputs and options that we shall introduce in the
following sections.

## Inputs

- **Sound** - The input sound.
- **Frame** - The input frame to analyse the sound at.
- **Attack** - The *Attack Time*, a value that defines how fast the sound
  intensity increases. A low value means the sound intensity will rapidly
  increase, while a high value means the sound intensity will slowly and
  gradually increase. This value only have an effect if the *Smoothing Samples*
  in the *Advancted Node Settings* is not zero.
- **Release** - The *Release Time*, a value that defines how fast the sound
  intensity decrease. A low value means the sound intensity will rapidly
  decrease, while a high value means the sound intensity will slowly and
  gradually decrease. This value only have an effect if the *Smoothing Samples*
  in the *Advancted Node Settings* is not zero.
- **Amplitude** - The maximum value the sound intensity can reach.
- **Scene** - The target scene. This only affects the frame rate of the
  animation.

## Outputs

- **Spectrum** - The output spectrum intensities.

## Advanced Node Settings

- **Reduction Function** - To compute the intensity of the sound at a
  particular frequency, a range of neighbouring frequencies are sampled and
  are *reduced* to a single value through a reduction function. The possible
  reduction functions are as follows.
  - **Max** - The maximum of the frequencies is used.
  - **Mean** - The average of the frequencies is used.
- **Smoothing Samples** - The number of samples used to compute the
  intensities. Multiple samples are needed to achieve attack and release times.
  A high values results in a more accurate and smoother result but takes more
  time to compute.
- **Kaiser Beta** - Beta parameter of the *Kasier* window function. High values
  corresponds to higher main-lob leaking and lower side-lobe leaking. If you
  are not sure what that means, leave the value at 6.
- **Minimum Duration** - The minimum duration of the sound used to compute the
  spectrum. Higher values corresponds to higher spectral resolution but will
  have overlapping spectrum.

## Types

### Full

In this mode of operation, the full spectral data is returned.

### Single

In this mode of operation, the spectral data in the input range are reduced to
a single value and returned.

#### Inputs

- **Low** - The lowest sound frequency to be considered. A value of zero means
  the lowest possible frequency while a value of one means the highest possible
  frequency.
- **High** - The highest sound frequency to be considered. A value of zero
  means the lowest possible frequency while a value of one means the highest
  possible frequency.

### Custom

In this mode of operation, the spectral data between each two consecutive pins
are reduced and returned.

#### Inputs

- **Pins** - A list of floats between zero and one. Each two consecutive pins
  will define the frequency range of one output frequency bin. So the number of
  frequency bins will be equal to the number of pins minus one. A pin value of
  zero means the lowest possible frequency while a value of one means the
  highest possible frequency.

### Exponential

In this mode of operation, the spectral data is partitioned into a number of
frequency bins that are exponentially distributed, then each bin data is
reduced into a single value and returned.

#### Inputs

- **Count** - The number of frequency bins to compute.
- **Exponential Rate** - The rate of the exponential distribution. Higher
  values corresponds to more bins in the low frequency region. But be careful
  not to set this to a very high value or else most bins will have the same
  value.
