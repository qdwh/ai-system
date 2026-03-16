
import re

def extract_python_code(text):

    # capture all <jupyter_code> blocks
    matches = re.findall(r"<jupyter_code>(.*?)<jupyter_", text, re.DOTALL)

    if matches:
        return "\n".join(matches)

    return text


def run_code(code):

    try:

        cleaned_code = extract_python_code(code)

        print("\n--- Cleaned Python Code ---\n")
        print(cleaned_code)

        exec(cleaned_code, globals())

        return "Success"

    except Exception as e:

        return str(e)
