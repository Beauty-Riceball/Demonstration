响应: Here is the structured analysis of the provided context:

---

### **Template/Category 1: Relative Position from a Reference Point**

**Definition:** Specifying a point relative to a given reference point (e.g., coordinates or object position) with directional and distance constraints.

- **Classified Context Parts:**
  - `"a point 10cm in front of [10, 15, 60]"` – Adjusts the x-axis based on a fixed reference.
  - `"a point 10cm to the right of [45, 49, 66], and 5cm above it"` – Modifies y and z axes from a fixed reference.
  - `"a point 1cm to the left of the brown block"` – Uses object AABB to adjust the y-axis.
  - `"a point 5cm above the blue block"` – Uses object AABB to adjust the z-axis.

**Reusable Template:**

```python
affordance_map = get_empty_affordance_map()
reference = parse_query_obj('[OBJECT]') or [COORDINATES]
x = reference.x ± cm2index(DISTANCE, 'x')
y = reference.y ± cm2index(DISTANCE, 'y')
z = reference.z ± cm2index(DISTANCE, 'z')
affordance_map[x, y, z] = 1
```

---

### **Template/Category 2: Object Boundary-Based Positioning**

**Definition:** Places a point at a specific boundary (e.g., side, corner) of an object using its AABB (Axis-Aligned Bounding Box).

- **Classified Context Parts:**
  - `"a point on the right side of the table"` – Uses `max_y` from the table’s AABB.
  - `"a point on the back side of the table"` – Uses `min_x` from the table’s AABB.
  - `"a point on the front right corner of the table"` – Combines `max_x` and `max_y`.

**Reusable Template:**

```python
affordance_map = get_empty_affordance_map()
obj = parse_query_obj('[OBJECT]')
(min_x, min_y, min_z), (max_x, max_y, max_z) = obj.aabb
x = min_x | max_x | obj.position[0]  # Choose based on direction
y = min_y | max_y | obj.position[1]  # e.g., "left" → min_y
z = min_z | max_z | obj.position[2]
affordance_map[x, y, z] = 1
```

---

### **Template/Category 3: Directional Offset from Object Normal**

**Definition:** Uses an object’s surface normal vector to compute offsets (e.g., "into" or "away from" the object).

- **Classified Context Parts:**
  - `"a point 30cm into the topmost drawer handle"` – Uses `-normal` for inward direction.
  - `"a point 20cm away from the leftmost block"` – Uses `normal` for outward direction.

**Reusable Template:**

```python
affordance_map = get_empty_affordance_map()
obj = parse_query_obj('[OBJECT]')
direction = obj.normal * (-1 if "into" else 1)
affordance_xyz = obj.position + cm2index(DISTANCE, direction)
affordance_map[affordance_xyz[0], affordance_xyz[1], affordance_xyz[2]] = 1
```

---

### **Template/Category 4: Compound Relative Positioning**

**Definition:** Combines multiple directional offsets (e.g., "left and above") from an object’s position or AABB.

- **Classified Context Parts:**

  - `"a point 4cm to the left of and 10cm on top of the tray"` – Adjusts y and z axes.

  - `"a point 10cm above and 5cm to the left of the yellow bowl"` – Similar multi-axis adjustment.

**Reusable Template:**

```python
affordance_map = get_empty_affordance_map()
obj = parse_query_obj('[OBJECT]')
(min_x, min_y, min_z), (max_x, max_y, max_z) = obj.aabb
x = obj.position[0]
y = min_y - cm2index(LEFT_DISTANCE, 'y')
z = max_z + cm2index(TOP_DISTANCE, 'z')
affordance_map[x, y, z] = 1
```

---

### **Template/Category 5: Radius-Based Occupancy**

**Definition:** Marks all points within a specified radius of a reference point or object.

- **Classified Context Part:**
  - `"anywhere within 20cm of the right most block"` – Uses `set_voxel_by_radius`.

**Reusable Template:**

```python
affordance_map = get_empty_affordance_map()
obj = parse_query_obj('[OBJECT]')
set_voxel_by_radius(affordance_map, obj.position, radius_cm=DISTANCE, value=1)
```

---

### **Template/Category 6: Direct Object Reference**

**Definition:** Uses the object’s inherent properties (e.g., occupancy map or center) without offsets.

- **Classified Context Parts:**
  - `"the blue circle"` – Returns the object’s `occupancy_map`.
  - `"a point at the center of the blue circle"` – Uses the object’s `position`.

**Reusable Template:**

```python
affordance_map = parse_query_obj('[OBJECT]').occupancy_map  # For full object
# OR
x, y, z = parse_query_obj('[OBJECT]').position  # For center point
affordance_map[x, y, z] = 1
```

---

### **Suggested New Tasks:**

1. **"A point 15cm below and 3cm behind the red box"** – Combines z-axis (below) and x-axis (behind) offsets.
2. **"All points along the edge of the table"** – Iterates over AABB boundaries to mark edges.
3. **"A point at the intersection of the line extending from the green block’s normal and the wall"** – Uses raycasting for dynamic collisions.

---

This framework ensures extensibility for new queries while minimizing redundancy. Each template can be adapted for future use cases.
