响应: Here’s the structured analysis of the provided context:

---

### **Template/Category 1: Object-Facing Rotation**

**Definition**: Commands that involve rotating to face the normal vector of a specific object (e.g., bowl, table).

- **Classified Context Parts**:

  - `face the support surface of the bowl` → Targets the bowl’s normal vector.
  - `face the table when within 30cm from table center` → Targets the table’s normal vector within a radius.
  - `face the blue bowl` → Targets the blue bowl’s normal vector (note: mislabeled as "brown block" in code).
  - `rotate the gripper to be 45 degrees slanted relative to the plate` → Targets the plate’s normal with an offset.

- **Reusable Template**:
  ```python
  rotation_map = get_empty_rotation_map()
  obj = parse_query_obj('[OBJECT_NAME]')
  target_rotation = vec2quat(-obj.normal)  # Optional: Add offset rotation
  rotation_map[:, :, :] = target_rotation  # Or use set_voxel_by_radius for spatial conditions
  ret_val = rotation_map
  ```

---

### **Template/Category 2: Fixed-Axis Rotation**

**Definition**: Commands that rotate by a fixed angle (clockwise/counter-clockwise) around the Z-axis (yaw).

- **Classified Context Parts**:

  - `turn clockwise by 45 degrees when at the center of the beer cap` → Applies a +45° Z-rotation at a specific location.
  - `turn counter-clockwise by 30 degrees` → Applies a -30° Z-rotation globally.

- **Reusable Template**:
  ```python
  rotation_map = get_empty_rotation_map()
  rotation_delta = euler2quat(0, 0, [ANGLE_IN_RADIANS])  # + for CW, - for CCW
  rotation_map[x, y, z] = qmult(curr_rotation, rotation_delta)  # Specific voxel or global
  ret_val = rotation_map
  ```

---

### **Template/Category 3: Offset Rotation Relative to Object**

**Definition**: Rotations that combine object-facing orientation with an additional offset (e.g., slanting).

- **Classified Context Part**:

  - `rotate the gripper to be 45 degrees slanted relative to the plate` → Faces the plate then offsets by 45° around X-axis.

- **Reusable Template**:
  ```python
  rotation_map = get_empty_rotation_map()
  obj = parse_query_obj('[OBJECT_NAME]')
  base_rotation = vec2quat(-obj.normal)
  offset_rotation = euler2quat([X_ANGLE], [Y_ANGLE], [Z_ANGLE])  # Custom offset
  target_rotation = qmult(base_rotation, offset_rotation)
  rotation_map[:, :, :] = target_rotation
  ret_val = rotation_map
  ```

---

### **Suggested New Tasks**:

1. **Proximity-Based Dynamic Rotation**:
   _"Face the cup when within 20cm of its handle, otherwise face the table."_
   (Combines spatial conditions with object-facing logic.)

2. **Sequential Rotations**:
   _"Turn 90 degrees clockwise, then slant 30 degrees upward relative to the box."_
   (Chains multiple rotations with offsets.)

3. **Object-Aligned Offset**:
   _"Rotate the gripper 60 degrees around the bowl’s normal vector."_
   (Uses the object’s local axis for rotation instead of global axes.)

---

**Key Improvements**:

- Eliminated redundancy by grouping all object-facing tasks under **Category 1**.
- Separated fixed-axis rotations (**Category 2**) from object-relative offsets (**Category 3**).
- Suggested tasks expand on spatial conditions, multi-step rotations, and local-axis manipulations.
