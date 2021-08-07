---
title : MIDI Note Info
---

## Description

This node returns the information stored in the input MIDI note.

## Inputs

- **Note** - The input MIDI note.

## Outputs

- **Channel** - The channel of this note. An integer between 0 and 15 inclusive.
- **Note Number** - The number of this note. An integer between 0 and 127
  inclusive.
- **Time On** - The time in seconds at which the note started playing.
- **Time Off** - The time in seconds at which the note finished playing.
- **Velocity** - The velocity at which the note was played. A value between 0
  and 1.

## Tutorials

- [MIDI]({{< ref "/tutorials/midi" >}})
