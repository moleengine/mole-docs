.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_BaseButton:

BaseButton
==========

**Inherits:** :ref:`Control<class_control>` **<** :ref:`CanvasItem<class_canvasitem>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Inherited By:** :ref:`LinkButton<class_linkbutton>`, :ref:`TextureButton<class_texturebutton>`, :ref:`Button<class_button>`

**Category:** Core

Brief Description
-----------------

Provides a base class for different kinds of buttons.

Member Functions
----------------

+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`_pressed<class_BaseButton__pressed>`  **(** **)** virtual                                                 |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`_toggled<class_BaseButton__toggled>`  **(** :ref:`bool<class_bool>` pressed  **)** virtual                |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`get_click_on_press<class_BaseButton_get_click_on_press>`  **(** **)** const                               |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_draw_mode<class_BaseButton_get_draw_mode>`  **(** **)** const                                         |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_enabled_focus_mode<class_BaseButton_get_enabled_focus_mode>`  **(** **)** const                       |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`  | :ref:`get_shortcut<class_BaseButton_get_shortcut>`  **(** **)** const                                           |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_disabled<class_BaseButton_is_disabled>`  **(** **)** const                                             |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_hovered<class_BaseButton_is_hovered>`  **(** **)** const                                               |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_pressed<class_BaseButton_is_pressed>`  **(** **)** const                                               |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_toggle_mode<class_BaseButton_is_toggle_mode>`  **(** **)** const                                       |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_click_on_press<class_BaseButton_set_click_on_press>`  **(** :ref:`bool<class_bool>` enable  **)**     |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_disabled<class_BaseButton_set_disabled>`  **(** :ref:`bool<class_bool>` disabled  **)**               |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_enabled_focus_mode<class_BaseButton_set_enabled_focus_mode>`  **(** :ref:`int<class_int>` mode  **)** |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_pressed<class_BaseButton_set_pressed>`  **(** :ref:`bool<class_bool>` pressed  **)**                  |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_shortcut<class_BaseButton_set_shortcut>`  **(** :ref:`Object<class_object>` shortcut  **)**           |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_toggle_mode<class_BaseButton_set_toggle_mode>`  **(** :ref:`bool<class_bool>` enabled  **)**          |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **button_down**  **(** **)**
Emitted when the button starts being held down.

-  **button_up**  **(** **)**
Emitted when the button stops being held down.

-  **pressed**  **(** **)**
This signal is emitted every time the button is toggled or pressed (i.e. activated, so on ``button_down`` if "Click on press" is active and on ``button_up`` otherwise).

-  **released**  **(** **)**
Emitted when the button was released. This is only emitted by non-toggle buttons and if "Click on press" is active.

-  **toggled**  **(** :ref:`bool<class_bool>` pressed  **)**
This signal is emitted when the button was just toggled between pressed and normal states (only if toggle_mode is active). The new state is contained in the *pressed* argument.


Numeric Constants
-----------------

- **DRAW_NORMAL** = **0** --- The normal state (i.e. not pressed, not hovered, not toggled and enabled) of buttons.
- **DRAW_PRESSED** = **1** --- The state of buttons are pressed.
- **DRAW_HOVER** = **2** --- The state of buttons are hovered.
- **DRAW_DISABLED** = **3** --- The state of buttons are disabled.

Description
-----------

BaseButton is the abstract base class for buttons, so it shouldn't be used directly (It doesn't display anything). Other types of buttons inherit from it.

Member Function Description
---------------------------

.. _class_BaseButton__pressed:

- void  **_pressed**  **(** **)** virtual

Called when button is pressed.

.. _class_BaseButton__toggled:

- void  **_toggled**  **(** :ref:`bool<class_bool>` pressed  **)** virtual

Called when button is toggled (only if toggle_mode is active).

.. _class_BaseButton_get_click_on_press:

- :ref:`bool<class_bool>`  **get_click_on_press**  **(** **)** const

Return the state of the click_on_press property (see :ref:`set_click_on_press<class_BaseButton_set_click_on_press>`).

.. _class_BaseButton_get_draw_mode:

- :ref:`int<class_int>`  **get_draw_mode**  **(** **)** const

Return the visual state used to draw the button. This is useful mainly when implementing your own draw code by either overriding _draw() or connecting to "draw" signal. The visual state of the button is defined by the DRAW\_\* enum.

.. _class_BaseButton_get_enabled_focus_mode:

- :ref:`int<class_int>`  **get_enabled_focus_mode**  **(** **)** const

Returns focus access mode used when switching between enabled/disabled (see :ref:`Control.set_focus_mode<class_Control_set_focus_mode>` and :ref:`set_disabled<class_BaseButton_set_disabled>`).

.. _class_BaseButton_get_shortcut:

- :ref:`Object<class_object>`  **get_shortcut**  **(** **)** const

.. _class_BaseButton_is_disabled:

- :ref:`bool<class_bool>`  **is_disabled**  **(** **)** const

Return whether the button is in disabled state (see :ref:`set_disabled<class_BaseButton_set_disabled>`).

.. _class_BaseButton_is_hovered:

- :ref:`bool<class_bool>`  **is_hovered**  **(** **)** const

Return true if mouse entered the button before it exit.

.. _class_BaseButton_is_pressed:

- :ref:`bool<class_bool>`  **is_pressed**  **(** **)** const

If toggle_mode is active, return whether the button is toggled. If toggle_mode is not active, return whether the button is pressed down.

.. _class_BaseButton_is_toggle_mode:

- :ref:`bool<class_bool>`  **is_toggle_mode**  **(** **)** const

Return the toggle_mode property (see :ref:`set_toggle_mode<class_BaseButton_set_toggle_mode>`).

.. _class_BaseButton_set_click_on_press:

- void  **set_click_on_press**  **(** :ref:`bool<class_bool>` enable  **)**

Set the button click_on_press mode. This mode generates click events when a mouse button or key is just pressed (by default events are generated when the button/keys are released and both press and release occur in the visual area of the Button).

.. _class_BaseButton_set_disabled:

- void  **set_disabled**  **(** :ref:`bool<class_bool>` disabled  **)**

Set the button into disabled state. When a button is disabled, it can't be clicked or toggled.

.. _class_BaseButton_set_enabled_focus_mode:

- void  **set_enabled_focus_mode**  **(** :ref:`int<class_int>` mode  **)**

Sets the focus access mode to use when switching between enabled/disabled (see :ref:`Control.set_focus_mode<class_Control_set_focus_mode>` and :ref:`set_disabled<class_BaseButton_set_disabled>`).

.. _class_BaseButton_set_pressed:

- void  **set_pressed**  **(** :ref:`bool<class_bool>` pressed  **)**

Set the button to pressed state (only if toggle_mode is active).

.. _class_BaseButton_set_shortcut:

- void  **set_shortcut**  **(** :ref:`Object<class_object>` shortcut  **)**

.. _class_BaseButton_set_toggle_mode:

- void  **set_toggle_mode**  **(** :ref:`bool<class_bool>` enabled  **)**

Set the button toggle_mode property. Toggle mode makes the button flip state between pressed and unpressed each time its area is clicked.


