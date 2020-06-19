---
title : Float To Text
weight : 1
---

## Description

This node forms a text out of a number.

![image](float_to_text_node.png)

## Inputs

  - **Number** - The number to be converted.
  - **Min Length** - The minimum number of characters in the output
    text. If The number is too short, zeroes are inserted to the left of
    the number to match the input minimum.
  - **Decimals** - The number of decimal numbers in the output text, if
    it exceed the number of decimals of the input number, zeroes are
    inserted at the end.
  - **Insert Sign** - A boolean which if true, a plus sign will be added
    to the left of the number if it was positive and negative otherwise.

## Outputs

  - **Text** - The output text.

## Advanced Node Settings

  - N/A

## Examples of Usage

{{< video float_to_text_node_example.mp4 >}}
