```python
import numpy as np
from perception_utils import detect
```

### **1. 'Direct Retrieval'**:

**Definition**: The query directly matches an object in the list, and the object is retrieved without additional logic.

- **Examples**:
  ```python
  # Example 1: Retrieve the gripper
  objects = ['green block', 'cardboard box']
  gripper = detect('gripper')
  ret_val = gripper
  ```
  ```python
  # Example 2: Retrieve the table
  objects = ['vase', 'napkin box', 'mask']
  table = detect('table')
  ret_val = table
  ```
  ```python
  # Example 3: Retrieve the brown line
  objects = ['brown line', 'red block', 'monitor']
  brown_line = detect('brown line')
  ret_val = brown_line
  ```
- **Reusable Template**:
  ```python
  objects = ['{object1}', '{object2}']
  # Query: {query}.
  {var} = detect('{query}')
  ret_val = {var}
  ```

---

### **2. 'Conditional Selection'**:

**Definition**: The query involves selecting an object based on a condition (e.g., position, distance, or attribute).

- **Examples**:
  ```python
  # Example 1: Select the topmost handle (z-axis comparison)
  objects = ['handle1', 'handle2', 'egg1', 'egg2', 'plate']
  handle1 = detect('handle1')
  handle2 = detect('handle2')
  if handle1.position[2] > handle2.position[2]:
      top_handle = handle1
  else:
      top_handle = handle2
  ret_val = top_handle
  ```
  ```python
  # Example 2: Select the bowl closest to a sticker (distance-based)
  objects = ['mouse', 'yellow bowl', 'brown bowl', 'sticker']
  yellow_bowl = detect('yellow bowl')
  brown_bowl = detect('brown bowl')
  sticker = detect('sticker')
  if np.linalg.norm(yellow_bowl.position - sticker.position) < np.linalg.norm(brown_bowl.position - sticker.position):
      closest_bowl = yellow_bowl
  else:
      closest_bowl = brown_bowl
  ret_val = closest_bowl
  ```
  ```python
  # Example 3: Select the tray containing bread (proximity-based)
  objects = ['grape', 'wood tray', 'strawberry', 'white tray', 'blue tray', 'bread']
  wood_tray = detect('wood tray')
  white_tray = detect('white tray')
  bread = detect('bread')
  if np.linalg.norm(wood_tray.position - bread.position) < np.linalg.norm(white_tray.position - bread.position):
      tray_with_bread = wood_tray
  else:
      tray_with_bread = white_tray
  ret_val = tray_with_bread
  ```
- **Reusable Template**:
  ```python
  objects = ['{object1}', '{object2}']
  # Query: {query} based on {condition}.
  {obj1} = detect('{object1}')
  {obj2} = detect('{object2}')
  if {condition_logic}:
      ret_val = {obj1}
  else:
      ret_val = {obj2}
  ```

---

### **3. 'Attribute-Based Filtering'**:

**Definition**: The query filters objects by a specific attribute (e.g., fragility, color, type).

- **Examples**:
  ```python
  # Example 1: Filter for any block
  objects = ['green block', 'cup holder', 'black block']
  block = detect('green block')
  ret_val = block
  ```
  ```python
  # Example 2: Filter for fragile items (glass, vase)
  objects = ['glass', 'vase', 'plastic bottle', 'block', 'phone case']
  fragile_items = []
  for obj in ['glass', 'vase']:
      item = detect(obj)
      fragile_items.append(item)
  ret_val = fragile_items
  ```
- **Reusable Template**:
  ```python
  objects = ['{object1}', '{object2}']
  # Query: {attribute/property} {object_type}.
  {attribute_items} = []
  for obj in [{matching_objects}]:
      item = detect(obj)
      {filtered_items}.append(item)
  ret_val = {filtered_items}
  ```

---

### **4. 'No Match (Returns None)'**:

**Definition**: The query returns `None` if no matching object is found.

- **Example**:
  ```python
  # Example: No green block exists
  objects = ['blue block', 'red block']
  ret_val = None
  ```
- **Reusable Template**:
  ```python
  objects = ['{object1}', '{object2}']
  # Query: {nonexistent_object}.
  ret_val = None
  ```

---
