---
title : Evaluate FCurve
weight : 1
---

## Description

This node evaluates a fcurve at a specific frame.

For a fcurve that correspond to the x-location of an object, evaluating
the fcurve at a frame will return the x-location of the object at that
frame.

![image](evaluate_fcurve_node.png)

## Option

- **Offset** - The input frame is relative to the current frame. So an
    input frame of 5 with the current frame at 5, the actual evaluation
    will be at frame 10.
- **Absolute** - The input frame is the frame at which evaluation will
    happen.

## Inputs

- **FCurve** - An fcurve to evaluate.
- **Frame** - The frame at which the fcurve is evaluated.

## Outputs

- **Value** - The value of fcurve at the input frame.

## Advanced Node Settings

- N/A

## Examples of Usage

{{< video evaluate_fcurve_node_example.mp4 >}}
