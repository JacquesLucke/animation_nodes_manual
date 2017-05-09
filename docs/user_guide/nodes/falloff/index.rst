Falloff
=======

.. toctree::
   :titlesonly:

   Fade Falloff <fade_falloff>
   Delay Falloff <delay_falloff>
   Wiggle Falloff <wiggle_falloff>
   Random Falloff <random_falloff>
   Index Mask Falloff <index_mask_falloff>
   Object Controller Falloff <object_controller_falloff>
   Sound Falloff <sound_falloff>
   Spline Falloff <spline_falloff>
   Constant Falloff <constant_falloff>
   Custom Falloff <custom_falloff>
   Directional Falloff <directional_falloff>
   Point Distance Falloff <point_distance_falloff>
   Interpolate Falloff <interpolate_falloff>
   Remape Falloff <remape_falloff>
   Invert Falloff <invert_falloff>
   Mix Falloff <mix_falloff>
   Evaluate Falloff <evaluate_falloff>

Abstractly speaking, a falloff is a function that associates a float to every input object. Those object can be vectors, matrices or indices. The computed floats are usually in the range of ``[0,1]`` but it is possible to go out of that range in some cases. Those floats can then be used as a factor for some effect where zero means no effect and one means full effect.

The simplest falloff is the **Constant Falloff** which associate a constant float for all input objects. A constant falloff is created automatically if no input falloff is provided.

The following example shows a node tree that creates 6 copies of a cube which all have a z-location of ``1.5``. While the offset matrices node moved every matrix ``3`` units in the z direction, the constant falloff---Which associated a float of ``0.5`` for every matrix---tuned down the effect of that translation to be ``3x0.5=1.5``, and that's why the final z-location is ``1.5`` and not 3.

    .. image:: images/falloff_overview_example.png

A more advanced falloff is the **Point Distance** falloff, which associate a float to every vector where that float equals inverse the distance between the object and an input vector. If we then used that falloff in the previous example, the objects that are closer to the input vector will move more along z-axis and the effect is tuned down as we move away from the input vector.

Another often used falloff is the **Object Controller Falloff** which makes it easier to construct falloffs by representing them with objects in the 3D viewport.

Falloffs are much more high level than other nodes, yet they give you a lot of control. E.g. It is possible to mix falloffs together with the **Mix Falloffs** node. If you need even more control there also is a **Custom Falloff** node that takes a Float List as input and associate those floats to the objects.

Everything that can be done using falloffs can also be done without them, but using falloffs has many benefits:

    1. Much better **Performance**.
    2. **Less nodes** are required to achieve desired effects.
    3. They provide a more "declarative" approach to express animations which in return makes falloffs much more **artist friendly**.
