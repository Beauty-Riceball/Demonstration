# Generate 100 affordance map "Query:" prompts with different objects and positions

import itertools

objects = ['bowl', 'mug', 'plate', 'container', 'brown block', 'blue block', 'green block', 'yellow bowl', 'blue circle', 'tray', 'lemon', 'topmost drawer handle', 'leftmost block']
directions = ['front', 'back', 'left', 'right', 'top', 'bottom']
distances = [5, 10, 25, 50]  # cm

prompts = []

# Template 1: Fixed distance from an object
for obj in objects[:3]:
    for dist in distances[0:1]:
        for dir_ in directions[4:]:
            prompts.append(f"Query: a point {dist}cm {dir_} of the {obj}.")
            
for obj in objects[9:]:
    for dist in distances[1:]:
        for dir_ in directions[1:2]:
            prompts.append(f"Query: a point {dist}cm {dir_} of the {obj}.")

# Template 2: Moving based on a relative position (x, y, z)
for obj in objects[:4]:
    for dist in distances[2:3]:
        prompts.append(f"Query: a point {dist}cm in front of the {obj}.")
        prompts.append(f"Query: a point {dist}cm above the {obj}.")
        
for obj in objects[7:11]:
    for dist in distances[:1]:
        prompts.append(f"Query: a point {dist}cm in front of the {obj}.")
        prompts.append(f"Query: a point {dist}cm above the {obj}.")

# Template 3: Combining two relative positions (for more complex movements)
for obj1, obj2 in itertools.combinations(objects[3:9], 2):
    for dist1, dist2 in itertools.product(distances[2:], repeat=2):
        prompts.append(f"Query: a point {dist1}cm to the left of the {obj1} and {dist2}cm on top of the {obj2}.")

# Template 4: Avoidance areas
for obj in objects[1:6]:
    for dist in distances[2:3]:
        prompts.append(f"Query: anywhere within {dist}cm of the {obj}.")
        
for obj in objects[9:12]:
    for dist in distances[1:3]:
        prompts.append(f"Query: anywhere within {dist}cm of the {obj}.")

# Template 5: Specifying relative positions from other reference points
for obj in objects[7:10]:
    for ref in objects[3:8]:
        if obj != ref:
            for dist in distances[:1]:
                prompts.append(f"Query: a point {dist}cm from the {ref} towards the {obj}.")

for obj in objects[10:]:
    for ref in objects[10:]:
        if obj != ref:
            for dist in distances[3:]:
                prompts.append(f"Query: a point {dist}cm from the {ref} towards the {obj}.")

# Template 6: Points based on combinations of relative directions
for obj in objects[5:8]:
    for dir_1, dir_2 in itertools.combinations(directions[3:], 2):
        for dist in distances[3:]:
            prompts.append(f"Query: a point {dist}cm {dir_1} and {dir_2} of the {obj}.")


with open("../prompts_100/get_affordance_map_prompt.txt", "w") as f:
    for prompt in prompts:
        f.write(prompt + "\n")
