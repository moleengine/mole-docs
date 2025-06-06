.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_GridMap:

GridMap
=======

**Inherits:** :ref:`Spatial<class_spatial>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------



Member Functions
----------------

+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`AABB<class_aabb>`                | :ref:`area_get_bounds<class_GridMap_area_get_bounds>`  **(** :ref:`int<class_int>` area  **)** const                                                                                                       |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`            | :ref:`area_get_name<class_GridMap_area_get_name>`  **(** :ref:`int<class_int>` area  **)** const                                                                                                           |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Color<class_color>`              | :ref:`area_get_portal_disable_color<class_GridMap_area_get_portal_disable_color>`  **(** :ref:`int<class_int>` area  **)** const                                                                           |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`              | :ref:`area_get_portal_disable_distance<class_GridMap_area_get_portal_disable_distance>`  **(** :ref:`int<class_int>` area  **)** const                                                                     |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`area_is_exterior_portal<class_GridMap_area_is_exterior_portal>`  **(** :ref:`int<class_int>` area  **)** const                                                                                       |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`area_set_exterior_portal<class_GridMap_area_set_exterior_portal>`  **(** :ref:`int<class_int>` area, :ref:`bool<class_bool>` enable  **)**                                                           |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`area_set_name<class_GridMap_area_set_name>`  **(** :ref:`int<class_int>` area, :ref:`String<class_string>` name  **)**                                                                               |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`area_set_portal_disable_color<class_GridMap_area_set_portal_disable_color>`  **(** :ref:`int<class_int>` area, :ref:`Color<class_color>` color  **)**                                                |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`area_set_portal_disable_distance<class_GridMap_area_set_portal_disable_distance>`  **(** :ref:`int<class_int>` area, :ref:`float<class_float>` distance  **)**                                       |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`bake_geometry<class_GridMap_bake_geometry>`  **(** **)**                                                                                                                                             |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`clear<class_GridMap_clear>`  **(** **)**                                                                                                                                                             |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                  | :ref:`create_area<class_GridMap_create_area>`  **(** :ref:`int<class_int>` id, :ref:`AABB<class_aabb>` area  **)**                                                                                         |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`erase_area<class_GridMap_erase_area>`  **(** :ref:`int<class_int>` area  **)**                                                                                                                       |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                  | :ref:`get_cell_item<class_GridMap_get_cell_item>`  **(** :ref:`int<class_int>` x, :ref:`int<class_int>` y, :ref:`int<class_int>` z  **)** const                                                            |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                  | :ref:`get_cell_item_orientation<class_GridMap_get_cell_item_orientation>`  **(** :ref:`int<class_int>` x, :ref:`int<class_int>` y, :ref:`int<class_int>` z  **)** const                                    |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`              | :ref:`get_cell_size<class_GridMap_get_cell_size>`  **(** **)** const                                                                                                                                       |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`get_center_x<class_GridMap_get_center_x>`  **(** **)** const                                                                                                                                         |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`get_center_y<class_GridMap_get_center_y>`  **(** **)** const                                                                                                                                         |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`get_center_z<class_GridMap_get_center_z>`  **(** **)** const                                                                                                                                         |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                  | :ref:`get_octant_size<class_GridMap_get_octant_size>`  **(** **)** const                                                                                                                                   |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`MeshLibrary<class_meshlibrary>`  | :ref:`get_theme<class_GridMap_get_theme>`  **(** **)** const                                                                                                                                               |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                  | :ref:`get_unused_area_id<class_GridMap_get_unused_area_id>`  **(** **)** const                                                                                                                             |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`is_baking_enabled<class_GridMap_is_baking_enabled>`  **(** **)** const                                                                                                                               |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`is_using_baked_light<class_GridMap_is_using_baked_light>`  **(** **)** const                                                                                                                         |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`resource_changed<class_GridMap_resource_changed>`  **(** :ref:`Object<class_object>` resource  **)**                                                                                                 |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_bake<class_GridMap_set_bake>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                                                       |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_cell_item<class_GridMap_set_cell_item>`  **(** :ref:`int<class_int>` x, :ref:`int<class_int>` y, :ref:`int<class_int>` z, :ref:`int<class_int>` item, :ref:`int<class_int>` orientation=0  **)** |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_cell_size<class_GridMap_set_cell_size>`  **(** :ref:`float<class_float>` size  **)**                                                                                                             |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_center_x<class_GridMap_set_center_x>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                                               |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_center_y<class_GridMap_set_center_y>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                                               |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_center_z<class_GridMap_set_center_z>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                                               |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_clip<class_GridMap_set_clip>`  **(** :ref:`bool<class_bool>` enabled, :ref:`bool<class_bool>` clipabove=true, :ref:`int<class_int>` floor=0, :ref:`int<class_int>` axis=0  **)**                 |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_octant_size<class_GridMap_set_octant_size>`  **(** :ref:`int<class_int>` size  **)**                                                                                                             |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_theme<class_GridMap_set_theme>`  **(** :ref:`MeshLibrary<class_meshlibrary>` theme  **)**                                                                                                        |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_use_baked_light<class_GridMap_set_use_baked_light>`  **(** :ref:`bool<class_bool>` use  **)**                                                                                                    |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **INVALID_CELL_ITEM** = **-1**

Member Function Description
---------------------------

.. _class_GridMap_area_get_bounds:

- :ref:`AABB<class_aabb>`  **area_get_bounds**  **(** :ref:`int<class_int>` area  **)** const

.. _class_GridMap_area_get_name:

- :ref:`String<class_string>`  **area_get_name**  **(** :ref:`int<class_int>` area  **)** const

.. _class_GridMap_area_get_portal_disable_color:

- :ref:`Color<class_color>`  **area_get_portal_disable_color**  **(** :ref:`int<class_int>` area  **)** const

.. _class_GridMap_area_get_portal_disable_distance:

- :ref:`float<class_float>`  **area_get_portal_disable_distance**  **(** :ref:`int<class_int>` area  **)** const

.. _class_GridMap_area_is_exterior_portal:

- :ref:`bool<class_bool>`  **area_is_exterior_portal**  **(** :ref:`int<class_int>` area  **)** const

.. _class_GridMap_area_set_exterior_portal:

- void  **area_set_exterior_portal**  **(** :ref:`int<class_int>` area, :ref:`bool<class_bool>` enable  **)**

.. _class_GridMap_area_set_name:

- void  **area_set_name**  **(** :ref:`int<class_int>` area, :ref:`String<class_string>` name  **)**

.. _class_GridMap_area_set_portal_disable_color:

- void  **area_set_portal_disable_color**  **(** :ref:`int<class_int>` area, :ref:`Color<class_color>` color  **)**

.. _class_GridMap_area_set_portal_disable_distance:

- void  **area_set_portal_disable_distance**  **(** :ref:`int<class_int>` area, :ref:`float<class_float>` distance  **)**

.. _class_GridMap_bake_geometry:

- void  **bake_geometry**  **(** **)**

.. _class_GridMap_clear:

- void  **clear**  **(** **)**

.. _class_GridMap_create_area:

- :ref:`int<class_int>`  **create_area**  **(** :ref:`int<class_int>` id, :ref:`AABB<class_aabb>` area  **)**

.. _class_GridMap_erase_area:

- void  **erase_area**  **(** :ref:`int<class_int>` area  **)**

.. _class_GridMap_get_cell_item:

- :ref:`int<class_int>`  **get_cell_item**  **(** :ref:`int<class_int>` x, :ref:`int<class_int>` y, :ref:`int<class_int>` z  **)** const

.. _class_GridMap_get_cell_item_orientation:

- :ref:`int<class_int>`  **get_cell_item_orientation**  **(** :ref:`int<class_int>` x, :ref:`int<class_int>` y, :ref:`int<class_int>` z  **)** const

.. _class_GridMap_get_cell_size:

- :ref:`float<class_float>`  **get_cell_size**  **(** **)** const

.. _class_GridMap_get_center_x:

- :ref:`bool<class_bool>`  **get_center_x**  **(** **)** const

.. _class_GridMap_get_center_y:

- :ref:`bool<class_bool>`  **get_center_y**  **(** **)** const

.. _class_GridMap_get_center_z:

- :ref:`bool<class_bool>`  **get_center_z**  **(** **)** const

.. _class_GridMap_get_octant_size:

- :ref:`int<class_int>`  **get_octant_size**  **(** **)** const

.. _class_GridMap_get_theme:

- :ref:`MeshLibrary<class_meshlibrary>`  **get_theme**  **(** **)** const

.. _class_GridMap_get_unused_area_id:

- :ref:`int<class_int>`  **get_unused_area_id**  **(** **)** const

.. _class_GridMap_is_baking_enabled:

- :ref:`bool<class_bool>`  **is_baking_enabled**  **(** **)** const

.. _class_GridMap_is_using_baked_light:

- :ref:`bool<class_bool>`  **is_using_baked_light**  **(** **)** const

.. _class_GridMap_resource_changed:

- void  **resource_changed**  **(** :ref:`Object<class_object>` resource  **)**

.. _class_GridMap_set_bake:

- void  **set_bake**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_GridMap_set_cell_item:

- void  **set_cell_item**  **(** :ref:`int<class_int>` x, :ref:`int<class_int>` y, :ref:`int<class_int>` z, :ref:`int<class_int>` item, :ref:`int<class_int>` orientation=0  **)**

.. _class_GridMap_set_cell_size:

- void  **set_cell_size**  **(** :ref:`float<class_float>` size  **)**

.. _class_GridMap_set_center_x:

- void  **set_center_x**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_GridMap_set_center_y:

- void  **set_center_y**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_GridMap_set_center_z:

- void  **set_center_z**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_GridMap_set_clip:

- void  **set_clip**  **(** :ref:`bool<class_bool>` enabled, :ref:`bool<class_bool>` clipabove=true, :ref:`int<class_int>` floor=0, :ref:`int<class_int>` axis=0  **)**

.. _class_GridMap_set_octant_size:

- void  **set_octant_size**  **(** :ref:`int<class_int>` size  **)**

.. _class_GridMap_set_theme:

- void  **set_theme**  **(** :ref:`MeshLibrary<class_meshlibrary>` theme  **)**

.. _class_GridMap_set_use_baked_light:

- void  **set_use_baked_light**  **(** :ref:`bool<class_bool>` use  **)**


