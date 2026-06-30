from typing import Literal

from pydantic import BaseModel


class ToolDecision(BaseModel):
    tool_name: Literal[
        "calculate_total_price",
        "convert_units",
        "create_todo",
        "unknown",
    ]
    confidence: Literal["low", "medium", "high"]
    reason: str
    arguments: dict[str, object]
    needs_clarification: bool
    clarification_question: str | None


class PriceItem(BaseModel):
    name: str
    unit_price: float
    quantity: int


class LineItem(BaseModel):
    name: str
    subtotal: float


class CalculateTotalPriceInput(BaseModel):
    items: list[PriceItem]
    currency: str


class CalculateTotalPriceOutput(BaseModel):
    total: float
    currency: str
    line_items: list[LineItem]


class ConvertUnitsInput(BaseModel):
    value: float
    from_unit: str
    to_unit: str


class ConvertUnitsOutput(BaseModel):
    converted_value: float
    from_unit: str
    to_unit: str


class CreateTodoInput(BaseModel):
    title: str
    due_date: str | None
    priority: Literal["low", "medium", "high", "unknown"]


class CreateTodoOutput(BaseModel):
    created: bool
    todo_id: str
    title: str