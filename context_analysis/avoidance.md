响应: Here’s the structured analysis of the provided context:

---

### **Template/Category 1: Object Initialization**

**Definition:** Code blocks that initialize or reset the `avoidance_map` and parse the queried object(s).

- `avoidance_map = get_empty_avoidance_map()`
  - Resets the map for a new query. Repeated in all examples.
- `bowl = parse_query_obj('bowl')` / `mug = parse_query_obj('mug')` / etc.
  - Parses the target object(s) from the query (e.g., bowl, mug, fragile objects).

---

### **Template/Category 2: Spatial Constraint Application**

**Definition:** Code that applies spatial constraints (radius-based avoidance zones) around objects.

- `set_voxel_by_radius(avoidance_map, bowl.position, radius_cm=10, value=1)`
  - Marks a 10cm avoidance radius around the bowl.
- `set_voxel_by_radius(avoidance_map, mug.position, radius_cm=20, value=1)`
  - Marks a 20cm avoidance radius around the mug.
- Loop for fragile objects:
  ```python
  for obj in fragile_objects:
      set_voxel_by_radius(avoidance_map, obj.position, radius_cm=10, value=1)
  ```
  - Applies a 10cm radius to each fragile object iteratively.

---

### **Template/Category 3: Query-Specific Logic**

**Definition:** Unique logic or combinations of constraints for complex queries.

- Combined query (mug + bowl):
  ```python
  set_voxel_by_radius(avoidance_map, mug.position, radius_cm=20, value=1)
  set_voxel_by_radius(avoidance_map, bowl.position, radius_cm=10, value=1)
  ```
  - Applies multiple radii to different objects in the same map.
- Fragile objects query:
  - Uses iteration to handle dynamic object lists (`parse_query_obj('anything fragile')` likely returns multiple objects).

---

### **Template/Category 4: Output Handling**

**Definition:** Final assignment of the result for the query.

- `ret_val = avoidance_map`
  - Returns the populated avoidance map after processing. Consistent across all examples.

---

### **Key Observations:**

1. **Pattern Repetition:**
   - All queries follow the same workflow:
     Initialize map → Parse object(s) → Apply radius → Return map.
2. **Flexibility:**
   - Handles single objects (`bowl`, `mug`), groups (`fragile_objects`), and combined constraints.
3. **Extensibility:**
   - Adding new queries would reuse these templates (e.g., new objects/radii).

Let me know if you'd like further refinement or additional categories!
