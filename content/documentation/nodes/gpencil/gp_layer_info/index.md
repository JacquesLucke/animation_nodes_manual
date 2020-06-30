---
title : GP Layer Info
weight : 20
---

## Description

This node returns some information about the gp layer like its frame(s), name, and blend mode, etc.

## Options

- **Frame Type** -
  - *Active* - This option outputs the active frame of the input gp layer.
  - *Frame Index* - This option allows to choose a frame by index of the input gp layer.
  - *Frame Number* - This option allows to choose a frame by frame-number of the input gp layer.
  - *All Frames* - This option outputs all frames of the input gp layer.

## Inputs

- **Layer** - A gp layer.
- **Scene** - The scene the object belong to.

## Outputs

- **Frame(s)** - A gp frame or A gp frame list that includes all the gp frames of the input gp layer.
- **Name** - The name of the input gp layer.
- **Blend Mode** - The blend mode of the input gp layer, *e.g., REGULAR, ADD, SUBTRACT, etc*.
- **Opacity** - The opacity of the input gp layer.
- **Use Lights** - Enable the use of lights on gp strokes and fill materials.
- **Tint Color** - The tint color of the input gp layer that tints the stroke colors.
- **Tint Factor** - Factor of tinting colors.
- **Stroke Thickness** - This changes the thickness of strokes in pixels.
- **Pass Index** - This is the 'Layer Index' pass of the input gp layer.
- **Mask Layers** - A gp layer list that is used for masking the input gp layer.
- **Invert Mask Layers** - A boolean list that allows to invert the mask layers.
