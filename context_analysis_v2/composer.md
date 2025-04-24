响应: Here’s the structured analysis of the provided context, categorized into distinct templates with reusable frameworks:

---

### **Template/Category 1: Basic Movement with Affordance**

**Definition**: Commands that involve moving an object (e.g., gripper, drawer handle) to a specific location or along a path, using only an affordance map.
**Examples**:

1. `move ee forward for 10cm` → Uses `affordance_map` to define the target position.
2. `move to the left of the brown block` → Direct movement with a positional affordance.
3. `push the second to the left block along the red line` → Path-based affordance.

**Reusable Template**:

```python
movable = parse_query_obj('[OBJECT]')
affordance_map = get_affordance_map('[TARGET_POSITION/PATH_DESCRIPTION]')
execute(movable, affordance_map=affordance_map)
```

**Use Case**: Simple navigation or object manipulation tasks.

---

### **Template/Category 2: Constrained Movement (Avoidance + Velocity)**

**Definition**: Commands that include movement with additional constraints (e.g., avoiding obstacles, speed adjustments).
**Examples**:

1. `move the gripper behind the bowl, and slow down when near the bowl` → Combines `affordance_map`, `avoidance_map`, and `velocity_map`.
2. `move to 5cm on top of the soda can... keep 15cm away from the wooden mug` → Avoidance and velocity conditions.
3. `move to the back side of the table while staying 5cm from the blue block` → Avoidance constraint.

**Reusable Template**:

```python
movable = parse_query_obj('[OBJECT]')
affordance_map = get_affordance_map('[TARGET_POSITION]')
avoidance_map = get_avoidance_map('[AVOIDANCE_CONDITION]')
velocity_map = get_velocity_map('[VELOCITY_CONDITION]')
execute(movable, affordance_map=affordance_map, avoidance_map=avoidance_map, velocity_map=velocity_map)
```

**Use Case**: Precision tasks requiring collision avoidance or dynamic speed.

---

### **Template/Category 3: Gripper/Rotation-Specific Actions**

**Definition**: Commands involving gripper state (open/close) or rotational adjustments.
**Examples**:

1. `drop the toy inside container` → Uses `gripper_map` for timed opening.
2. `turn counter-clockwise by 180 degrees` → Pure `rotation_map` action.
3. `grasp the blue block...` → Combines `affordance_map`, `gripper_map`, and `velocity_map`.

**Reusable Template**:

```python
movable = parse_query_obj('[OBJECT]')
affordance_map = get_affordance_map('[TARGET_POSITION]')  # Optional
gripper_map = get_gripper_map('[GRIPPER_STATE_CONDITION]')
rotation_map = get_rotation_map('[ROTATION_INSTRUCTION]')  # Optional
execute(movable, affordance_map=affordance_map, gripper_map=gripper_map, rotation_map=rotation_map)
```

**Use Case**: Grasping, releasing, or reorienting objects.

---

### **Template/Category 4: Compound Multi-Action Tasks**

**Definition**: Commands combining multiple constraints (affordance, avoidance, velocity, rotation, gripper).
**Examples**:

1. `grasp the bottom drawer handle while moving at 0.5x speed` → Uses all four maps.
2. `move to 10cm on top of the soup bowl... while away from the glass` → Multi-constraint movement.

**Reusable Template**:

```python
movable = parse_query_obj('[OBJECT]')
affordance_map = get_affordance_map('[TARGET_POSITION]')
avoidance_map = get_avoidance_map('[AVOIDANCE_CONDITION]')
velocity_map = get_velocity_map('[VELOCITY_CONDITION]')
rotation_map = get_rotation_map('[ROTATION_CONDITION]')  # Optional
gripper_map = get_gripper_map('[GRIPPER_CONDITION]')  # Optional
execute(movable, affordance_map, avoidance_map, velocity_map, rotation_map, gripper_map)
```

**Use Case**: Complex tasks requiring synchronized constraints.

---

### **Template/Category 5: Reset/Default Actions**

**Definition**: Commands to reset the system or execute a default action (no maps needed).
**Example**:

- `go back to default` → Uses `reset_to_default_pose()`.

**Reusable Template**:

```python
reset_to_default_pose()
```

**Use Case**: System initialization or error recovery.

---

### **Key Insights**:

1. **Modularity**: Maps (`affordance`, `avoidance`, etc.) are reusable components.
2. **Extensibility**: New constraints (e.g., `acceleration_map`) could be added without disrupting existing logic.
3. **Patterns**: Most tasks follow `parse_query_obj → get_[X]_map → execute` flow.

This structure enables efficient scaling for new commands while minimizing redundancy.
