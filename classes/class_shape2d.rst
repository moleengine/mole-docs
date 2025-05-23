.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_Shape2D:

Shape2D
=======

**Inherits:** :ref:`Resource<class_resource>` **<** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Inherited By:** :ref:`RayShape2D<class_rayshape2d>`, :ref:`CapsuleShape2D<class_capsuleshape2d>`, :ref:`LineShape2D<class_lineshape2d>`, :ref:`CircleShape2D<class_circleshape2d>`, :ref:`ConcavePolygonShape2D<class_concavepolygonshape2d>`, :ref:`ConvexPolygonShape2D<class_convexpolygonshape2d>`, :ref:`RectangleShape2D<class_rectangleshape2d>`, :ref:`SegmentShape2D<class_segmentshape2d>`

**Category:** Core

Brief Description
-----------------

Base class for all 2D Shapes.

Member Functions
----------------

+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`collide<class_Shape2D_collide>`  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform  **)**                                                                                                                                                   |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Variant<class_variant>`  | :ref:`collide_and_get_contacts<class_Shape2D_collide_and_get_contacts>`  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform  **)**                                                                                                                 |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`collide_with_motion<class_Shape2D_collide_with_motion>`  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Vector2<class_vector2>` local_motion, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform, :ref:`Vector2<class_vector2>` shape_motion  **)**                                   |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Variant<class_variant>`  | :ref:`collide_with_motion_and_get_contacts<class_Shape2D_collide_with_motion_and_get_contacts>`  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Vector2<class_vector2>` local_motion, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform, :ref:`Vector2<class_vector2>` shape_motion  **)** |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_custom_solver_bias<class_Shape2D_get_custom_solver_bias>`  **(** **)** const                                                                                                                                                                                                                                                   |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_custom_solver_bias<class_Shape2D_set_custom_solver_bias>`  **(** :ref:`float<class_float>` bias  **)**                                                                                                                                                                                                                         |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Base class for all 2D Shapes. All 2D shape types inherit from this.

Member Function Description
---------------------------

.. _class_Shape2D_collide:

- :ref:`bool<class_bool>`  **collide**  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform  **)**

Return whether this shape is colliding with another.

This method needs the transformation matrix for this shape (``local_xform``), the shape to check collisions with (``with_shape``), and the transformation matrix of that shape (``shape_xform``).

.. _class_Shape2D_collide_and_get_contacts:

- :ref:`Variant<class_variant>`  **collide_and_get_contacts**  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform  **)**

Return a list of the points where this shape touches another. If there are no collisions, the list is empty.

This method needs the transformation matrix for this shape (``local_xform``), the shape to check collisions with (``with_shape``), and the transformation matrix of that shape (``shape_xform``).

.. _class_Shape2D_collide_with_motion:

- :ref:`bool<class_bool>`  **collide_with_motion**  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Vector2<class_vector2>` local_motion, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform, :ref:`Vector2<class_vector2>` shape_motion  **)**

Return whether this shape would collide with another, if a given movement was applied.

This method needs the transformation matrix for this shape (``local_xform``), the movement to test on this shape (``local_motion``), the shape to check collisions with (``with_shape``), the transformation matrix of that shape (``shape_xform``), and the movement to test onto the other object (``shape_motion``).

.. _class_Shape2D_collide_with_motion_and_get_contacts:

- :ref:`Variant<class_variant>`  **collide_with_motion_and_get_contacts**  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Vector2<class_vector2>` local_motion, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform, :ref:`Vector2<class_vector2>` shape_motion  **)**

Return a list of the points where this shape would touch another, if a given movement was applied. If there are no collisions, the list is empty.

This method needs the transformation matrix for this shape (``local_xform``), the movement to test on this shape (``local_motion``), the shape to check collisions with (``with_shape``), the transformation matrix of that shape (``shape_xform``), and the movement to test onto the other object (``shape_motion``).

.. _class_Shape2D_get_custom_solver_bias:

- :ref:`float<class_float>`  **get_custom_solver_bias**  **(** **)** const

Return the custom solver bias.

.. _class_Shape2D_set_custom_solver_bias:

- void  **set_custom_solver_bias**  **(** :ref:`float<class_float>` bias  **)**

Use a custom solver bias. No need to change this unless you really know what you are doing.

The solver bias is a factor controlling how much two objects "rebound" off each other, when colliding, to avoid them getting into each other because of numerical imprecision.


