---
title : Booleans
weight : 1
---



## Compare Node

There is a new condition (`Is None`) which checks if the input is a
Python `None` object. Many types in AN are (by definition) never None.
However certain types (like Object, Sequence, Generic, ...) are allowed
to be None, so this mode only makes sense when used with one of those
types.

![image](compare_node.png)

## Logic Operators

Two new operators were added: `Not (A and B)`, `Not (A or B)`.

## Boolean List Logic

Two new options were added to the boolean list logic node: `Not All
True`, `Not All False`.

![image](boolean_list_logic.png)

## Number To Boolean

This node converts a number into a boolean in a standard way. If the
number is zero, it will return False and otherwise True.

![image](number_to_boolean.png)
