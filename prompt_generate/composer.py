import random

# 参数列表
objects = ['bowl', 'plate', 'cup', 'bottle', 'block', 'drawer handle', 'beer cap', 'tray', 'soup bowl', 'soda can', 'mug']
surfaces = ['table', 'shelf', 'bench', 'desk']
containers = ['container', 'cupboard', 'drawer']
lines = ['red line', 'green line', 'table edge']
particles = ['particles', 'debris', 'crumbs']
directions = ['left', 'right', 'front', 'back']
speeds = ['0.25x speed', '0.5x speed', '0.75x speed', '1x speed']
distances = [5, 15, 40]  # cm
angles = [45, 90, 135, 180]  # degrees
sides = ['left side', 'right side', 'front side', 'back side', 'top', 'bottom']

prompts = []

# 模板1: move ee forward/backward for Xcm
for dist in distances[2:]:
    prompts.append(f"Query: move ee forward for {dist}cm.")
for dist in distances[:2]:
    prompts.append(f"Query: move ee backward for {dist}cm.")

# 模板2: move to direction of object
for obj in objects[:4]:
    for dir_ in directions[2:]:
        prompts.append(f"Query: move to the {dir_} of the {obj}.")
        
for obj in objects[5:8]:
    for dir_ in directions[:2]:
        prompts.append(f"Query: move to the {dir_} of the {obj}.")
        
for obj in objects[10:]:
    for dir_ in directions[2:]:
        prompts.append(f"Query: move to the {dir_} of the {obj}.")

# 模板3: move to Xcm above object while Y speed and avoiding Zcm from another object
for obj1 in objects[:6]:
    for obj2 in objects[9:]:
        if obj1 == obj2: continue
        for dist in distances[2:]:
            for speed in speeds[2:]:
                prompts.append(
                    f"Query: move to {dist}cm above the {obj1}, at {speed} when within {dist*2}cm of the {obj2}, "
                    f"and keep at least {dist}cm away from the {obj2}."
                )

# 模板4: drop object inside container
for obj in objects[4:6]:
    for cont in containers[2:]:
        prompts.append(f"Query: drop the {obj} inside the {cont}.")
        
for obj in objects[8:10]:
    for cont in containers[:2]:
        prompts.append(f"Query: drop the {obj} inside the {cont}.")

# 模板5: push object along a line
for obj in objects[2:]:
    for line in lines[:2]:
        prompts.append(f"Query: push the {obj} along the {line}.")

for obj in objects[:2]:
    for line in lines[2:]:
        prompts.append(f"Query: push the {obj} along the {line}.")

# 模板6: grasp object from surface at X speed
for obj in objects[2:8]:
    for surface in surfaces[2:]:
        for speed in speeds[:3]:
            prompts.append(f"Query: grasp the {obj} from the {surface} at {speed}.")


# 模板7: wipe object but avoid another object
for obj1 in objects[8:]:
    for obj2 in objects[:3]:
        if obj1 == obj2: continue
        prompts.append(f"Query: wipe the {obj1} but avoid the {obj2}.")

# 模板8: turn gripper clockwise/counter-clockwise by angle
for angle in angles:
    prompts.append(f"Query: turn clockwise by {angle} degrees.")
    prompts.append(f"Query: turn counter-clockwise by {angle} degrees.")

# 模板9: open/close gripper
prompts.append("Query: open gripper.")
prompts.append("Query: close gripper.")

# 模板10: sweep all particles to side of object
for part in particles[2:]:
    for side in sides[2:]:
        for surface in surfaces[:2]:
            prompts.append(f"Query: sweep all {part} to the {side} of the {surface}.")

for part in particles[:2]:
    for side in sides[:2]:
        for surface in surfaces[2:]:
            prompts.append(f"Query: sweep all {part} to the {side} of the {surface}.")
            
with open("../prompts_100/composer_prompt.txt", "w") as f:
    for prompt in prompts:
        f.write(prompt + "\n")