---
title : Get Spline Samples
weight : 1
---

## Description

This node will return <span class="title-ref">n</span> number of points
along with their tangent vectors where <span class="title-ref">n</span>
is the **Amount** input, Those points are points on the spline in the
input interval that are distributed based on the evaluation
option---Uniform or Resolution.

![image](get_spline_samples_node.png)

## Inputs

  - **Spline** - A spline to evaluate.
  - **Amount** - The amount of point to return.
  - **Start** - The starting point of the interval.
  - **End** - The ending point of the interval.

## Outputs

  - **Positions** - A vector list that contains the evaluated points
    positions.
  - **Tangent** - A vector list that contains vectors that are aligned
    with the tangent line to the evaluated points.

## Advanced Node Settings

  - **Resolution** - It is the quality of the evaluated spline, in other
    words, it is the number of handles in the spline used in evaluation.

## Examples of Usage

{{< video get_spline_samples_node_example.mp4 >}}
