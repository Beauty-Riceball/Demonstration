```python
import numpy as np
from perception_utils import parse_query_obj
from plan_utils import get_empty_gripper_map, set_voxel_by_radius, cm2index
```

### **1. 'Radius-Based Exclusion':**

**Definition:** Apply an action globally except within a specified radius around an object.

- **Example:**

  ```python
  # Query: open everywhere except 1cm around the green block.
  gripper_map = get_empty_gripper_map()
  # open everywhere
  gripper_map[:, :, :] = 1
  # close when 1cm around the green block
  green_block = parse_query_obj('green block')
  set_voxel_by_radius(gripper_map, green_block.position, radius_cm=1, value=0)
  ret_val = gripper_map
  ```

- **Reusable Template:**
  ```python
  gripper_map = get_empty_gripper_map()
  gripper_map[:, :, :] = {default_action}  # {action} everywhere
  set_voxel_by_radius(gripper_map, {object}.position, radius_cm={distance}, value={exception_action})  # {opposite_action} around {object}
  ```

---

### **2. 'Position-Specific Exception':**

**Definition:** Apply an action globally but reverse it at a specific position relative to an object (e.g., corner, edge).

- **Example:**

  ```python
  # Query: close everywhere but open when on top of the back left corner of the table.
  gripper_map = get_empty_gripper_map()
  # close everywhere
  gripper_map[:, :, :] = 0
  # open when on top of the back left corner of the table
  table = parse_query_obj('table')
  (min_x, min_y, min_z), (max_x, max_y, max_z) = table.aabb
  center_x, center_y, center_z = table.position
  # back so x = min_x, left so y = min_y, top so we add to z
  x = min_x
  y = min_y
  z = max_z + cm2index(15, 'z')
  set_voxel_by_radius(gripper_map, (x, y, z), radius_cm=10, value=1)
  ret_val = gripper_map
  ```

- **Reusable Template:**
  ```python
  gripper_map = get_empty_gripper_map()
  gripper_map[:, :, :] = {default_action}  # {action} everywhere
  {position_logic}  # e.g., (x, y, z) = (min_x, min_y, max_z + offset)
  set_voxel_by_radius(gripper_map, (x, y, z), radius_cm={radius}, value={exception_action})  # {opposite_action} at {position}
  ```

---

### **3. 'Directional Exclusion':**

**Definition:** Apply an action globally but reverse it on a specific side/direction of an object.

- **Example:**

  ```python
  # Query: always open except when you are on the right side of the table.
  gripper_map = get_empty_gripper_map()
  # always open
  gripper_map[:, :, :] = 1
  # close when you are on the right side of the table
  table = parse_query_obj('table')
  center_x, center_y, center_z = table.position
  # right side so y is greater than center_y
  gripper_map[:, center_y:, :] = 0
  ```

- **Reusable Template:**
  ```python
  gripper_map = get_empty_gripper_map()
  gripper_map[:, :, :] = {default_action}  # {action} everywhere
  gripper_map[{direction_slice}] = {exception_action}  # {opposite_action} on {direction} side
  # Common direction slices:
  # - Right: [:, center_y:, :]
  # - Left: [:, :center_y, :]
  # - Back: [:center_x, :, :]
  # - Front: [center_x:, :, :]
  ```

---

### **4. 'Direction-Specific Activation':**

**Definition:** Apply an action globally but reverse it only on a specific side (variant of Directional Exclusion).

- **Example:**

  ```python
  # Query: always close except when you are on the back side of the table.
  gripper_map = get_empty_gripper_map()
  # always close
  gripper_map[:, :, :] = 0
  # open when you are on the back side of the table
  table = parse_query_obj('table')
  center_x, center_y, center_z = table.position
  # back side so x is less than center_x
  gripper_map[:center_x, :, :] = 1
  ret_val = gripper_map
  ```

- **Reusable Template:**
  ```python
  gripper_map = get_empty_gripper_map()
  gripper_map[:, :, :] = {default_action}  # {action} everywhere
  gripper_map[{direction_slice}] = {exception_action}  # {opposite_action} on {direction} side
  ```

---
