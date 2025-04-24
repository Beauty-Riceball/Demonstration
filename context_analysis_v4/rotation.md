响应: Here is the structured analysis, classification, and template extraction for the provided context:

---

### **1. 'a {object} faces the {surface_normal} of the {target_object}'**:

[Definition] The object (e.g., gripper) is oriented to align with the surface normal of a target object (e.g., bowl, table).

- **Classified context part**:
  - `face the support surface of the bowl`
  - `face the table when within 30cm from table center`
  - `face the blue bowl`
- **Reason**: All involve aligning an object’s orientation with the surface normal of another object.
- **Reusable Template**:
  ```python
  rotation_map = get_empty_rotation_map()
  target_obj = parse_query_obj('{target_object}')
  target_rotation = vec2quat(-target_obj.normal)
  rotation_map[:, :, :] = target_rotation  # or set_voxel_by_radius for proximity
  ret_val = rotation_map
  ```

### **2. 'a {object} rotates {direction} by {angle} degrees {condition}'**:

[Definition] The object performs a relative rotation (clockwise/counter-clockwise) by a specified angle, optionally under a condition (e.g., at a location).

- **Classified context part**:
  - `turn clockwise by 45 degrees when at the center of the beer cap`
  - `turn counter-clockwise by 30 degrees`
- **Reason**: Both involve delta rotations (fixed or positional) applied to the current orientation.
- **Reusable Template**:
  ```python
  rotation_map = get_empty_rotation_map()
  rotation_delta = euler2quat(0, 0, {angle_radians})  # +/- for direction
  if {condition}:  # e.g., "at beer cap center"
      (x, y, z) = parse_query_obj('{object}').position
      rotation_map[x, y, z] = qmult(rotation_map[x, y, z], rotation_delta)
  else:
      rotation_map[:, :, :] = qmult(rotation_map[0, 0, 0], rotation_delta)
  ret_val = rotation_map
  ```

### **3. 'a {object} slants {angle} degrees relative to the {target_object}'**:

[Definition] The object is rotated at a fixed angular offset (e.g., slant) relative to a target object’s normal.

- **Classified context part**:
  - `rotate the gripper to be 45 degrees slanted relative to the plate`
- **Reason**: Involves a composite rotation combining alignment with an object and an additional offset.
- **Reusable Template**:
  ```python
  rotation_map = get_empty_rotation_map()
  target_obj = parse_query_obj('{target_object}')
  base_rotation = vec2quat(-target_obj.normal)
  rotation_delta = euler2quat({axis_angle}, 0, 0)  # e.g., x-axis slant
  target_rotation = qmult(base_rotation, rotation_delta)
  rotation_map[:, :, :] = target_rotation
  ret_val = rotation_map
  ```

---

### **Suggested New Tasks**:

1. **"Face the ceiling when holding the red cup"**:
   - Expands orientation rules to include environmental features (ceiling) with object-specific conditions.
2. **"Tilt 20 degrees away from the table edge if within 10cm"**:
   - Combines proximity-based conditions with angular offsets for collision avoidance.
3. **"Align parallel to the longest edge of the rectangular box"**:
   - Uses object geometry (edges) instead of surface normals for orientation.

---

### **Key Observations**:

- **Proximity vs. Global**: Some rules apply universally (`[:, :, :]`), while others use spatial triggers (`set_voxel_by_radius`).
- **Rotation Composition**: Most tasks use `qmult` to combine rotations (e.g., surface alignment + offset).
- **Error Handling**: The "blue bowl" query incorrectly parses a "brown block", suggesting a need for input validation.

The templates abstract the core logic (normal alignment, delta rotations, offsets) for reuse in similar robotics/3D manipulation tasks.
