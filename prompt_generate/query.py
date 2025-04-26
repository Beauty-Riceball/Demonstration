import itertools

# Define object lists
blocks = ['red block', 'green block', 'blue block', 'yellow block', 'black block']
bowls = ['white bowl', 'brown bowl', 'ceramic bowl', 'plastic bowl']
handles = ['handle1', 'handle2', 'handle3', 'handle4']
trays = ['wood tray', 'metal tray', 'plastic tray']
fragile_items = ['glass', 'vase', 'porcelain plate', 'ceramic mug']
others = ['monitor', 'mouse', 'keyboard', 'phone case', 'tablet', 'chair', 'table']

# Combined list for simple detection
all_objects = blocks + bowls + handles + trays + fragile_items + others + ['gripper']

prompts = []

# 1. Simple detect prompts
for obj in all_objects:
    prompts.append(f"Query: detect('{obj}').")
    
# 2. Topmost handle prompts
for a, b in itertools.combinations(handles, 2):
    prompts.append(f"Query: topmost handle between '{a}' and '{b}'.")
   

# 3. Closest object prompts among blocks and others
for block1, block2 in itertools.combinations(blocks, 2):
    for ref in others:
        prompts.append(f"Query: which of '{block1}' and '{block2}' is closest to the '{ref}'.")

# 4. Tray contains item prompts
items = ['bread', 'apple', 'banana', 'cookie', 'egg']
for tray in trays:
    for item in items:
        prompts.append(f"Query: tray that contains the '{item}'.")

# 5. Any category prompts
prompts.append("Query: any block.")
prompts.append("Query: any bowl.")
prompts.append("Query: anything fragile.")
prompts.append("Query: table.")
prompts.append("Query: gripper.")

# 6. Handle corner prompts
corners = ['front-left', 'front-right', 'back-left', 'back-right']
for corner in corners:
        prompts.append(f"Query: handle at the {corner} corner of the drawer.")

with open('../prompts_100/parse_query_obj_prompt.txt', 'w') as f:
    for prompt in prompts:
        f.write(prompt + '\n')