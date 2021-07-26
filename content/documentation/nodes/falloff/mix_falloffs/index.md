---
title : Mix Falloffs
---

## Description

This node takes two or multiple falloffs and mix them together using one
of the available algorithms.

## Options

- **Max** - The output float will be the largest float of all falloffs.
- **Min** - The output float will be the lowest float of all falloffs.
- **Add** - The output will be the sum of the floats of the falloffs.
- **Subtract** - The output will be the difference between the floats of the
  falloffs.
- **Multiply** - The output will be the product of the floats of the falloffs.
- **Overlay** - The B falloff is added to the A falloff such that the addition
  is full when A is equal to 0.5 and decreases gradually as A goes to zero or
  one. For instance, if A is a linear falloff that goes from zero to one and B
  is a random falloff, the output will be a linear falloff with some randomness
  such that the randomness is maximum at the mid point at 0.5 and none existent
  at the start and end of the linear falloff.
- **Use Falloff List** - It is the option you see beside the menu, if enabled,
  the input will be a falloff list. This is not available for the *Subtract* and
  *Overlay* option, as they are not commutative.

## Inputs

- **A** - A falloff.
- **B** - A falloff.
- **Falloffs**- The falloffs. If *Use Falloffs List* is enabled.

## Outputs

- **Falloff** - The actual falloff object.
