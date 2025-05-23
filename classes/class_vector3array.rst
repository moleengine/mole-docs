.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_Vector3Array:

Vector3Array
============

**Category:** Built-In Types

Brief Description
-----------------

An Array of Vector3.

Member Functions
----------------

+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3Array<class_vector3array>`  | :ref:`Vector3Array<class_Vector3Array_Vector3Array>`  **(** :ref:`Array<class_array>` from  **)**                       |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`append<class_Vector3Array_append>`  **(** :ref:`Vector3<class_vector3>` vector3  **)**                            |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`append_array<class_Vector3Array_append_array>`  **(** :ref:`Vector3Array<class_vector3array>` array  **)**        |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                    | :ref:`insert<class_Vector3Array_insert>`  **(** :ref:`int<class_int>` idx, :ref:`Vector3<class_vector3>` vector3  **)** |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`invert<class_Vector3Array_invert>`  **(** **)**                                                                   |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`push_back<class_Vector3Array_push_back>`  **(** :ref:`Vector3<class_vector3>` vector3  **)**                      |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`remove<class_Vector3Array_remove>`  **(** :ref:`int<class_int>` idx  **)**                                        |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`resize<class_Vector3Array_resize>`  **(** :ref:`int<class_int>` idx  **)**                                        |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set<class_Vector3Array_set>`  **(** :ref:`int<class_int>` idx, :ref:`Vector3<class_vector3>` vector3  **)**       |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                    | :ref:`size<class_Vector3Array_size>`  **(** **)**                                                                       |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+

Description
-----------

An Array specifically designed to hold Vector3.

Member Function Description
---------------------------

.. _class_Vector3Array_Vector3Array:

- :ref:`Vector3Array<class_vector3array>`  **Vector3Array**  **(** :ref:`Array<class_array>` from  **)**

Construct a new Vector3Array. Optionally, you can pass in an Array that will be converted.

.. _class_Vector3Array_append:

- void  **append**  **(** :ref:`Vector3<class_vector3>` vector3  **)**

Append an element at the end of the array (alias of :ref:`push_back<class_Vector3Array_push_back>`).

.. _class_Vector3Array_append_array:

- void  **append_array**  **(** :ref:`Vector3Array<class_vector3array>` array  **)**

Append an :ref:`Vector3Array<class_vector3array>` at the end of this array.

.. _class_Vector3Array_insert:

- :ref:`int<class_int>`  **insert**  **(** :ref:`int<class_int>` idx, :ref:`Vector3<class_vector3>` vector3  **)**

Insert a new element at a given position in the array. The position must be valid, or at the end of the array (pos==size()).

.. _class_Vector3Array_invert:

- void  **invert**  **(** **)**

Reverse the order of the elements in the array (so first element will now be the last).

.. _class_Vector3Array_push_back:

- void  **push_back**  **(** :ref:`Vector3<class_vector3>` vector3  **)**

Insert a Vector3 at the end.

.. _class_Vector3Array_remove:

- void  **remove**  **(** :ref:`int<class_int>` idx  **)**

Remove an element from the array by index.

.. _class_Vector3Array_resize:

- void  **resize**  **(** :ref:`int<class_int>` idx  **)**

Set the size of the Vector3Array. If larger than the current size it will reserve some space beforehand, and if it is smaller it will cut off the array.

.. _class_Vector3Array_set:

- void  **set**  **(** :ref:`int<class_int>` idx, :ref:`Vector3<class_vector3>` vector3  **)**

Change the :ref:`Vector3<class_vector3>` at the given index.

.. _class_Vector3Array_size:

- :ref:`int<class_int>`  **size**  **(** **)**

Return the size of the array.


