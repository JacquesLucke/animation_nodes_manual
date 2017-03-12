Options
-------

- **Uniform** - This option samples the points regardless of the geometry of the spline.
- **Resolution** - This option samples the points based on the geometry of the spline.

To understand this better lets look at the following example:

.. image:: /includes/nodes/images/uniform_vs_resolution_interpolation.png

The above example shows 2 identical splines, The splines have some small handles as well as large ones, the small handles shows high density parts(dense geometry)---You can see those parts where lines are close to each others---while the large ones show low density parts(relaxed geometry). If we were to plug some values`0.1`,`0.2`,`0.3`,... in the parameter input when using **Uniform** option, we will get some equally distant points---See upper spline---and that makes sense because we plugged in some numbers at regular intervals. Now If we were to plug some values`0.1`,`0.2`,`0.3`,... in the parameter input when using **Resolution** option, we will get some irregularly distant points---See lower spline---we plugged in some numbers at regular intervals and we got some points at different distances. We conclude that the **Uniform** option sample point in regardless of the geometry of the spline while **Resolution** option sample points based on the geometry of the spline. It is also observed that the **Uniform** option took much longer time to sample than the **Resolution** and that is the cost of using **Uniform**.
