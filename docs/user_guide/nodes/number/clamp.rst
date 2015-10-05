Clamp
======

The clamp node is used to make sure a value is in a certain range. If it is not the output value is clamped / clipped to the maximum or minimum value.

**Inputs:**
- Value
- Max
- Min

**Behavior:**

If Min <= Value <= Max **Output:** Value
If Value > Max **Output:** Max
If Value < Min **Output:** Min