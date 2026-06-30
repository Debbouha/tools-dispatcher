# tools-dispatcher

Local tool execution pipeline using Gemini structured output and Pydantic validation.

## Overview

`tools-dispatcher` takes a user request, asks Gemini to return a structured tool decision, validates that decision with Pydantic, dispatches the request to a local Python tool, validates the tool output, and displays the result.

Gemini decides which tool should be called and with which arguments. Python owns validation, dispatching, execution, and output validation.

## Flow

```text
user request
→ Gemini ToolDecision
→ Pydantic validation
→ registry lookup
→ tool input validation
→ local tool execution
→ tool output validation
→ display result
```

## Tools

- `calculate_total_price`: computes item subtotals and total price.
- `convert_units`: converts supported units with a local conversion table.
- `create_todo`: creates a local todo object with a generated ID.
- `unknown`: handles unsupported or unclear requests.

## Project Structure

```text
tools-dispatcher/
  main.py
  models.py
  llm_client.py
  prompts.py
  tools.py
  dispatcher.py
  registry.py
  display.py
  samples/
    price_request.txt
    unit_request.txt
    todo_request.txt
    unknown_request.txt
  README.md
```

## Run

```bash
python main.py samples/price_request.txt
python main.py samples/unit_request.txt
python main.py samples/todo_request.txt
python main.py samples/unknown_request.txt
```

## Core Contract

`ToolDecision` is the structured decision returned by Gemini.

```text
tool_name
confidence
reason
arguments
needs_clarification
clarification_question
```

Each tool defines:

```text
input model
output model
local function
registry entry
```

## Dispatcher

The dispatcher validates the decision, checks whether the selected tool is registered, validates the tool arguments, executes the local function, validates the output, and returns the validated result.

## Design Notes

- Local tools only.
- No agent loop.
- No external tool execution.
- No persistent storage.
- Gemini does not execute functions.
- Python handles validation and execution.
