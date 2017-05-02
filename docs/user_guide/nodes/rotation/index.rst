Rotation
========

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

Rotations in CG are represented in three ways including:

- **Euler Angles** - Define rotations as three angles in each of the three axis. It has some problems like *gimbal lock* and nonsmooth animation interpolations.
- **Axis Angle** - Defined by a vector and an angle, the rotation is represented as the rotation around that vector with the angle. It is non usually used.
- **Quaternions** - Defined as a unit 4D vector, which is juts like axis angle but more easier to operate on. It doesn't have gimbal lock and have smooth animation interpolation so it is usually used in making animations.

This category include nodes that creates and operates on eulers and quaternions.
