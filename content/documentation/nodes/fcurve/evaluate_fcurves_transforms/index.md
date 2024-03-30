---
title : Evaluate FCurves Transforms
---

## Description

This node evaluates the location, rotation, and scale fcurve at a specific
frame, returning the transformation of the object at that frame.

## Option

- **Offset** - The input frame is relative to the current frame. So an
    input frame of 5 with the current frame at 5, the actual evaluation
    will be at frame 10.
- **Absolute** - The input frame is the frame at which evaluation will
    happen.

## Inputs

- **FCurves** - A list of fcurves from which the transformation fcurves will be
  evaluated. Non transform fcurves will be ignored.
- **Frame** - The frame at which the fcurve is evaluated.

## Outputs

- **Matrix** - The evaluated transformation in the form of a matrix.
- **Frame** - The input frame delayed by the duration of the fcurve.

