import re

with open("prompts\get_affordance_map_promt.txt", "r") as file:
    affordance_map_prompt_content = file.read()

prompts = {
    "base": 
        f"""
            You are a coding assistant for the VoxPoser framework, tasked with generating Python code to create 3D affordance maps based on natural language queries. Below is a set of example queries and their corresponding Python code from `get_affordance_map_prompt.txt`. Your job is to:
            1. Generate Python code for a new query using the provided tools (numpy, parse_query_obj, get_empty_affordance_map, set_voxel_by_radius, cm2index).
            2. Explicitly state which example from the context you referenced to generate the code.

            Here are the examples:
            {affordance_map_prompt_content}

            New query: "{{new_query}}"
            Please provide:
            - The generated Python code.
            - A clear explanation of which example from the context you referenced and why.
        """,
    "enhanced_prompt": 
        f"""
            You are an advanced reasoning assistant for the VoxPoser framework, specializing in generating Python code for 3D affordance maps based on natural language queries. Below is a set of example queries and their corresponding Python code from `get_affordance_map_prompt.txt`. Your task is to:
            1. Generate accurate Python code for a new query using the provided tools (numpy, parse_query_obj, get_empty_affordance_map, set_voxel_by_radius, cm2index).
            2. Analyze the examples and explicitly identify which one you referenced to generate the code, explaining your reasoning based on the query's spatial relationship and the example's structure.

            Here are the examples:
            {affordance_map_prompt_content}

            New query: "{{new_query}}"
            Please provide:
            - The generated Python code in a code block.
            - A detailed explanation in a separate section, stating which example you referenced, why it was chosen, and how it applies to this query.
            """,
    "cot_prompt": 
        f"""
            You are a coding assistant for the VoxPoser framework, tasked with generating Python code for 3D affordance maps based on natural language queries. Below is a set of example queries and their corresponding Python code from `get_affordance_map_prompt.txt`. Your job is to:
            1. Generate Python code for a new query using the provided tools (numpy, parse_query_obj, get_empty_affordance_map, set_voxel_by_radius, cm2index).
            2. Think step-by-step to determine which example from the context you will reference, and explain your reasoning clearly.
            3. Output the code and the reasoning process, including which example you referenced.
            
            Here are the examples:
            {affordance_map_prompt_content}

            New query: "{{new_query}}"
            Please provide your response in the following format:
            - Step-by-step reasoning: Explain how you analyze the query and choose an example.
            - Generated Python code: In a code block.
            - Referenced example: State the specific example you used and why.

            Think step-by-step before generating the code.
        """
}