---
title : Evaluate Sound
weight : 1
---

## Description

This node returns the baked data---Ones that are baked using the sound
bake node.

![image](evaluate_sound_node.png)

## Options

  -   - **Type**:
        
          - **Average** - Returns a float that represent the intensity
            of the sound---Those that are baked using the Bake button
            and not the Bake Equalizer Data.
          - **Spectrum** - Returns a list of floats that represent the
            intensity of the frequencies---Those that were baked using
            the Bake Spectrum button.

## Inputs

  - **Sound** - An input sound to evaluate.
  - **Frame** - The frame at which the sound is evaluated. (Only
    available when **Use Current Frame** is disabled.)

## Outputs

  - **Volume** - The intensity of the sound at the current frame. (Only
    available in **Average** option)
  - **Volumes** - A float list that contain the intensities of the
    *Spectrum Data*. (Only available in **Spectrum** option)

## Advanced Node Settings

  - **Use Current Frame** - If enabled, the sound will be evaluated at
    the current frame, if not, the sound will be evaluate at the input
    frame.

## Examples of Usage

{{< video evaluate_sound_node_example.mp4 >}}
