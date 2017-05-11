Intersect Sphere Sphere
=======================

Description
-----------

This node returns some information about the intersection of the two input spheres.

.. image:: images/intersect_sphere_sphere_node.png
   :width: 160pt

Illustration
------------

.. image:: images/intersect_sphere_sphere_node_illustration.png

Orange point is the center of the blue intersected circle.

Inputs
------

- **Sphere 1 Center** - The location of the center of the first required sphere.
- **Sphere 1 Radius** - The radius length of the first required sphere.
- **Sphere 2 Center** - The location of the center of the second required sphere.
- **Sphere 2 Radius** - The radius length of the second required sphere.

Outputs
-------

- **Circle Center** - The location of the center of the intersected circle.
- **Circle Radius** - The radius length of the intersected circle. if this values is zero and Is valid is True, that means that the spheres are touching at the Circle Center.
- **Is Valid** - A boolean which is True if an intersection was found, and False otherwise.

Advanced Node Settings
----------------------

- N/A
