.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_Font:

Font
====

**Inherits:** :ref:`Resource<class_resource>` **<** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Inherited By:** :ref:`DynamicFont<class_dynamicfont>`, :ref:`BitmapFont<class_bitmapfont>`

**Category:** Core

Brief Description
-----------------

Internationalized font and text drawing support.

Member Functions
----------------

+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`draw<class_Font_draw>`  **(** :ref:`RID<class_rid>` canvas_item, :ref:`Vector2<class_vector2>` pos, :ref:`String<class_string>` string, :ref:`Color<class_color>` modulate=Color(1,1,1,1), :ref:`int<class_int>` clip_w=-1  **)** const |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`draw_char<class_Font_draw_char>`  **(** :ref:`RID<class_rid>` canvas_item, :ref:`Vector2<class_vector2>` pos, :ref:`int<class_int>` char, :ref:`int<class_int>` next=-1, :ref:`Color<class_color>` modulate=Color(1,1,1,1)  **)** const |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_ascent<class_Font_get_ascent>`  **(** **)** const                                                                                                                                                                                   |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_descent<class_Font_get_descent>`  **(** **)** const                                                                                                                                                                                 |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_height<class_Font_get_height>`  **(** **)** const                                                                                                                                                                                   |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_string_size<class_Font_get_string_size>`  **(** :ref:`String<class_string>` string  **)** const                                                                                                                                     |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_distance_field_hint<class_Font_is_distance_field_hint>`  **(** **)** const                                                                                                                                                           |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`update_changes<class_Font_update_changes>`  **(** **)**                                                                                                                                                                                 |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Font contains an unicode compatible character set, as well as the ability to draw it with variable width, ascent, descent and kerning. For creating fonts from TTF files (or other font formats), see the editor support for fonts. TODO check wikipedia for graph of ascent/baseline/descent/height/etc.

Member Function Description
---------------------------

.. _class_Font_draw:

- void  **draw**  **(** :ref:`RID<class_rid>` canvas_item, :ref:`Vector2<class_vector2>` pos, :ref:`String<class_string>` string, :ref:`Color<class_color>` modulate=Color(1,1,1,1), :ref:`int<class_int>` clip_w=-1  **)** const

Draw "string" into a canvas item using the font at a given "pos" position, with "modulate" color, and optionally clipping the width. "pos" specifies the baseline, not the top. To draw from the top, *ascent* must be added to the Y axis.

.. _class_Font_draw_char:

- :ref:`float<class_float>`  **draw_char**  **(** :ref:`RID<class_rid>` canvas_item, :ref:`Vector2<class_vector2>` pos, :ref:`int<class_int>` char, :ref:`int<class_int>` next=-1, :ref:`Color<class_color>` modulate=Color(1,1,1,1)  **)** const

Draw character "char" into a canvas item using the font at a given "pos" position, with "modulate" color, and optionally kerning if "next" is passed. clipping the width. "pos" specifies the baseline, not the top. To draw from the top, *ascent* must be added to the Y axis. The width used by the character is returned, making this function useful for drawing strings character by character.

.. _class_Font_get_ascent:

- :ref:`float<class_float>`  **get_ascent**  **(** **)** const

Return the font ascent (number of pixels above the baseline).

.. _class_Font_get_descent:

- :ref:`float<class_float>`  **get_descent**  **(** **)** const

Return the font descent (number of pixels below the baseline).

.. _class_Font_get_height:

- :ref:`float<class_float>`  **get_height**  **(** **)** const

Return the total font height (ascent plus descent) in pixels.

.. _class_Font_get_string_size:

- :ref:`Vector2<class_vector2>`  **get_string_size**  **(** :ref:`String<class_string>` string  **)** const

Return the size of a string, taking kerning and advance into account.

.. _class_Font_is_distance_field_hint:

- :ref:`bool<class_bool>`  **is_distance_field_hint**  **(** **)** const

.. _class_Font_update_changes:

- void  **update_changes**  **(** **)**

After editing a font (changing size, ascent, char rects, etc.). Call this function to propagate changes to controls that might use it.


