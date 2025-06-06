.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_SamplePlayer2D:

SamplePlayer2D
==============

**Inherits:** :ref:`SoundPlayer2D<class_soundplayer2d>` **<** :ref:`Node2D<class_node2d>` **<** :ref:`CanvasItem<class_canvasitem>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Sample player for positional 2D Sound.

Member Functions
----------------

+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                      | :ref:`get_polyphony<class_SamplePlayer2D_get_polyphony>`  **(** **)** const                                                                              |
+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                  | :ref:`get_random_pitch_scale<class_SamplePlayer2D_get_random_pitch_scale>`  **(** **)** const                                                            |
+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`SampleLibrary<class_samplelibrary>`  | :ref:`get_sample_library<class_SamplePlayer2D_get_sample_library>`  **(** **)** const                                                                    |
+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                    | :ref:`is_voice_active<class_SamplePlayer2D_is_voice_active>`  **(** :ref:`int<class_int>` voice  **)** const                                             |
+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                      | :ref:`play<class_SamplePlayer2D_play>`  **(** :ref:`String<class_string>` sample, :ref:`int<class_int>` voice=-2  **)**                                  |
+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`set_polyphony<class_SamplePlayer2D_set_polyphony>`  **(** :ref:`int<class_int>` max_voices  **)**                                                  |
+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`set_random_pitch_scale<class_SamplePlayer2D_set_random_pitch_scale>`  **(** :ref:`float<class_float>` val  **)**                                   |
+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`set_sample_library<class_SamplePlayer2D_set_sample_library>`  **(** :ref:`SampleLibrary<class_samplelibrary>` library  **)**                       |
+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`stop_all<class_SamplePlayer2D_stop_all>`  **(** **)**                                                                                              |
+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`stop_voice<class_SamplePlayer2D_stop_voice>`  **(** :ref:`int<class_int>` voice  **)**                                                             |
+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`voice_set_pitch_scale<class_SamplePlayer2D_voice_set_pitch_scale>`  **(** :ref:`int<class_int>` voice, :ref:`float<class_float>` ratio  **)**      |
+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`voice_set_volume_scale_db<class_SamplePlayer2D_voice_set_volume_scale_db>`  **(** :ref:`int<class_int>` voice, :ref:`float<class_float>` db  **)** |
+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **INVALID_VOICE** = **-1** --- Value returned if the voice or sample are invalid.
- **NEXT_VOICE** = **-2** --- Default voice for the play method. Corresponds to the first voice following the last used voice.

Description
-----------

Sample player for positional 2D Sound. Plays sound samples positionally, left and right depending on the distance/place on the screen.

Member Function Description
---------------------------

.. _class_SamplePlayer2D_get_polyphony:

- :ref:`int<class_int>`  **get_polyphony**  **(** **)** const

Return the polyphony of the player.

.. _class_SamplePlayer2D_get_random_pitch_scale:

- :ref:`float<class_float>`  **get_random_pitch_scale**  **(** **)** const

Return the amplitude used for random pitch scale variations.

.. _class_SamplePlayer2D_get_sample_library:

- :ref:`SampleLibrary<class_samplelibrary>`  **get_sample_library**  **(** **)** const

Return the sample library used by the player.

.. _class_SamplePlayer2D_is_voice_active:

- :ref:`bool<class_bool>`  **is_voice_active**  **(** :ref:`int<class_int>` voice  **)** const

Return whether a voice is still active or has stopped playing.

.. _class_SamplePlayer2D_play:

- :ref:`int<class_int>`  **play**  **(** :ref:`String<class_string>` sample, :ref:`int<class_int>` voice=-2  **)**

Play a sample. An internal polyphony ID can optionally be passed, or defaults to NEXT_VOICE.

Return a voice ID which can be used to modify the voice parameters, or INVALID_VOICE if the voice or sample are invalid.

.. _class_SamplePlayer2D_set_polyphony:

- void  **set_polyphony**  **(** :ref:`int<class_int>` max_voices  **)**

Set the polyphony of the player (maximum amount of simultaneous voices).

.. _class_SamplePlayer2D_set_random_pitch_scale:

- void  **set_random_pitch_scale**  **(** :ref:`float<class_float>` val  **)**

Set the amplitude for random pitch scale variations. If different from zero, the pitch scale will vary randomly around 1.0 in a range defined by val.

The actual pitch scale will be, with "variation" ranging from -val to val:

\* variation > 0: 1.0 + variation

\* variation < 0: 1.0/(1.0 - variation)

.. _class_SamplePlayer2D_set_sample_library:

- void  **set_sample_library**  **(** :ref:`SampleLibrary<class_samplelibrary>` library  **)**

Set the sample library for the player.

.. _class_SamplePlayer2D_stop_all:

- void  **stop_all**  **(** **)**

Stop all playing voices.

.. _class_SamplePlayer2D_stop_voice:

- void  **stop_voice**  **(** :ref:`int<class_int>` voice  **)**

Stop a given voice.

.. _class_SamplePlayer2D_voice_set_pitch_scale:

- void  **voice_set_pitch_scale**  **(** :ref:`int<class_int>` voice, :ref:`float<class_float>` ratio  **)**

Change the pitch scale of a currently playing voice.

.. _class_SamplePlayer2D_voice_set_volume_scale_db:

- void  **voice_set_volume_scale_db**  **(** :ref:`int<class_int>` voice, :ref:`float<class_float>` db  **)**

Change the volume scale (in dB) of a currently playing voice.


