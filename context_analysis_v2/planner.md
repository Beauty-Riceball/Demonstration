响应: Here’s the structured analysis of the provided context, including identified templates/categories, classified context parts, and reusable templates:

---

### **Template/Category 1: Object Manipulation with Constraints**

**Definition:** Actions involving grasping, moving, or placing objects while adhering to spatial or safety constraints (e.g., avoiding obstacles, maintaining distance).

**Classified Context Parts:**

1. `"grasp the blue block while keeping at least 15cm away from the mug"`
   - _Reason:_ Combines grasping with a safety constraint (distance from another object).
2. `"grasp the fridge handle and keep at least 15cm away from the hot soup"`
   - _Reason:_ Explicitly includes a safety constraint during manipulation.
3. `"move to 5cm on top of the yellow block while keeping at least 15cm away from the mug"`
   - _Reason:_ Movement with dual constraints (precise placement + avoidance).

**Reusable Template:**

```python
composer("[action] the [target object] [optional: with precision/speed] while [constraint, e.g., keeping Xcm away from Y]")
```

---

### **Template/Category 2: Sequential Task Execution**

**Definition:** Multi-step tasks where actions are performed in a specific sequence to achieve a goal (e.g., grasp → move → release).

**Classified Context Parts:**

1. `"grasp the tissue" → "back to default pose" → "move to 10cm to the right of the bowl" → "open gripper"`
   - _Reason:_ Standard sequence for relocating an object.
2. `"grasp the steak" → "back to default pose" → "rotate gripper..." → "move to plate" → "open gripper"`
   - _Reason:_ Complex sequence involving rotation and placement.
3. `"grasp the fork" → "back to default pose" → "move to plate" → "open gripper"`
   - _Reason:_ Repetitive pattern for utensil setup.

**Reusable Template:**

```python
composer("grasp the [object]")
composer("back to default pose")
composer("move to [target location/relation]")
composer("open gripper")
# Optional: Add intermediate steps like rotation or speed adjustments.
```

---

### **Template/Category 3: Tool-Based Interaction**

**Definition:** Tasks requiring the use of a tool (e.g., broom, gripper) to interact with objects indirectly.

**Classified Context Parts:**

1. `"grasp the broom" → "push the marbles into the tray"`
   - _Reason:_ Uses a tool (broom) to manipulate marbles.
2. `"close the gripper" → "move to the center of the switch"`
   - _Reason:_ Uses gripper as a tool to toggle a switch.
3. `"grasp the beer cap" → "turn clockwise by 180 degrees"`
   - _Reason:_ Gripper acts as a tool to twist/open an object.

**Reusable Template:**

```python
composer("grasp the [tool]")
composer("[action] the [target object] [optional: with parameters like degrees/speed]")

```

---

### **Template/Category 4: Environment Navigation**

**Definition:** Actions focused on moving or adjusting objects within an environment (e.g., opening/closing drawers, sliding items).

**Classified Context Parts:**

1. `"push close the drawer handle by 25cm"`
   - _Reason:_ Direct interaction with environmental components (drawer).
2. `"push the iPhone towards the airpods"`
   - _Reason:_ Relies on sliding motion within a space.
3. `"move away from the drawer handle by 25cm"`
   - _Reason:_ Navigation relative to fixed environmental objects.

**Reusable Template:**

```python
composer("[action] the [environmental object] [optional: direction/distance/speed]")
```

---

### **Template/Category 5: Context-Aware Selection**

**Definition:** Tasks requiring implicit or explicit context to select objects (e.g., "sweeter fruit" or "sour fruit").

**Classified Context Parts:**

1. `"grasp the grape"` (from "sweeter fruit in the tray")
   - _Reason:_ Requires inferring which object matches the descriptor.
2. `"grasp the lemon"` (from "sour fruit into the top drawer")
   - _Reason:_ Uses contextual knowledge (lemon = sour) for selection.

**Reusable Template:**

```python
# Pre-step: Parse query for descriptors (e.g., "sweeter", "sour").
composer("grasp the [object matching descriptor]")
```

---

### **Summary of Reusable Templates**

1. **Constrained Manipulation:**
   ```python
   composer("[action] [object] while [constraint]")
   ```
2. **Sequential Execution:**
   ```python
   composer("grasp [X]") → composer("move to [Y]") → composer("open gripper")
   ```
3. **Tool Usage:**
   ```python
   composer("grasp [tool]") → composer("use tool to [action]")
   ```
4. **Environment Interaction:**
   ```python
   composer("[action] [environmental object] [parameters]")
   ```
5. **Contextual Selection:**
   ```python
   composer("grasp the [object matching query descriptor]")
   ```

These templates can be adapted for future tasks by replacing placeholders (e.g., `[object]`, `[constraint]`) with context-specific details.
