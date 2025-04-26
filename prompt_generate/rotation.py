import random
import numpy as np

objects    = ['bowl', 'plate', 'cup', 'gripper', 'mug', 'bottle', 'book', 'block', 'wall', 'shelf', 'table', 'chair', 'cap', 'door']
directions = ['left', 'right', 'north', 'south', 'east', 'west', 'forward', 'backward']
angles     = [np.pi/6, np.pi, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 3*np.pi/4, 2*np.pi]
axes       = ['x', 'y', 'z']
distances  = [5, 15, 30, 50, 100]

templates = []

# 面向某个物体或表面
for obj in objects[11:]:
    for direction in directions[4:]:
        templates.append(f"Face the support surface of the {obj}.")
        for dist in distances[5:7]:
            templates.append(f"Face the {obj} when within {dist}cm from table center.")
        templates.append(f"Face the {obj} while keeping {random.choice(directions)} from the table.")

    for angle in angles[:2]:
        deg = angle * 180 / np.pi
        templates.append(f"Turn clockwise by {deg:.1f} degrees when at the {obj}.")
        templates.append(f"Turn counter-clockwise by {deg:.1f} degrees when near the {obj}.")
        templates.append(f"Rotate the {obj} by {deg:.1f} degrees around the {random.choice(axes)}-axis.")

for obj in objects[2:5]:
    for direction in directions[2:3]:
        templates.append(f"Face the support surface of the {obj}.")
        for dist in distances[:2]:
            templates.append(f"Face the {obj} when within {dist}cm from table center.")
        templates.append(f"Face the {obj} while keeping {random.choice(directions)} from the table.")

    for angle in angles[6:]:
        deg = angle * 180 / np.pi
        templates.append(f"Turn clockwise by {deg:.1f} degrees when at the {obj}.")
        templates.append(f"Turn counter-clockwise by {deg:.1f} degrees when near the {obj}.")
        templates.append(f"Rotate the {obj} by {deg:.1f} degrees around the {random.choice(axes)}-axis.")

# 相对于其它物体旋转
for obj in objects[:3]:
    for ref in objects[8:11]:
        if obj != ref:
            templates.append(f"Rotate the {obj} to face the {ref}.")
            deg = random.choice(angles) * 180 / np.pi
            templates.append(f"Rotate the {obj} to be {deg:.1f} degrees slanted relative to the {ref}.")
            templates.append(f"Rotate the {obj} based on the normal of the {ref}.")

# 复杂旋转操作
for obj in objects[9:12]:
    for dist in distances[1:2]:
        deg1 = random.choice(angles) * 180 / np.pi
        deg2 = random.choice(angles) * 180 / np.pi
        templates.append(f"Turn clockwise by {deg1:.1f} degrees, then face the {obj}.")
        templates.append(f"Face the {obj}, then rotate it {deg1:.1f}° clockwise and {deg2:.1f}° counter-clockwise.")
        templates.append(f"Rotate the {obj} by {deg1:.1f}° around {random.choice(axes)}-axis, then face the {obj}.")

# 根据位置调整旋转
for obj in objects[3:7]:
    for dist in distances[3:4]:
        templates.append(f"Rotate the {obj} to align with the table when within {dist}cm of it.")
        deg = random.choice(angles) * 180 / np.pi
        templates.append(f"Turn the {obj} by {deg:.1f}° counter-clockwise when at the center of the {obj}.")
        templates.append(f"Rotate the {obj} to match the orientation of the {random.choice(objects)} when near it.")

# 随机生成不同方向旋转
for obj in objects[5:8]:
    deg1 = random.choice(angles) * 180 / np.pi
    deg2 = random.choice(angles) * 180 / np.pi
    templates.append(f"Face the {obj}, then rotate it {deg1:.1f}° clockwise and {deg2:.1f}° counter-clockwise.")

# 写入文件（确保路径存在且以 UTF-8 保存）
with open('../prompts_100/get_rotation_map_prompt.txt', 'w', encoding='utf-8') as f:
    for tmpl in templates:
        f.write("Query: " + tmpl + '\n')