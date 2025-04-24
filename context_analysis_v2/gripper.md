响应: Here’s the structured analysis of the provided context, identifying key templates/categories, classifying the code snippets, and creating reusable templates for future use:

---

### **Template/Category 1: Default State with Radial Exception**

**Definition**: Code that sets a default state (open/close) for the entire gripper map, then modifies a radial region around a specific object or position.

**Classified Context Parts**:

1. `open everywhere except 1cm around the green block`
   - Sets default state (`gripper_map[:, :, :] = 1`), then closes a radial region around the green block.
2. `close everywhere but open when on top of the back left corner of the table`
   - Sets default state (`gripper_map[:, :, :] = 0`), then opens a radial region at a computed position.

**Reusable Template**:

```python
gripper_map = get_empty_gripper_map()
gripper_map[:, :, :] = <DEFAULT_STATE>  # 1 (open) or 0 (close)
<OBJECT> = parse_query_obj('<OBJECT_NAME>')
set_voxel_by_radius(
    gripper_map,
    <POSITION>,  # e.g., object.position or computed coordinates
    radius_cm=<RADIUS>,
    value=<EXCEPTION_VALUE>  # Opposite of DEFAULT_STATE
)
```

---

### **Template/Category 2: Default State with Planar Exception**

**Definition**: Code that sets a default state (open/close) for the entire gripper map, then modifies a planar region (e.g., half-space) based on object bounds or center.

**Classified Context Parts**:

1. `always open except when you are on the right side of the table`
   - Sets default state (`gripper_map[:, :, :] = 1`), then closes all voxels where `y >= center_y` (right side).
2. `always close except when you are on the back side of the table`
   - Sets default state (`gripper_map[:, :, :] = 0`), then opens all voxels where `x < center_x` (back side).

**Reusable Template**:

```python
gripper_map = get_empty_gripper_map()
gripper_map[:, :, :] = <DEFAULT_STATE>  # 1 (open) or 0 (close)
<OBJECT> = parse_query_obj('<OBJECT_NAME>')
center_x, center_y, center_z = <OBJECT>.position
gripper_map[<SLICE_CONDITION>] = <EXCEPTION_VALUE>  # e.g., [:center_x, :, :] for "back"
```

---

### **Template/Category 3: Position Computation for Exceptions**

**Definition**: Code that computes a specific position (e.g., table corner, offset from bounds) to define an exception region.

**Classified Context Parts**:

1. `on top of the back left corner of the table`
   - Computes `(min_x, min_y, max_z + offset)` using table bounds (`aabb`) and adds an offset in the z-direction.

**Reusable Template**:

```python
(min_x, min_y, min_z), (max_x, max_y, max_z) = <OBJECT>.aabb
x = <BOUND_OR_CENTER>  # e.g., min_x for "back"
y = <BOUND_OR_CENTER>  # e.g., min_y for "left"
z = <BOUND_OR_CENTER> + cm2index(<OFFSET>, 'z')  # e.g., max_z + offset for "top"
```

---

### **Key Observations**:

1. **Patterns**:
   - All examples follow a **default state + exception** structure.
   - Exceptions are either **radial** (using `set_voxel_by_radius`) or **planar** (using array slicing).
   - Object positions are either directly used or derived from bounds (`aabb`).
2. **Reusability**:
   - The templates abstract the logic for handling spatial conditions (radial/planar) and position computation.
   - Future queries can reuse these by plugging in object names, directions, and offsets.

Let me know if you'd like additional refinements or edge-case handling!
