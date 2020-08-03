---
title : L-System
---

## Description

This node implements an L-System. First, the node computes the system symbols
from the initial axiom and set of rules, then, the symbols are used to
construct a mesh based on the parameters of the node.

## Rules

In each iteration of the system, the rules are applied on the symbol list that
is initially the input axiom symbol list. The rules are applied by replacing
the symbols on the left hand side by the symbols on the right hand side. The
symbols on the left hand side, called the *Variables*, can be any of `A`, `B`,
`X`, `Y`, or `Z` in addition to the command symbols described below. The left
and right hand sides are separated by an equal sign. Spaces are ignored For
instance, the following are some rules that can be used.

```
F = F--F
A = A+A/B\A-A
```

## Grammar

The system is modeled after a *Tutle Graphics* system, where a *turtle* moves
in space and the generated geometry is a trace of its movements. In such
systems, the turtle is a system state storing a location, an orientation, a
step size, and a width. The grammar of the system defines how the symbols
corresponds to turtle movements. Essentially, symbols change the state of the
turtle and we call them *commands*.

### Commands

The following are the list of supported commands.

#### F

Move the turtle forward along its local orientation creating geometry in the
process. The magnitude of the movement is equal to the step size.

#### f

Move the turtle forward along its local orientation **without** creating
geometry in the process. The magnitude of the movement is equal to the step
size.

#### [

Start a new branch. A branch is a subsystem where the turtle move freely until
the branch is terminated, in which case, the turtle reverts back to its state
right before the branch started.

#### ]

End the last started branch.

#### "

Scale the step size by the input *Scale Step Size*.

#### !

Scale the width by the input *Scale Width*.

#### +

Rotate the turtle by the input *Angle* along the local Y axis in the positive
direction.

#### -

Rotate the turtle by the input *Angle* along the local Y axis in the negative
direction.

#### &

Rotate the turtle by the input *Angle* along the local X axis in the positive
direction.

#### ^

Rotate the turtle by the input *Angle* along the local X axis in the negative
direction.

#### \

Rotate the turtle by the input *Angle* along the local Z axis in the positive
direction.

#### /

Rotate the turtle by the input *Angle* along the local Z axis in the negative
direction.

#### ~

Rotate the turtle by a random Euler whose components have a maximum magnitude
of the input *Random Angle*.

#### T

Rotate the turtle in the global negative Z direction by the input *Gravity*.
This simulate gravity during movement.

#### J

Append the current orientation of the turtle to the output *J States* list.

#### K

Append the current orientation of the turtle to the output *K States* list.

#### M

Append the current orientation of the turtle to the output *M States* list.

#### A

Ignored.

#### B

Ignored.

#### X

Ignored.

#### Y

Ignored.

#### Z

Ignored.

## Inputs

- **Axiom** - The initial symbol list.
- **Rules** - A text list including the rules to be applied.
- **Generations** - The number of iterations to compute. See the *Only Partial
  Moves* input for more information.
- **Step Size** - The initial step size for the `F` and `f` commands.
- **Angle** - The initial angle for the rotation commands.
- **Seed** - A seed for the random commands.
- **Scale Width** - The scaling factor for the `!` command.
- **Scale Step SIze** - The scaling factor for the `"` command.
- **Gravity** - The magnitude if velocity resulted from gravity for the `T`
  command.
- **Random Angle** - The magnitude of the maximum value for the random Euler
  components for the `~` command.
- **Only Partial Moves** - For fractional generations value, the movements and
  rotations in that last iteration would only be partial, that is, the step
  sizes and angles would be multiplied by the fractional part. If this input is
  True, only the step sizes will be partial, that is, rotations will be done in
  full.

## Outputs

- **Mesh** - The output mesh.
- **Edge Widths** - The width of the edges of the mesh.
- **Sybmols** - The final computed symbols list as a text.
- **J** - The list of all *J States* appended by the `J` command.
- **K** - The list of all *K States* appended by the `K` command.
- **M** - The list of all *M States* appended by the `M` command.

## Advanced Node Settings

- **Symbol Limit** - If enabled, the node will stop computing after the
  specified number of symbols is reached.
- **Preset** - Use one of the available presents.
