响应: Here’s the structured analysis of the provided context, categorized into reusable templates and expanded with new task suggestions:

---

### **1. 'a {movable} moves {distance} {direction} the {target}':**

**Definition:** Commands where a movable object (e.g., gripper) moves a specified distance in a direction relative to a target object.

- **Classified Context Part:**
  - `move ee forward for 10cm`
  - `move the gripper behind the bowl`
  - `move to the left of the brown block`
  - `close drawer by 5cm`
  - `move to 5cm on top of the soda can`
    **Reason:** All involve directional movement with explicit distance and target.
- **Reusable Template:**
  `{movable} moves {distance} {direction} the {target}`

---

### **2. 'a {movable} moves to {position} while avoiding {constraint}':**

**Definition:** Movement with positional goals and avoidance constraints (e.g., proximity limits).

- **Classified Context Part:**
  - `move to the back side of the table while staying at least 5cm from the blue block`
  - `move to 10cm on top of the soup bowl, and 5cm to the left ... while away from the glass`
  - `wipe the red dot but avoid the blue block`
    **Reason:** Combines affordance (target position) with avoidance (proximity constraints).
- **Reusable Template:**
  `{movable} moves to {position} while avoiding {constraint}`

---

### **3. 'a {movable} adjusts {property} when {condition}':**

**Definition:** Dynamic adjustments (e.g., speed, rotation) triggered by conditions.

- **Classified Context Part:**
  - `slow down when near the bowl`
  - `move at 0.5x speed when within 20cm of the wooden mug`
  - `turn counter-clockwise by 180 degrees`
    **Reason:** Specifies conditional changes to velocity, rotation, or gripper state.
- **Reusable Template:**
  `{movable} adjusts {property} when {condition}`

---

### **4. 'a {movable} interacts with {target} using {gripper_state}':**

**Definition:** Gripper-based interactions (grasping, dropping) with state rules.

- **Classified Context Part:**
  - `drop the toy inside container`
  - `grasp the blue block ... at a quarter of the speed`
  - `grasp the mug from the shelf`
    **Reason:** Focuses on gripper actions with positional/state constraints.
- **Reusable Template:**
  `{movable} interacts with {target} using {gripper_state}`

---

### **5. 'a {movable} resets to {default_state}':**

**Definition:** Commands to return to a predefined default state.

- **Classified Context Part:**
  - `go back to default`
  - `open gripper`
    **Reason:** Explicit reset or state initialization.
- **Reusable Template:**
  `{movable} resets to {default_state}`

---

### **6. 'a {movable} performs {action} along {path}':**

**Definition:** Path-based actions (e.g., pushing, sweeping) with linear trajectories.

- **Classified Context Part:**
  - `push the second to the left block along the red line`
  - `sweep all particles to the left side of the table`
    **Reason:** Involves movement along a defined path or area.
- **Reusable Template:**
  `{movable} performs {action} along {path}`

---

### **Suggested New Tasks:**

1. **"Rotate the gripper 90 degrees clockwise while moving toward the cup, avoiding the saucer."**
   - Combines rotation, directional movement, and avoidance.
2. **"Place the book on the shelf, aligning it parallel to the edge, and slow down near fragile objects."**
   - Adds alignment constraints and conditional speed adjustment.
3. **"Move the robot arm in a spiral path around the vase, maintaining 10cm distance."**
   - Introduces complex trajectories with proximity rules.

---

**Summary:** The templates cover core robotics tasks (movement, interaction, constraints), while new tasks expand into precision alignment, complex paths, and multi-condition actions. Each template is reusable for generating similar commands.
