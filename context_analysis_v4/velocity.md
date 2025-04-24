响应: Here’s the structured analysis of the provided context, including categorized templates, reusable templates, and suggested new tasks:

---

### 1. **'a {object} {verb} {speed} when {position} the {reference_object}':**

_Definition: Adjusts speed based on positional relationship to a reference object._

- **Classified context part:**
  ```python
  # Query: faster when on the right side of the table and slower when on the left side of the table.
  velocity_map[:, center_y:, :] = 1.5  # Faster on right
  velocity_map[:, :center_y, :] = 0.5  # Slower on left
  ```
- **Reason:** Speed changes based on position relative to the table (right/left).
- **Reusable Template:**
  ```python
  velocity_map[:, {position_condition}, :] = {speed_value}  # Speed adjustment based on position
  ```

---

### 2. **'a {system} {verb} by {fraction} of the {baseline_speed}':**

_Definition: Uniformly scales speed by a fraction of the baseline._

- **Classified context part:**
  ```python
  # Query: slow down by a quarter.
  velocity_map[:] = 0.75
  ```
- **Reason:** Global speed reduction by a fixed fraction (0.75 = 1 - 0.25).
- **Reusable Template:**
  ```python
  velocity_map[:] = {baseline_speed} * (1 - {fraction})
  ```

---

### 3. **'a {object} {verb} {speed} within {distance} cm of {fragile_objects}':**

_Definition: Reduces speed near fragile objects within a radius._

- **Classified context part:**
  ```python
  # Query: slow down by a half when near fragile objects.
  set_voxel_by_radius(velocity_map, mug.position, radius_cm=10, value=0.5)
  set_voxel_by_radius(velocity_map, bowl.position, radius_cm=10, value=0.5)
  ```
- **Reason:** Speed halves within 10 cm of fragile objects (e.g., mug, bowl).
- **Reusable Template:**
  ```python
  for obj in {fragile_objects}:
      set_voxel_by_radius(velocity_map, obj.position, radius_cm={distance}, value={speed})
  ```

---

### 4. **'a {object} {verb} {speed} within {distance} cm of {reference_feature}':**

_Definition: Adjusts speed near a specific feature (e.g., line, boundary)._

- **Classified context part:**
  ```python
  # Query: quarter speed within 9cm of the yellow line.
  set_voxel_by_radius(velocity_map, yellow_line.position, radius_cm=9, value=0.25)
  ```
- **Reason:** Speed reduces to 0.25 within 9 cm of the yellow line.
- **Reusable Template:**
  ```python
  set_voxel_by_radius(velocity_map, {reference_feature}.position, radius_cm={distance}, value={speed})
  ```

---

### Suggested New Tasks:

1. **Directional Speed Gradient:**
   ```python
   # Query: speed increases linearly from left (0.5) to right (1.5) of the table.
   velocity_map[:, :, :] = np.linspace(0.5, 1.5, num=velocity_map.shape[1])
   ```
2. **Proximity to Moving Objects:**
   ```python
   # Query: slow down dynamically if a human hand is within 15 cm.
   hand = parse_query_obj('hand')
   if np.linalg.norm(hand.position - robot.position) < 15:
       velocity_map[:] = 0.3
   ```
3. **Time-Based Speed Adjustment:**
   ```python
   # Query: reduce speed by 10% every 5 seconds after task initiation.
   velocity_map[:] = max(0.1, 1.0 - (0.1 * (current_time // 5)))
   ```

---

### Key Observations:

- **Patterns:** Speed adjustments are triggered by **position**, **proximity**, or **uniform scaling**.
- **Flexibility:** Templates use placeholders like `{distance}`, `{fraction}`, and `{reference_feature}` for adaptability.
- **Expansion:** New tasks introduce dynamic (time/motion) and non-binary (gradient) behaviors.

Let me know if you'd like further refinements!
