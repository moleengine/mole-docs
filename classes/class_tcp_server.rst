.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_TCP_Server:

TCP_Server
==========

**Inherits:** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

TCP Server.

Member Functions
----------------

+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_connection_available<class_TCP_Server_is_connection_available>`  **(** **)** const                                   |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`listen<class_TCP_Server_listen>`  **(** :ref:`int<class_int>` port, :ref:`String<class_string>` bind_address="*"  **)** |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`stop<class_TCP_Server_stop>`  **(** **)**                                                                               |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`  | :ref:`take_connection<class_TCP_Server_take_connection>`  **(** **)**                                                         |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

TCP Server class. Listens to connections on a port and returns a :ref:`StreamPeerTCP<class_streampeertcp>` when got a connection.

Member Function Description
---------------------------

.. _class_TCP_Server_is_connection_available:

- :ref:`bool<class_bool>`  **is_connection_available**  **(** **)** const

Return true if a connection is available for taking.

.. _class_TCP_Server_listen:

- :ref:`int<class_int>`  **listen**  **(** :ref:`int<class_int>` port, :ref:`String<class_string>` bind_address="*"  **)**

Listen on the "port" binding to "bind_address".

If "bind_address" is set as "\*" (default), the server will listen on all available addresses (both IPv4 and IPv6).

If "bind_address" is set as "0.0.0.0" (for IPv4) or "::" (for IPv6), the server will listen on all available addresses matching that IP type.

If "bind_address" is set to any valid address (e.g. "192.168.1.101", "::1", etc), the server will only listen on the interface with that addresses (or fail if no interface with the given address exists).

.. _class_TCP_Server_stop:

- void  **stop**  **(** **)**

Stop listening.

.. _class_TCP_Server_take_connection:

- :ref:`Object<class_object>`  **take_connection**  **(** **)**

If a connection is available, return a StreamPeerTCP with the connection/


