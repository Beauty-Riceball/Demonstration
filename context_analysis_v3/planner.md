响应: Here’s the structured analysis of the provided context:

---

### **Template/Category 1: Object Manipulation with Constraints**

- **Definition**: Actions involving grasping, moving, or placing objects while adhering to specific constraints (e.g., avoiding obstacles, maintaining distance, or adjusting speed).
- **Classified Context Parts**:
  - `"grasp the blue block while keeping at least 15cm away from the mug"` - Involves grasping with a distance constraint.
  - `"grasp the fridge handle and keep at least 15cm away from the hot soup"` - Includes a safety constraint.
  - `"grasp the drawer handle, at 0.5x speed"` - Specifies speed as a constraint.
- **Reusable Template**:
  _"Perform [action] on [object] while [constraint]."_
  Example: _"Grasp the mug while avoiding the hot plate."_

---

### **Template/Category 2: Sequential Multi-Step Tasks**

- **Definition**: Tasks requiring a sequence of actions to achieve a goal (e.g., grasping, moving, releasing, or resetting).
- **Classified Context Parts**:
  - `"grasp the tissue" → "back to default pose" → "move to 10cm to the right of the bowl" → "open gripper"` - Multi-step task for placing an object.
  - `"grasp the steak" → "back to default pose" → "rotate gripper" → "move to plate" → "open gripper"` - Complex sequence for precise placement.
- **Reusable Template**:
  _"1. [Action 1]. 2. [Action 2]. ... N. [Final action]."_
  Example: _"1. Grasp the pen. 2. Move to the notebook. 3. Open gripper."_

---

### **Template/Category 3: Tool-Based Interaction**

- **Definition**: Tasks where tools (e.g., broom, gripper) are used to interact with objects (e.g., sweeping, pushing, or turning).
- **Classified Context Parts**:
  - `"grasp the broom" → "push the marbles into the tray"` - Uses a tool to manipulate objects.
  - `"grasp the beer cap" → "turn clockwise by 180 degrees"` - Uses gripper as a tool for twisting.
- **Reusable Template**:
  _"Use [tool] to [action] [object]."_
  Example: _"Use the spatula to flip the pancake."_

---

### **Template/Category 4: Context-Aware Object Selection**

- **Definition**: Actions where objects are selected based on implicit context (e.g., "sweeter fruit" refers to a grape, "sour fruit" to a lemon).
- **Classified Context Parts**:
  - `"grasp the grape"` - Selected due to "sweeter fruit" in the query.
  - `"grasp the lemon"` - Selected due to "sour fruit" in the query.
- **Reusable Template**:
  _"Identify [object] based on [contextual descriptor] and [action]."_
  Example: _"Identify the ripe banana and place it in the basket."_

---

### **Template/Category 5: Environmental State Changes**

- **Definition**: Actions that alter the state of the environment (e.g., opening/closing drawers, turning off lamps).
- **Classified Context Parts**:
  - `"push close the drawer handle by 25cm"` - Changes the drawer’s state.
  - `"move to the center of the switch"` - Implies turning off the lamp.
- **Reusable Template**:
  _"Change [environmental object] state to [new state]."_
  Example: _"Close the window to block the wind."_

---

### **Suggested New Tasks**:

1. **Dynamic Obstacle Avoidance**:
   _"Move the vase to the shelf while avoiding the moving fan."_
   (Expands on constraints by introducing dynamic obstacles.)
2. **Tool-Based Assembly**:
   _"Use the screwdriver to attach the shelf to the wall."_
   (Extends tool interactions to assembly tasks.)
3. **Contextual Sorting**:
   _"Arrange the books by size, placing the largest on the bottom shelf."_
   (Adds sorting based on implicit rules.)

---

This analysis ensures adaptability for future tasks while minimizing redundancy. Let me know if you'd like refinements!
