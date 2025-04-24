from prompt import prompt4
from openai import OpenAI
from dotenv import load_dotenv
import os
# ================= 初始化配置 =================
base_url = "https://api.deepseek.com"
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(api_key = api_key, base_url = base_url)
model = "deepseek-chat"
model_r = "deepseek-reasoner"

# ================= 读取上下文 =================
def read_context(file_path):
    """"读取完整文件"""
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content      
    except Exception as e:
        print(f"文件读取失败: {str(e)}")
        return 
    
# ================= 核心处理逻辑 =================
def process_single_query(context):
    """处理单个查询"""

    # API调用
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt4},
                {"role": "user", "content": context},
            ],
            stream=False,
            n=1
        )
        response_text = response.choices[0].message.content
        print(f"响应: {response_text}\n")
    except Exception as e:
        print(f"API 调用失败: {str(e)}")
        response_text = "处理失败"
    
    
# ================= 主执行流程 =================
if __name__ == "__main__":

    context_paths = ["..\prompts\composer_prompt.txt", 
                    "..\prompts\get_affordance_map_promt.txt",
                    "..\prompts\get_avoidance_map_prompt.txt", 
                    "..\prompts\get_gripper_map_prompt.txt", 
                    "..\prompts\get_rotation_map_prompt.txt",
                    "..\prompts\get_velocity_map_prompt.txt",
                    "..\prompts\parse_query_obj_prompt.txt",
                    "..\prompts\planner_prompt.txt"
                    ]

    for context_path in context_paths:
        context = read_context(context_path)
        
        process_single_query(context)
    
