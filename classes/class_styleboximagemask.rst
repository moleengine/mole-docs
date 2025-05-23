.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_StyleBoxImageMask:

StyleBoxImageMask
=================

**Inherits:** :ref:`StyleBox<class_stylebox>` **<** :ref:`Resource<class_resource>` **<** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Image mask based StyleBox, for mask test.

Member Functions
----------------

+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`    | :ref:`get_expand<class_StyleBoxImageMask_get_expand>`  **(** **)** const                                                                                 |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`get_expand_margin_size<class_StyleBoxImageMask_get_expand_margin_size>`  **(** :ref:`int<class_int>` margin  **)** const                           |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Image<class_image>`  | :ref:`get_image<class_StyleBoxImageMask_get_image>`  **(** **)** const                                                                                   |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_expand<class_StyleBoxImageMask_set_expand>`  **(** :ref:`bool<class_bool>` expand  **)**                                                       |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_expand_margin_size<class_StyleBoxImageMask_set_expand_margin_size>`  **(** :ref:`int<class_int>` margin, :ref:`float<class_float>` size  **)** |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_image<class_StyleBoxImageMask_set_image>`  **(** :ref:`Image<class_image>` image  **)**                                                        |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

This StyleBox is similar to :ref:`StyleBoxTexture<class_styleboxtexture>`, but only meant to be used for mask testing. It takes an image and applies stretch rules to determine if the point clicked is masked or not.

Member Function Description
---------------------------

.. _class_StyleBoxImageMask_get_expand:

- :ref:`bool<class_bool>`  **get_expand**  **(** **)** const

Return whether the expand property is set(default). When expanding, the image will use the same rules as :ref:`StyleBoxTexture<class_styleboxtexture>` for expand. If not expanding, the image will always be tested at its original size.

.. _class_StyleBoxImageMask_get_expand_margin_size:

- :ref:`float<class_float>`  **get_expand_margin_size**  **(** :ref:`int<class_int>` margin  **)** const

Return the expand margin size (from enum MARGIN\_\*). Parts of the image below the size of the margin (and in the direction of the margin) will not expand.

.. _class_StyleBoxImageMask_get_image:

- :ref:`Image<class_image>`  **get_image**  **(** **)** const

Return the image used for mask testing. (see :ref:`set_image<class_StyleBoxImageMask_set_image>`).

.. _class_StyleBoxImageMask_set_expand:

- void  **set_expand**  **(** :ref:`bool<class_bool>` expand  **)**

Set the expand property (default). When expanding, the image will use the same rules as :ref:`StyleBoxTexture<class_styleboxtexture>` for expand. If not expanding, the image will always be tested at its original size.

.. _class_StyleBoxImageMask_set_expand_margin_size:

- void  **set_expand_margin_size**  **(** :ref:`int<class_int>` margin, :ref:`float<class_float>` size  **)**

Set an expand margin size (from enum MARGIN\_\*). Parts of the image below the size of the margin (and in the direction of the margin) will not expand.

.. _class_StyleBoxImageMask_set_image:

- void  **set_image**  **(** :ref:`Image<class_image>` image  **)**

Set the image used for mask testing. Pixels (converted to grey) that have a value, less than 0.5 will fail the test.


