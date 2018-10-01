Rotation
========

.. toctree::
   :titlesonly:

    Direction to Rotation <direction_to_rotation>
    Rotation to Direction <rotation_to_direction>
    Convert Rotation Types <convert_rotation_types>
    Separate Euler <separate_euler>
    Combine Euler <combine_euler>
    Euler List <euler_list>
    Euler Math <euler_math>
    Mix Euler <mix_euler>
    Random Euler <random_euler>
    Euler Wiggle <euler_wiggle>
    Separate Quaternion <separate_quaternion>
    Combine Quaternion <combine_quaternion>
    Quaternion List <quaternion_list>
    Quaternion Math <quaternion_math>
    Mix Quaternions <mix_quaternions>
    Random Quaternion <random_quaternion>
    Quaternion Wiggle <quaternion_wiggle>
    Combine Quaternion Rotation <combine_quaternion_rotations>

Rotations in CG are represented in three ways including:

- **Euler Angles** - Define rotations as three angles in each of the three axis. It has some problems like *gimbal lock* and nonsmooth animation interpolations.
- **Axis Angle** - Defined by a vector and an angle, the rotation is represented as the rotation around that vector with the angle. It is non usually used.
- **Quaternions** - Defined as a unit 4D vector, which is just like axis angle but more easier to operate on. It doesn't have gimbal lock and have smooth animation interpolation so it is usually used in making animations.

This category include nodes that creates and operates on eulers and quaternions.
