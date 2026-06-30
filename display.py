from pydantic import BaseModel

from models import ToolDecision


def display_decision(decision: ToolDecision) -> None:
    print(decision.model_dump_json(indent=2))


def display_result(result: BaseModel) -> None:
    print(result.model_dump_json(indent=2))


def display_error(error: Exception) -> None:
    print(f"ERROR: {error}")