.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_TextureFrame:

TextureFrame
============

**Inherits:** :ref:`Control<class_control>` **<** :ref:`CanvasItem<class_canvasitem>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Control Frame that draws a texture.

Member Functions
----------------

+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`Color<class_color>`    | :ref:`get_modulate<class_TextureFrame_get_modulate>`  **(** **)** const                                       |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_stretch_mode<class_TextureFrame_get_stretch_mode>`  **(** **)** const                               |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`  | :ref:`get_texture<class_TextureFrame_get_texture>`  **(** **)** const                                         |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`has_expand<class_TextureFrame_has_expand>`  **(** **)** const                                           |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_expand<class_TextureFrame_set_expand>`  **(** :ref:`bool<class_bool>` enable  **)**                 |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_modulate<class_TextureFrame_set_modulate>`  **(** :ref:`Color<class_color>` modulate  **)**         |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_stretch_mode<class_TextureFrame_set_stretch_mode>`  **(** :ref:`int<class_int>` stretch_mode  **)** |
+------------------------------+---------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_texture<class_TextureFrame_set_texture>`  **(** :ref:`Object<class_object>` texture  **)**          |
+------------------------------+---------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

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

Control frame that simply draws an assigned texture. It can stretch or not. It's a simple way to just show an image in a UI.

Member Function Description
---------------------------

.. _class_TextureFrame_get_modulate:

- :ref:`Color<class_color>`  **get_modulate**  **(** **)** const

.. _class_TextureFrame_get_stretch_mode:

- :ref:`int<class_int>`  **get_stretch_mode**  **(** **)** const

.. _class_TextureFrame_get_texture:

- :ref:`Object<class_object>`  **get_texture**  **(** **)** const

.. _class_TextureFrame_has_expand:

- :ref:`bool<class_bool>`  **has_expand**  **(** **)** const

.. _class_TextureFrame_set_expand:

- void  **set_expand**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_TextureFrame_set_modulate:

- void  **set_modulate**  **(** :ref:`Color<class_color>` modulate  **)**

.. _class_TextureFrame_set_stretch_mode:

- void  **set_stretch_mode**  **(** :ref:`int<class_int>` stretch_mode  **)**

.. _class_TextureFrame_set_texture:

- void  **set_texture**  **(** :ref:`Object<class_object>` texture  **)**


