响应: Here’s the structured analysis of the provided context:

---

### **Template/Category 1: Directional Velocity Adjustment**

**Definition**: Adjusting velocity based on spatial direction or position relative to an object (e.g., left/right, above/below).

**Classified Context Part**:

```python
# Query: faster when on the right side of the table and slower when on the left side of the table.
velocity_map = get_empty_velocity_map()
table = parse_query_obj('table')
center_x, center_y, center_z = table.position
velocity_map[:, center_y:, :] = 1.5  # Faster on right (y > center_y)
velocity_map[:, :center_y, :] = 0.5  # Slower on left (y < center_y)
```

**Reason**: The velocity is modified based on the robot's position relative to the table's y-axis (left/right).

**Reusable Template**:

```python
velocity_map = get_empty_velocity_map()
obj = parse_query_obj('[OBJECT_NAME]')
center_x, center_y, center_z = obj.position
velocity_map[:, [DIRECTIONAL_CONDITION], :] = [VELOCITY_VALUE]  # Example: y > center_y for "right"
```

---

### **Template/Category 2: Global Velocity Scaling**

**Definition**: Applying a uniform velocity adjustment across the entire workspace.

**Classified Context Part**:

```python
# Query: slow down by a quarter.
velocity_map = get_empty_velocity_map()
velocity_map[:] = 0.75  # 25% reduction (1 - 0.25 = 0.75)
```

**Reason**: The velocity is scaled globally without spatial conditions.

**Reusable Template**:

```python
velocity_map = get_empty_velocity_map()
velocity_map[:] = [GLOBAL_VELOCITY_VALUE]  # e.g., 0.5 for "slow down by half"
```

---

### **Template/Category 3: Proximity-Based Velocity Adjustment**

**Definition**: Modifying velocity based on proximity to specific objects or regions (e.g., fragile items, boundaries).

**Classified Context Parts**:

1. Fragile objects slowdown:

   ```python
   # Query: slow down by a half when near fragile objects.
   velocity_map = get_empty_velocity_map()
   mug = parse_query_obj('mug')
   set_voxel_by_radius(velocity_map, mug.position, radius_cm=10, value=0.5)
   ```

   **Reason**: Velocity is reduced within a radius of fragile objects (`mug`, `bowl`).

2. Yellow line proximity:
   ```python
   # Query: quarter speed within 9cm of the yellow line.
   velocity_map = get_empty_velocity_map()
   yellow_line = parse_query_obj('yellow_line')
   set_voxel_by_radius(velocity_map, yellow_line.position, radius_cm=9, value=0.25)
   ```
   **Reason**: Velocity adjusts based on distance to a boundary (yellow line).

**Reusable Template**:

```python
velocity_map = get_empty_velocity_map()
obj = parse_query_obj('[OBJECT_NAME]')
set_voxel_by_radius(velocity_map, obj.position, radius_cm=[RADIUS_CM], value=[VELOCITY_VALUE])
```

---

### **Key Observations**:

1. **Redundancy**: All cases use `get_empty_velocity_map()` and `ret_val = velocity_map`. These can be abstracted into a higher-level function.
2. **Patterns**:
   - **Directional**: Split space along an axis (e.g., `y > center_y`).
   - **Global**: Apply a single value to all voxels.
   - **Proximity**: Use `set_voxel_by_radius` for object-centric adjustments.

**Suggested Improvement**:
Create a wrapper function to handle repetitive setup/return steps:

```python
def apply_velocity_rule(rule_func, *args):
    velocity_map = get_empty_velocity_map()
    rule_func(velocity_map, *args)  # Custom logic per rule
    return velocity_map
```

Let me know if you'd like further refinements!
