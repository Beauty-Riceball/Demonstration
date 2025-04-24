```python
import numpy as np
from env_utils import execute
from perception_utils import parse_query_obj
import action_utils import composer
```

### 1. **Safe Interaction with Hazard Avoidance:**

_Definition: Commands where the gripper interacts with an object while maintaining a specified safe distance from hazardous or avoided objects._

- **Examples:**

  ```python
  objects = ['blue block', 'yellow block', 'mug']
  # Query: place the blue block on the yellow block, and avoid the mug at all time.
  composer("grasp the blue block while keeping at least 15cm away from the mug")
  composer("back to default pose")
  composer("move to 5cm on top of the yellow block while keeping at least 15cm away from the mug")
  composer("open gripper")
  # done
  ```

  ```python
  objects = ['fridge', 'hot soup']
  # Query: Open the fridge door and be careful around the hot soup.
  composer("grasp the fridge handle and keep at least 15cm away from the hot soup")
  composer("move away from the fridge handle by 25cm and keep at least 15cm away from the hot soup")
  composer("open gripper")
  # done
  ```

- **Reusable Template**:

  ```python
  composer("grasp the {object} while keeping at least {distance} cm away from the {hazard}")
  composer("move to {position} while keeping at least {distance} cm away from the {hazard}")
  ```

### 2. **Speed-Controlled Relative Movement:**

_Definition: Commands where the gripper moves relative to an object with specified speed and distance parameters._

- **Examples:**

  ```python
  objects = ['airpods', 'drawer']
  # Query: Open the drawer slowly.
  composer("grasp the drawer handle, at 0.5x speed")
  composer("move away from the drawer handle by 25cm, at 0.5x speed")
  composer("open gripper, at 0.5x speed")
  # done
  ```

- **Reusable Template**:

  ```python
  composer("{action} {direction} the {object} by {distance} cm at {speed}x speed")
  ```

### 3. **Object-Relative Positioning:**

_Definition: Commands where the gripper positions itself or an object relative to another target object._

- **Examples:**

  ```python
  objects = ['cyan bowl', 'yellow bowl', 'box', 'ice cream']
  # Query: move to the top of the cyan bowl.
  composer("move to the top of the cyan bowl")
  # done
  ```

  ```python
  objects = ['tissue box', 'tissue', 'bowl']
  # Query: Can you pass me a tissue and place it next to the bowl?
  composer("grasp the tissue")
  composer("back to default pose")
  composer("move to 10cm to the right of the bowl")
  composer("open gripper")
  composer("back to default pose")
  # done
  ```

- **Reusable Template**:

  ```python
  composer("move to {distance} {preposition} the {target}")
  ```

### 4. **Content-Aware Manipulation:**

_Definition: Commands where the gripper interacts with objects based on their contents or container relationships._

- **Examples:**

  ```python
  objects = ['grape', 'lemon', 'drill', 'router', 'bread', 'tray']
  # Query: put the sweeter fruit in the tray that contains the bread.
  composer("grasp the grape")
  composer("back to default pose")
  composer("move to the top of the tray that contains the bread")
  composer("open gripper")
  # done
  ```

- **Reusable Template**:

  ```python
  composer("{action} the {object} {preposition} the {target} that contains the {contents}")
  ```

### 5. **Object Translation Commands:**

_Definition: Commands where the gripper pushes or slides objects toward specific targets_

- **Examples:**

  ```python
  objects = ['iPhone', 'airpods']
  # Query: slide the iPhone towards the airpods.
  composer("push the iPhone towards the airpods")
  # done
  ```

  ```python
  objects = ['marbles', 'tray', 'broom']
  # Query: Can you sweep the marbles into the tray?
  composer("grasp the broom")
  composer("back to default pose")
  composer("push the marbles into the tray")
  # done
  ```

- **Reusable Template**:

  ```python
  composer("{action} the {object} towards the {target}")
  ```

### 6. **Rotational Movement:**

_Definition: Commands involving specific rotational movements of the gripper or objects._

- **Examples:**

  ```python
  objects = ['beer']
  # Query: turn close the beer.
  composer("grasp the beer cap")
  composer("turn clockwise by 180 degrees")
  composer("back to default pose")
  # done
  ```

- **Reusable Template**:

  ```python
  composer("{rotate} by {degrees} degrees")
  ```

### 7. **Orientation-Sensitive Actions':**

_Definition: Commands where the gripper interacts with an object while adjusting orientation relative to another object._

- **Examples:**

  ```python
  objects = ['steak', 'grill', 'plate']
  # Query: Take the steak out of the grill and put it flat on the plate.
  composer("grasp the steak")
  composer("back to default pose")
  composer("rotate the gripper to be 45 degrees slanted relative to the plate")
  composer("move to 10cm on top of the plate")
  composer("open gripper")
  composer("back to default pose")
  # done
  ```

- **Reusable Template**:

  ```python
  composer("{action} the {object} with {orientation} relative to the {target}")
  ```

### 8. **System State Management:**

_Definition: Commands that return the system or gripper to default states._

- **Examples:**

  ```python
  composer("back to default pose")
  ```

- **Reusable Template**:

  ```python
  composer("{action} the {object} and {return} to default pose")
  ```

### 9. **Force-Applied Manipulation:**

_Definition: Commands involving application of force to objects (pushing, closing)._

- **Examples:**

  ```python
  objects = ['drawer', 'umbrella']
  # Query: close the drawer.
  composer("push close the drawer handle by 25cm")
  # done
  ```

- **Reusable Template**:

  ```python
  composer("{action} the {object} {preposition} the {target} with {force}")
  ```

### 10. **State Change Commands:**

_Definition: Commands that change the state of objects or the gripper itself._

- **Examples:**

  ```python
  objects = ['lamp', 'switch']
  # Query: Turn off the lamp.
  composer("close the gripper")
  composer("move to the center of the switch")
  composer("back to default pose")
  # done
  ```

- **Reusable Template**:

  ```python
  composer("{action} the {object} to {state}")
  ```

---
