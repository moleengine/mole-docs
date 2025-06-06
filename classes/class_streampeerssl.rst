.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_StreamPeerSSL:

StreamPeerSSL
=============

**Inherits:** :ref:`StreamPeer<class_streampeer>` **<** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

SSL Stream peer.

Member Functions
----------------

+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Error                  | :ref:`accept<class_StreamPeerSSL_accept>`  **(** :ref:`StreamPeer<class_streampeer>` stream  **)**                                                                                              |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Error                  | :ref:`connect<class_StreamPeerSSL_connect>`  **(** :ref:`StreamPeer<class_streampeer>` stream, :ref:`bool<class_bool>` validate_certs=false, :ref:`String<class_string>` for_hostname=""  **)** |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                   | :ref:`disconnect<class_StreamPeerSSL_disconnect>`  **(** **)**                                                                                                                                  |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`  | :ref:`get_status<class_StreamPeerSSL_get_status>`  **(** **)** const                                                                                                                            |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **STATUS_DISCONNECTED** = **0** --- A status representing a :ref:`StreamPeerSSL<class_streampeerssl>` that is disconnected.
- **STATUS_CONNECTED** = **1** --- A status representing a :ref:`StreamPeerSSL<class_streampeerssl>` that is connected to a host.
- **STATUS_ERROR_NO_CERTIFICATE** = **2** --- An errot status that shows the peer did not present a SSL certificate and validation was requested.
- **STATUS_ERROR_HOSTNAME_MISMATCH** = **3** --- An error status that shows a mismatch in the SSL certificate domain presented by the host and the domain requested for validation.

Description
-----------

SSL Stream peer. This object can be used to connect to SSL servers.

Member Function Description
---------------------------

.. _class_StreamPeerSSL_accept:

- Error  **accept**  **(** :ref:`StreamPeer<class_streampeer>` stream  **)**

.. _class_StreamPeerSSL_connect:

- Error  **connect**  **(** :ref:`StreamPeer<class_streampeer>` stream, :ref:`bool<class_bool>` validate_certs=false, :ref:`String<class_string>` for_hostname=""  **)**

Connect to a peer using an underlying :ref:`StreamPeer<class_streampeer>` "stream", when "validate_certs" is true, :ref:`StreamPeerSSL<class_streampeerssl>` will validate that the certificate presented by the peer matches the "for_hostname".

.. _class_StreamPeerSSL_disconnect:

- void  **disconnect**  **(** **)**

Disconnect from host.

.. _class_StreamPeerSSL_get_status:

- :ref:`int<class_int>`  **get_status**  **(** **)** const

Return the status of the connection, one of STATUS\_\* enum.


