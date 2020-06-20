---
title : Sequence Info
weight : 1
---

## Description

This node returns some information about the input sequence.

![image](sequence_info_node.png)

## Inputs

- **Sequence** - A strip to return its info.

## Outputs

- **Name** - The name of the strip.
- **Type** - The type of strip.(TEXT,SOUND,IMAGE,...)
- **Channel** - The index of its channel.
- **Final Duration** - The actual length of the strip in frames.
- **Final Start Frame** - The actual frame at which the strip start.
- **Final End Frame** - The actual frame at which the strip end.
- **Opacity** - The opacity of the strip. (Only for visual strips like
    images and movies)
- **Blend Type** - The blending algorithm of the strip. (Only for
    visual strips like images and movies)
- **Effect Fader** - The fading factor for certain effect.
- **Start Frame** - The frame at which the strip start in regardless
    of the trimming and effects.
- **Start Offset** - The difference between the original and final
    start frame.
- **End Offset** - The difference between the original and final end
    frame.
- **Total Duration** - The length of the strip in frames in regardless
    of the trimming and effects.
- **Still Frame Start** - The frame at which the image strip start.
- **Still Frame End** - The frame at which the image strip end.
- **Lock** - A boolean which is True if *Transformation Lock* is
    enabled for the strip.
- **Mute** - A boolean which is True if *Mute* is enabled for the
    strip.
- **Select** - A boolean which is True if the strip is selected.
- **Speed Factor** - The speed factor of the *Speed Control* strip.
    (Assuming *Stretch to input strip length* is disabled and *Use as
    speed* is enabled for the *Speed Control* effect)
- **Use Default Fade** - A boolean which is True if *Use Default Fade*
    is enabled.
- **Use Default Fade** - A boolean which is True if *Use Linear
    Modifiers* is enabled.

## Advanced Node Settings

- N/A

## Examples of Usage

{{< video sequence_info_node_example.mp4 >}}
