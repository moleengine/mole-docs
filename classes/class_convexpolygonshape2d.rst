.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_ConvexPolygonShape2D:

ConvexPolygonShape2D
====================

**Inherits:** :ref:`Shape2D<class_shape2d>` **<** :ref:`Resource<class_resource>` **<** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Convex Polygon Shape for 2D physics.

Member Functions
----------------

+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2Array<class_vector2array>`  | :ref:`get_points<class_ConvexPolygonShape2D_get_points>`  **(** **)** const                                                          |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_point_cloud<class_ConvexPolygonShape2D_set_point_cloud>`  **(** :ref:`Vector2Array<class_vector2array>` point_cloud  **)** |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_points<class_ConvexPolygonShape2D_set_points>`  **(** :ref:`Vector2Array<class_vector2array>` points  **)**                |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Convex Polygon Shape for 2D physics. A convex polygon, whatever its shape, is internally decomposed into as many convex polygons as needed to ensure all collision checks against it are always done on convex polygons (which are faster to check).

The main difference between a :ref:`ConvexPolygonShape2D<class_convexpolygonshape2d>` and a :ref:`ConcavePolygonShape2D<class_concavepolygonshape2d>` is that a concave polygon assumes it is concave and uses a more complex method of collision detection, and a convex one forces itself to be convex in order to speed up collision detection.

Member Function Description
---------------------------

.. _class_ConvexPolygonShape2D_get_points:

- :ref:`Vector2Array<class_vector2array>`  **get_points**  **(** **)** const

Return a list of points in either clockwise or counter clockwise order, forming a convex polygon.

.. _class_ConvexPolygonShape2D_set_point_cloud:

- void  **set_point_cloud**  **(** :ref:`Vector2Array<class_vector2array>` point_cloud  **)**

Currently, this method does nothing.

.. _class_ConvexPolygonShape2D_set_points:

- void  **set_points**  **(** :ref:`Vector2Array<class_vector2array>` points  **)**

Set a list of points in either clockwise or counter clockwise order, forming a convex polygon.


