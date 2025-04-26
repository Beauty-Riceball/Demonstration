# -*- coding: utf-8 -*-
import itertools
import os
distances = [5, 15, 25, 50]  # cm
objects = ['bowl', 'mug', 'plate', 'bottle', 'red block', 'blue block', 'green cylinder', 'yellow sphere', 'cup', 'fork']
categories = ['anything fragile', 'anything metallic', 'anything soft', 'anything sharp']
prompts = []

# 单对象距离模板：N cm from/near/around the object
for dist, obj, variant in itertools.product(distances[2:], objects[:4], ['from', 'near', 'around']):
    prompts.append(f"Query: {dist}cm {variant} the {obj}.")
    
for dist, obj, variant in itertools.product(distances[:2], objects[6:], ['from', 'near', 'around']):
    prompts.append(f"Query: {dist}cm {variant} the {obj}.")

# 类别距离模板：N cm from the category
for dist, cat in itertools.product(distances[:2], categories[2:]):
    prompts.append(f"Query: {dist}cm from {cat}.")
    
for dist, cat in itertools.product(distances[2:], categories[:2]):
    prompts.append(f"Query: {dist}cm from {cat}.")



# 双对象组合模板：N cm around obj1 and M cm around obj2
for (dist1, dist2), (obj1, obj2) in itertools.product(itertools.product(distances[:1], distances[3:]), itertools.combinations(objects[:5], 2)):
    prompts.append(f"Query: {dist1}cm around the {obj1} and {dist2}cm around the {obj2}.")
for (dist1, dist2), (obj1, obj2) in itertools.product(itertools.product(distances[2:], distances[2:]), itertools.combinations(objects[5:], 2)):
    prompts.append(f"Query: {dist1}cm around the {obj1} and {dist2}cm around the {obj2}.")


# 混合模板：不同距离对象
for dist in distances:
    prompts.append(f"Query: slower when within {dist}cm of the bowl and faster when outside {dist}cm.")


with open("../prompts_100/get_avoidance_map_prompt.txt", "w", encoding="utf-8") as f:
    for prompt in prompts:
        f.write(prompt + "\n")

