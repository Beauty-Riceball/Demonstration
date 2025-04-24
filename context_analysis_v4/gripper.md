响应: Here is the structured analysis of the provided context, including identified templates, classifications, reusable templates, and suggested new tasks:

---

### **1. 'a {gripper_map} {action} everywhere except {distance} cm around the {object}':**

**Definition:** A template for defining gripper behavior where an action (open/close) is applied globally except within a specified radius around an object.

- **Classified context part:**

  ```python
  # Query: open everywhere except 1cm around the green block.
  gripper_map[:, :, :] = 1  # open everywhere
  set_voxel_by_radius(gripper_map, green_block.position, radius_cm=1, value=0)  # close around green block
  ```

  **Reason:** The gripper is set to open everywhere except within 1cm of the green block, matching the template.

- **Reusable Template:**
  ```python
  gripper_map = get_empty_gripper_map()
  gripper_map[:, :, :] = {default_action}  # {action} everywhere
  set_voxel_by_radius(gripper_map, {object}.position, radius_cm={distance}, value={exception_action})  # {opposite_action} around {object}
  ```

---

### **2. 'a {gripper_map} {action} everywhere but {action} when {position} the {object}':**

**Definition:** A template for defining gripper behavior where an action is applied globally but reversed at a specific position relative to an object (e.g., corner, side).

- **Classified context part:**

  ```python
  # Query: close everywhere but open when on top of the back left corner of the table.
  gripper_map[:, :, :] = 0  # close everywhere
  x, y, z = min_x, min_y, max_z + cm2index(15, 'z')  # back left corner + offset
  set_voxel_by_radius(gripper_map, (x, y, z), radius_cm=10, value=1)  # open at position
  ```

  **Reason:** The gripper is closed globally but opened at a specific position (back left corner of the table).

- **Reusable Template:**
  ```python
  gripper_map = get_empty_gripper_map()
  gripper_map[:, :, :] = {default_action}  # {action} everywhere
  {position_logic}  # e.g., (x, y, z) = (min_x, min_y, max_z + offset)
  set_voxel_by_radius(gripper_map, (x, y, z), radius_cm={radius}, value={exception_action})  # {opposite_action} at {position}
  ```

---

### **3. 'a {gripper_map} {action} everywhere except when {direction} the {object}':**

**Definition:** A template for defining gripper behavior where an action is applied globally but reversed on a specific side/direction of an object.

- **Classified context part:**

  ```python
  # Query: always open except when you are on the right side of the table.
  gripper_map[:, :, :] = 1  # open everywhere
  gripper_map[:, center_y:, :] = 0  # close on right side (y >= center_y)
  ```

  **Reason:** The gripper is open globally but closed on the right side of the table.

- **Reusable Template:**
  ```python
  gripper_map = get_empty_gripper_map()
  gripper_map[:, :, :] = {default_action}  # {action} everywhere
  gripper_map[{direction_slice}] = {exception_action}  # {opposite_action} on {direction} side
  ```

---

### **4. 'a {gripper_map} {action} everywhere but {action} when {direction} the {object}':**

**Definition:** A template for defining gripper behavior where an action is applied globally but reversed on a specific side/direction of an object (variant of Template 3).

- **Classified context part:**

  ```python
  # Query: always close except when you are on the back side of the table.
  gripper_map[:, :, :] = 0  # close everywhere
  gripper_map[:center_x, :, :] = 1  # open on back side (x < center_x)
  ```

  **Reason:** The gripper is closed globally but opened on the back side of the table.

- **Reusable Template:**
  ```python
  gripper_map = get_empty_gripper_map()
  gripper_map[:, :, :] = {default_action}  # {action} everywhere
  gripper_map[{direction_slice}] = {exception_action}  # {opposite_action} on {direction} side
  ```

---

### **Suggested New Task:**

**Task:** "Always open except when within 5cm of any red object or on the front side of the table."
**Implementation:**

```python
gripper_map = get_empty_gripper_map()
gripper_map[:, :, :] = 1  # open everywhere
red_objects = [obj for obj in scene_objects if obj.color == 'red']
for obj in red_objects:
    set_voxel_by_radius(gripper_map, obj.position, radius_cm=5, value=0)  # close near red objects
table = parse_query_obj('table')
center_x, center_y, center_z = table.position
gripper_map[center_x:, :, :] = 0  # close on front side (x >= center_x)
```

**Rationale:** Expands the theme by combining proximity-based and directional exceptions, introducing multi-condition logic.

---

### **Summary of Reusable Templates:**

1. **Global action with proximity exception:**
   ```python
   set_voxel_by_radius(gripper_map, {object}.position, radius_cm={distance}, value={exception_action})
   ```
2. **Global action with positional exception:**
   ```python
   set_voxel_by_radius(gripper_map, (x, y, z), radius_cm={radius}, value={exception_action})
   ```
3. **Global action with directional exception:**
   ```python
   gripper_map[{direction_slice}] = {exception_action}
   ```

These templates cover all cases in the context while enabling expansion to new scenarios (e.g., multi-object or compound conditions).
