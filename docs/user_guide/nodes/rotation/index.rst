Rotation
========

Rotations in CG are either represented by an euler angle (which you probably know) or a quaternion which is a better rotation system especially when it comes to animations.

Quaternion is a system that is used to represent data. It extends the complex number which is in the form of ``(w+xi)`` where ``w`` is the real part and ``xi`` is the imaginary part, Quaternions are 4 dimentional in the form of ``w+xi+yj+zk`` where ``i = j = k = ijk = -1``, As CG artists we tend to think of quaternion as a real number plus a vector ``(w+V)`` where `w` is a real number and `V` is a vector.

Quaternions are usually used to represent rotations as an alternative to euler's angles because it has a smoother interpolation and it has no **Gimball lock**. Rotations are represented in a form of a **Unit Quaternion** which is a quaternion that has a length of 1 (``w^2 +x^2 +y^2 +z^2 = 1``), where w is the amount of rotation around the vector defined by the points (X,Y,Z). Since the magnitude is always equal to 1, you can think of this vector as a point on a sphere with radius of 1. Well it is a hypersphere (4D sphere), but for the sake of simplicity we will just think of it as a sphere.

We said before that the amount of rotation is defined by the real number ``W``. That angle can be defined in 2 ways:

-  ``θ = 2 Arccos w``
-  ``θ = 2 Arcsine (x^2 +y^2 +z^2) ^ 0.5``

Remember what we said about the quaternion being unit quaternion, we conclude that ``W`` affect ``X,Y,Z`` in the normalization process and that's why it was omitted in
the second equation.

Quaternion multiplication is very important, it is known as **Hamilton Product**. The multiplication is done based on the rule ``i=j=k=ijk=-1``. Things get very interesting when it comes to the relation between quaternion multiplication and rotation, Suppose we have a vector or a point defined as ``V = (X,Y,Z)``, we can describe this vector as a quaternion like: ``P = (0,X,Y,Z)`` and this form is called **Pure quaternion** which is quaterion with the real part being zero. If we want to rotate this point ``P`` by the quaternion ``Q`` (remember that a quaternion define a rotation around a specific vector by a specific amount). All we you have to do is to use the rotation law which state that ``P' = QPQ*`` where ``P'`` is the rotated vector, ``P`` the original vector (quaternion), ``Q`` is the rotation quaternion and ``Q*`` is the conjugate of the rotation quaternion. It is also pretty important to remember that quaternion multiplication is not commutative!

.. toctree::
   :titlesonly:

    Combine Euler <combine_euler>
    Separate Euler <separate_euler>
    Euler List <euler_list>
    Euler Math <euler_math>
    Mix Euler <mix_euler>
    Random Euler <random_euler>
    Euler Wiggle <euler_wiggle>
    Combine Quaternion <combine_quaternion>
    Separate Quaternion <separate_quaternion>
    Combine Quaternion Rotation <combine_quaternion_rotations>
    Mix Quaternions <mix_quaternions>
    Quaternion Wiggle <quaternion_wiggle>
    Random Quaternion <random_quaternion>
    Quaternion List <quaternion_list>
    Quaternion Math <quaternion_math>
    Convert Rotation Types <convert_rotation_types>
    Direction to Rotation <direction_to_rotation>
    Rotation to Direction <rotation_to_direction>

.. image:: images/rotation_overview.png
