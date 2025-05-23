.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_BoneAttachment:

BoneAttachment
==============

**Inherits:** :ref:`Spatial<class_spatial>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

A node that will attach to a bone.

Member Functions
----------------

+------------------------------+--------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_bone_name<class_BoneAttachment_get_bone_name>`  **(** **)** const                                  |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_bone_name<class_BoneAttachment_set_bone_name>`  **(** :ref:`String<class_string>` bone_name  **)** |
+------------------------------+--------------------------------------------------------------------------------------------------------------+

Description
-----------

This node must be the child of a :ref:`Skeleton<class_skeleton>` node. You can then select a bone for this node to attach to. The BoneAttachment node will copy the transform of the selected bone.

Member Function Description
---------------------------

.. _class_BoneAttachment_get_bone_name:

- :ref:`String<class_string>`  **get_bone_name**  **(** **)** const

.. _class_BoneAttachment_set_bone_name:

- void  **set_bone_name**  **(** :ref:`String<class_string>` bone_name  **)**


