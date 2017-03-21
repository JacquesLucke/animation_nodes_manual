Options
-------

- **Uniform** - This option samples the points regardless of the geometry of the spline.
- **Resolution** - This option samples the points based on the geometry of the spline.

To understand this better lets look at the following example:

.. image:: /includes/nodes/images/uniform_vs_resolution_interpolation.png

The above example shows 2 identical splines where the upper one uses **Uniform** and the other uses **Resolution**.
If one were to sample some points at regular intervals on both splines, He would observe that:

- Points on **Uniform** are regularly distributed.
- Points on **Resolution** are dense at some areas and spaced at others.

So we notice that **Resolution** care about the geometry of the spline and so a regularly spaced parameters will be closer at parts of the spline where it has dense geometry and spaced at relaxed parts.

**Uniform** on the other hand will yield results based on the actual distance along the spline, however, it is much slower to compute.
