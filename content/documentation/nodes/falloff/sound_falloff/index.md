---
title : Sound Falloff
---

## Description

This node constructs a falloff from the input sound. The nature of the falloff
depends on the mode of operation of the node. All mode of operations have a
number of common inputs and options that we shall introduce in the following
sections.

## Inputs

- **Sound** - The input sound.
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
- **Low** - The lowest sound frequency to be considered. A value of zero means
  the lowest possible frequency while a value of one means the highest possible
  frequency.
- **High** - The highest sound frequency to be considered. A value of zero
  means the lowest possible frequency while a value of one means the highest
  possible frequency.
- **Scene** - The target scene. This only affects the frame rate of the
  animation.

## Outputs

- **Falloff** - The output falloff.

## Advanced Node Settings

- **Fade To Zero** - The node will consider the intensity of the terminal
  frequencies to be zero.
  - **Low Frequencies** - The node will consider the intensity of the low
    requency to be zero.
  - **High Frequencies** - The node will consider the intensity of the high
    requency to be zero.
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

## Types

### Average

In this mode of operation, the output falloff will be an index-based falloff
where the falloff value of an element is equal to the average spectral
intensity between the input low and high frequencies at a certain time. The
element at index 0 will have the average value at the input frame, the element
at index 1 will have the average value of the frame preceding the input frame
by a certain interval, and so on. See the *scale* input below for more
information about the interval.

One can think of this mode of operation as an average intensity with a temporal
trail. As the index increase, the value is the average intensity at some
previous frame. Consequently, this mode of operation can be rather expensive
for any moderately large evaluation domain, since many spectral analyses has to
be performed in a single execution.

#### Inputs

- **Scale** - The scale defines the length of the interval at which values are
  sampled. For an input scale `s` and an input frame `t`, the values will be
  sampled at `t`, `t - s`, `t - 2s`, and so on.

### Spectrum Index

In this mode of operation, the output falloff will be an index-based falloff
where the falloff value of an element is equal to the spectral intensity at a
certain frequency. The node only computes a limited number of spectral
intensities, called the frequency bins. The frequency bins will be distributed
along the input distribution in the frequency domain specified by the input low
and high values. See the inputs in the following section for more information.

#### Options

- **Extension Type** - The number of elements that will be assigned to the
  computed frequency is limited and is controlled by the *Length* input. Other
  elements will be given values by extending the range somehow. The extension
  mechanisms available are listed as follows.
  - **Loop** - The frequency bins will be repeated. For instance, if the input
    *length* is set to 10, elements with indices from 0 to 9 will be assigned
    the computed frequency bins from the lowest frequency to the highest in
    order, elements with indices from 10 to 19 will be assigned the same
    freqiuency bins from the lowest frequency to the highest in order, and so
    on.
  - **Mirror** - The frequency bins will be ping-pong repeated. For instance,
    if the input *length* is set to 10, elements with indices from 0 to 9 will
    be assigned the computed frequency bins from the lowest frequency to the
    highest in order, elements with indices from 10 to 19 will be assigned the
    same freqiuency bins but from the highest frequency to the lowest in order,
    and so on.
  - **Extend Last** - The extra elements will be assigned the value of the
    last frequency bin.

#### Inputs

- **Count** - The number of frequency bins to compute.
- **Distribution** - An interpolation that defines the distribution of the
  frequency bins. Typically, an exponential distribution will be used to get
  more bins from the low frequency regions as opposed to the high frequency
  regions.
- **Length** - The number of elements that will be assigned the frequency bins.
  If more elements are evaluated, the frequency bins will be extended depending
  on the extension type explained above.
- **Offset** - An offset that is added to the index of the element before
  evaluating the falloff. The offset can be used in conjunction with extensions
  to move the start and end of the frequency bins.

### Spectrum Falloff

In this mode of operation, the output falloff will be an index-based falloff
just like the *Spectrum Index* mode. The only difference is that the index of
the elements will be the value of the input falloff at the element. So, in
reality, it is a falloff-based falloff. For instance, if the input falloff is a
*Point Distance* falloff, the elements closer to the center will be assigned
the lowest frequencies while the elements further away will be assigned the
highest frequencies.

#### Inputs

- **Falloff** - The input falloff.
