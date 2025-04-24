```python
import numpy as np
from env_utils import execute, reset_to_default_pose
from perception_utils import parse_query_obj
from plan_utils import get_affordance_map, get_avoidance_map, get_velocity_map, get_rotation_map, get_gripper_map

```

### **1. 'Basic Relative Movement:**

**Definition:** Commands that move an object a specified distance in a direction relative to its current position or another object's position.

- **Examples:**
  ```python
  # Query: move ee forward for 10cm.
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map(f'a point 10cm in front of {movable.position}')
  execute(movable, affordance_map)
  ```
  ```python
  # Query: move the gripper behind the bowl, and slow down when near the bowl.
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map('a point 15cm behind the bowl')
  avoidance_map = get_avoidance_map('10cm near the bowl')
  velocity_map = get_velocity_map('slow down when near the bowl')
  execute(movable, affordance_map=affordance_map, avoidance_map=avoidance_map, velocity_map=velocity_map)
  ```
  ```python
  # Query: move to the left of the brown block.
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map('a point 10cm to the left of the brown block')
  execute(movable, affordance_map=affordance_map)
  ```
  ```python
  # Query: close drawer by 5cm.
  movable = parse_query_obj('drawer handle')
  affordance_map = get_affordance_map('a point 5cm into the drawer handle')
  execute(movable, affordance_map=affordance_map)
  ```
  ```python
  # Query: move to 5cm on top of the soda can, at 0.5x speed when within 20cm of the wooden mug, and keep at least 15cm away from the wooden mug.
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map('a point 5cm above the soda can')
  avoidance_map = get_avoidance_map('15cm from the wooden mug')
  velocity_map = get_velocity_map('0.5x speed when within 20cm of the wooden mug')
  execute(movable, affordance_map=affordance_map, avoidance_map=avoidance_map, velocity_map=velocity_map)
  ```
- **Reusable Template:**

  ```python
  movable = parse_query_obj('{movable}')
  affordance_map = get_affordance_map('point {distance} {direction} {reference}')
  execute(movable, affordance_map)
  ```

---

### **2. 'Constrained Movement:**

**Definition:** Movement commands that include constraints such as avoidance zones or speed adjustments relative to other objects.

- **Examples:**

  ```python
  # Query: move to the back side of the table while staying at least 5cm from the blue block.
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map('a point on the back side of the table')
  avoidance_map = get_avoidance_map('5cm from the blue block')
  execute(movable, affordance_map=affordance_map, avoidance_map=avoidance_map)
  ```

  ```python
  # Query: move to 10cm on top of the soup bowl, and 5cm to the left of the soup bowl, while away from the glass, at 0.75x speed.
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map('a point 10cm above and 5cm to the left of the soup bowl')
  avoidance_map = get_avoidance_map('10cm from the glass')
  velocity_map = get_velocity_map('0.75x speed')
  execute(movable, affordance_map=affordance_map, avoidance_map=avoidance_map, velocity_map=velocity_map)
  ```

  ```python
  # Query: wipe the red dot but avoid the blue block.
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map('the red dot')
  avoidance_map = get_avoidance_map('10cm from the blue block')
  execute(movable, affordance_map=affordance_map, avoidance_map=avoidance_map)
  ```

- **Reusable Template:**

  ```python
  movable = parse_query_obj('{movable}')
  affordance_map = get_affordance_map('{target_position}')
  avoidance_map = get_avoidance_map('{avoidance_condition}') if needed else None
  velocity_map = get_velocity_map('{speed_condition}') if needed else None
  execute(movable, affordance_map, avoidance_map, velocity_map)
  ```

---

### **3. 'Dynamic Adjustment Commands:**

**Definition:** Commands that modify movement properties (speed, rotation) based on specific conditions.

- **Examples:**
  ```python
  # Query: move the gripper behind the bowl, and slow down when near the bowl.
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map('a point 15cm behind the bowl')
  avoidance_map = get_avoidance_map('10cm near the bowl')
  velocity_map = get_velocity_map('slow down when near the bowl')
  execute(movable, affordance_map=affordance_map, avoidance_map=avoidance_map, velocity_map=velocity_map)
  ```
  ```python
  # Query: move to 5cm on top of the soda can, at 0.5x speed when within 20cm of the wooden mug, and keep at least 15cm away from the wooden mug.
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map('a point 5cm above the soda can')
  avoidance_map = get_avoidance_map('15cm from the wooden mug')
  velocity_map = get_velocity_map('0.5x speed when within 20cm of the wooden mug')
  execute(movable, affordance_map=affordance_map, avoidance_map=avoidance_map, velocity_map=velocity_map)
  ```
  ```python
  # Query: turn counter-clockwise by 180 degrees.
  movable = parse_query_obj('gripper')
  rotation_map = get_rotation_map('turn counter-clockwise by 180 degrees')
  execute(movable, rotation_map=rotation_map)
  ```
- **Reusable Template:**

  ```python
  movable = parse_query_obj('{movable}')
  affordance_map = get_affordance_map('{target_position}') if needed else None
  rotation_map = get_rotation_map('{rotation_condition}') if needed else None
  velocity_map = get_velocity_map('{speed_condition}') if needed else None
  execute(movable, affordance_map, rotation_map=rotation_map, velocity_map=velocity_map)
  ```

---

### **4. 'Object Interaction Commands:**

**Definition:** Gripper-based interactions (grasping, dropping) with state rules.

- **Examples:**

  ```python
  # Query: drop the toy inside container.
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map('a point 15cm above the container')
  gripper_map = get_gripper_map('close everywhere but open when on top of the container')
  execute(movable, affordance_map=affordance_map, gripper_map=gripper_map)
  ```

  ```python
  # Query: grasp the blue block from the table at a quarter of the speed.
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map('a point at the center of blue block')
  velocity_map = get_velocity_map('quarter of the speed')
  gripper_map = get_gripper_map('open everywhere except 1cm around the blue block')
  execute(movable, affordance_map=affordance_map, velocity_map=velocity_map, gripper_map=gripper_map)
  ```

  ```python
  # Query: grasp the mug from the shelf.
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map('a point at the center of the mug handle')
  gripper_map = get_gripper_map('open everywhere except 1cm around the mug handle')
  execute(movable, affordance_map=affordance_map, gripper_map=gripper_map)
  ```

- **Reusable Template:**

  ```python
  movable = parse_query_obj('{movable}')
  affordance_map = get_affordance_map('{target_position}')
  gripper_map = get_gripper_map('{gripper_state}')
  execute(movable, affordance_map, gripper_map=gripper_map)
  ```

---

### **5. 'System Reset Commands:**

**Definition:** Commands to return to a predefined default state.

- **Examples:**
  ```python
  # Query: go back to default.
  reset_to_default_pose()
  ```
  ```python
  # Query: open gripper.
  movable = parse_query_obj('gripper')
  gripper_map = get_gripper_map('open everywhere')
  execute(movable, gripper_map=gripper_map)
  ```
- **Reusable Template:**

  ```python
  reset_to_default_pose()  # For full system reset
  # OR
  movable = parse_query_obj('{movable}')
  gripper_map = get_gripper_map('{default_state}')
  execute(movable, gripper_map=gripper_map)
  ```

---

### **6. 'Path-Based Actions:**

**Definition:** Commands that involve movement along specified paths or trajectories.

- **Examples:**
  ```python
  # Query: push the second to the left block along the red line.
  movable = parse_query_obj('second to the left block')
  affordance_map = get_affordance_map('the red line')
  execute(movable, affordance_map=affordance_map)
  ```
  ```python
  # Query: sweep all particles to the left side of the table.
  particles = parse_query_obj('particles')
  for particle in particles:
      movable = particle
      affordance_map = get_affordance_map('a point on the left side of the table')
      execute(particle, affordance_map=affordance_map)
  ```
- **Reusable Template:**

  ```python
  movable = parse_query_obj('{movable}')
  affordance_map = get_affordance_map('{path_specification}')
  execute(movable, affordance_map)
  ```

---
