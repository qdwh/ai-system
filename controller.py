from llm_interface import generate_code
from executor import run_code
from debugger_agent import fix_code

MAX_ATTEMPTS = 5

def run_task(task):

    print("Generating initial code...")

    code = generate_code(task)

    for attempt in range(MAX_ATTEMPTS):

        print(f"\n--- Attempt {attempt+1} ---")

        result = run_code(code)

        if result == "Success":

            print("\nCode executed successfully!")
            return code

        else:

            print("Error detected. Sending to debugger...")

            code = fix_code(code, result)

    print("Max attempts reached.")

    return code
