---
title : Float Range
---

## Description

This node is used to generates a float list that represents an arithmetic
sequence.

## Options

- **Start/Step** - This option allows you to define the arithmetic sequence by
  a starting value and a *Step* value which is the difference between each two
  consecutive terms.
- **Start/Stop** - This option allows you to define the arithmetic sequence by
  a starting value and an end value.
    - **Include End Point** - If enabled, stop value will be included in the
      sequence, otherwise, it will not be included.

## Inputs

- **Amount** - The length of the arithmetic sequence which is also the length
  of the output integer list.
- **Start** - It is the starting value of the arithmetic sequence.
- **Step** - It is the difference between each two consecutive terms of the
  arithmetic sequence. (Only available in the *Start/Step* option)
- **Stop** - It is the end value of the arithmetic sequence.  (Only available
  in the *Start/Stop* option)

## Outputs

- **Float List** - A float list that contains the generated floats.
