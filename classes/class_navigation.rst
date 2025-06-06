.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_Navigation:

Navigation
==========

**Inherits:** :ref:`Spatial<class_spatial>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------



Member Functions
----------------

+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`            | :ref:`get_closest_point<class_Navigation_get_closest_point>`  **(** :ref:`Vector3<class_vector3>` to_point  **)**                                                                                                    |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`            | :ref:`get_closest_point_normal<class_Navigation_get_closest_point_normal>`  **(** :ref:`Vector3<class_vector3>` to_point  **)**                                                                                      |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`              | :ref:`get_closest_point_owner<class_Navigation_get_closest_point_owner>`  **(** :ref:`Vector3<class_vector3>` to_point  **)**                                                                                        |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`            | :ref:`get_closest_point_to_segment<class_Navigation_get_closest_point_to_segment>`  **(** :ref:`Vector3<class_vector3>` start, :ref:`Vector3<class_vector3>` end, :ref:`bool<class_bool>` use_collision=false  **)** |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3Array<class_vector3array>`  | :ref:`get_simple_path<class_Navigation_get_simple_path>`  **(** :ref:`Vector3<class_vector3>` start, :ref:`Vector3<class_vector3>` end, :ref:`bool<class_bool>` optimize=true  **)**                                 |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`            | :ref:`get_up_vector<class_Navigation_get_up_vector>`  **(** **)** const                                                                                                                                              |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                    | :ref:`navmesh_create<class_Navigation_navmesh_create>`  **(** :ref:`NavigationMesh<class_navigationmesh>` mesh, :ref:`Transform<class_transform>` xform, :ref:`Object<class_object>` owner=NULL  **)**               |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`navmesh_remove<class_Navigation_navmesh_remove>`  **(** :ref:`int<class_int>` id  **)**                                                                                                                        |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`navmesh_set_transform<class_Navigation_navmesh_set_transform>`  **(** :ref:`int<class_int>` id, :ref:`Transform<class_transform>` xform  **)**                                                                 |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_up_vector<class_Navigation_set_up_vector>`  **(** :ref:`Vector3<class_vector3>` up  **)**                                                                                                                  |
+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Member Function Description
---------------------------

.. _class_Navigation_get_closest_point:

- :ref:`Vector3<class_vector3>`  **get_closest_point**  **(** :ref:`Vector3<class_vector3>` to_point  **)**

.. _class_Navigation_get_closest_point_normal:

- :ref:`Vector3<class_vector3>`  **get_closest_point_normal**  **(** :ref:`Vector3<class_vector3>` to_point  **)**

.. _class_Navigation_get_closest_point_owner:

- :ref:`Object<class_object>`  **get_closest_point_owner**  **(** :ref:`Vector3<class_vector3>` to_point  **)**

.. _class_Navigation_get_closest_point_to_segment:

- :ref:`Vector3<class_vector3>`  **get_closest_point_to_segment**  **(** :ref:`Vector3<class_vector3>` start, :ref:`Vector3<class_vector3>` end, :ref:`bool<class_bool>` use_collision=false  **)**

.. _class_Navigation_get_simple_path:

- :ref:`Vector3Array<class_vector3array>`  **get_simple_path**  **(** :ref:`Vector3<class_vector3>` start, :ref:`Vector3<class_vector3>` end, :ref:`bool<class_bool>` optimize=true  **)**

.. _class_Navigation_get_up_vector:

- :ref:`Vector3<class_vector3>`  **get_up_vector**  **(** **)** const

.. _class_Navigation_navmesh_create:

- :ref:`int<class_int>`  **navmesh_create**  **(** :ref:`NavigationMesh<class_navigationmesh>` mesh, :ref:`Transform<class_transform>` xform, :ref:`Object<class_object>` owner=NULL  **)**

.. _class_Navigation_navmesh_remove:

- void  **navmesh_remove**  **(** :ref:`int<class_int>` id  **)**

.. _class_Navigation_navmesh_set_transform:

- void  **navmesh_set_transform**  **(** :ref:`int<class_int>` id, :ref:`Transform<class_transform>` xform  **)**

.. _class_Navigation_set_up_vector:

- void  **set_up_vector**  **(** :ref:`Vector3<class_vector3>` up  **)**


