from google import genai
from google.genai.errors import APIError
from pydantic import ValidationError

from models import ToolDecision
from prompts import build_tool_decision_prompt
from config import MODEL_NAME


client = genai.Client()


def generate_tool_decision(user_message: str) -> ToolDecision:
    prompt = build_tool_decision_prompt(user_message)

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_json_schema": ToolDecision.model_json_schema(),
            },
        )
    except APIError as err:
        raise RuntimeError(f"Gemini API error: {err}") from err

    try:
        decision = ToolDecision.model_validate_json(response.text)
    except ValidationError as err:
        raise ValueError(f"Invalid tool schema: {err}") from err

    return decision