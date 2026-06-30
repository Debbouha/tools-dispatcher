from models import ToolDecision
from dispatcher import dispatch_tool


decision = ToolDecision(
    tool_name="calculate_total_price",
    confidence="high",
    reason="User asks to calculate a cart total.",
    arguments={
        "currency": "EUR",
        "items": [
            {"name": "apple", "unit_price": 2.0, "quantity": 3},
            {"name": "banana", "unit_price": 1.5, "quantity": 2},
        ],
    },
    needs_clarification=False,
    clarification_question=None,
)

result = dispatch_tool(decision)

print(result.model_dump_json(indent=2))

decision = ToolDecision(
    tool_name="convert_units",
    confidence="high",
    reason="User asks to convert kilometers to meters.",
    arguments={
        "value": 2.5,
        "from_unit": "km",
        "to_unit": "m",
    },
    needs_clarification=False,
    clarification_question=None,
)

result = dispatch_tool(decision)

print(result.model_dump_json(indent=2))

decision = ToolDecision(
    tool_name="create_todo",
    confidence="high",
    reason="User asks to create a todo.",
    arguments={
        "title": "Finish tools dispatcher lab",
        "due_date": "2026-06-30",
        "priority": "high",
    },
    needs_clarification=False,
    clarification_question=None,
)

result = dispatch_tool(decision)

print(result.model_dump_json(indent=2))
decision = ToolDecision(
    tool_name="create_todo",
    confidence="medium",
    reason="User wants to create a todo but the title is missing.",
    arguments={},
    needs_clarification=True,
    clarification_question="What todo would you like me to create?",
)

try:
    result = dispatch_tool(decision)
    print(result.model_dump_json(indent=2))
except ValueError as err:
    print(f"STOP: {err}")

