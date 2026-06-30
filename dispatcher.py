from pydantic import ValidationError, BaseModel

from models import ToolDecision
from registry import TOOL_REGISTRY


def dispatch_tool(decision: ToolDecision) -> BaseModel:
    tool_name = decision.tool_name

    if decision.needs_clarification:
        raise ValueError(decision.clarification_question or "Clarification needed")
    if decision.confidence == "low":
        raise ValueError(f"Low confidence: {decision.reason}")
    if tool_name == "unknown":
        raise ValueError(f"Unknown tool: {decision.reason}")
    if tool_name not in TOOL_REGISTRY:
        raise ValueError(f"Tool not registered: {tool_name}")

    tool = TOOL_REGISTRY[tool_name]

    try:
        tool_input = tool["input_model"].model_validate(decision.arguments)
    except ValidationError as err:
        raise ValueError(f"Invalid tool arguments: {err}") from err

    raw_tool_output = tool["function"](tool_input)

    try:
        tool_output = tool["output_model"].model_validate(raw_tool_output)
    except ValidationError as err:
        raise ValueError(f"Invalid tool output: {err}") from err

    return tool_output