Falloff
*******

This whole category was newly added and it provide a high level approach to controlling effects and animating them. Below is some of the nodes that is includes with it.

Fade Falloff
============

This falloff can be used to fade between two values, in the example below, we fade between 0 and 1 scale of some object where the starting point is the inverse of the current frame.

.. image:: images/fade_falloff.gif

Delay Falloff
=============

This falloff can be used to delay the effect of some objects than other based on time, in the below example, we make some objects appear earlier than others.

.. image:: images/point_distance_id.gif

Wiggle Falloff
==============

This falloff can be used to control an effect based a noise function, in the example below, we move the vertices up with some factor we got from the noise function.

.. image:: images/wiggle_falloff.gif

Random Falloff
==============

Much like the wiggle falloff, this can be used to control and effect based on a random factor except this factor is completely random and can't be animated, it is much faster than wiggle falloff so use this node if you are not going to animate.

.. image:: images/random_falloff.gif

Index Mask Falloff
==================

This falloff choose between two factors based on some pattern, a possible pattern is the nth pattern like ABABAB or ABBABBABB or ABBBABBBABBB ... . A possible pattern is also a random pattern like ABAABAbABAbAA.

.. image:: images/index_mask_falloff.gif

Object Controller Falloff
=========================

This falloff can be used to control an effect based on the distance some object (usually an empty) where the size of the object control the offset of that falloff. The distance can be a normal euclidean distance as the following example:

.. image:: images/object_controller_falloff1.gif

Or a distance along the local axis of the object, like this example:

.. image:: images/object_controller_falloff2.gif

Sound Falloff
=============

Sound falloff provide a much more efficient way to evaluate baked sound data. You can evaluate the sound data based on the object indices or based on another falloff ! So I may use a point distance falloff no evaluate the sound data resulting in this radial sound visualization:

.. image:: images/sound_falloff.gif

Spline Falloff
==============

Spline falloff enables you to control and effect based on the shortest distance to some spline object.

.. image:: images/curve_falloff.gif

Constant Falloff
================

Constant Falloff is the default falloff where it just set a constant factor for all effects' objects.

Custom Falloff
==============

Custom falloff lets you create a falloff from a list of factors for total control.

Directional Falloff
===================

Directional falloff lets you control an effect based on the distance along some vector from some point. It is the same as the direction option in the object controller falloff but inputs are exposed and not controlled by an object.

.. image:: images/directional_falloff.gif

Point Distance Falloff
======================
Point distance falloff lets you control an effect based on the distance to some point. It is the same as the sphere option in the object controller falloff but inputs are exposed and not controlled by an object.

.. image:: images/point_distance_falloff.gif

Interpolate Falloff
===================

This node lets you edit falloffs based on an interpolation.

.. image:: images/interpolate_falloff.gif

Remap Falloff
=============

This node remaps the floats of the input falloff to a new range. The node assumes that the original range was ``[0,1]``, which is usually the case.

.. image:: images/remap_falloff_node_example.gif


Invert Falloff
==============

This node invert the factors of the input falloff.

.. image:: images/invert_falloff.gif

Mix Falloff
===========

This node mixes between two falloffs, mixing can be done by taking the maximum or the minimum of the falloffs, it can also be the sume or multiple of both falloffs.

.. image:: images/mix_falloff.gif

Evaluate Falloff
================

This node returns the factors of the input falloff evaluated at the inputs, in essence, a falloff just associates a float (factor) to every object either based on its transforms or index, this factor or float is then used to mix between effects. Here is an example of a falloff evaluate at the locations of the cubes:

.. image:: images/evaluate_falloff.gif
