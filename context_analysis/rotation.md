响应: Here’s the structured analysis of the provided code, categorized by the key themes and patterns observed:

---

### **Template/Category 1: Object-Facing Rotation**

**Definition**: Commands that involve rotating to face the normal vector of a specified object (e.g., bowl, table).

- **Classified Context Parts**:
  1. `face the support surface of the bowl` → Rotates to align with the bowl's normal vector.
  2. `face the table when within 30cm from table center` → Rotates to align with the table's normal vector within a radius.
  3. `face the blue bowl` → Rotates to align with the (mislabeled) "brown block" normal vector (likely a typo).
  4. `rotate the gripper to be 45 degrees slanted relative to the plate` → First aligns with the plate's normal, then adds a 45° slant.
  - **Reason**: All cases use `vec2quat(-obj.normal)` to derive a target rotation from the object's surface normal.

---

### **Template/Category 2: Relative Angle Adjustment**

**Definition**: Commands that apply a fixed angular offset (clockwise/counter-clockwise) to the current rotation.

- **Classified Context Parts**:
  1. `turn clockwise by 45 degrees when at the center of the beer cap` → Applies a +45° (π/4) Z-axis rotation at a specific voxel.
  2. `turn counter-clockwise by 30 degrees` → Applies a -30° (-π/6) Z-axis rotation globally.
  - **Reason**: Both use `euler2quat` to create a delta rotation (Z-axis) and `qmult` to combine it with the current rotation.

---

### **Template/Category 3: Spatial Conditionals**

**Definition**: Operations triggered only when certain spatial conditions (e.g., proximity) are met.

- **Classified Context Part**:
  `face the table when within 30cm from table center` → Uses `set_voxel_by_radius` to limit rotation updates to voxels near the table center.
  - **Reason**: Uniquely combines object-facing rotation with a spatial constraint (radius check).

---

### **Template/Category 4: Global vs. Local Rotation**

**Definition**: Distinguishes between rotations applied globally (all voxels) vs. locally (specific voxels).

- **Classified Context Parts**:
  1. **Global**:
     - `face the support surface of the bowl`, `face the blue bowl`, `turn counter-clockwise by 30 degrees`, `rotate the gripper...` → Use `rotation_map[:, :, :]` to apply rotation everywhere.
  2. **Local**:
     - `turn clockwise... at the center of the beer cap` → Targets only `rotation_map[x, y, z]`.
  - **Reason**: Highlights whether the rotation is spatially constrained or universally applied.

---

### **Template/Category 5: Quaternion Operations**

**Definition**: Shared utilities for quaternion math (rotation representation).

- **Classified Context Parts**:
  All code snippets use:
  - `vec2quat` (vector to quaternion),
  - `euler2quat` (Euler angles to quaternion),
  - `qmult` (quaternion multiplication),
  - `qinverse` (unused but imported).
  - **Reason**: Fundamental to all rotation calculations, regardless of context.

---

### **Template/Category 6: Potential Errors**

**Definition**: Likely typos or inconsistencies in the input.

- **Classified Context Part**:
  `parse_query_obj('brown block')` for the query `face the blue bowl` → Object name mismatch.
  - **Reason**: Suggests a bug or mislabeling in object parsing.

---

### **Summary of Insights**:

1. The code follows a **modular pattern**: Each query initializes a fresh `rotation_map` and defines rotations via object normals or Euler angles.
2. **Key Variations**:
   - Object-facing vs. fixed-angle rotations.
   - Global (entire map) vs. local (voxel-specific) application.
3. **Utility Functions**: `set_voxel_by_radius` and quaternion math enable spatial and rotational flexibility.
4. **Error Flag**: The "blue bowl" query parses a "brown block," indicating a possible issue.

This structure eliminates redundancy by grouping similar operations (e.g., all object-facing rotations) and highlights distinct logic (e.g., spatial conditionals).
