响应: Here’s the structured analysis of the provided context:

---

### **Template/Category 1: Single-Object Avoidance Zone**

**Definition**: Creating an avoidance zone around a single object with a specified radius.

- **Classified Context Parts**:

  - `10cm from the bowl` - Specifies a radius around a single object (bowl).
  - `20cm near the mug` - Specifies a radius around a single object (mug).
  - `10cm from the blue circle` - Specifies a radius around a single object (blue circle).

- **Reusable Template**:
  ```python
  avoidance_map = get_empty_avoidance_map()
  obj = parse_query_obj('[OBJECT_NAME]')
  set_voxel_by_radius(avoidance_map, obj.position, radius_cm=[RADIUS_CM], value=1)
  ret_val = avoidance_map
  ```

---

### **Template/Category 2: Multi-Object Avoidance Zone**

**Definition**: Creating avoidance zones around multiple objects, each with potentially different radii.

- **Classified Context Parts**:

  - `20cm around the mug and 10cm around the bowl` - Combines two avoidance zones with different radii.

- **Reusable Template**:
  ```python
  avoidance_map = get_empty_avoidance_map()
  obj1 = parse_query_obj('[OBJECT_NAME_1]')
  set_voxel_by_radius(avoidance_map, obj1.position, radius_cm=[RADIUS_1_CM], value=1)
  obj2 = parse_query_obj('[OBJECT_NAME_2]')
  set_voxel_by_radius(avoidance_map, obj2.position, radius_cm=[RADIUS_2_CM], value=1)
  ret_val = avoidance_map
  ```

---

### **Template/Category 3: Category-Based Avoidance Zone**

**Definition**: Creating avoidance zones around all objects belonging to a specific category (e.g., "fragile").

- **Classified Context Parts**:

  - `10cm from anything fragile` - Applies avoidance zones to all objects matching a category.

- **Reusable Template**:

  ```python
  avoidance_map = get_empty_avoidance_map()
  objects = parse_query_obj('[CATEGORY_DESCRIPTOR]')
  for obj in objects:
      set_voxel_by_radius(avoidance_map, obj.position, radius_cm=[RADIUS_CM], value=1)

  ret_val = avoidance_map
  ```

---

### **Suggested New Tasks**:

1. **Dynamic Radius Adjustment**:

   - _Example Query_: "Avoid the mug by 15cm if moving fast, otherwise 10cm."
   - _Logic_: Adjust avoidance radius based on robot speed or context.

2. **Exclusion Zones**:

   - _Example Query_: "Avoid everything except the table."
   - _Logic_: Apply avoidance to all objects except those explicitly excluded.

3. **Conditional Avoidance**:

   - _Example Query_: "Only avoid the vase if it’s tipped over."
   - _Logic_: Check object state before applying avoidance.

4. **Temporal Avoidance**:
   - _Example Query_: "Avoid the dog for the next 30 seconds."
   - _Logic_: Expire avoidance zones after a time threshold.

These suggestions extend functionality beyond the original context while maintaining relevance to spatial avoidance tasks.
