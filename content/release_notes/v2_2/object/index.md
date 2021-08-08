---
title : Object
---

## Shade Object Smooth

The *Smooth* socket of the *Shade Object Smooth* node now have an *Is Used*
property, if enabled, the node will take effect, otherwise the node will be
disabled and will not take effect.

## Object Attribute Output

The *Value* socket of the *Object Attribute Output* node now have an *Is Used*
property, if enabled, the node will take effect, otherwise the node will be
disabled and will not take effect.

## Copy Object Modifiers

The *Copy Object Modifiers* node was added. This node copies the modifiers of
some source object into some target object. The modifiers in the target object
is first cleared and is effectively overwritten.

## Update Object Matrices

The *Update Object Matrices* node was removed. The node never worked correctly
and was confusing to the end user. The *Evaluate Object* node was added as an
alternative, though its use is discouraged.

## Get Selected Objects

The output of the *Get Selected Objects* node is no longer ordered by the
selection order. This is because ordering the objects was a very expensive
background process.

## Evaluate Object

The *Evaluate Object* node was added. The node force evaluate the object after
changes have happened in the node tree.

## Object Attribute Input

A new *Evaluate Object* option was added. If enabled, the object will be
evaluated before retrieving the target attribute.

## Object Instancer

The *Object Instancer* node is about 4x faster.
