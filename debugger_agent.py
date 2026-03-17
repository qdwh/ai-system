from llm_interface import generate_code

def fix_code(code, error):

    prompt = f"""
You are a Python debugging AI.

The following code produced an error.

CODE:
{code}

ERROR:
{error}

Fix the code. Output ONLY the corrected Python code.
"""

    fixed_code = generate_code(prompt)

    return fixed_code
