"""Mock data for the Sales Lead Assistant demo.

This file defines the fixed messages, response styles, and style rules used by
the public demo. It has no external dependencies.
"""

from __future__ import annotations


RESPONSE_STYLES = [
    {"id": "friendly", "label": "Amable"},
    {"id": "direct", "label": "Directa"},
    {"id": "consultative", "label": "Consultiva"},
    {"id": "ask_more_data", "label": "Pedir más datos"},
    {"id": "schedule_call", "label": "Agendar llamada"},
    {"id": "handle_objection", "label": "Manejar objeción"},
]


LEAD_MESSAGES = [
    {
        "id": "price_question",
        "text": "Hola, ¿cuánto cuesta este servicio?",
        "allowed_style_ids": [
            "friendly",
            "direct",
            "consultative",
            "ask_more_data",
        ],
    },
    {
        "id": "urgent_deadline",
        "text": "Necesito tener algo funcionando para la semana que viene. ¿Se puede?",
        "allowed_style_ids": [
            "friendly",
            "direct",
            "consultative",
            "ask_more_data",
            "schedule_call",
        ],
    },
    {
        "id": "comparing_providers",
        "text": "Estoy comparando varios proveedores antes de decidir.",
        "allowed_style_ids": [
            "friendly",
            "consultative",
            "ask_more_data",
            "handle_objection",
        ],
    },
    {
        "id": "low_budget",
        "text": "Me interesa, pero tengo poco presupuesto.",
        "allowed_style_ids": [
            "friendly",
            "consultative",
            "ask_more_data",
            "handle_objection",
        ],
    },
    {
        "id": "demo_request",
        "text": "¿Podemos coordinar una llamada o demo rápida?",
        "allowed_style_ids": [
            "friendly",
            "direct",
            "schedule_call",
        ],
    },
]


def get_style_ids() -> set[str]:
    return {style["id"] for style in RESPONSE_STYLES}


def get_message_ids() -> set[str]:
    return {message["id"] for message in LEAD_MESSAGES}


def get_allowed_style_ids(message_id: str) -> set[str]:
    for message in LEAD_MESSAGES:
        if message["id"] == message_id:
            return set(message["allowed_style_ids"])

    raise ValueError(f"Unknown message id: {message_id}")


def get_disabled_style_ids(message_id: str) -> set[str]:
    return get_style_ids() - get_allowed_style_ids(message_id)


def is_style_allowed(message_id: str, style_id: str) -> bool:
    return style_id in get_allowed_style_ids(message_id)


def validate_mock_data() -> None:
    message_ids = get_message_ids()
    style_ids = get_style_ids()

    if len(message_ids) != len(LEAD_MESSAGES):
        raise ValueError("Message ids must be unique")

    if len(style_ids) != len(RESPONSE_STYLES):
        raise ValueError("Style ids must be unique")

    if len(LEAD_MESSAGES) != 5:
        raise ValueError("The demo must start with five lead messages")

    if len(RESPONSE_STYLES) != 6:
        raise ValueError("The demo must start with six response styles")

    for message in LEAD_MESSAGES:
        allowed_style_ids = set(message["allowed_style_ids"])

        if not allowed_style_ids:
            raise ValueError(f"Message {message['id']} has no allowed styles")

        unknown_style_ids = allowed_style_ids - style_ids
        if unknown_style_ids:
            raise ValueError(
                f"Message {message['id']} references unknown styles: "
                f"{sorted(unknown_style_ids)}"
            )

    expected_rules = {
        "price_question": {
            "allowed": {"friendly", "direct", "consultative", "ask_more_data"},
            "disabled": {"handle_objection", "schedule_call"},
        },
        "low_budget": {
            "allowed": {
                "friendly",
                "consultative",
                "ask_more_data",
                "handle_objection",
            },
            "disabled": {"direct", "schedule_call"},
        },
        "demo_request": {
            "allowed": {"friendly", "direct", "schedule_call"},
            "disabled": {"consultative", "ask_more_data", "handle_objection"},
        },
    }

    for message_id, expected in expected_rules.items():
        if get_allowed_style_ids(message_id) != expected["allowed"]:
            raise ValueError(f"Allowed styles changed for {message_id}")

        if get_disabled_style_ids(message_id) != expected["disabled"]:
            raise ValueError(f"Disabled styles changed for {message_id}")


def print_mock_data_summary() -> None:
    validate_mock_data()
    print(f"Lead messages: {len(LEAD_MESSAGES)}")
    print(f"Response styles: {len(RESPONSE_STYLES)}")
    print("Mock data is valid")


if __name__ == "__main__":
    print_mock_data_summary()
