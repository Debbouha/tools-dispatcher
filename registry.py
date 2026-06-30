from models import (
    CalculateTotalPriceInput,
    CalculateTotalPriceOutput,
    ConvertUnitsInput,
    ConvertUnitsOutput,
    CreateTodoInput,
    CreateTodoOutput,
)
from tools import (
    calculate_total_price,
    convert_units,
    create_todo,
)


TOOL_REGISTRY = {
    "calculate_total_price": {
        "input_model": CalculateTotalPriceInput,
        "output_model": CalculateTotalPriceOutput,
        "function": calculate_total_price,
    },
    "convert_units": {
        "input_model": ConvertUnitsInput,
        "output_model": ConvertUnitsOutput,
        "function": convert_units,
    },
    "create_todo": {
        "input_model": CreateTodoInput,
        "output_model": CreateTodoOutput,
        "function": create_todo,
    },
}