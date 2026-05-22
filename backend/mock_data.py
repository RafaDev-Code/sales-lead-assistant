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


def obtener_ids_de_estilos():
    ids_de_estilos = []

    for estilo in RESPONSE_STYLES:
        ids_de_estilos.append(estilo["id"])

    return ids_de_estilos


def obtener_ids_de_mensajes():
    ids_de_mensajes = []

    for mensaje in LEAD_MESSAGES:
        ids_de_mensajes.append(mensaje["id"])

    return ids_de_mensajes


def buscar_mensaje(id_mensaje):
    for mensaje in LEAD_MESSAGES:
        if mensaje["id"] == id_mensaje:
            return mensaje

    raise ValueError("Mensaje desconocido: " + id_mensaje)


def obtener_estilos_permitidos(id_mensaje):
    mensaje = buscar_mensaje(id_mensaje)
    return mensaje["allowed_style_ids"]


def obtener_estilos_bloqueados(id_mensaje):
    estilos_permitidos = obtener_estilos_permitidos(id_mensaje)
    estilos_bloqueados = []

    for estilo in RESPONSE_STYLES:
        id_estilo = estilo["id"]

        if id_estilo not in estilos_permitidos:
            estilos_bloqueados.append(id_estilo)

    return estilos_bloqueados


def estilo_esta_permitido(id_mensaje, id_estilo):
    estilos_permitidos = obtener_estilos_permitidos(id_mensaje)
    return id_estilo in estilos_permitidos


def tiene_valores_repetidos(valores):
    valores_vistos = []

    for valor in valores:
        if valor in valores_vistos:
            return True

        valores_vistos.append(valor)

    return False


def validar_datos_simulados():
    ids_de_mensajes = obtener_ids_de_mensajes()
    ids_de_estilos = obtener_ids_de_estilos()

    if tiene_valores_repetidos(ids_de_mensajes):
        raise ValueError("Los ids de mensajes no se pueden repetir")

    if tiene_valores_repetidos(ids_de_estilos):
        raise ValueError("Los ids de estilos no se pueden repetir")

    if len(LEAD_MESSAGES) != 5:
        raise ValueError("La demo debe empezar con cinco mensajes")

    if len(RESPONSE_STYLES) != 6:
        raise ValueError("La demo debe empezar con seis estilos de respuesta")

    for mensaje in LEAD_MESSAGES:
        estilos_permitidos = mensaje["allowed_style_ids"]

        if len(estilos_permitidos) == 0:
            raise ValueError("El mensaje no tiene estilos permitidos")

        for id_estilo in estilos_permitidos:
            if id_estilo not in ids_de_estilos:
                raise ValueError("El mensaje usa un estilo que no existe")

    reglas_esperadas = [
        {
            "id_mensaje": "price_question",
            "permitidos": ["friendly", "direct", "consultative", "ask_more_data"],
            "bloqueados": ["schedule_call", "handle_objection"],
        },
        {
            "id_mensaje": "low_budget",
            "permitidos": [
                "friendly",
                "consultative",
                "ask_more_data",
                "handle_objection",
            ],
            "bloqueados": ["direct", "schedule_call"],
        },
        {
            "id_mensaje": "demo_request",
            "permitidos": ["friendly", "direct", "schedule_call"],
            "bloqueados": ["consultative", "ask_more_data", "handle_objection"],
        },
    ]

    for regla in reglas_esperadas:
        id_mensaje = regla["id_mensaje"]

        if obtener_estilos_permitidos(id_mensaje) != regla["permitidos"]:
            raise ValueError("Cambiaron los estilos permitidos de " + id_mensaje)

        if obtener_estilos_bloqueados(id_mensaje) != regla["bloqueados"]:
            raise ValueError("Cambiaron los estilos bloqueados de " + id_mensaje)


def mostrar_resumen_de_datos_simulados():
    validar_datos_simulados()
    print("Mensajes simulados:", len(LEAD_MESSAGES))
    print("Estilos de respuesta:", len(RESPONSE_STYLES))
    print("Datos simulados validos")


if __name__ == "__main__":
    mostrar_resumen_de_datos_simulados()
