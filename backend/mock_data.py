"""Datos simulados para la demo Sales Lead Assistant.

Este archivo no usa FastAPI ni OpenAI. Solo define datos fijos y reglas
simples para que la demo pueda funcionar en modo simulado.
"""

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


def get_style_ids():
    style_ids = []

    for style in RESPONSE_STYLES:
        style_ids.append(style["id"])

    return style_ids


def get_message_ids():
    message_ids = []

    for message in LEAD_MESSAGES:
        message_ids.append(message["id"])

    return message_ids


def find_message(message_id):
    for message in LEAD_MESSAGES:
        if message["id"] == message_id:
            return message

    raise ValueError("Mensaje desconocido: " + message_id)


def get_allowed_style_ids(message_id):
    message = find_message(message_id)
    return message["allowed_style_ids"]


def get_disabled_style_ids(message_id):
    allowed_style_ids = get_allowed_style_ids(message_id)
    disabled_style_ids = []

    for style in RESPONSE_STYLES:
        style_id = style["id"]

        if style_id not in allowed_style_ids:
            disabled_style_ids.append(style_id)

    return disabled_style_ids


def is_style_allowed(message_id, style_id):
    allowed_style_ids = get_allowed_style_ids(message_id)
    return style_id in allowed_style_ids


def has_duplicate_values(values):
    seen_values = []

    for value in values:
        if value in seen_values:
            return True

        seen_values.append(value)

    return False


def validate_mock_data():
    message_ids = get_message_ids()
    style_ids = get_style_ids()

    if has_duplicate_values(message_ids):
        raise ValueError("Los ids de mensajes no se pueden repetir")

    if has_duplicate_values(style_ids):
        raise ValueError("Los ids de estilos no se pueden repetir")

    if len(LEAD_MESSAGES) != 5:
        raise ValueError("La demo debe empezar con cinco mensajes")

    if len(RESPONSE_STYLES) != 6:
        raise ValueError("La demo debe empezar con seis estilos de respuesta")

    for message in LEAD_MESSAGES:
        allowed_style_ids = message["allowed_style_ids"]

        if len(allowed_style_ids) == 0:
            raise ValueError("El mensaje no tiene estilos permitidos")

        for style_id in allowed_style_ids:
            if style_id not in style_ids:
                raise ValueError("El mensaje usa un estilo que no existe")

    expected_rules = [
        {
            "message_id": "price_question",
            "allowed": ["friendly", "direct", "consultative", "ask_more_data"],
            "disabled": ["schedule_call", "handle_objection"],
        },
        {
            "message_id": "low_budget",
            "allowed": [
                "friendly",
                "consultative",
                "ask_more_data",
                "handle_objection",
            ],
            "disabled": ["direct", "schedule_call"],
        },
        {
            "message_id": "demo_request",
            "allowed": ["friendly", "direct", "schedule_call"],
            "disabled": ["consultative", "ask_more_data", "handle_objection"],
        },
    ]

    for rule in expected_rules:
        message_id = rule["message_id"]

        if get_allowed_style_ids(message_id) != rule["allowed"]:
            raise ValueError("Cambiaron los estilos permitidos de " + message_id)

        if get_disabled_style_ids(message_id) != rule["disabled"]:
            raise ValueError("Cambiaron los estilos bloqueados de " + message_id)


def print_mock_data_summary():
    validate_mock_data()
    print("Mensajes simulados:", len(LEAD_MESSAGES))
    print("Estilos de respuesta:", len(RESPONSE_STYLES))
    print("Datos simulados validos")


if __name__ == "__main__":
    print_mock_data_summary()
