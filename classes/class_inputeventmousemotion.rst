.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_InputEventMouseMotion:

InputEventMouseMotion
=====================

**Category:** Built-In Types

Brief Description
-----------------

Built-in input event type for mouse motion events.

Member Functions
----------------

+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_action<class_InputEventMouseMotion_is_action>`  **(** :ref:`String<class_string>` action  **)**                                          |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_action_pressed<class_InputEventMouseMotion_is_action_pressed>`  **(** :ref:`String<class_string>` action  **)**                          |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_action_released<class_InputEventMouseMotion_is_action_released>`  **(** :ref:`String<class_string>` action  **)**                        |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_echo<class_InputEventMouseMotion_is_echo>`  **(** **)**                                                                                  |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_pressed<class_InputEventMouseMotion_is_pressed>`  **(** **)**                                                                            |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`set_as_action<class_InputEventMouseMotion_set_as_action>`  **(** :ref:`String<class_string>` action, :ref:`bool<class_bool>` pressed  **)** |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

Member Variables
----------------

- :ref:`int<class_int>` **ID** - Event identifier, positive integer increased at each new event.
- :ref:`bool<class_bool>` **alt** - State of the Alt modifier.
- :ref:`int<class_int>` **button_mask** - Mouse button mask identifier, one of or a bitwise combination of the BUTTON_MASK_* constants in [@Global Scope].
- :ref:`bool<class_bool>` **control** - State of the Ctrl modifier.
- :ref:`int<class_int>` **device** - Device identifier.
- :ref:`Vector2<class_vector2>` **global_pos** - Global position of the mouse pointer.
- :ref:`int<class_int>` **global_x** - Global X coordinate of the mouse pointer.
- :ref:`int<class_int>` **global_y** - Global Y coordinate of the mouse pointer.
- :ref:`bool<class_bool>` **meta** - State of the Meta modifier.
- :ref:`Vector2<class_vector2>` **pos** - Local position of the mouse pointer.
- :ref:`Vector2<class_vector2>` **relative_pos** - Position of the mouse pointer relative to the previous mouse position.
- :ref:`int<class_int>` **relative_x** - X coordinate of the mouse pointer relative to the previous mouse position.
- :ref:`int<class_int>` **relative_y** - Y coordinate of the mouse pointer relative to the previous mouse position.
- :ref:`bool<class_bool>` **shift** - State of the Shift modifier.
- :ref:`Vector2<class_vector2>` **speed** - Speed of the mouse pointer.
- :ref:`float<class_float>` **speed_x** - Speed of the mouse pointer on the X axis.
- :ref:`float<class_float>` **speed_y** - Speed of the mouse pointer on the Y axis.
- :ref:`int<class_int>` **type** - Type of event (one of the [InputEvent] constants).
- :ref:`int<class_int>` **x** - Local X coordinate of the mouse pointer.
- :ref:`int<class_int>` **y** - Local Y coordinate of the mouse pointer.

Numeric Constants
-----------------

- **NONE** = **0** --- Empty input event.
- **KEY** = **1** --- Key event.
- **MOUSE_MOTION** = **2** --- Mouse motion event.
- **MOUSE_BUTTON** = **3** --- Mouse button event.
- **JOYSTICK_MOTION** = **4** --- Joystick motion event.
- **JOYSTICK_BUTTON** = **5** --- Joystick button event.
- **SCREEN_TOUCH** = **6** --- Screen touch event.
- **SCREEN_DRAG** = **7** --- Screen drag event.
- **ACTION** = **8** --- Pre-defined action event (see :ref:`InputMap<class_inputmap>`).

Description
-----------

Input event type for mouse motion events that extends the global :ref:`InputEvent<class_inputevent>` type.

Member Function Description
---------------------------

.. _class_InputEventMouseMotion_is_action:

- :ref:`bool<class_bool>`  **is_action**  **(** :ref:`String<class_string>` action  **)**

Return if this input event matches a pre-defined action.

.. _class_InputEventMouseMotion_is_action_pressed:

- :ref:`bool<class_bool>`  **is_action_pressed**  **(** :ref:`String<class_string>` action  **)**

Return whether the given action is being pressed. Not relevant for MOUSE_MOTION events, always false.

.. _class_InputEventMouseMotion_is_action_released:

- :ref:`bool<class_bool>`  **is_action_released**  **(** :ref:`String<class_string>` action  **)**

Return whether the given action is released (i.e. not pressed). Not relevant for MOUSE_MOTION events, can be true or false depending on whether :ref:`is_action<class_InputEventMouseMotion_is_action>` is true.

.. _class_InputEventMouseMotion_is_echo:

- :ref:`bool<class_bool>`  **is_echo**  **(** **)**

Return if this input event is an echo event (only for events of type KEY, i.e. always false for this type).

.. _class_InputEventMouseMotion_is_pressed:

- :ref:`bool<class_bool>`  **is_pressed**  **(** **)**

Return if this input event is pressed. Not relevant for MOUSE_MOTION events, always false.

.. _class_InputEventMouseMotion_set_as_action:

- void  **set_as_action**  **(** :ref:`String<class_string>` action, :ref:`bool<class_bool>` pressed  **)**

Change the input event to an action event of the given name with the (irrelevant for this type) pressed status passed as argument.


