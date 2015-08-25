************
Socket Types
************

A socket is the point where 2 nodes can be linked. Therefor sockets are the
main interface between a node and the user. You might think having many
different socket types is unnecessary but it has very important advantages.

    - It can help finding which sockets make sense to connect; Although this is
      not always the case because some sockets change there type automatically
      when they are linked.
    - The clearer a socket is defined the better the performance of a node
      because it doesn't have to check the input type which adds a lot of overhead.
      That is also the main reason why Python is slower than many compiled languages.

Currently there are 36 different socket types, but this may change over time.
To see which sockets you have installed go to the addon directory and take a look
into the ``sockets`` folder. All files except ``__init__.py`` and ``info.py``
represent one socket.

Many sockets come in pairs. E.g. there is an ``Object`` and an ``Object List`` socket.
List sockets are by default just an empty python list (not a tuple!).
To get the ``bl_idname`` of a list socket take the base id name and insert ``List`` before ``Socket``.
Sockets that have a corresponding list data type are often called ``base sockets``.


+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Data Type       | bl_idname                   |List | Function or the data it carries                                     |
+=================+=============================+=====+=====================================================================+
| Boolean         | ``an_BooleanSocket``        |  No | ``True`` or ``False``                                               |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Color           | ``an_ColorSocket``          |  No | List with four floats: ``[red, green, blue, alpha]                  |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Edge Indices    | ``an_EdgeIndicesSocket``    | Yes | Tuple containing two integers                                       |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Float           | ``an_FloatSocket``          | Yes | Normal python float value                                           |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Generic         | ``an_GenericSocket``        |  No | Can contain anything; Take care when converting to another type     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Integer         | ``an_IntegerSocket``        | Yes | Normal python integer value                                         |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Interpolation   | ``an_InterpolationSocket``  |  No | Tuple: ``(interpolation function, settings; is often None)``        |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Matrix          | ``an_MatrixSocket``         | Yes | `Matrix`_ object                                                    |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Mesh            | ``an_MeshSocket``           |  No | `BMesh`_ object                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Mesh Data       | ``an_MeshDataSocket``       |  No | Class that contains vertex locations and edge/polygon indices       |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Node Control    | ``an_NodeControlSocket``    |  No | Contains no data; the function depends on the node where it is used |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Object          | ``an_ObjectSocket``         | Yes | `Object`_ (can be a mesh, lamp, camera, ...) or ``None``            |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Object Group    | ``an_ObjectGroupSocket``    |  No | `Object Group`_ or ``None``                                         |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Particle        | ``an_ParticleSocket``       | Yes | `Particle`_ object or ``None``                                      |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Particle System | ``an_ParticleSystemSocket`` | Yes | `Particle System`_ object or ``None``                               |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Polygon         | ``an_PolygonSocket``        | Yes | Contains vertices, area, center, normal and material index          |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Polygon Indices | ``an_PolygonIndicesSocket`` | Yes | Tuple containing at least 3 integers                                |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Sequence        | ``an_SequenceSocket``       |  No | `Sequence`_                                                         |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Spline          | ``an_SplineSocket``         | Yes | Either a poly or bezier spline object                               |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| String          | ``an_StringSocket``         | Yes | Normal python text                                                  |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Text Block      | ``an_TextBlockSocket``      |  No | `Text`_                                                             |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Vector          | ``an_VectorSocket``         | Yes | `Vector`_                                                           |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Vertex          | ``an_VertexSocket``         | Yes | Contains a location, normal and vertex group weights                |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+


.. _Matrix: http://www.blender.org/api/blender_python_api_2_75_1/mathutils.html?highlight=mathutils#mathutils.Matrix
.. _BMesh: http://www.blender.org/api/blender_python_api_2_75_1/bmesh.types.html#bmesh.types.BMesh
.. _Object: http://www.blender.org/api/blender_python_api_2_75_1/bpy.types.Object.html
.. _Object Group: http://www.blender.org/api/blender_python_api_2_75_1/bpy.types.Group.html
.. _Particle: http://www.blender.org/api/blender_python_api_2_75_1/bpy.types.Particle.html
.. _Particle System: http://www.blender.org/api/blender_python_api_2_75_1/bpy.types.ParticleSystem.html
.. _Sequence: http://www.blender.org/api/blender_python_api_2_75_1/bpy.types.Sequence.html
.. _Text: http://www.blender.org/api/blender_python_api_2_75_1/bpy.types.Text.html
.. _Vector: http://www.blender.org/api/blender_python_api_2_75_1/mathutils.html#mathutils.Vector
