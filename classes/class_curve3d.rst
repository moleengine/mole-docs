.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_Curve3D:

Curve3D
=======

**Inherits:** :ref:`Resource<class_resource>` **<** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Describes a Bezier curve in 3D space.

Member Functions
----------------

+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`add_point<class_Curve3D_add_point>`  **(** :ref:`Vector3<class_vector3>` pos, :ref:`Vector3<class_vector3>` in=Vector3(0, 0, 0), :ref:`Vector3<class_vector3>` out=Vector3(0, 0, 0), :ref:`int<class_int>` atpos=-1  **)** |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`clear_points<class_Curve3D_clear_points>`  **(** **)**                                                                                                                                                                     |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                | :ref:`get_bake_interval<class_Curve3D_get_bake_interval>`  **(** **)** const                                                                                                                                                     |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                | :ref:`get_baked_length<class_Curve3D_get_baked_length>`  **(** **)** const                                                                                                                                                       |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3Array<class_vector3array>`  | :ref:`get_baked_points<class_Curve3D_get_baked_points>`  **(** **)** const                                                                                                                                                       |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`RealArray<class_realarray>`        | :ref:`get_baked_tilts<class_Curve3D_get_baked_tilts>`  **(** **)** const                                                                                                                                                         |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                    | :ref:`get_point_count<class_Curve3D_get_point_count>`  **(** **)** const                                                                                                                                                         |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`            | :ref:`get_point_in<class_Curve3D_get_point_in>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                                                    |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`            | :ref:`get_point_out<class_Curve3D_get_point_out>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                                                  |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`            | :ref:`get_point_pos<class_Curve3D_get_point_pos>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                                                  |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                | :ref:`get_point_tilt<class_Curve3D_get_point_tilt>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                                                |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`            | :ref:`interpolate<class_Curve3D_interpolate>`  **(** :ref:`int<class_int>` idx, :ref:`float<class_float>` t  **)** const                                                                                                         |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`            | :ref:`interpolate_baked<class_Curve3D_interpolate_baked>`  **(** :ref:`float<class_float>` offset, :ref:`bool<class_bool>` cubic=false  **)** const                                                                              |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`            | :ref:`interpolatef<class_Curve3D_interpolatef>`  **(** :ref:`float<class_float>` fofs  **)** const                                                                                                                               |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`remove_point<class_Curve3D_remove_point>`  **(** :ref:`int<class_int>` idx  **)**                                                                                                                                          |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_bake_interval<class_Curve3D_set_bake_interval>`  **(** :ref:`float<class_float>` distance  **)**                                                                                                                       |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_point_in<class_Curve3D_set_point_in>`  **(** :ref:`int<class_int>` idx, :ref:`Vector3<class_vector3>` pos  **)**                                                                                                       |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_point_out<class_Curve3D_set_point_out>`  **(** :ref:`int<class_int>` idx, :ref:`Vector3<class_vector3>` pos  **)**                                                                                                     |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_point_pos<class_Curve3D_set_point_pos>`  **(** :ref:`int<class_int>` idx, :ref:`Vector3<class_vector3>` pos  **)**                                                                                                     |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_point_tilt<class_Curve3D_set_point_tilt>`  **(** :ref:`int<class_int>` idx, :ref:`float<class_float>` tilt  **)**                                                                                                      |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3Array<class_vector3array>`  | :ref:`tesselate<class_Curve3D_tesselate>`  **(** :ref:`int<class_int>` max_stages=5, :ref:`float<class_float>` tolerance_degrees=4  **)** const                                                                                  |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

This class describes a Bezier curve in 3D space. It is mainly used to give a shape to a :ref:`Path<class_path>`, but can be manually sampled for other purposes.

It keeps a cache of precalculated points along the curve, to speed further calculations up.

Member Function Description
---------------------------

.. _class_Curve3D_add_point:

- void  **add_point**  **(** :ref:`Vector3<class_vector3>` pos, :ref:`Vector3<class_vector3>` in=Vector3(0, 0, 0), :ref:`Vector3<class_vector3>` out=Vector3(0, 0, 0), :ref:`int<class_int>` atpos=-1  **)**

Adds a point to a curve, at position "pos", with control points "in" and "out".

If "atpos" is given, the point is inserted before the point number "atpos", moving that point (and every point after) after the inserted point. If "atpos" is not given, or is an illegal value (atpos <0 or atpos >= :ref:`get_point_count<class_Curve3D_get_point_count>`), the point will be appended at the end of the point list.

.. _class_Curve3D_clear_points:

- void  **clear_points**  **(** **)**

.. _class_Curve3D_get_bake_interval:

- :ref:`float<class_float>`  **get_bake_interval**  **(** **)** const

Returns the distance between two adjacent cached points.

.. _class_Curve3D_get_baked_length:

- :ref:`float<class_float>`  **get_baked_length**  **(** **)** const

Returns the total length of the curve, based on the cached points. Given enough density (see :ref:`set_bake_interval<class_Curve3D_set_bake_interval>`), it should be approximate enough.

.. _class_Curve3D_get_baked_points:

- :ref:`Vector3Array<class_vector3array>`  **get_baked_points**  **(** **)** const

Returns the cache of points as a :ref:`Vector3Array<class_vector3array>`.

.. _class_Curve3D_get_baked_tilts:

- :ref:`RealArray<class_realarray>`  **get_baked_tilts**  **(** **)** const

Returns the cache of tilts as a :ref:`RealArray<class_realarray>`.

.. _class_Curve3D_get_point_count:

- :ref:`int<class_int>`  **get_point_count**  **(** **)** const

Returns the number of points describing the curve.

.. _class_Curve3D_get_point_in:

- :ref:`Vector3<class_vector3>`  **get_point_in**  **(** :ref:`int<class_int>` idx  **)** const

Returns the position of the control point leading to the vertex "idx". If the index is out of bounds, the function sends an error to the console, and returns (0, 0, 0).

.. _class_Curve3D_get_point_out:

- :ref:`Vector3<class_vector3>`  **get_point_out**  **(** :ref:`int<class_int>` idx  **)** const

Returns the position of the control point leading out of the vertex "idx". If the index is out of bounds, the function sends an error to the console, and returns (0, 0, 0).

.. _class_Curve3D_get_point_pos:

- :ref:`Vector3<class_vector3>`  **get_point_pos**  **(** :ref:`int<class_int>` idx  **)** const

Returns the position of the vertex "idx". If the index is out of bounds, the function sends an error to the console, and returns (0, 0, 0).

.. _class_Curve3D_get_point_tilt:

- :ref:`float<class_float>`  **get_point_tilt**  **(** :ref:`int<class_int>` idx  **)** const

Returns the tilt angle in radians for the point "idx". If the index is out of bounds, the function sends an error to the console, and returns 0.

.. _class_Curve3D_interpolate:

- :ref:`Vector3<class_vector3>`  **interpolate**  **(** :ref:`int<class_int>` idx, :ref:`float<class_float>` t  **)** const

Returns the position between the vertex "idx" and the vertex "idx"+1, where "t" controls if the point is the first vertex (t = 0.0), the last vertex (t = 1.0), or in between. Values of "t" outside the range (0.0 >= t  <=1) give strange, but predictable results.

If "idx" is out of bounds it is truncated to the first or last vertex, and "t" is ignored. If the curve has no points, the function sends an error to the console, and returns (0, 0, 0).

.. _class_Curve3D_interpolate_baked:

- :ref:`Vector3<class_vector3>`  **interpolate_baked**  **(** :ref:`float<class_float>` offset, :ref:`bool<class_bool>` cubic=false  **)** const

Returns a point within the curve at position "offset", where "offset" is measured as a distance in 3D units along the curve.

To do that, it finds the two cached points where the "offset" lies between, then interpolates the values. This interpolation is cubic if "cubic" is set to true, or linear if set to false.

Cubic interpolation tends to follow the curves better, but linear is faster (and often, precise enough).

.. _class_Curve3D_interpolatef:

- :ref:`Vector3<class_vector3>`  **interpolatef**  **(** :ref:`float<class_float>` fofs  **)** const

Returns the position at the vertex "fofs". It calls :ref:`interpolate<class_Curve3D_interpolate>` using the integer part of fofs as "idx", and its fractional part as "t".

.. _class_Curve3D_remove_point:

- void  **remove_point**  **(** :ref:`int<class_int>` idx  **)**

Deletes the point "idx" from the curve. Sends an error to the console if "idx" is out of bounds.

.. _class_Curve3D_set_bake_interval:

- void  **set_bake_interval**  **(** :ref:`float<class_float>` distance  **)**

Sets the distance in 3D units between two adjacent cached points. Changing it forces the cache to be recomputed the next time a xxx_baked_xxx function is called. The less distance, the more points the cache will have, and the more memory it will consume, so use with care.

.. _class_Curve3D_set_point_in:

- void  **set_point_in**  **(** :ref:`int<class_int>` idx, :ref:`Vector3<class_vector3>` pos  **)**

Sets the position of the control point leading to the vertex "idx". If the index is out of bounds, the function sends an error to the console.

.. _class_Curve3D_set_point_out:

- void  **set_point_out**  **(** :ref:`int<class_int>` idx, :ref:`Vector3<class_vector3>` pos  **)**

Sets the position of the control point leading out of the vertex "idx". If the index is out of bounds, the function sends an error to the console.

.. _class_Curve3D_set_point_pos:

- void  **set_point_pos**  **(** :ref:`int<class_int>` idx, :ref:`Vector3<class_vector3>` pos  **)**

Sets the position for the vertex "idx". If the index is out of bounds, the function sends an error to the console.

.. _class_Curve3D_set_point_tilt:

- void  **set_point_tilt**  **(** :ref:`int<class_int>` idx, :ref:`float<class_float>` tilt  **)**

Sets the tilt angle in radians for the point "idx". If the index is out of bounds, the function sends an error to the console.

The tilt controls the rotation along the look-at axis an object traveling the path would have. In the case of a curve controlling a :ref:`PathFollow<class_pathfollow>`, this tilt is an offset over the natural tilt the PathFollow calculates.

.. _class_Curve3D_tesselate:

- :ref:`Vector3Array<class_vector3array>`  **tesselate**  **(** :ref:`int<class_int>` max_stages=5, :ref:`float<class_float>` tolerance_degrees=4  **)** const

Returns a list of points along the curve, with a curvature controlled point density. That is, the curvier parts will have more points than the straighter parts.

This approximation makes straight segments between each point, then subdivides those segments until the resulting shape is similar enough.

"max_stages" controls how many subdivisions a curve segment may face before it is considered approximate enough. Each subdivision splits the segment in half, so the default 5 stages may mean up to 32 subdivisions per curve segment. Increase with care!

"tolerance_degrees" controls how many degrees the midpoint of a segment may deviate from the real curve, before the segment has to be subdivided.


