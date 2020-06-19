---
title : Sound From Sequences
weight : 1
---

## Description

When sounds are baked using the *Sound bake* node, they are in fact
added to the sequence editor at a certain channel, and you can select a
sound by its location in the sequencer channels.

![image](sound_from_sequences_node.png)

## Options

  -   - **Sound Type**:
        
          - **Average** - Returns the sound which was baked using the
            **Bake Average** button.
          - **Spectrum** - Returns the sound which was baked using the
            **Bake Spectrum** button.

## Inputs

  - **Sequences** - The sequences at which the sound strips exist, you
    can get sequences list by using the *Sequences From Channel* node.
  - **Bake Index** - The index of the baked data. Multiple sound data
    can be baked using the *Sound Bake* node and this index let you
    choose which one to get.

## Outputs

  - **Sound** - The sound data of the sound strip.

## Advanced Node Settings

  - N/A

## Examples of Usage

{{< video evaluate_sound_node_example.mp4 >}}
