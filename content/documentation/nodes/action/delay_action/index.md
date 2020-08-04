---
title : Delay Action
---

## Description

This node delay the starting time of the input bounded action.

## Options

- **Relative** - If enabled, the input delay amount will be multiplied by the
  evaluation index. In other words, when evaluating the action with an index of
  0, there will be no delay, when evaluating with an index of 1, the delay will
  be the input delay amount, when evaluating with an index of 2, the delay will
  be double the input delay amount, and so on.

## Inputs

- **Action** - The input action.
- **Delay** - The delay amount in number of frames.

## Outputs

- **Action** - The output action.
