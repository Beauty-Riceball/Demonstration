import itertools

objects = ['block', 'sphere', 'cylinder', 'cup', 'plate', 'bowl', 'bottle']
colors = ['red', 'blue', 'green', 'yellow', 'brown', 'white', 'black']
distances = [2, 5, 10, 15, 30, 50] 
sides = [
    'left side of the table', 'right side of the table', 'front side of the chair',
    'back side of the shelf', 'top of the cabinet', 'bottom of the box',
    'front-left corner of the desk', 'back-right corner of the bench',
    'wall next to the table', 'window near the desk'
]
positions = [
    'above the red block', 'below the blue sphere', 'in front of the yellow cylinder',
    'behind the green cup', 'between the bowl and the plate',
    'at the center of the table', 'at the back-left corner of the shelf',
    'on top of the chair', 'under the desk', 'on the right side of the cabinet'
]

templates = []

# 1. open everywhere except N cm around colored objects
for color, obj, dist in itertools.product(colors[4:], objects[5:], distances[3:]):
    templates.append(f"Query: open everywhere except {dist}cm around the {color} {obj}.")

# 2. close everywhere except N cm around colored objects
for color, obj, dist in itertools.product(colors[:4], objects[:4], distances[:3]):
    templates.append(f"Query: close everywhere except {dist}cm around the {color} {obj}.")

# 3. always open except on specific sides/locations
for side in sides:
    templates.append(f"Query: always open except on the {side}.")

# 4. always close except on specific sides/locations
for side in sides:
    templates.append(f"Query: always close except on the {side}.")

# 5. open only when at specific positions
for pos in positions:
    templates.append(f"Query: open only when {pos}.")

# 6. close only when at specific positions
for pos in positions:
    templates.append(f"Query: close only when {pos}.")


with open('../prompts_100/get_gripper_map_prompt.txt', 'w') as f:
    for template in templates:
        f.write(template + '\n')