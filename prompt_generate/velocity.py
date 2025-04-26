# 生成100条 velocity_map "Query:" 模板

import itertools

# 参数定义
directions = ['left', 'right', 'front', 'back', 'top', 'bottom']
opposites = {'left':'right', 'right':'left', 'front':'back', 'back':'front', 'top':'bottom', 'bottom':'top'}
surfaces = ['table', 'desk', 'shelf']
fractions = [0.25, 0.5, 0.75, 1, 1.5, 2]
objects = ['block', 'bowl', 'mug', 'bottle', 'phone', 'plate', 'chips', 'glass']
distances = [5, 15, 40]

prompts = []

# 模板1: 方向性速度控制
for dir_ in directions[:3]:
    for surface in surfaces[1:]:
        prompts.append(
            f"Query: faster when on the {dir_} side of the {surface} and slower on the {opposites[dir_]} side of the {surface}."
        )
for dir_ in directions[3:]:
    for surface in surfaces[:2]:
        prompts.append(
            f"Query: faster when on the {dir_} side of the {surface} and slower on the {opposites[dir_]} side of the {surface}."
        )

# 模板2: 全局速度调整
prompts.extend([
    "Query: slow down by a quarter.",
    "Query: slow down by a half.",
    "Query: increase speed by 25%.",
    "Query: decrease speed by 50%.",
])

# 模板3: 距离感知速度控制
for obj, frac, dist in itertools.product(objects[:4], fractions[:3], distances):
    prompts.append(
        f"Query: speed at {frac}x when within {dist}cm of the {obj}."
    )   
for obj, frac, dist in itertools.product(objects[4:], fractions[2:], distances):
    prompts.append(
        f"Query: speed at {frac}x when within {dist}cm of the {obj}."
    )

# 模板4: 除外区域速度设置
for obj, frac in itertools.product(objects[:4], fractions[:2]):
    prompts.append(
        f"Query: speed at {frac}x everywhere except within 10cm of the {obj}."
    )
for obj, frac in itertools.product(objects[4:], fractions[2:]):
    prompts.append(
        f"Query: speed at {frac}x everywhere except within 10cm of the {obj}."
    )

with open('../prompts_100/get_velocity_map_prompt.txt', 'w', encoding='utf-8') as f:
    for prompt in prompts:
        f.write(prompt + '\n')
