.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_GridContainer:

GridContainer
=============

**Inherits:** :ref:`Container<class_container>` **<** :ref:`Control<class_control>` **<** :ref:`CanvasItem<class_canvasitem>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Grid container used to arrange elements in a grid like layout

Member Functions
----------------

+------------------------+-------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`  | :ref:`get_columns<class_GridContainer_get_columns>`  **(** **)** const                          |
+------------------------+-------------------------------------------------------------------------------------------------+
| void                   | :ref:`set_columns<class_GridContainer_set_columns>`  **(** :ref:`int<class_int>` columns  **)** |
+------------------------+-------------------------------------------------------------------------------------------------+

Description
-----------

Grid container will arrange its children in a grid like structure, the grid columns are specified using the :ref:`set_columns<class_GridContainer_set_columns>` method and the number of rows will be equal to the number of children in the container divided by the number of columns, for example: if the container has 5 children, and 2 columns, there will be 3 rows in the container. Notice that grid layout will preserve the columns and rows for every size of the container.

Member Function Description
---------------------------

.. _class_GridContainer_get_columns:

- :ref:`int<class_int>`  **get_columns**  **(** **)** const

Returns the number of columns in this container

.. _class_GridContainer_set_columns:

- void  **set_columns**  **(** :ref:`int<class_int>` columns  **)**

Sets the numbers of columns in the container, then reorder its children to accommodate the new layout


