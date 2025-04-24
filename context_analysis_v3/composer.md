响应: Here’s the structured analysis of the provided context:

---

### **Template/Category 1: Basic Movement**

**Definition**: Commands that involve simple directional movement of the gripper or object without additional constraints like speed, rotation, or avoidance.

- **Classified context parts**:
  - `move ee forward for 10cm` - Only involves moving the gripper forward.
  - `move to the left of the brown block` - Direct movement to a relative position.
  - `move to the top of the tray that contains the lemon` - Movement to a specific point above an object.
- **Reusable Template**:
  ```python
  movable = parse_query_obj('[gripper/object]')
  affordance_map = get_affordance_map('a point [distance] [direction] of [reference object]')
  execute(movable, affordance_map)
  ```

---

### **Template/Category 2: Constrained Movement**

**Definition**: Movement commands with additional constraints like avoidance zones, speed adjustments, or rotation requirements.

- **Classified context parts**:
  - `move the gripper behind the bowl, and slow down when near the bowl` - Combines movement with speed and avoidance.
  - `move to the back side of the table while staying at least 5cm from the blue block` - Avoidance constraint.
  - `move to 5cm on top of the soda can, at 0.5x speed when within 20cm of the wooden mug` - Speed and avoidance constraints.
- **Reusable Template**:
  ```python
  movable = parse_query_obj('[gripper/object]')
  affordance_map = get_affordance_map('a point [position description]')
  avoidance_map = get_avoidance_map('[distance] from [object]')  # Optional
  velocity_map = get_velocity_map('[speed adjustment] when [condition]')  # Optional
  execute(movable, affordance_map, avoidance_map, velocity_map)
  ```

---

### **Template/Category 3: Gripper Actions**

**Definition**: Commands involving gripper-specific actions like opening/closing or grasping objects.

- **Classified context parts**:

  - `drop the toy inside container` - Involves gripper manipulation (opening/closing).

  - `grasp the blue block from the table at a quarter of the speed` - Combines grasping with speed.
  - `open gripper` - Pure gripper action.

- **Reusable Template**:
  ```python
  movable = parse_query_obj('gripper')
  affordance_map = get_affordance_map('[target position]')  # Optional
  gripper_map = get_gripper_map('[open/close] [condition]')
  execute(movable, affordance_map, gripper_map)  # Omit affordance_map if not needed
  ```

---

### **Template/Category 4: Rotation or Orientation**

**Definition**: Commands that require changing the orientation of the gripper or object.

- **Classified context parts**:
  - `move to the top of the plate and face the plate` - Includes rotation to face an object.
  - `turn counter-clockwise by 180 degrees` - Pure rotation command.
- **Reusable Template**:
  ```python
  movable = parse_query_obj('[gripper/object]')
  rotation_map = get_rotation_map('[action: face/turn] [target/degrees]')
  execute(movable, rotation_map)  # Can be combined with affordance_map
  ```

---

### **Template/Category 5: Compound or Multi-Step Actions**

**Definition**: Commands that combine multiple constraints (e.g., movement + rotation + gripper action) or involve iterative actions (e.g., sweeping particles).

- **Classified context parts**:
  - `sweep all particles to the left side of the table` - Iterative action on multiple objects.
  - `grasp the bottom drawer handle while moving at 0.5x speed` - Combines grasping, speed, and rotation.
- **Reusable Template**:

  ```python
  # For iterative actions:
  objects = parse_query_obj('[group of objects]')
  for obj in objects:
      affordance_map = get_affance_map('[target position]')
      execute(obj, affordance_map)

  # For compound actions:
  movable = parse_query_obj('[gripper/object]')
  affordance_map = get_affordance_map('[target position]')
  velocity_map = get_velocity_map('[speed adjustment]')  # Optional
  rotation_map = get_rotation_map('[orientation]')  # Optional
  gripper_map = get_gripper_map('[action]')  # Optional
  execute(movable, affordance_map, velocity_map, rotation_map, gripper_map)
  ```

---

### **Template/Category 6: Reset or Default Actions**

**Definition**: Commands that reset the system to a default state or pose.

- **Classified context parts**:
  - `go back to default` - Resets to a predefined pose.
- **Reusable Template**:
  ```python
  reset_to_default_pose()
  ```

---

### **Suggested New Tasks**:

1. **"Move the gripper in a circular path around the bowl while maintaining a 10cm distance."**

   - Expands on constrained movement with a non-linear path.
   - Requires `get_affordance_map` to define a circular trajectory.

2. **"Pour the contents of the mug into the bowl by tilting the gripper 45 degrees when above the bowl."**

   - Combines gripper action (tilting) with orientation and positioning.

3. **"Arrange all blocks in a straight line on the table, spaced 5cm apart."**

   - Iterative multi-object task with precise positioning.

4. **"Move the gripper to the center of the room while avoiding all objects and adjusting speed based on proximity to walls."**
   - Complex avoidance and velocity mapping with dynamic conditions.

---

This structured approach ensures clarity, reusability, and scalability for similar robotic command systems. Let me know if you'd like further refinements!
