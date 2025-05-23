.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_TileSet:

TileSet
=======

**Inherits:** :ref:`Resource<class_resource>` **<** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Tile library for tilemaps.

Member Functions
----------------

+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`clear<class_TileSet_clear>`  **(** **)**                                                                                                                                              |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`create_tile<class_TileSet_create_tile>`  **(** :ref:`int<class_int>` id  **)**                                                                                                        |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                                | :ref:`find_tile_by_name<class_TileSet_find_tile_by_name>`  **(** :ref:`String<class_string>` name  **)** const                                                                              |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                                | :ref:`get_last_unused_tile_id<class_TileSet_get_last_unused_tile_id>`  **(** **)** const                                                                                                    |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`                            | :ref:`get_tiles_ids<class_TileSet_get_tiles_ids>`  **(** **)** const                                                                                                                        |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`remove_tile<class_TileSet_remove_tile>`  **(** :ref:`int<class_int>` id  **)**                                                                                                        |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`OccluderPolygon2D<class_occluderpolygon2d>`    | :ref:`tile_get_light_occluder<class_TileSet_tile_get_light_occluder>`  **(** :ref:`int<class_int>` id  **)** const                                                                          |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`CanvasItemMaterial<class_canvasitemmaterial>`  | :ref:`tile_get_material<class_TileSet_tile_get_material>`  **(** :ref:`int<class_int>` id  **)** const                                                                                      |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`                          | :ref:`tile_get_name<class_TileSet_tile_get_name>`  **(** :ref:`int<class_int>` id  **)** const                                                                                              |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`NavigationPolygon<class_navigationpolygon>`    | :ref:`tile_get_navigation_polygon<class_TileSet_tile_get_navigation_polygon>`  **(** :ref:`int<class_int>` id  **)** const                                                                  |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`                        | :ref:`tile_get_navigation_polygon_offset<class_TileSet_tile_get_navigation_polygon_offset>`  **(** :ref:`int<class_int>` id  **)** const                                                    |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`                        | :ref:`tile_get_occluder_offset<class_TileSet_tile_get_occluder_offset>`  **(** :ref:`int<class_int>` id  **)** const                                                                        |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`                            | :ref:`tile_get_region<class_TileSet_tile_get_region>`  **(** :ref:`int<class_int>` id  **)** const                                                                                          |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Shape2D<class_shape2d>`                        | :ref:`tile_get_shape<class_TileSet_tile_get_shape>`  **(** :ref:`int<class_int>` id  **)** const                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`                        | :ref:`tile_get_shape_offset<class_TileSet_tile_get_shape_offset>`  **(** :ref:`int<class_int>` id  **)** const                                                                              |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`                            | :ref:`tile_get_shapes<class_TileSet_tile_get_shapes>`  **(** :ref:`int<class_int>` id  **)** const                                                                                          |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`                        | :ref:`tile_get_texture<class_TileSet_tile_get_texture>`  **(** :ref:`int<class_int>` id  **)** const                                                                                        |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`                        | :ref:`tile_get_texture_offset<class_TileSet_tile_get_texture_offset>`  **(** :ref:`int<class_int>` id  **)** const                                                                          |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`tile_set_light_occluder<class_TileSet_tile_set_light_occluder>`  **(** :ref:`int<class_int>` id, :ref:`OccluderPolygon2D<class_occluderpolygon2d>` light_occluder  **)**              |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`tile_set_material<class_TileSet_tile_set_material>`  **(** :ref:`int<class_int>` id, :ref:`CanvasItemMaterial<class_canvasitemmaterial>` material  **)**                              |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`tile_set_name<class_TileSet_tile_set_name>`  **(** :ref:`int<class_int>` id, :ref:`String<class_string>` name  **)**                                                                  |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`tile_set_navigation_polygon<class_TileSet_tile_set_navigation_polygon>`  **(** :ref:`int<class_int>` id, :ref:`NavigationPolygon<class_navigationpolygon>` navigation_polygon  **)**  |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`tile_set_navigation_polygon_offset<class_TileSet_tile_set_navigation_polygon_offset>`  **(** :ref:`int<class_int>` id, :ref:`Vector2<class_vector2>` navigation_polygon_offset  **)** |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`tile_set_occluder_offset<class_TileSet_tile_set_occluder_offset>`  **(** :ref:`int<class_int>` id, :ref:`Vector2<class_vector2>` occluder_offset  **)**                               |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`tile_set_region<class_TileSet_tile_set_region>`  **(** :ref:`int<class_int>` id, :ref:`Rect2<class_rect2>` region  **)**                                                              |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`tile_set_shape<class_TileSet_tile_set_shape>`  **(** :ref:`int<class_int>` id, :ref:`Shape2D<class_shape2d>` shape  **)**                                                             |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`tile_set_shape_offset<class_TileSet_tile_set_shape_offset>`  **(** :ref:`int<class_int>` id, :ref:`Vector2<class_vector2>` shape_offset  **)**                                        |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`tile_set_shapes<class_TileSet_tile_set_shapes>`  **(** :ref:`int<class_int>` id, :ref:`Array<class_array>` shapes  **)**                                                              |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`tile_set_texture<class_TileSet_tile_set_texture>`  **(** :ref:`int<class_int>` id, :ref:`Texture<class_texture>` texture  **)**                                                       |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                 | :ref:`tile_set_texture_offset<class_TileSet_tile_set_texture_offset>`  **(** :ref:`int<class_int>` id, :ref:`Vector2<class_vector2>` texture_offset  **)**                                  |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

A TileSet is a library of tiles for a :ref:`TileMap<class_tilemap>`. It contains a list of tiles, each consisting of a sprite and optional collision shapes.

Tiles are referenced by a unique integer ID.

Member Function Description
---------------------------

.. _class_TileSet_clear:

- void  **clear**  **(** **)**

Clear all tiles.

.. _class_TileSet_create_tile:

- void  **create_tile**  **(** :ref:`int<class_int>` id  **)**

Create a new tile which will be referenced by the given ID.

.. _class_TileSet_find_tile_by_name:

- :ref:`int<class_int>`  **find_tile_by_name**  **(** :ref:`String<class_string>` name  **)** const

Find the first tile matching the given name.

.. _class_TileSet_get_last_unused_tile_id:

- :ref:`int<class_int>`  **get_last_unused_tile_id**  **(** **)** const

Return the ID following the last currently used ID, useful when creating a new tile.

.. _class_TileSet_get_tiles_ids:

- :ref:`Array<class_array>`  **get_tiles_ids**  **(** **)** const

Return an array of all currently used tile IDs.

.. _class_TileSet_remove_tile:

- void  **remove_tile**  **(** :ref:`int<class_int>` id  **)**

Remove the tile referenced by the given ID.

.. _class_TileSet_tile_get_light_occluder:

- :ref:`OccluderPolygon2D<class_occluderpolygon2d>`  **tile_get_light_occluder**  **(** :ref:`int<class_int>` id  **)** const

Return the light occluder of the tile.

.. _class_TileSet_tile_get_material:

- :ref:`CanvasItemMaterial<class_canvasitemmaterial>`  **tile_get_material**  **(** :ref:`int<class_int>` id  **)** const

Return the material of the tile.

.. _class_TileSet_tile_get_name:

- :ref:`String<class_string>`  **tile_get_name**  **(** :ref:`int<class_int>` id  **)** const

Return the name of the tile.

.. _class_TileSet_tile_get_navigation_polygon:

- :ref:`NavigationPolygon<class_navigationpolygon>`  **tile_get_navigation_polygon**  **(** :ref:`int<class_int>` id  **)** const

Return the navigation polygon of the tile.

.. _class_TileSet_tile_get_navigation_polygon_offset:

- :ref:`Vector2<class_vector2>`  **tile_get_navigation_polygon_offset**  **(** :ref:`int<class_int>` id  **)** const

Return the offset of the tile's navigation polygon.

.. _class_TileSet_tile_get_occluder_offset:

- :ref:`Vector2<class_vector2>`  **tile_get_occluder_offset**  **(** :ref:`int<class_int>` id  **)** const

Return the offset of the tile's light occluder.

.. _class_TileSet_tile_get_region:

- :ref:`Rect2<class_rect2>`  **tile_get_region**  **(** :ref:`int<class_int>` id  **)** const

Return the tile sub-region in the texture.

.. _class_TileSet_tile_get_shape:

- :ref:`Shape2D<class_shape2d>`  **tile_get_shape**  **(** :ref:`int<class_int>` id  **)** const

Return the shape of the tile.

.. _class_TileSet_tile_get_shape_offset:

- :ref:`Vector2<class_vector2>`  **tile_get_shape_offset**  **(** :ref:`int<class_int>` id  **)** const

Return the shape offset of the tile.

.. _class_TileSet_tile_get_shapes:

- :ref:`Array<class_array>`  **tile_get_shapes**  **(** :ref:`int<class_int>` id  **)** const

Return the array of shapes of the tile.

.. _class_TileSet_tile_get_texture:

- :ref:`Texture<class_texture>`  **tile_get_texture**  **(** :ref:`int<class_int>` id  **)** const

Return the texture of the tile.

.. _class_TileSet_tile_get_texture_offset:

- :ref:`Vector2<class_vector2>`  **tile_get_texture_offset**  **(** :ref:`int<class_int>` id  **)** const

Return the texture offset of the tile.

.. _class_TileSet_tile_set_light_occluder:

- void  **tile_set_light_occluder**  **(** :ref:`int<class_int>` id, :ref:`OccluderPolygon2D<class_occluderpolygon2d>` light_occluder  **)**

Set a light occluder for the tile.

.. _class_TileSet_tile_set_material:

- void  **tile_set_material**  **(** :ref:`int<class_int>` id, :ref:`CanvasItemMaterial<class_canvasitemmaterial>` material  **)**

Set the material of the tile.

.. _class_TileSet_tile_set_name:

- void  **tile_set_name**  **(** :ref:`int<class_int>` id, :ref:`String<class_string>` name  **)**

Set the name of the tile, for descriptive purposes.

.. _class_TileSet_tile_set_navigation_polygon:

- void  **tile_set_navigation_polygon**  **(** :ref:`int<class_int>` id, :ref:`NavigationPolygon<class_navigationpolygon>` navigation_polygon  **)**

Set a navigation polygon for the tile.

.. _class_TileSet_tile_set_navigation_polygon_offset:

- void  **tile_set_navigation_polygon_offset**  **(** :ref:`int<class_int>` id, :ref:`Vector2<class_vector2>` navigation_polygon_offset  **)**

Set an offset for the tile's navigation polygon.

.. _class_TileSet_tile_set_occluder_offset:

- void  **tile_set_occluder_offset**  **(** :ref:`int<class_int>` id, :ref:`Vector2<class_vector2>` occluder_offset  **)**

Set an offset for the tile's light occluder.

.. _class_TileSet_tile_set_region:

- void  **tile_set_region**  **(** :ref:`int<class_int>` id, :ref:`Rect2<class_rect2>` region  **)**

Set the tile sub-region in the texture. This is common in texture atlases.

.. _class_TileSet_tile_set_shape:

- void  **tile_set_shape**  **(** :ref:`int<class_int>` id, :ref:`Shape2D<class_shape2d>` shape  **)**

Set a shape for the tile, enabling physics to collide with it.

.. _class_TileSet_tile_set_shape_offset:

- void  **tile_set_shape_offset**  **(** :ref:`int<class_int>` id, :ref:`Vector2<class_vector2>` shape_offset  **)**

Set the shape offset of the tile.

.. _class_TileSet_tile_set_shapes:

- void  **tile_set_shapes**  **(** :ref:`int<class_int>` id, :ref:`Array<class_array>` shapes  **)**

Set an array of shapes for the tile, enabling physics to collide with it.

.. _class_TileSet_tile_set_texture:

- void  **tile_set_texture**  **(** :ref:`int<class_int>` id, :ref:`Texture<class_texture>` texture  **)**

Set the texture of the tile.

.. _class_TileSet_tile_set_texture_offset:

- void  **tile_set_texture_offset**  **(** :ref:`int<class_int>` id, :ref:`Vector2<class_vector2>` texture_offset  **)**

Set the texture offset of the tile.


