from openai import OpenAI
from dotenv import load_dotenv
import os
import re
from prompt_templates import prompts

# ================= 初始化配置 =================
base_url = "https://api.deepseek.com"
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(api_key = api_key, base_url = base_url)
model = "deepseek-chat"
model_r = "deepseek-reasoner"

# ================= 文件处理 =================
def read_queries(file_path):
    """"从文件中读取所有查询"""
    new_queries = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                if line.startswith("new_query:"):
                    query = line.split(":", 1)[1].strip()
                    new_queries.append(query)
        return new_queries       
    except Exception as e:
        print(f"文件读取失败: {str(e)}")
        return []

# ================= 统计系统 =================
class ExampleTracker:
    def __init__(self, prompt_file):
        self.counter = {}
        self._init_counter(prompt_file)
        
    def _init_counter(self, file_path):
        """解析prompt文件中的示例query初始化计数器"""
        with open(file_path, "r") as file:
            content = file.read()
            queries = re.findall(r'# Query: (.*?)\n', content)
            for query in queries:
                self.counter[query.strip()] = 0

    def update(self, response_text):
        """更新统计"""
        references = re.findall(r'# Query: (.*?)\n', response_text)
        for ref in references:
            if ref in self.counter:
                self.counter[ref] += 1
            else:
                print(f"不存在对应地上下文: {ref}")
        
    def get_stats(self):
        """获取统计结果"""
        print("\n============统计结果============")
        for example, count in sorted(self.counter.items(), key = lambda x : -x[1]):
            print(f"{example}: {count}")
    
# ================= 核心处理逻辑 =================
def process_single_query(new_query, tracker, prompt_type):
    """处理单个查询"""
    prompt_template = prompts[prompt_type]
    full_prompt = prompt_template.replace("{new_query}", new_query)

    # API调用
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": full_prompt},
            ],
            stream=False,
            n=1
        )
        response_text = response.choices[0].message.content
        tracker.update(response_text)
        print(f"查询: {new_query}")
        print(f"响应: {response_text}\n")
    except Exception as e:
        print(f"API 调用失败: {str(e)}")
        response_text = "处理失败"
    
    print(f"查询: {new_query}")
    print(f"响应: {response_text}\n")
    
    # 解析响应
    response_text = response.choices[0].message.content
    tracker.update(response_text)
    
# ================= 主执行流程 =================
if __name__ == "__main__":
    # 初始化系统
    tracker = ExampleTracker("prompts\get_affordance_map_promt.txt")
    
    # 读取所有查询
    new_queries = read_queries("test_queries_affordance_map.txt")
    
    print(f"开始批量处理 {len(new_queries)} 个查询...\n")
    
    for idx, new_query in enumerate(new_queries, 1):
        print(f"正在处理查询 ({idx}/{len(new_queries)})")
        process_single_query(new_query, tracker, prompt_type = "base")
          
    # 获取最终统计
    tracker.get_stats()