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
Sockets that have a corresponding list data type are often called ``base sockets``.


+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Boolean         | ``an_BooleanSocket``        |  No |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Color           | ``an_ColorSocket``          |  No |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Edge Indices    | ``an_EdgeIndicesSocket``    | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Float           | ``an_FloatSocket``          | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Generic         | ``an_GenericSocket``        |  No |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Integer         | ``an_IntegerSocket``        | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Interpolation   | ``an_InterpolationSocket``  |  No |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Matrix          | ``an_MatrixSocket``         | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Mesh            | ``an_MeshSocket``           |  No |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Mesh Data       | ``an_MeshDataSocket``       |  No |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Node Control    | ``an_NodeControlSocket``    |  No |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Object          | ``an_ObjectSocket``         | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Object Group    | ``an_ObjectGroupSocket``    |  No |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Particle        | ``an_ParticleSocket``       | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Particle System | ``an_ParticleSystemSocket`` | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Polygon         | ``an_PolygonSocket``        | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Polygon Indices | ``an_PolygonIndicesSocket`` | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Sequence        | ``an_SequenceSocket``       |  No |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Spline          | ``an_SplineSocket``         | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| String          | ``an_StringSocket``         | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Text Block      | ``an_TextBlockSocket``      |  No |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Vector          | ``an_VectorSocket``         | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
| Vertex          | ``an_VertexSocket``         | Yes |                                                                     |
+-----------------+-----------------------------+-----+---------------------------------------------------------------------+
