---
title : Time Info
---

## Description

This node returns some information about scene playback.

## Inputs

- **Scene** - A scene to return its playback information.

## Outputs

- **Frame** - Current frame. It is a float because of existence of
    subframes.
- **Start Frame** - First frame of the scene playback range.
- **End Frame** - Last frame of the scene playback range.
- **Frame Rate** - The frame rate of the playback.
