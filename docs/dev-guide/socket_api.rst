**********
Socket API
**********

Every socket is a subclass of ``mn_node_base.mn_BaseSocket`` and ``mn_node_base.mn_SocketProperties``. The ``bl_idname`` should be the same as the class name and the bl_label a more readable Version.

.. code-block:: python
    :linenos:
    
    class mn_VectorSocket(mn_BaseSocket, mn_SocketProperties):
        bl_idname = "mn_VectorSocket"
        bl_label = "Vector Socket"
        dataType = "Vector"
        allowedInputTypes = ["Vector"]
        drawColor = (0.05, 0.05, 0.8, 0.7)
   
   
**dataType:** The type that the socket outputs. Should be as short and understandable as possible.
**allowedInputTypes:** These types are like subtypes and are internally convertable into ``dataType``. Use ``"all"`` if the user can make a link from everywhere to here (used in ``Generic`` and ``Empty`` socket).
**drawColor:** RGBA tupel of the color being used to draw this socket in the node editor.