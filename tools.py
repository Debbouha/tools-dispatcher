import uuid

from models import (
    CalculateTotalPriceInput,
    CalculateTotalPriceOutput,
    ConvertUnitsInput,
    ConvertUnitsOutput,
    CreateTodoInput,
    CreateTodoOutput,
    LineItem,
)


CONVERSION_FACTORS = {
    ("km", "m"): 1000,
    ("m", "km"): 0.001,
    ("kg", "g"): 1000,
    ("g", "kg"): 0.001,
}


def calculate_total_price(data: CalculateTotalPriceInput) -> CalculateTotalPriceOutput:
    total: float = 0.0
    line_items: list[LineItem] = []

    for item in data.items:
        subtotal = item.unit_price * item.quantity
        line_item = LineItem(
            name=item.name,
            subtotal=subtotal,
        )
        line_items.append(line_item)
        total += subtotal

    return CalculateTotalPriceOutput(
        total=total,
        currency=data.currency,
        line_items=line_items,
    )


def convert_units(data: ConvertUnitsInput) -> ConvertUnitsOutput:
    key = (data.from_unit, data.to_unit)

    if key not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported conversion: {data.from_unit} -> {data.to_unit}")

    factor = CONVERSION_FACTORS[key]

    return ConvertUnitsOutput(
        converted_value=data.value * factor,
        from_unit=data.from_unit,
        to_unit=data.to_unit,
    )


def create_todo(data: CreateTodoInput) -> CreateTodoOutput:
    return CreateTodoOutput(
        created=True,
        todo_id=str(uuid.uuid4()),
        title=data.title,
    )