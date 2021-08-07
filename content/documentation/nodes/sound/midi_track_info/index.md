---
title : MIDI Track Info
---

## Description

This node returns the information stored in the input MIDI track.

## Inputs

- **Track** - The input MIDI track.

## Outputs

- **Notes** - A list of MIDI notes inside the input track.
- **Name** - The name of the MIDI track. If no name is specified in the track,
  this will be an empty text. If multiple names were provided, the name provided
  in the last event will be returned.
- **Index** - The index of the track in the MIDI file.

## Tutorials

- [MIDI]({{< ref "/tutorials/midi" >}})
