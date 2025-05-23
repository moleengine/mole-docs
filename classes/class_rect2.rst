.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_Rect2:

Rect2
=====

**Category:** Built-In Types

Brief Description
-----------------

2D Axis-aligned bounding box.

Member Functions
----------------

+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`  | :ref:`Rect2<class_Rect2_Rect2>`  **(** :ref:`Vector2<class_vector2>` pos, :ref:`Vector2<class_vector2>` size  **)**                                                                                 |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`  | :ref:`Rect2<class_Rect2_Rect2>`  **(** :ref:`float<class_float>` x, :ref:`float<class_float>` y, :ref:`float<class_float>` width, :ref:`float<class_float>` height  **)**                           |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`  | :ref:`clip<class_Rect2_clip>`  **(** :ref:`Rect2<class_rect2>` b  **)**                                                                                                                             |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`    | :ref:`encloses<class_Rect2_encloses>`  **(** :ref:`Rect2<class_rect2>` b  **)**                                                                                                                     |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`  | :ref:`expand<class_Rect2_expand>`  **(** :ref:`Vector2<class_vector2>` to  **)**                                                                                                                    |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`get_area<class_Rect2_get_area>`  **(** **)**                                                                                                                                                  |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`  | :ref:`grow<class_Rect2_grow>`  **(** :ref:`float<class_float>` by  **)**                                                                                                                            |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`  | :ref:`grow_individual<class_Rect2_grow_individual>`  **(** :ref:`float<class_float>` left, :ref:`float<class_float>` top, :ref:`float<class_float>` right, :ref:`float<class_float>`  bottom  **)** |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`  | :ref:`grow_margin<class_Rect2_grow_margin>`  **(** :ref:`int<class_int>` margin, :ref:`float<class_float>` by  **)**                                                                                |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`    | :ref:`has_no_area<class_Rect2_has_no_area>`  **(** **)**                                                                                                                                            |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`    | :ref:`has_point<class_Rect2_has_point>`  **(** :ref:`Vector2<class_vector2>` point  **)**                                                                                                           |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`    | :ref:`intersects<class_Rect2_intersects>`  **(** :ref:`Rect2<class_rect2>` b  **)**                                                                                                                 |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`  | :ref:`merge<class_Rect2_merge>`  **(** :ref:`Rect2<class_rect2>` b  **)**                                                                                                                           |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Member Variables
----------------

- :ref:`Vector2<class_vector2>` **end** - Ending corner.
- :ref:`Vector2<class_vector2>` **pos** - Position (starting corner).
- :ref:`Vector2<class_vector2>` **size** - Size from position to end.

Description
-----------

Rect2 provides an 2D Axis-Aligned Bounding Box. It consists of a position, a size, and several utility functions. It is typically used for fast overlap tests.

Member Function Description
---------------------------

.. _class_Rect2_Rect2:

- :ref:`Rect2<class_rect2>`  **Rect2**  **(** :ref:`Vector2<class_vector2>` pos, :ref:`Vector2<class_vector2>` size  **)**

Construct a :ref:`Rect2<class_rect2>` by position and size.

.. _class_Rect2_Rect2:

- :ref:`Rect2<class_rect2>`  **Rect2**  **(** :ref:`float<class_float>` x, :ref:`float<class_float>` y, :ref:`float<class_float>` width, :ref:`float<class_float>` height  **)**

Construct a :ref:`Rect2<class_rect2>` by x, y, width and height.

.. _class_Rect2_clip:

- :ref:`Rect2<class_rect2>`  **clip**  **(** :ref:`Rect2<class_rect2>` b  **)**

Returns the intersection of this :ref:`Rect2<class_rect2>` and b.

.. _class_Rect2_encloses:

- :ref:`bool<class_bool>`  **encloses**  **(** :ref:`Rect2<class_rect2>` b  **)**

Returns true if this :ref:`Rect2<class_rect2>` completely encloses another one.

.. _class_Rect2_expand:

- :ref:`Rect2<class_rect2>`  **expand**  **(** :ref:`Vector2<class_vector2>` to  **)**

Return this :ref:`Rect2<class_rect2>` expanded to include a given point.

.. _class_Rect2_get_area:

- :ref:`float<class_float>`  **get_area**  **(** **)**

Get the area of the :ref:`Rect2<class_rect2>`.

.. _class_Rect2_grow:

- :ref:`Rect2<class_rect2>`  **grow**  **(** :ref:`float<class_float>` by  **)**

Return a copy of the :ref:`Rect2<class_rect2>` grown a given amount of units towards all the sides.

.. _class_Rect2_grow_individual:

- :ref:`Rect2<class_rect2>`  **grow_individual**  **(** :ref:`float<class_float>` left, :ref:`float<class_float>` top, :ref:`float<class_float>` right, :ref:`float<class_float>`  bottom  **)**

.. _class_Rect2_grow_margin:

- :ref:`Rect2<class_rect2>`  **grow_margin**  **(** :ref:`int<class_int>` margin, :ref:`float<class_float>` by  **)**

.. _class_Rect2_has_no_area:

- :ref:`bool<class_bool>`  **has_no_area**  **(** **)**

Return true if the :ref:`Rect2<class_rect2>` is flat or empty.

.. _class_Rect2_has_point:

- :ref:`bool<class_bool>`  **has_point**  **(** :ref:`Vector2<class_vector2>` point  **)**

Return true if the :ref:`Rect2<class_rect2>` contains a point.

.. _class_Rect2_intersects:

- :ref:`bool<class_bool>`  **intersects**  **(** :ref:`Rect2<class_rect2>` b  **)**

Return true if the :ref:`Rect2<class_rect2>` overlaps with another.

.. _class_Rect2_merge:

- :ref:`Rect2<class_rect2>`  **merge**  **(** :ref:`Rect2<class_rect2>` b  **)**

Combine this :ref:`Rect2<class_rect2>` with another, a larger one is returned that contains both.


