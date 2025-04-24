响应: Here’s the structured analysis of the provided context, categorized into distinct templates based on the key themes and patterns observed in the code snippets:

---

### **Template/Category 1: Relative Position Adjustment**

**Definition:** Adjusting a point's position relative to an object or coordinate by a specified distance along an axis (e.g., "10cm in front of").

**Classified Context Parts:**

1. `Query: a point 10cm in front of [10, 15, 60]`
   - Adjusts `x` by +10cm.
2. `Query: a point 20cm on top of the container`
   - Adjusts `z` by +20cm from the container’s `max_z`.
3. `Query: a point 1cm to the left of the brown block`
   - Adjusts `y` by -1cm from the block’s `min_y`.
4. `Query: a point 5cm above the blue block`
   - Adjusts `z` by +5cm from the block’s `max_z`.

**Reusable Template:**

```python
affordance_map = get_empty_affordance_map()
obj = parse_query_obj('[OBJECT_NAME]')
(min_x, min_y, min_z), (max_x, max_y, max_z) = obj.aabb
center_x, center_y, center_z = obj.position
# Adjust [AXIS] by [DISTANCE]cm
x = [center_x/min_x/max_x] ± cm2index([DISTANCE], '[AXIS]')
y = [center_y/min_y/max_y] ± cm2index([DISTANCE], '[AXIS]')
z = [center_z/min_z/max_z] ± cm2index([DISTANCE], '[AXIS]')
affordance_map[x, y, z] = 1
ret_val = affordance_map
```

---

### **Template/Category 2: Object Boundary Reference**

**Definition:** Referencing an object’s bounding box (AABB) or specific side/corner (e.g., "right side of the table").

**Classified Context Parts:**

1. `Query: a point on the right side of the table`
   - Uses `max_y` from the table’s AABB.
2. `Query: a point on the back side of the table`
   - Uses `min_x` from the table’s AABB.
3. `Query: a point on the front right corner of the table`
   - Combines `max_x` and `max_y` from the AABB.

**Reusable Template:**

```python
affordance_map = get_empty_affordance_map()
obj = parse_query_obj('[OBJECT_NAME]')
(min_x, min_y, min_z), (max_x, max_y, max_z) = obj.aabb
# Select a side/corner
x = [min_x/max_x/center_x]
y = [min_y/max_y/center_y]
z = [min_z/max_z/center_z]
affordance_map[x, y, z] = 1
ret_val = affordance_map
```

---

### **Template/Category 3: Directional Offset Using Normal Vector**

**Definition:** Adjusting position along an object’s normal vector (e.g., "30cm into the handle").

**Classified Context Parts:**

1. `Query: a point 30cm into the topmost drawer handle`
   - Uses `-normal` to move "into" the handle.
2. `Query: a point 20cm away from the leftmost block`
   - Uses `normal` to move "away" from the block.

**Reusable Template:**

```python
affordance_map = get_empty_affordance_map()
obj = parse_query_obj('[OBJECT_NAME]')
direction = [obj.normal / -obj.normal]  # Choose sign based on "into" or "away"
affordance_xyz = obj.position + cm2index([DISTANCE], direction)
affordance_map[affordance_xyz[0], affordance_xyz[1], affordance_xyz[2]] = 1
ret_val = affordance_map
```

---

### **Template/Category 4: Compound Adjustments**

**Definition:** Combining multiple positional adjustments (e.g., "10cm above and 5cm to the left").

**Classified Context Parts:**

1. `Query: a point 4cm to the left of and 10cm on top of the tray`
   - Adjusts `y` (-4cm) and `z` (+10cm).
2. `Query: a point 10cm to the right of [45 49 66], and 5cm above it`
   - Adjusts `y` (+10cm) and `z` (+5cm).
3. `Query: a point 10cm above and 5cm to the left of the yellow bowl`
   - Adjusts `y` (-5cm) and `z` (+10cm).

**Reusable Template:**

```python
affordance_map = get_empty_affordance_map()
obj = parse_query_obj('[OBJECT_NAME]')  # or use fixed coordinates
(min_x, min_y, min_z), (max_x, max_y, max_z) = obj.aabb
# Adjust multiple axes
x = [center_x/min_x/max_x] ± cm2index([DISTANCE_X], '[AXIS_X]')
y = [center_y/min_y/max_y] ± cm2index([DISTANCE_Y], '[AXIS_Y]')
z = [center_z/min_z/max_z] ± cm2index([DISTANCE_Z], '[AXIS_Z]')
affordance_map[x, y, z] = 1
ret_val = affordance_map
```

---

### **Template/Category 5: Direct Object Reference**

**Definition:** Referencing an object’s intrinsic properties (e.g., occupancy map or center point).

**Classified Context Parts:**

1. `Query: the blue circle`
   - Returns the object’s `occupancy_map`.
2. `Query: a point at the center of the blue circle`
   - Uses the object’s `position`.

**Reusable Template:**

```python
affordance_map = get_empty_affordance_map()
obj = parse_query_obj('[OBJECT_NAME]')
# Option 1: Use occupancy map
affordance_map = obj.occupancy_map
# Option 2: Use center position
x, y, z = obj.position
affordance_map[x, y, z] = 1
ret_val = affordance_map
```

---

### **Key Observations:**

- **Redundancy Eliminated:** All queries follow a pattern of (1) parsing an object/coordinate, (2) computing adjustments, and (3) updating `affordance_map`.
- **Flexibility:** Templates support fixed coordinates (`[10, 15, 60]`) or object references (`table`).
- **Extensibility:** New queries can reuse these templates by plugging in object names, axes, and distances.

Let me know if you'd like to refine any category or template further!
