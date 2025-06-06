.. Generated automatically by doc/tools/makerst.py in Mole's source tree.
.. DO NOT EDIT THIS FILE, but the doc/base/classes.xml source instead.

.. _class_PhysicsDirectBodyState:

PhysicsDirectBodyState
======================

**Inherits:** :ref:`Object<class_object>`

**Inherited By:** :ref:`PhysicsDirectBodyStateSW<class_physicsdirectbodystatesw>`

**Category:** Core

Brief Description
-----------------



Member Functions
----------------

+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                           | :ref:`add_force<class_PhysicsDirectBodyState_add_force>`  **(** :ref:`Vector3<class_vector3>` force, :ref:`Vector3<class_vector3>` pos  **)**                        |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                           | :ref:`apply_impulse<class_PhysicsDirectBodyState_apply_impulse>`  **(** :ref:`Vector3<class_vector3>` pos, :ref:`Vector3<class_vector3>` j  **)**                    |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`                                  | :ref:`get_angular_velocity<class_PhysicsDirectBodyState_get_angular_velocity>`  **(** **)** const                                                                    |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`RID<class_rid>`                                          | :ref:`get_contact_collider<class_PhysicsDirectBodyState_get_contact_collider>`  **(** :ref:`int<class_int>` contact_idx  **)** const                                 |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                                          | :ref:`get_contact_collider_id<class_PhysicsDirectBodyState_get_contact_collider_id>`  **(** :ref:`int<class_int>` contact_idx  **)** const                           |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`                                    | :ref:`get_contact_collider_object<class_PhysicsDirectBodyState_get_contact_collider_object>`  **(** :ref:`int<class_int>` contact_idx  **)** const                   |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`                                  | :ref:`get_contact_collider_pos<class_PhysicsDirectBodyState_get_contact_collider_pos>`  **(** :ref:`int<class_int>` contact_idx  **)** const                         |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                                          | :ref:`get_contact_collider_shape<class_PhysicsDirectBodyState_get_contact_collider_shape>`  **(** :ref:`int<class_int>` contact_idx  **)** const                     |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`                                  | :ref:`get_contact_collider_velocity_at_pos<class_PhysicsDirectBodyState_get_contact_collider_velocity_at_pos>`  **(** :ref:`int<class_int>` contact_idx  **)** const |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                                          | :ref:`get_contact_count<class_PhysicsDirectBodyState_get_contact_count>`  **(** **)** const                                                                          |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`                                  | :ref:`get_contact_local_normal<class_PhysicsDirectBodyState_get_contact_local_normal>`  **(** :ref:`int<class_int>` contact_idx  **)** const                         |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`                                  | :ref:`get_contact_local_pos<class_PhysicsDirectBodyState_get_contact_local_pos>`  **(** :ref:`int<class_int>` contact_idx  **)** const                               |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                                          | :ref:`get_contact_local_shape<class_PhysicsDirectBodyState_get_contact_local_shape>`  **(** :ref:`int<class_int>` contact_idx  **)** const                           |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`                                  | :ref:`get_inverse_inertia<class_PhysicsDirectBodyState_get_inverse_inertia>`  **(** **)** const                                                                      |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                                      | :ref:`get_inverse_mass<class_PhysicsDirectBodyState_get_inverse_mass>`  **(** **)** const                                                                            |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`                                  | :ref:`get_linear_velocity<class_PhysicsDirectBodyState_get_linear_velocity>`  **(** **)** const                                                                      |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PhysicsDirectSpaceState<class_physicsdirectspacestate>`  | :ref:`get_space_state<class_PhysicsDirectBodyState_get_space_state>`  **(** **)**                                                                                    |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                                      | :ref:`get_step<class_PhysicsDirectBodyState_get_step>`  **(** **)** const                                                                                            |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                                      | :ref:`get_total_angular_damp<class_PhysicsDirectBodyState_get_total_angular_damp>`  **(** **)** const                                                                |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`                                  | :ref:`get_total_gravity<class_PhysicsDirectBodyState_get_total_gravity>`  **(** **)** const                                                                          |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                                      | :ref:`get_total_linear_damp<class_PhysicsDirectBodyState_get_total_linear_damp>`  **(** **)** const                                                                  |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`                              | :ref:`get_transform<class_PhysicsDirectBodyState_get_transform>`  **(** **)** const                                                                                  |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                           | :ref:`integrate_forces<class_PhysicsDirectBodyState_integrate_forces>`  **(** **)**                                                                                  |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                        | :ref:`is_sleeping<class_PhysicsDirectBodyState_is_sleeping>`  **(** **)** const                                                                                      |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                           | :ref:`set_angular_velocity<class_PhysicsDirectBodyState_set_angular_velocity>`  **(** :ref:`Vector3<class_vector3>` velocity  **)**                                  |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                           | :ref:`set_linear_velocity<class_PhysicsDirectBodyState_set_linear_velocity>`  **(** :ref:`Vector3<class_vector3>` velocity  **)**                                    |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                           | :ref:`set_sleep_state<class_PhysicsDirectBodyState_set_sleep_state>`  **(** :ref:`bool<class_bool>` enabled  **)**                                                   |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                           | :ref:`set_transform<class_PhysicsDirectBodyState_set_transform>`  **(** :ref:`Transform<class_transform>` transform  **)**                                           |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Member Function Description
---------------------------

.. _class_PhysicsDirectBodyState_add_force:

- void  **add_force**  **(** :ref:`Vector3<class_vector3>` force, :ref:`Vector3<class_vector3>` pos  **)**

.. _class_PhysicsDirectBodyState_apply_impulse:

- void  **apply_impulse**  **(** :ref:`Vector3<class_vector3>` pos, :ref:`Vector3<class_vector3>` j  **)**

.. _class_PhysicsDirectBodyState_get_angular_velocity:

- :ref:`Vector3<class_vector3>`  **get_angular_velocity**  **(** **)** const

.. _class_PhysicsDirectBodyState_get_contact_collider:

- :ref:`RID<class_rid>`  **get_contact_collider**  **(** :ref:`int<class_int>` contact_idx  **)** const

.. _class_PhysicsDirectBodyState_get_contact_collider_id:

- :ref:`int<class_int>`  **get_contact_collider_id**  **(** :ref:`int<class_int>` contact_idx  **)** const

.. _class_PhysicsDirectBodyState_get_contact_collider_object:

- :ref:`Object<class_object>`  **get_contact_collider_object**  **(** :ref:`int<class_int>` contact_idx  **)** const

.. _class_PhysicsDirectBodyState_get_contact_collider_pos:

- :ref:`Vector3<class_vector3>`  **get_contact_collider_pos**  **(** :ref:`int<class_int>` contact_idx  **)** const

.. _class_PhysicsDirectBodyState_get_contact_collider_shape:

- :ref:`int<class_int>`  **get_contact_collider_shape**  **(** :ref:`int<class_int>` contact_idx  **)** const

.. _class_PhysicsDirectBodyState_get_contact_collider_velocity_at_pos:

- :ref:`Vector3<class_vector3>`  **get_contact_collider_velocity_at_pos**  **(** :ref:`int<class_int>` contact_idx  **)** const

.. _class_PhysicsDirectBodyState_get_contact_count:

- :ref:`int<class_int>`  **get_contact_count**  **(** **)** const

.. _class_PhysicsDirectBodyState_get_contact_local_normal:

- :ref:`Vector3<class_vector3>`  **get_contact_local_normal**  **(** :ref:`int<class_int>` contact_idx  **)** const

.. _class_PhysicsDirectBodyState_get_contact_local_pos:

- :ref:`Vector3<class_vector3>`  **get_contact_local_pos**  **(** :ref:`int<class_int>` contact_idx  **)** const

.. _class_PhysicsDirectBodyState_get_contact_local_shape:

- :ref:`int<class_int>`  **get_contact_local_shape**  **(** :ref:`int<class_int>` contact_idx  **)** const

.. _class_PhysicsDirectBodyState_get_inverse_inertia:

- :ref:`Vector3<class_vector3>`  **get_inverse_inertia**  **(** **)** const

.. _class_PhysicsDirectBodyState_get_inverse_mass:

- :ref:`float<class_float>`  **get_inverse_mass**  **(** **)** const

.. _class_PhysicsDirectBodyState_get_linear_velocity:

- :ref:`Vector3<class_vector3>`  **get_linear_velocity**  **(** **)** const

.. _class_PhysicsDirectBodyState_get_space_state:

- :ref:`PhysicsDirectSpaceState<class_physicsdirectspacestate>`  **get_space_state**  **(** **)**

.. _class_PhysicsDirectBodyState_get_step:

- :ref:`float<class_float>`  **get_step**  **(** **)** const

.. _class_PhysicsDirectBodyState_get_total_angular_damp:

- :ref:`float<class_float>`  **get_total_angular_damp**  **(** **)** const

.. _class_PhysicsDirectBodyState_get_total_gravity:

- :ref:`Vector3<class_vector3>`  **get_total_gravity**  **(** **)** const

.. _class_PhysicsDirectBodyState_get_total_linear_damp:

- :ref:`float<class_float>`  **get_total_linear_damp**  **(** **)** const

.. _class_PhysicsDirectBodyState_get_transform:

- :ref:`Transform<class_transform>`  **get_transform**  **(** **)** const

.. _class_PhysicsDirectBodyState_integrate_forces:

- void  **integrate_forces**  **(** **)**

.. _class_PhysicsDirectBodyState_is_sleeping:

- :ref:`bool<class_bool>`  **is_sleeping**  **(** **)** const

.. _class_PhysicsDirectBodyState_set_angular_velocity:

- void  **set_angular_velocity**  **(** :ref:`Vector3<class_vector3>` velocity  **)**

.. _class_PhysicsDirectBodyState_set_linear_velocity:

- void  **set_linear_velocity**  **(** :ref:`Vector3<class_vector3>` velocity  **)**

.. _class_PhysicsDirectBodyState_set_sleep_state:

- void  **set_sleep_state**  **(** :ref:`bool<class_bool>` enabled  **)**

.. _class_PhysicsDirectBodyState_set_transform:

- void  **set_transform**  **(** :ref:`Transform<class_transform>` transform  **)**


