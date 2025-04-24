from openai import OpenAI
from dotenv import load_dotenv
import os
import re


def init_example_counter(promt_file_path):
    example_counter = {}
    with open(promt_file_path, "r") as file:
        content = file.read()
        queries = re.findall(r'# Query: (.*?)\n', content) # ?表示非贪婪模式，.匹配除了换行符
        
        for query in queries:
            example_counter[query.strip()] = 0
            
    return example_counter

prompt_file_path = "prompts\get_affordance_map_promt.txt"

# 初始化上下文example计数器
example_counter = init_example_counter(prompt_file_path)
print(example_counter)
print(len(example_counter))

"""
group() 方法：
match.group(n) 返回正则表达式中第 n 个捕获组的内容。
match.group(0) 返回整个匹配的字符串。
match.group(1) 返回第一个捕获组的内容（从 1 开始计数）
"""