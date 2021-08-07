---
title : Evaluate MIDI Track
---

## Description

This node evaluates the input MIDI track at the input time. Evaluating a track
in this context means evaluating the *ADSR* envelope of the note currently
playing on a certain channel with a certain note number with a maximum sustain
level. This means that the output of the evaluation will be zero at the start of
the note and will gradually increase to reach 1 in a time period called the
*Attack Time* and after the note ends, the output will gradually decrease from 1
to reach zero in a time period called the *Release Time*. Both periods can have
custom interpolations to define how fast the values decrease or increase. There
are two modes of evaluation. You can either evaluate a single note number or all
128 note numbers at the same time.

## Options

- **Single** - Only a single note number is evaluated.
- **All** - All 128 note numbers are evaluated.

## Inputs

- **Track** - The MIDI track to evaluate.
- **Frame** - The frame to evaluate the track at.
- **Channel** - The MIDI channel to evaluate the track at.
- **Note Number** - The MIDI note number to evaluate the track at. This is only
  available in the *Single* option.
- **Attack Time** - The attack time of the ADSR envelope.
- **Attack Interpolation** - An interpolation describing the rate of increase of
  the note value up to the maximum sustain level.
- **Release Time** - The release time of the ADSR envelope.
- **Attack Interpolation** - An interpolation describing the rate of decrease of
  the note value to zero.
- **Scene** - Only used to get the FPS to compute the time from the input frame.

## Outputs

- **Note Value(s)** - The value(s) of the note(s) at the current time.

## Tutorials

- [MIDI]({{< ref "/tutorials/midi" >}})
