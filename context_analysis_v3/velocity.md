响应: Here’s the structured analysis of the provided context, which involves velocity map adjustments based on spatial conditions and object properties:

---

### **Template/Category 1: Spatial Velocity Adjustment (Relative to Object Position)**

- **Definition**: Adjust velocity based on the robot's position relative to a reference object (e.g., left/right, above/below).
  - _Classified context part_:
    ```python
    # Query: faster when on the right side of the table and slower when on the left side of the table.
    velocity_map[:, center_y:, :] = 1.5  # Right side = faster
    velocity_map[:, :center_y, :] = 0.5  # Left side = slower
    ```
    - **Reason**: Velocity is modified based on the robot's y-coordinate relative to the table's center.
  - **Reusable Template**:
    ```python
    velocity_map[:, {condition_for_region}] = {speed_value}  # Adjust speed based on spatial region relative to {reference_object}.
    ```

---

### **Template/Category 2: Global Speed Scaling**

- **Definition**: Apply a uniform velocity multiplier across the entire map.
  - _Classified context part_:
    ```python
    # Query: slow down by a quarter.
    velocity_map[:] = 0.75  # Global reduction to 75% speed
    ```
    - **Reason**: Speed is scaled uniformly without spatial or object dependencies.
  - **Reusable Template**:
    ```python
    velocity_map[:] = {scaling_factor}  # Apply global speed scaling.
    ```

---

### **Template/Category 3: Proximity-Based Speed Reduction (Fragile Objects)**

- **Definition**: Reduce speed near specific objects (e.g., fragile items) within a defined radius.
  - _Classified context part_:
    ```python
    # Query: slow down by a half when near fragile objects.
    set_voxel_by_radius(velocity_map, mug.position, radius_cm=10, value=0.5)
    set_voxel_by_radius(velocity_map, bowl.position, radius_cm=10, value=0.5)
    ```
    - **Reason**: Speed is reduced near objects tagged as "fragile" using a radial proximity check.
  - **Reusable Template**:
    ```python
    set_voxel_by_radius(velocity_map, {object}.position, radius_cm={distance}, value={reduced_speed})  # Slow down near {object_type}.
    ```

---

### **Template/Category 4: Boundary-Aware Speed Adjustment**

- **Definition**: Modify speed based on proximity to a boundary or line (e.g., a marked safety line).

  - _Classified context part_:

    ```python
    # Query: quarter speed within 9cm of the yellow line.
    set_voxel_by_radius(velocity_map, yellow_line.position, radius_cm=9, value=0.25)
    ```

    - **Reason**: Speed is reduced near a boundary (yellow line) within a fixed radius.

  - **Reusable Template**:
    ```python
    set_voxel_by_radius(velocity_map, {boundary_object}.position, radius_cm={distance}, value={reduced_speed})  # Adjust speed near {boundary_description}.
    ```

---

### **Suggested New Tasks**

1. **Task**: _"Slow down to 20% speed when within 5cm of any object labeled ‘hot’ (e.g., stove, coffee cup)."_

   - **Alignment**: Expands on proximity-based speed reduction but introduces a new object property (temperature hazard).
   - **Implementation**:
     ```python
     hot_objects = parse_query_obj('hot')  # Hypothetical label-based query
     for obj in hot_objects:
         set_voxel_by_radius(velocity_map, obj.position, radius_cm=5, value=0.2)
     ```

2. **Task**: _"Double speed in open areas (no objects within 30cm)."_
   - **Alignment**: Introduces speed boosts based on absence of nearby objects, contrasting existing proximity-based reductions.

---

This breakdown ensures modular reuse of velocity-adjustment logic while suggesting creative extensions (e.g., temperature hazards or open-space boosts) not present in the original context.
