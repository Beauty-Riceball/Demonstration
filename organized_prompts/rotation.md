```python
import numpy as np
from plan_utils import get_empty_rotation_map, set_voxel_by_radius, cm2index, vec2quat
from perception_utils import parse_query_obj
from transforms3d.euler import euler2quat, quat2euler
from transforms3d.quaternions import qmult, qinverse
```

### **1. 'Surface Normal Alignment'**:

[Definition] The object (e.g., gripper) is oriented to align with the surface normal of a target object (e.g., bowl, table).

- **Examples**:

  ```python
  # Query: face the support surface of the bowl.
  rotation_map = get_empty_rotation_map()
  bowl = parse_query_obj('bowl')
  target_rotation = vec2quat(-bowl.normal)
  rotation_map[:, :, :] = target_rotation
  ret_val = rotation_map
  ```

  ```python
  # Query: face the table when within 30cm from table center.
  rotation_map = get_empty_rotation_map()
  table = parse_query_obj('table')
  table_center = table.position
  target_rotation = vec2quat(-table.normal)
  set_voxel_by_radius(rotation_map, table_center, radius_cm=30, value=target_rotation)
  ret_val = rotation_map
  ```

  ```python
  # Query: face the blue bowl.
  rotation_map = get_empty_rotation_map()
  blue_bowl = parse_query_obj('brown block')
  target_rotation = vec2quat(-blue_bowl.normal)
  rotation_map[:, :, :] = target_rotation
  ret_val = rotation_map
  ```

- **Template**:
  ```python
  rotation_map = get_empty_rotation_map()
  target_obj = parse_query_obj('{target_object}')
  target_rotation = vec2quat(-target_obj.normal)
  if {proximity_condition}:  # Optional spatial constraint
      set_voxel_by_radius(rotation_map, target_obj.position, radius_cm={distance}, value=target_rotation)
  else:
      rotation_map[:, :, :] = target_rotation
  ret_val = rotation_map
  ```

### **2. 'Relative Rotation'**:

[Definition] The object performs a relative rotation (clockwise/counter-clockwise) by a specified angle, optionally under a condition (e.g., at a location).

- **Examples**:
  ```python
  # Query: turn clockwise by 45 degrees when at the center of the beer cap.
  rotation_map = get_empty_rotation_map()
  beer_cap = parse_query_obj('beer cap')
  (x, y, z) = beer_cap.position
  curr_rotation = rotation_map[x, y, z]
  rotation_delta = euler2quat(0, 0, np.pi / 4)
  rotation_map[x, y, z] = qmult(curr_rotation, rotation_delta)
  ret_val = rotation_map
  ```
  ```python
  # Query: turn counter-clockwise by 30 degrees.
  rotation_map = get_empty_rotation_map()
  curr_rotation = rotation_map[0, 0, 0]
  rotation_delta = euler2quat(0, 0, -np.pi / 6)
  rotation_map[:, :, :] = qmult(curr_rotation, rotation_delta)
  ret_val = rotation_map
  ```
- **Reusable Template**:
  ```python
  rotation_map = get_empty_rotation_map()
  rotation_delta = euler2quat(0, 0, {angle_radians})  # +/- for direction
  if {position_condition}:
      (x, y, z) = parse_query_obj('{anchor_object}').position
      rotation_map[x, y, z] = qmult(rotation_map[x, y, z], rotation_delta)
  else:
      rotation_map[:, :, :] = qmult(rotation_map[0, 0, 0], rotation_delta)
  ret_val = rotation_map
  ```

### **3. 'Slanted Orientation'**:

[Definition] Orients an object at a fixed angular offset relative to a target's surface normal.

- **Example**:
  ```python
  # Query: rotate the gripper to be 45 degrees slanted relative to the plate.
  rotation_map = get_empty_rotation_map()
  plate = parse_query_obj('plate')
  face_plate_quat = vec2quat(-plate.normal)
  # rotate 45 degrees around the x-axis
  rotation_delta = euler2quat(-np.pi / 4, 0, 0)
  target_rotation = qmult(face_plate_quat, rotation_delta)
  rotation_map[:, :, :] = target_rotation
  ret_val = rotation_map
  ```
- **Reusable Template**:
  ```python
  rotation_map = get_empty_rotation_map()
  target_obj = parse_query_obj('{target_object}')
  base_rotation = vec2quat(-target_obj.normal)
  slant_radians = np.radians({slant_angle})
  slant_rotation = euler2quat(slant_radians, 0, 0)  # X-axis slant by default
  target_rotation = qmult(base_rotation, slant_rotation)
  rotation_map[:, :, :] = target_rotation
  ret_val = rotation_map
  ```

---
