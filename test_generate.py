import random
import itertools

manual_queries = [
    "a point 15 cm behind the red block",
    "a point 5 cm below the table",
    "a point on the door",
    "a point at the center of the blue block",
    "a point 10 cm to the left of the chair",
    "a point 20 cm above the green container",
    "anywhere within 15 cm of the yellow cup",
    "a point on the back side of the window",
    "a point 30 cm inside the top drawer",
    "a point 4 cm to the right of and 10 cm above the book",
    "a point 10 cm outside the robot arm",
    "a point at the midpoint between two blocks",
    "a point 5 cm above the table and 3 cm to the left of the red block",
    "a point 25 cm in front of [10, 20, 30]",
    "a point on the front right corner of the chair",
    "anywhere within 20 cm of the green door",
    "a point 8 cm below and 6 cm behind the blue window",
    "a point at the edge of the yellow table",
    "a point 15 cm away from the black cup",
    "a point 10 cm to the right of and 5 cm above [45, 49, 66]"
]

distances = [5, 25, 50]
directions = ["in front of", "behind", "to the right of", "above", "inside", "on top of"]
objects = ["table", "container", "door", "book"]
colors = ["red", ]

templates = [
    "a point {distance} cm {direction} the {color} {object}",
    "a point at the center of the {color} {object}",
    "anywhere within {distance} cm of the {color} {object}",
    "a point at the midpoint between two {object}s",
    "a point {distance} cm {direction} and {distance} cm above the {color} {object}"
]

auto_queries = []

# 遍历所有模板
for distance, direction, color, object in itertools.product(distances, directions, colors, objects):
    query = templates[0].format(distance=distance, direction=direction, color=color, object=object)
    auto_queries.append(query)
    

all_quries = manual_queries + auto_queries

with open("test_queries_affordance_map.txt", "w") as file:
    for query in all_quries:
        file.write(f"new_query: {query}\n")
        
print(f"Successfully generate {len(all_quries)} samples, save to 'test_queries_affordance_map.txt'. ")
        