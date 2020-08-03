---
title : Decompose Text
---

## Description

This node takes a text and decomposes it into characters, words, or lines and
returns the elements with their position in 3D space as a form of matrices.

## Options

- **Decompose Type** - The method used for decomposition, can be character
  decomposition or word decomposition.

## Inputs

- **Text** - The input text.
- **Font** - The font to be used. Can't be the default Blender font `BFont`.
- **Size** - The size of the text in 3D space.
- **Character Spacing** - The spacing between characters.
- **Word Spacing** - The spacing between words.
- **Line Spacing** - The spacing between lines.
- **Alighnment** - The horizontal alignment of text. Can be `LEFT`, `RIGHT`, or
  `CENTER`.
- **Include White Spaces** - If enabled, white spaces will be included in the
  output.

## Outputs

- **Transoforms** - The output transforms of the elements.
- **Characters/Words** - The elements.
- **Length** - The number of elements.
