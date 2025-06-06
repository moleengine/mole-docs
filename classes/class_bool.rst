.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_bool:

bool
====

**Category:** Built-In Types

Brief Description
-----------------

Boolean built-in type

Member Functions
----------------

+--------------------------+-----------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`bool<class_bool_bool>`  **(** :ref:`int<class_int>` from  **)**       |
+--------------------------+-----------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`bool<class_bool_bool>`  **(** :ref:`float<class_float>` from  **)**   |
+--------------------------+-----------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`bool<class_bool_bool>`  **(** :ref:`String<class_string>` from  **)** |
+--------------------------+-----------------------------------------------------------------------------+

Description
-----------

Boolean built-in type.

Member Function Description
---------------------------

.. _class_bool_bool:

- :ref:`bool<class_bool>`  **bool**  **(** :ref:`int<class_int>` from  **)**

Cast an :ref:`int<class_int>` value to a boolean value, this method will return true if called with an integer value different to 0 and false in other case.

.. _class_bool_bool:

- :ref:`bool<class_bool>`  **bool**  **(** :ref:`float<class_float>` from  **)**

Cast a :ref:`float<class_float>` value to a boolean value, this method will return true if called with a floating point value different to 0 and false in other case.

.. _class_bool_bool:

- :ref:`bool<class_bool>`  **bool**  **(** :ref:`String<class_string>` from  **)**

Cast a :ref:`String<class_string>` value to a boolean value, this method will return true if called with a non empty string and false in other case. Examples: ``bool('False')`` returns true, ``bool('')``. returns false


