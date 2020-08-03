---
title : Trim Text
---

## Description

This node lets you cut a number of characters from the input text either
from start or from the end.

It will return the text that start at the character with index **Start**
and end at the character at index **End**. So if I set the start index
to be 0 and the end index to be 5 the output will be "Anima".

## Options

- **Start** - This option lets you set the starting index. If it is
    disabled, then it will be considered zero.
- **End** - This option lets you set the ending index. If it is
    disabled, then it will be considered the last index.

## Inputs

- **Text** - An input text to trim.
- **Start** - The start index.(integer)
- **End** - The end index.(integer)

## Outputs

- **Text** - The output string.

## Advanced Node Settings

- **Negative Indices** - If enabled, you can enter negative indices in the
  start and end inputs. A negative index `-i` means the index `n-i` where `n`
  is the number of letters.
