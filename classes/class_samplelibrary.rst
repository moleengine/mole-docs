.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_SampleLibrary:

SampleLibrary
=============

**Inherits:** :ref:`Resource<class_resource>` **<** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Library that contains a collection of samples.

Member Functions
----------------

+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`add_sample<class_SampleLibrary_add_sample>`  **(** :ref:`String<class_string>` name, :ref:`Sample<class_sample>` sample  **)**                      |
+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Sample<class_sample>`  | :ref:`get_sample<class_SampleLibrary_get_sample>`  **(** :ref:`String<class_string>` name  **)** const                                                    |
+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`    | :ref:`get_sample_list<class_SampleLibrary_get_sample_list>`  **(** **)** const                                                                            |
+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`has_sample<class_SampleLibrary_has_sample>`  **(** :ref:`String<class_string>` name  **)** const                                                    |
+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`remove_sample<class_SampleLibrary_remove_sample>`  **(** :ref:`String<class_string>` name  **)**                                                    |
+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`    | :ref:`sample_get_pitch_scale<class_SampleLibrary_sample_get_pitch_scale>`  **(** :ref:`String<class_string>` name  **)** const                            |
+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`sample_get_priority<class_SampleLibrary_sample_get_priority>`  **(** :ref:`String<class_string>` name  **)** const                                  |
+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`    | :ref:`sample_get_volume_db<class_SampleLibrary_sample_get_volume_db>`  **(** :ref:`String<class_string>` name  **)** const                                |
+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`sample_set_pitch_scale<class_SampleLibrary_sample_set_pitch_scale>`  **(** :ref:`String<class_string>` name, :ref:`float<class_float>` pitch  **)** |
+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`sample_set_priority<class_SampleLibrary_sample_set_priority>`  **(** :ref:`String<class_string>` name, :ref:`int<class_int>` priority  **)**        |
+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`sample_set_volume_db<class_SampleLibrary_sample_set_volume_db>`  **(** :ref:`String<class_string>` name, :ref:`float<class_float>` db  **)**        |
+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Library that contains a collection of :ref:`Sample<class_sample>`, each identified by a text ID. This is used as a data container for the majority of the SamplePlayer classes and derivatives.

Sample players will never yield an active (currently playing) voice for a new playback request when there are no inactive voices available if the priority of the sample requested to be played is lower than that of every currently played samples.

Member Function Description
---------------------------

.. _class_SampleLibrary_add_sample:

- void  **add_sample**  **(** :ref:`String<class_string>` name, :ref:`Sample<class_sample>` sample  **)**

Add a sample to the library, with a given text ID.

.. _class_SampleLibrary_get_sample:

- :ref:`Sample<class_sample>`  **get_sample**  **(** :ref:`String<class_string>` name  **)** const

Return the sample from the library matching the given text ID. Return null if the sample is not found.

.. _class_SampleLibrary_get_sample_list:

- :ref:`Array<class_array>`  **get_sample_list**  **(** **)** const

.. _class_SampleLibrary_has_sample:

- :ref:`bool<class_bool>`  **has_sample**  **(** :ref:`String<class_string>` name  **)** const

Return true if the sample text ID exists in the library.

.. _class_SampleLibrary_remove_sample:

- void  **remove_sample**  **(** :ref:`String<class_string>` name  **)**

Remove the sample matching the given text ID.

.. _class_SampleLibrary_sample_get_pitch_scale:

- :ref:`float<class_float>`  **sample_get_pitch_scale**  **(** :ref:`String<class_string>` name  **)** const

Return the pitch scale for the given sample.

.. _class_SampleLibrary_sample_get_priority:

- :ref:`int<class_int>`  **sample_get_priority**  **(** :ref:`String<class_string>` name  **)** const

Return the priority for the given sample.

.. _class_SampleLibrary_sample_get_volume_db:

- :ref:`float<class_float>`  **sample_get_volume_db**  **(** :ref:`String<class_string>` name  **)** const

Return the volume (in dB) for the given sample.

.. _class_SampleLibrary_sample_set_pitch_scale:

- void  **sample_set_pitch_scale**  **(** :ref:`String<class_string>` name, :ref:`float<class_float>` pitch  **)**

Set the pitch scale for the given sample.

.. _class_SampleLibrary_sample_set_priority:

- void  **sample_set_priority**  **(** :ref:`String<class_string>` name, :ref:`int<class_int>` priority  **)**

Set the priority for the given sample.

.. _class_SampleLibrary_sample_set_volume_db:

- void  **sample_set_volume_db**  **(** :ref:`String<class_string>` name, :ref:`float<class_float>` db  **)**

Set the volume (in dB) for the given sample.


