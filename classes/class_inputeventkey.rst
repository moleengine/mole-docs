.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_InputEventKey:

InputEventKey
=============

**Category:** Built-In Types

Brief Description
-----------------

Built-in input event type for keyboard events.

Member Functions
----------------

+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_action<class_InputEventKey_is_action>`  **(** :ref:`String<class_string>` action  **)**                                          |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_action_pressed<class_InputEventKey_is_action_pressed>`  **(** :ref:`String<class_string>` action  **)**                          |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_action_released<class_InputEventKey_is_action_released>`  **(** :ref:`String<class_string>` action  **)**                        |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_echo<class_InputEventKey_is_echo>`  **(** **)**                                                                                  |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_pressed<class_InputEventKey_is_pressed>`  **(** **)**                                                                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`set_as_action<class_InputEventKey_set_as_action>`  **(** :ref:`String<class_string>` action, :ref:`bool<class_bool>` pressed  **)** |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

Member Variables
----------------

- :ref:`int<class_int>` **ID** - Event identifier, positive integer increased at each new event.
- :ref:`bool<class_bool>` **alt** - State of the Alt modifier.
- :ref:`bool<class_bool>` **control** - State of the Ctrl modifier.
- :ref:`int<class_int>` **device** - Device identifier.
- :ref:`bool<class_bool>` **echo** - Echo state of the key, i.e. whether it's a repeat event or not.
- :ref:`bool<class_bool>` **meta** - State of the Meta modifier.
- :ref:`bool<class_bool>` **pressed** - Pressed state of the key.
- :ref:`int<class_int>` **scancode** - Scancode of the key, one of the KEY_* constants in [@Global Scope].
- :ref:`bool<class_bool>` **shift** - State of the Shift modifier.
- :ref:`int<class_int>` **type** - Type of event (one of the [InputEvent] constants).
- :ref:`int<class_int>` **unicode** - Unicode identifier of the key (when relevant).

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

Input event type for keyboard events that extends the global :ref:`InputEvent<class_inputevent>` type.

Member Function Description
---------------------------

.. _class_InputEventKey_is_action:

- :ref:`bool<class_bool>`  **is_action**  **(** :ref:`String<class_string>` action  **)**

Return if this input event matches a pre-defined action.

.. _class_InputEventKey_is_action_pressed:

- :ref:`bool<class_bool>`  **is_action_pressed**  **(** :ref:`String<class_string>` action  **)**

Return whether the given action is being pressed.

.. _class_InputEventKey_is_action_released:

- :ref:`bool<class_bool>`  **is_action_released**  **(** :ref:`String<class_string>` action  **)**

Return whether the given action is released (i.e. not pressed).

.. _class_InputEventKey_is_echo:

- :ref:`bool<class_bool>`  **is_echo**  **(** **)**

Return if this input event is an echo event.

.. _class_InputEventKey_is_pressed:

- :ref:`bool<class_bool>`  **is_pressed**  **(** **)**

Return if this input event is pressed.

.. _class_InputEventKey_set_as_action:

- void  **set_as_action**  **(** :ref:`String<class_string>` action, :ref:`bool<class_bool>` pressed  **)**

Change the input event to an action event of the given name with the pressed status passed as argument.


