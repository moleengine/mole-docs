.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_SplitContainer:

SplitContainer
==============

**Inherits:** :ref:`Container<class_container>` **<** :ref:`Control<class_control>` **<** :ref:`CanvasItem<class_canvasitem>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Inherited By:** :ref:`HSplitContainer<class_hsplitcontainer>`, :ref:`VSplitContainer<class_vsplitcontainer>`

**Category:** Core

Brief Description
-----------------

Container for splitting and adjusting.

Member Functions
----------------

+--------------------------+---------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`    | :ref:`get_dragger_visibility<class_SplitContainer_get_dragger_visibility>`  **(** **)** const                       |
+--------------------------+---------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`    | :ref:`get_split_offset<class_SplitContainer_get_split_offset>`  **(** **)** const                                   |
+--------------------------+---------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_collapsed<class_SplitContainer_is_collapsed>`  **(** **)** const                                           |
+--------------------------+---------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`set_collapsed<class_SplitContainer_set_collapsed>`  **(** :ref:`bool<class_bool>` collapsed  **)**            |
+--------------------------+---------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`set_dragger_visibility<class_SplitContainer_set_dragger_visibility>`  **(** :ref:`int<class_int>` mode  **)** |
+--------------------------+---------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`set_split_offset<class_SplitContainer_set_split_offset>`  **(** :ref:`int<class_int>` offset  **)**           |
+--------------------------+---------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **dragged**  **(** :ref:`int<class_int>` offset  **)**
Emmited when the dragger is gragged by user.


Numeric Constants
-----------------

- **DRAGGER_VISIBLE** = **0** --- The split dragger is visible.
- **DRAGGER_HIDDEN** = **1** --- The split dragger is invisible.
- **DRAGGER_HIDDEN_COLLAPSED** = **2** --- The split dragger is invisible and collapsed.

Description
-----------

Container for splitting two controls vertically or horizontally, with a grabber that allows adjusting the split offset or ratio.

Member Function Description
---------------------------

.. _class_SplitContainer_get_dragger_visibility:

- :ref:`int<class_int>`  **get_dragger_visibility**  **(** **)** const

Return visibility of the split dragger(One of DRAGGER_VISIBLE, DRAGGER_HIDDEN or DRAGGER_HIDDEN_COLLAPSED).

.. _class_SplitContainer_get_split_offset:

- :ref:`int<class_int>`  **get_split_offset**  **(** **)** const

Return the split offset.

.. _class_SplitContainer_is_collapsed:

- :ref:`bool<class_bool>`  **is_collapsed**  **(** **)** const

Return true if the split is collapsed.

.. _class_SplitContainer_set_collapsed:

- void  **set_collapsed**  **(** :ref:`bool<class_bool>` collapsed  **)**

Set if the split must be collapsed.

.. _class_SplitContainer_set_dragger_visibility:

- void  **set_dragger_visibility**  **(** :ref:`int<class_int>` mode  **)**

Set visibility of the split dragger(*mode* must be one of DRAGGER_VISIBLE, DRAGGER_HIDDEN or DRAGGER_HIDDEN_COLLAPSED).

.. _class_SplitContainer_set_split_offset:

- void  **set_split_offset**  **(** :ref:`int<class_int>` offset  **)**

Set the split offset.


