import sys

from llm_client import generate_tool_decision
from display import display_decision, display_error, display_result
from dispatcher import dispatch_tool


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python main.py samples/<request.txt>")
        return 1

    file_name = sys.argv[1]

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            user_msg = file.read()
    except FileNotFoundError:
        print(f"Error: file not found: {file_name}")
        return 1

    try:
        decision = generate_tool_decision(user_msg)
    except (RuntimeError, ValueError) as err:
        display_error(err)
        return 1

    display_decision(decision)

    try:
        tool_output = dispatch_tool(decision)
    except ValueError as err:
        display_error(err)
        return 1

    display_result(tool_output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())