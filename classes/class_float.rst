.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_float:

float
=====

**Category:** Built-In Types

Brief Description
-----------------

Float built-in type

Member Functions
----------------

+----------------------------+--------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`float<class_float_float>`  **(** :ref:`bool<class_bool>` from  **)**     |
+----------------------------+--------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`float<class_float_float>`  **(** :ref:`int<class_int>` from  **)**       |
+----------------------------+--------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`float<class_float_float>`  **(** :ref:`String<class_string>` from  **)** |
+----------------------------+--------------------------------------------------------------------------------+

Description
-----------

Float built-in type.

Member Function Description
---------------------------

.. _class_float_float:

- :ref:`float<class_float>`  **float**  **(** :ref:`bool<class_bool>` from  **)**

Cast a :ref:`bool<class_bool>` value to a floating point value, ``float(true)`` will be equals to 1.0 and ``float(false)`` will be equals to 0.0.

.. _class_float_float:

- :ref:`float<class_float>`  **float**  **(** :ref:`int<class_int>` from  **)**

Cast an :ref:`int<class_int>` value to a floating point value, ``float(1)`` will be equals to 1.0.

.. _class_float_float:

- :ref:`float<class_float>`  **float**  **(** :ref:`String<class_string>` from  **)**

Cast a :ref:`String<class_string>` value to a floating point value. This method accepts float value strings like `` '1.23' `` and exponential notation strings for its parameter so calling `` float('1e3') `` will return 1000.0 and calling `` float('1e-3') `` will return -0.001.


