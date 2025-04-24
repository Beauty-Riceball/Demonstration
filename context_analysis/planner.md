响应: Here’s the structured analysis of the provided context, organized into distinct templates/categories based on key themes and patterns:

---

### **Template/Category 1: Object Manipulation (Basic)**

**Definition:** Actions involving grasping, moving, or releasing objects without additional constraints or complexities.

- `composer("grasp the tissue")` – Simple grasp action.
- `composer("open gripper")` – Releasing an object.
- `composer("back to default pose")` – Returning to a neutral position.
- `composer("move to the top of the cyan bowl")` – Basic positional movement.

---

### **Template/Category 2: Constrained/Object-Aware Manipulation**

**Definition:** Actions involving spatial/safety constraints (e.g., avoiding objects, maintaining distance) or object-specific adjustments (e.g., speed, orientation).

- `composer("grasp the blue block while keeping at least 15cm away from the mug")` – Avoidance constraint.
- `composer("move to 5cm on top of the yellow block while keeping 15cm away from the mug")` – Dual constraints (position + avoidance).
- `composer("grasp the fridge handle and keep 15cm away from the hot soup")` – Safety-aware action.
- `composer("rotate the gripper to be 45 degrees slanted relative to the plate")` – Orientation-specific placement.

---

### **Template/Category 3: Tool-Mediated Actions**

**Definition:** Actions where a tool (e.g., broom, fork) is used to interact with other objects.

- `composer("grasp the broom")` followed by `composer("push the marbles into the tray")` – Tool-based sweeping.
- `composer("grasp the fork")` followed by placement for steak setup – Utensil handling.

---

### **Template/Category 4: Composite Tasks**

**Definition:** Multi-step tasks involving sequential object interactions or conditional logic (e.g., selecting objects by property).

- `composer("grasp the grape")` (sweeter fruit) → `composer("move to the top of the tray")` – Property-based selection and placement.
- `composer("grasp the lemon")` (sour fruit) → `composer("move to 10cm on top of the top drawer")` – Conditional object handling.

---

### **Template/Category 5: Mechanical Interactions**

**Definition:** Actions involving mechanical adjustments (e.g., opening/closing, turning, sliding).

- `composer("push close the drawer handle by 25cm")` – Closing a drawer.
- `composer("turn clockwise by 180 degrees")` – Rotational action (beer cap).
- `composer("push the iPhone towards the airpods")` – Sliding motion.

---

### **Template/Category 6: Speed-Adjusted Actions**

**Definition:** Actions explicitly modulated by speed parameters.

- `composer("grasp the drawer handle, at 0.5x speed")` – Slow-speed handling.
- `composer("move away from the drawer handle by 25cm, at 0.5x speed")` – Slow retraction.

---

### **Template/Category 7: State Change Tasks**

**Definition:** Actions altering the state of an object/system (e.g., turning off a lamp, unplugging).

- `composer("close the gripper")` → `composer("move to the center of the switch")` – Lamp deactivation.
- `composer("grasp the charger")` → `composer("back to default pose")` – Unplugging.

---

### **Key Observations:**

1. **Redundancy Elimination:**

   - `back to default pose` appears across multiple categories but is classified under **Basic Manipulation** as a common intermediate step.
   - Avoidance constraints (`keep 15cm away`) are grouped under **Constrained Manipulation** despite varying contexts (safety, clutter).

2. **Patterns:**
   - Most tasks follow a `grasp → move → release` flow, with variations in constraints/tools.
   - Speed adjustments and mechanical actions are niche but distinct categories.

This taxonomy ensures clarity and scalability for similar robotic task datasets.
