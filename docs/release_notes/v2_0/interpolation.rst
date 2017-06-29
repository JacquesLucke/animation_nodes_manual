Interpolation
*************

Interpolations From Curve Mapping >> Curve Interpolation
========================================================

The Interpolation From Curve Mapping node was renamed to Curve Interpolation. The node now support caching of interpolation for tremendously faster future large evaluation. Below is a curve interpolation with and without cache option.

.. image:: images/curve_interpolation.png

Mix Interpolation
=================

This newly added node mixes between two interpolation using one of two algorithms. **Overlay** which simply overlay both interpolation where zero means the first interpolation and 1 means the second. **Chain** which stack input interpolations beside each others, below is a visualization for what chain option does, the first interpolation is a linear one while the second interpolation is an exponential one, both interpolations are remapped based on End 1 and Start 2 inputs then they are stacked beside each other with some fading.

.. image:: images/mix_interpolation.png

Mirror Interpolation
====================

This newly added node invert the interpolation and possibly combine it with the original if chain was checked (Resulting in a mirror).

.. image:: images/mirror_interpolation.gif
