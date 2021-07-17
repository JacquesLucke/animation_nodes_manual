---
title : Repeat List Elements
---

## Description

This node is used to repeat the elements of the list a specific number of times.
For instance, repeating the elements of the list `[0, 1, 2]` three times will
return `[0, 0, 0, 1, 1, 1, 2, 2, 2]`. If the amount of repetition is a list,
then each amount list element controls the amount of repetitions for its
corresponding element in the list.

## Inputs

- **List** - An input list.
- **Amount(s)** - The number of repetitions.

## Outputs

- **List** - The repeated list.

## Advanced Node Settings

- **Make Element Copies** - Copy the element before repeating them.
    This makes sure the elements are independent of the original
    elements in the list and so changing those elements won't affect the
    following repetitions.
- **Change type** - Change the type of the list to another list type.
