响应: Here’s the structured analysis of the provided context, categorized by the type of rotational operation being performed:

---

### **Template/Category 1: Face the Normal of an Object**

**Definition**: Commands that involve aligning the gripper's orientation to face the normal vector of a specified object (e.g., bowl, table).

**Classified Context Parts**:

1. `face the support surface of the bowl` - Aligns the gripper to the bowl's normal.
2. `face the table when within 30cm from table center` - Aligns the gripper to the table's normal within a radius.
3. `face the blue bowl` - Aligns the gripper to the blue bowl's normal (though the object name is mismatched in the code).

**Reusable Template**:

```python
rotation_map = get_empty_rotation_map()
obj = parse_query_obj('[OBJECT_NAME]')
target_rotation = vec2quat(-obj.normal)
[SET_ROTATION_LOGIC]  # e.g., rotation_map[:, :, :] = target_rotation or radius-based assignment
ret_val = rotation_map
```

---

### **Template/Category 2: Apply Fixed Angular Offset**

**Definition**: Commands that apply a fixed rotation (clockwise/counter-clockwise) to the gripper's current orientation, either globally or at a specific location.

**Classified Context Parts**:

1. `turn clockwise by 45 degrees when at the center of the beer cap` - Applies a +45° Z-axis rotation at the beer cap's position.
2. `turn counter-clockwise by 30 degrees` - Applies a -30° Z-axis rotation globally.

**Reusable Template**:

```python
rotation_map = get_empty_rotation_map()
[OPTIONAL_POSITION_LOGIC]  # e.g., (x, y, z) = obj.position
curr_rotation = rotation_map[x, y, z]  # or rotation_map[0, 0, 0] for global
rotation_delta = euler2quat(0, 0, [ANGLE_RADIANS])  # Z-axis rotation
rotation_map[POSITION] = qmult(curr_rotation, rotation_delta)
ret_val = rotation_map
```

---

### **Template/Category 3: Slanted Relative Rotation**

**Definition**: Commands that rotate the gripper relative to an object's normal but with an additional slant (e.g., 45° around another axis).

**Classified Context Part**:

1. `rotate the gripper to be 45 degrees slanted relative to the plate` - Faces the plate's normal, then tilts 45° around the X-axis.

**Reusable Template**:

```python
rotation_map = get_empty_rotation_map()
obj = parse_query_obj('[OBJECT_NAME]')
face_quat = vec2quat(-obj.normal)
rotation_delta = euler2quat([X_RADIANS], [Y_RADIANS], [Z_RADIANS])  # Slant offset
target_rotation = qmult(face_quat, rotation_delta)
rotation_map[:, :, :] = target_rotation
ret_val = rotation_map
```

---

### **Key Observations**:

1. **Patterns**:
   - All cases start with `get_empty_rotation_map()` and end with `ret_val = rotation_map`.
   - Object normals are inverted (`-obj.normal`) to "face" the surface.
   - Quaternion math (`qmult`, `euler2quat`) handles rotations.
2. **Edge Cases**:
   - The `blue bowl` example references a `brown block` (likely a typo).
   - Global rotations default to `[0, 0, 0]` if no position is specified.

### **Future Use**:

The templates abstract the logic for handling:

- Object-relative alignment.
- Position-specific or global rotations.
- Multi-axis offsets (e.g., slanting).
  Adjust placeholders (`[OBJECT_NAME]`, `[ANGLE_RADIANS]`) as needed.
