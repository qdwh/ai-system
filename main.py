
from llm_interface import ask_llm
from executor import run_code
from file_manager import save_file

task = "Write a Python function that calculates the factorial of a number."

print("Sending task to LLM...")

generated_code = ask_llm(task)

print("\nGenerated Code:\n")
print(generated_code)

save_file("generated_code.py", generated_code)

print("\nRunning generated code...")

result = run_code(generated_code)

print("\nExecution Result:", result)
