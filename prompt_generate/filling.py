import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
api_key = 'sk-d63649b9f5494ba4b2a8b955ea72e85f'
base_url = "https://api.deepseek.com"
client = OpenAI(api_key=api_key, base_url=base_url)
model = "deepseek-chat"
model_r = "deepseek-resoner"

prompt_types = [
    # "composer_prompt", 
    # "get_affordance_map_prompt",
    # "get_avoidance_map_prompt",
    # "get_gripper_map_prompt",
    # "get_rotation_map_prompt",
    # "get_velocity_map_prompt",
    "parse_query_obj_prompt",
    "planner_prompt"
]

os.makedirs('../prompts_100_filled', exist_ok=True)

for prompt in prompt_types:
    inst_path = f"../prompts/{prompt}.txt"
    query_path = f'../prompts_100/{prompt}.txt'
    
    with open(inst_path, 'r') as f:
        instruction = f.read().strip()

    with open(query_path, 'r') as f:
        input_queries = [line.strip() for line in f if line.strip()]

    responses = []

    for query in input_queries:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": instruction},
                    {"role": "user", "content": f'Based on the prompt above, please provide the response: {query}'},
                ],
                stream=False,
                n=1
            )
            response_text=response.choices[0].message.content 
            response_text = '# ' + query + "\n" + response_text + "\n\n"
            response_text += "\n"
            responses.append(response_text.strip())
            print(f"Processed: {query}")
        except Exception as e:
            print(f"Error processing prompt: {prompt}: {e}")
            
    output_path = f'../prompts_100_filled/{prompt}.txt'
    with open(output_path, 'w') as f:
        for resp in responses:
            f.write(resp + '\n')
        
    print(f"All prompts have been processed and saved to {output_path}")



