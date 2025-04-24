响应: Here’s the structured analysis of the provided context, categorized by key themes and patterns:

---

### **Template/Category 1: Basic Movement Commands**

**Definition**: Commands that involve moving the end-effector (gripper) or an object to a specified location without additional constraints like speed, avoidance, or rotation.

- `move ee forward for 10cm` - Simple linear movement.
- `move to the left of the brown block` - Direct positional movement.
- `move to the top of the tray that contains the lemon` - Movement to a static target.
- `close drawer by 5cm` - Linear movement with a fixed displacement.

---

### **Template/Category 2: Constrained Movement**

**Definition**: Movement commands with additional constraints (e.g., avoidance zones, speed adjustments, or rotation requirements).

- `move the gripper behind the bowl, and slow down when near the bowl` - Combines affordance, avoidance, and velocity maps.
- `move to the back side of the table while staying at least 5cm from the blue block` - Avoidance constraint added.
- `move to the top of the plate and face the plate` - Includes rotation alignment.
- `move to 5cm on top of the soda can, at 0.5x speed when within 20cm of the wooden mug` - Speed and avoidance constraints.
- `wipe the red dot but avoid the blue block` - Target + avoidance.

---

### **Template/Category 3: Gripper Actions**

**Definition**: Commands involving gripper state changes (open/close) or grasping logic.

- `drop the toy inside container` - Gripper opens at a specific location.
- `grasp the blue block from the table at a quarter of the speed` - Combines grasp logic with speed.
- `grasp the mug from the shelf` - Precision grasping with gripper constraints.
- `open gripper` - State change without movement.

---

### **Template/Category 4: Compound Actions**

**Definition**: Multi-step or multi-parameter actions (e.g., combined movement, rotation, and gripper control).

- `grasp the bottom drawer handle while moving at 0.5x speed` - Includes affordance, velocity, rotation, and gripper maps.
- `move to 10cm on top of the soup bowl, and 5cm to the left ... while away from the glass` - Complex positional + avoidance + speed.

---

### **Template/Category 5: Reset/Default Actions**

**Definition**: Commands that reset the system to a predefined state.

- `go back to default` - Resets to a default pose.

---

### **Template/Category 6: Rotational Commands**

**Definition**: Commands that involve changing the orientation of the gripper or object.

- `turn counter-clockwise by 180 degrees` - Pure rotation.
- `face the plate` - Alignment with an object.

---

### **Template/Category 7: Batch/Iterative Actions**

**Definition**: Actions applied to multiple objects or particles iteratively.

- `sweep all particles to the left side of the table` - Loops over particles to execute the same affordance.

---

### **Template/Category 8: Object-Specific Manipulation**

**Definition**: Actions targeting specific objects (e.g., drawers, blocks) with contextual affordances.

- `push close the topmost drawer` - Targets a drawer handle.
- `push the second to the left block along the red line` - Directs an object along a path.

---

### **Key Observations**:

1. **Modularity**: The code uses utility functions (`get_affordance_map`, `get_avoidance_map`, etc.) to dynamically construct constraints.
2. **Patterns**:
   - Most commands follow `parse_query_obj → define maps → execute`.
   - Constraints (avoidance, velocity) are optional and additive.
3. **Redundancy**:
   - `movable = parse_query_obj('gripper')` repeats often; could be streamlined.
   - Template 2 (Constrained Movement) and Template 4 (Compound Actions) overlap but are separated by complexity.

This categorization helps in designing higher-level APIs or reusable components for similar robotic command systems.
