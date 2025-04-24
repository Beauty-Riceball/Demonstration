```python
import numpy as np
from perception_utils import parse_query_obj
from plan_utils import get_empty_avoidance_map, set_voxel_by_radius, cm2index
```

### **Template/Category 1: Single Object Avoidance**

**Definition:** Creates an avoidance zone around a specifically named object with a defined radius.

- **Examples:**

  ```python
  # Example 1: 10cm avoidance around bowl
  avoidance_map = get_empty_avoidance_map()
  bowl = parse_query_obj('bowl')
  set_voxel_by_radius(avoidance_map, bowl.position, radius_cm=10, value=1)
  ret_val = avoidance_map
  ```

  ```python
  # Example 2: 20cm avoidance near mug
  avoidance_map = get_empty_avoidance_map()
  mug = parse_query_obj('mug')
  set_voxel_by_radius(avoidance_map, mug.position, radius_cm=20, value=1)
  ret_val = avoidance_map
  ```

- **Reusable Template:**

  ```python
  avoidance_map = get_empty_avoidance_map()
  {object} = parse_query_obj('{object}')
  set_voxel_by_radius(avoidance_map, {object}.position, radius_cm={distance}, value=1)
  ret_val = avoidance_map
  ```

### **Template/Category 2: Property-Based Avoidance**

**Definition:** Creates avoidance zones around all objects matching a descriptive property (e.g., fragile, red).

- **Example:**

  ```python
  # Example: 10cm avoidance around fragile objects
  avoidance_map = get_empty_avoidance_map()
  fragile_objects = parse_query_obj('anything fragile')
  for obj in fragile_objects:
      set_voxel_by_radius(avoidance_map, obj.position, radius_cm=10, value=1)
  ret_val = avoidance_map
  ```

- **Reusable Template:**

  ```python
  avoidance_map = get_empty_avoidance_map()
  {property}_objects = parse_query_obj('anything {property}')
  for obj in {property}_objects:
      set_voxel_by_radius(avoidance_map, obj.position, radius_cm={distance}, value=1)
  ret_val = avoidance_map
  ```

### **Template/Category 3: Multi-Object Avoidance**

**Definition:** Combines avoidance zones for multiple objects with potentially different radii.

- **Classified Context Parts:**

  ```python
  # Example: 20cm around mug AND 10cm around bowl
  avoidance_map = get_empty_avoidance_map()
  mug = parse_query_obj('mug')
  set_voxel_by_radius(avoidance_map, mug.position, radius_cm=20, value=1)
  bowl = parse_query_obj('bowl')
  set_voxel_by_radius(avoidance_map, bowl.position, radius_cm=10, value=1)
  ret_val = avoidance_map
  ```

- **Reusable Template:**

  ```python
  avoidance_map = get_empty_avoidance_map()
  # First object
  {object1} = parse_query_obj('{object1}')
  set_voxel_by_radius(avoidance_map, {object1}.position, radius_cm={distance1}, value=1)
  # Second object
  {object2} = parse_query_obj('{object2}')
  set_voxel_by_radius(avoidance_map, {object2}.position, radius_cm={distance2}, value=1)
  ret_val = avoidance_map
  ```
