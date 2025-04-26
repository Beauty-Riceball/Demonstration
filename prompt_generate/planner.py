import random

# Pools of objects and items
items = [
    'blue block', 'yellow block', 'red ball', 'green cup', 'mug', 'bottle', 'book',
    'plate', 'bowl', 'tray', 'drawer handle', 'soda can', 'steak', 'fork', 'knife',
    'spoon', 'lamp', 'switch', 'beer cap', 'grill', 'marbles', 'tissue', 'charger',
    'outlet', 'bread', 'broom', 'orange', 'lemon', 'router', 'drill', 'fridge',
    'hot soup', 'cyan bowl', 'yellow bowl', 'box', 'airpods', 'iPhone', 'tablet',
    'keyboard', 'mouse'
]
containers = ['tray', 'container', 'drawer', 'cupboard', 'box', 'shelf']
locations = ['on top of', 'next to', 'in front of', 'behind', 'to the left of',
             'to the right of', 'above', 'below']
actions = [
    # grasp and place
    ("place the {obj1} on the {obj2}", []),
    # pass item
    ("pass me a {obj1} and place it {loc} the {obj2}", []),
    # unplug charger
    ("unplug the {obj1} from the {obj2}", []),
    # drop in container
    ("drop the {obj1} inside the {container}", []),
    # sweep into container
    ("sweep the {obj1} into the {container}", []),
    # open drawer
    ("open the {container}", []),
    # close drawer
    ("close the {container}", []),
    # slide phone
    ("slide the {obj1} towards the {obj2}", []),
    # set utensil
    ("set up the {obj1} for the {obj2}", []),
    # turn off lamp
    ("turn off the lamp", []),
    # turn cap
    ("turn the {obj1}", []),
    # rotate relative
    ("take the {obj1} out of the {container} and put it flat on the {obj2}", [])
]

# Generate only the Query lines
prompts = set()
for template, _ in actions[1:2]:
    for obj1 in items[4:5]:
        for obj2 in (items + containers)[38:40]:
            for container in containers[1:2]:
                for loc in locations[3:4]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")
                
                    
for template, _ in actions[:1]:
    for obj1 in items[:2]:
        for obj2 in (items + containers)[35:38]:
            for container in containers[:1]:
                for loc in locations[2:3]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")

for template, _ in actions[2:3]:
    for obj1 in items[7:11]:
        for obj2 in (items + containers)[23:26]:
            for container in containers[1:2]:
                for loc in locations[6:7]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")
                    
for template, _ in actions[3:4]:
    for obj1 in items[5:7]:
        for obj2 in (items + containers)[20:23]:
            for container in containers[:1]:
                for loc in locations[7:]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")
   
                      
for template, _ in actions[5:6]:
    for obj1 in items[13:16]:
        for obj2 in (items + containers)[26:28]:
            for container in containers[3:4]:
                for loc in locations[1:2]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")
                                
for template, _ in actions[4:5]:
    for obj1 in items[11:13]:
        for obj2 in (items + containers)[28:30]:
            for container in containers[4:5]:
                for loc in locations[2:3]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}") 
                        
for template, _ in actions[6:7]:
    for obj1 in items[16:18]:
        for obj2 in items + containers[17:20]:
            for container in containers[5:]:
                for loc in locations[:1]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")
                    
for template, _ in actions[7:8]:
    for obj1 in items[18:20]:
        for obj2 in items + containers[14:17]:
            for container in containers[2:3]:
                for loc in locations[1:2]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")
                    
for template, _ in actions[3:4]:
    for obj1 in items[20:23]:
        for obj2 in (items + containers)[12:15]:
            for container in containers[:1]:
                for loc in locations[3:4]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")
                    
for template, _ in actions[4:5]:
    for obj1 in items[23:27]:
        for obj2 in (items + containers)[10:12]:
            for container in containers[1:2]:
                for loc in locations[3:4]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")          
          
for template, _ in actions[7:8]:
    for obj1 in items[27:30]:
        for obj2 in (items + containers)[30:35]:
            for container in containers[3:4]:
                for loc in locations[4:6]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")    
                    
                                                    
for template, _ in actions[9:10]:
    for obj1 in items[30:33]:
        for obj2 in (items + containers)[2:5]:
            for container in containers[4:5]:
                for loc in locations[5:6]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")
                    
for template, _ in actions[8:9]:
    for obj1 in items[33:36]:
        for obj2 in (items + containers)[0:2]:
            for container in containers[2:3]:
                for loc in locations[6:7]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")
                    
for template, _ in actions[10:11]:
    for obj1 in items[37:]:
        for obj2 in (items + containers)[7:10]:
            for container in containers[1:2]:
                for loc in locations[7:8]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")
                    
for template, _ in actions[11:]:
    for obj1 in items[33:37]:
        for obj2 in (items + containers)[5:7]:
            for container in containers[:1]:
                for loc in locations[7:]:
                    if "{obj2}" in template and obj1 == obj2:
                        continue
                    query = template.format(obj1=obj1, obj2=obj2, container=container, loc=loc)
                    prompts.add(f"Query: {query}")                      
# Write to file
output_path = '../prompts_100/planner_prompt.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    for prompt in prompts:
        f.write(prompt + "\n")

print(f"Wrote {len(prompts)} queries to {output_path}")

