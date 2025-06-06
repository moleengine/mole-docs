.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_TextureButton:

TextureButton
=============

**Inherits:** :ref:`BaseButton<class_basebutton>` **<** :ref:`Control<class_control>` **<** :ref:`CanvasItem<class_canvasitem>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Button that can be themed with textures.

Member Functions
----------------

+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`BitMap<class_bitmap>`    | :ref:`get_click_mask<class_TextureButton_get_click_mask>`  **(** **)** const                                              |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`  | :ref:`get_disabled_texture<class_TextureButton_get_disabled_texture>`  **(** **)** const                                  |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`  | :ref:`get_focused_texture<class_TextureButton_get_focused_texture>`  **(** **)** const                                    |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`  | :ref:`get_hover_texture<class_TextureButton_get_hover_texture>`  **(** **)** const                                        |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`Color<class_color>`      | :ref:`get_modulate<class_TextureButton_get_modulate>`  **(** **)** const                                                  |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`  | :ref:`get_normal_texture<class_TextureButton_get_normal_texture>`  **(** **)** const                                      |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`  | :ref:`get_pressed_texture<class_TextureButton_get_pressed_texture>`  **(** **)** const                                    |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_resize_mode<class_TextureButton_get_resize_mode>`  **(** **)** const                                            |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_stretch_mode<class_TextureButton_get_stretch_mode>`  **(** **)** const                                          |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_texture_scale<class_TextureButton_get_texture_scale>`  **(** **)** const                                        |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_click_mask<class_TextureButton_set_click_mask>`  **(** :ref:`BitMap<class_bitmap>` mask  **)**                  |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_disabled_texture<class_TextureButton_set_disabled_texture>`  **(** :ref:`Texture<class_texture>` texture  **)** |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_focused_texture<class_TextureButton_set_focused_texture>`  **(** :ref:`Texture<class_texture>` texture  **)**   |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_hover_texture<class_TextureButton_set_hover_texture>`  **(** :ref:`Texture<class_texture>` texture  **)**       |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_modulate<class_TextureButton_set_modulate>`  **(** :ref:`Color<class_color>` color  **)**                       |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_normal_texture<class_TextureButton_set_normal_texture>`  **(** :ref:`Texture<class_texture>` texture  **)**     |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_pressed_texture<class_TextureButton_set_pressed_texture>`  **(** :ref:`Texture<class_texture>` texture  **)**   |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_resize_mode<class_TextureButton_set_resize_mode>`  **(** :ref:`int<class_int>` p_mode  **)**                    |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_stretch_mode<class_TextureButton_set_stretch_mode>`  **(** :ref:`int<class_int>` p_mode  **)**                  |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_texture_scale<class_TextureButton_set_texture_scale>`  **(** :ref:`Vector2<class_vector2>` scale  **)**         |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **RESIZE_SCALE** = **0**
- **RESIZE_STRETCH** = **1**
- **STRETCH_SCALE_ON_EXPAND** = **0**
- **STRETCH_SCALE** = **1**
- **STRETCH_TILE** = **2**
- **STRETCH_KEEP** = **3**
- **STRETCH_KEEP_CENTERED** = **4**
- **STRETCH_KEEP_ASPECT** = **5**
- **STRETCH_KEEP_ASPECT_CENTERED** = **6**
- **STRETCH_KEEP_ASPECT_COVERED** = **7**

Description
-----------

Button that can be themed with textures. This is like a regular :ref:`Button<class_button>` but can be themed by assigning textures to it. This button is intended to be easy to theme, however a regular button can expand (that uses styleboxes) and still be better if the interface is expect to have internationalization of texts.

Only the normal texture is required, the others are optional.

Member Function Description
---------------------------

.. _class_TextureButton_get_click_mask:

- :ref:`BitMap<class_bitmap>`  **get_click_mask**  **(** **)** const

.. _class_TextureButton_get_disabled_texture:

- :ref:`Texture<class_texture>`  **get_disabled_texture**  **(** **)** const

.. _class_TextureButton_get_focused_texture:

- :ref:`Texture<class_texture>`  **get_focused_texture**  **(** **)** const

.. _class_TextureButton_get_hover_texture:

- :ref:`Texture<class_texture>`  **get_hover_texture**  **(** **)** const

.. _class_TextureButton_get_modulate:

- :ref:`Color<class_color>`  **get_modulate**  **(** **)** const

.. _class_TextureButton_get_normal_texture:

- :ref:`Texture<class_texture>`  **get_normal_texture**  **(** **)** const

.. _class_TextureButton_get_pressed_texture:

- :ref:`Texture<class_texture>`  **get_pressed_texture**  **(** **)** const

.. _class_TextureButton_get_resize_mode:

- :ref:`int<class_int>`  **get_resize_mode**  **(** **)** const

.. _class_TextureButton_get_stretch_mode:

- :ref:`int<class_int>`  **get_stretch_mode**  **(** **)** const

.. _class_TextureButton_get_texture_scale:

- :ref:`Vector2<class_vector2>`  **get_texture_scale**  **(** **)** const

.. _class_TextureButton_set_click_mask:

- void  **set_click_mask**  **(** :ref:`BitMap<class_bitmap>` mask  **)**

.. _class_TextureButton_set_disabled_texture:

- void  **set_disabled_texture**  **(** :ref:`Texture<class_texture>` texture  **)**

.. _class_TextureButton_set_focused_texture:

- void  **set_focused_texture**  **(** :ref:`Texture<class_texture>` texture  **)**

.. _class_TextureButton_set_hover_texture:

- void  **set_hover_texture**  **(** :ref:`Texture<class_texture>` texture  **)**

.. _class_TextureButton_set_modulate:

- void  **set_modulate**  **(** :ref:`Color<class_color>` color  **)**

.. _class_TextureButton_set_normal_texture:

- void  **set_normal_texture**  **(** :ref:`Texture<class_texture>` texture  **)**

.. _class_TextureButton_set_pressed_texture:

- void  **set_pressed_texture**  **(** :ref:`Texture<class_texture>` texture  **)**

.. _class_TextureButton_set_resize_mode:

- void  **set_resize_mode**  **(** :ref:`int<class_int>` p_mode  **)**

.. _class_TextureButton_set_stretch_mode:

- void  **set_stretch_mode**  **(** :ref:`int<class_int>` p_mode  **)**

.. _class_TextureButton_set_texture_scale:

- void  **set_texture_scale**  **(** :ref:`Vector2<class_vector2>` scale  **)**


