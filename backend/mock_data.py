"""Datos simulados para la demo Sales Lead Assistant.

Este archivo no usa FastAPI ni OpenAI. Solo define datos fijos y reglas
simples para que la demo pueda funcionar en modo simulado.
"""

# Datos simulados

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
            "ask_more_data",
        ],
    },
    {
        "id": "urgent_deadline",
        "text": "Necesito tener algo funcionando para la semana que viene. ¿Se puede?",
        "allowed_style_ids": [
            "direct",
            "consultative",
            "schedule_call",
        ],
    },
    {
        "id": "comparing_providers",
        "text": "Estoy comparando varios proveedores antes de decidir.",
        "allowed_style_ids": [
            "friendly",
            "consultative",
            "handle_objection",
        ],
    },
    {
        "id": "low_budget",
        "text": "Me interesa, pero tengo poco presupuesto.",
        "allowed_style_ids": [
            "friendly",
            "consultative",
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


ANALISIS_SIMULADOS = [
    {
        "id_mensaje": "price_question",
        "brief": "El lead quiere entender el precio antes de avanzar.",
        "intencion": "consultar precio",
        "prioridad": "media",
        "datos_faltantes": ["alcance del servicio", "plazo esperado"],
        "siguiente_paso": "responder claro y pedir datos basicos para cotizar mejor",
    },
    {
        "id_mensaje": "urgent_deadline",
        "brief": "El lead tiene urgencia y necesita saber si se puede llegar a tiempo.",
        "intencion": "resolver una necesidad urgente",
        "prioridad": "alta",
        "datos_faltantes": ["alcance minimo", "fecha exacta de entrega"],
        "siguiente_paso": "validar alcance y proponer una llamada corta",
    },
    {
        "id_mensaje": "comparing_providers",
        "brief": "El lead esta evaluando opciones y todavia no tomo una decision.",
        "intencion": "comparar proveedores",
        "prioridad": "media",
        "datos_faltantes": ["criterios de decision", "proveedores comparados"],
        "siguiente_paso": "diferenciar la propuesta y preguntar que esta priorizando",
    },
    {
        "id_mensaje": "low_budget",
        "brief": "El lead esta interesado, pero tiene una objecion de presupuesto.",
        "intencion": "validar si el presupuesto alcanza",
        "prioridad": "media",
        "datos_faltantes": ["presupuesto aproximado", "funcionalidad indispensable"],
        "siguiente_paso": "manejar la objecion y proponer un alcance inicial mas chico",
    },
    {
        "id_mensaje": "demo_request",
        "brief": "El lead ya quiere coordinar una llamada o demo.",
        "intencion": "agendar una conversacion",
        "prioridad": "alta",
        "datos_faltantes": ["disponibilidad horaria", "objetivo de la llamada"],
        "siguiente_paso": "proponer horarios concretos para coordinar",
    },
]


RESPUESTAS_SIMULADAS = [
    {
        "id_mensaje": "price_question",
        "id_estilo": "friendly",
        "respuesta": "Hola, gracias por escribir. El precio depende del alcance que necesites. Si me contás qué querés resolver y para cuándo, puedo orientarte mejor.",
    },
    {
        "id_mensaje": "price_question",
        "id_estilo": "direct",
        "respuesta": "Hola. Para pasarte un precio necesito saber el alcance del servicio y el plazo esperado. Con esos datos puedo darte una estimación más clara.",
    },
    {
        "id_mensaje": "price_question",
        "id_estilo": "ask_more_data",
        "respuesta": "Hola. Para cotizar bien, necesito algunos datos: qué necesitás exactamente, para cuándo y si ya tenés alguna referencia de presupuesto.",
    },
    {
        "id_mensaje": "urgent_deadline",
        "id_estilo": "direct",
        "respuesta": "Sí, puede ser posible, pero primero habría que definir el alcance mínimo para llegar bien a la semana que viene.",
    },
    {
        "id_mensaje": "urgent_deadline",
        "id_estilo": "consultative",
        "respuesta": "Podemos evaluarlo. Lo importante es separar qué tiene que estar listo sí o sí y qué puede quedar para una segunda etapa.",
    },
    {
        "id_mensaje": "urgent_deadline",
        "id_estilo": "schedule_call",
        "respuesta": "Coordinemos una llamada breve para revisar alcance y tiempos. Si te sirve, puedo proponerte dos horarios para hoy o mañana.",
    },
    {
        "id_mensaje": "comparing_providers",
        "id_estilo": "friendly",
        "respuesta": "Perfecto, tiene sentido comparar antes de decidir. Si querés, te puedo contar en qué se diferencia mi propuesta y qué incluye.",
    },
    {
        "id_mensaje": "comparing_providers",
        "id_estilo": "consultative",
        "respuesta": "Para ayudarte a comparar mejor, te preguntaría qué estás priorizando: precio, velocidad, soporte, calidad o experiencia previa.",
    },
    {
        "id_mensaje": "comparing_providers",
        "id_estilo": "handle_objection",
        "respuesta": "Entiendo que estés comparando. La clave es mirar no solo el precio, sino también el alcance, los tiempos y el acompañamiento incluido.",
    },
    {
        "id_mensaje": "low_budget",
        "id_estilo": "friendly",
        "respuesta": "Gracias por contármelo. Podemos buscar una opción más simple para empezar y dejar mejoras para una segunda etapa.",
    },
    {
        "id_mensaje": "low_budget",
        "id_estilo": "consultative",
        "respuesta": "Podemos adaptarlo. Primero definiría qué es indispensable para que tengas valor rápido sin gastar de más.",
    },
    {
        "id_mensaje": "low_budget",
        "id_estilo": "handle_objection",
        "respuesta": "Entiendo la limitación de presupuesto. Una alternativa es empezar con un alcance mínimo que resuelva lo más importante y escalar después.",
    },
    {
        "id_mensaje": "demo_request",
        "id_estilo": "friendly",
        "respuesta": "Sí, claro. Podemos coordinar una llamada o demo rápida. Decime qué horarios te quedan cómodos y lo organizamos.",
    },
    {
        "id_mensaje": "demo_request",
        "id_estilo": "direct",
        "respuesta": "Sí. Pasame dos horarios posibles y coordinamos una llamada breve para revisar tu caso.",
    },
    {
        "id_mensaje": "demo_request",
        "id_estilo": "schedule_call",
        "respuesta": "Coordinemos una demo rápida. Te propongo una llamada de 20 minutos para entender tu necesidad y mostrarte cómo sería el flujo.",
    },
]


# Funciones auxiliares

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


def buscar_analisis(id_mensaje):
    for analisis in ANALISIS_SIMULADOS:
        if analisis["id_mensaje"] == id_mensaje:
            return analisis

    raise ValueError("Analisis desconocido: " + id_mensaje)


def buscar_respuesta(id_mensaje, id_estilo):
    for respuesta in RESPUESTAS_SIMULADAS:
        if respuesta["id_mensaje"] == id_mensaje and respuesta["id_estilo"] == id_estilo:
            return respuesta

    raise ValueError("Respuesta desconocida")


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


# Funciones principales

def analizar_mensaje(id_mensaje):
    mensaje = buscar_mensaje(id_mensaje)
    analisis = buscar_analisis(id_mensaje)

    return {
        "id_mensaje": mensaje["id"],
        "mensaje": mensaje["text"],
        "brief": analisis["brief"],
        "json_tecnico": {
            "intencion": analisis["intencion"],
            "prioridad": analisis["prioridad"],
            "datos_faltantes": analisis["datos_faltantes"],
            "siguiente_paso": analisis["siguiente_paso"],
            "estilos_permitidos": obtener_estilos_permitidos(id_mensaje),
            "estilos_bloqueados": obtener_estilos_bloqueados(id_mensaje),
        },
    }


def generar_respuesta(id_mensaje, id_estilo):
    mensaje = buscar_mensaje(id_mensaje)

    if not estilo_esta_permitido(id_mensaje, id_estilo):
        raise ValueError("El estilo no esta permitido para este mensaje")

    respuesta = buscar_respuesta(id_mensaje, id_estilo)

    return {
        "id_mensaje": mensaje["id"],
        "id_estilo": id_estilo,
        "mensaje": mensaje["text"],
        "respuesta": respuesta["respuesta"],
    }


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
    ids_de_analisis = []
    ids_de_respuestas = []

    for analisis in ANALISIS_SIMULADOS:
        ids_de_analisis.append(analisis["id_mensaje"])

    for respuesta in RESPUESTAS_SIMULADAS:
        ids_de_respuestas.append(respuesta["id_mensaje"] + ":" + respuesta["id_estilo"])

    if tiene_valores_repetidos(ids_de_mensajes):
        raise ValueError("Los ids de mensajes no se pueden repetir")

    if tiene_valores_repetidos(ids_de_estilos):
        raise ValueError("Los ids de estilos no se pueden repetir")

    if tiene_valores_repetidos(ids_de_analisis):
        raise ValueError("Los ids de analisis no se pueden repetir")

    if tiene_valores_repetidos(ids_de_respuestas):
        raise ValueError("Las respuestas simuladas no se pueden repetir")

    if len(LEAD_MESSAGES) != 5:
        raise ValueError("La demo debe empezar con cinco mensajes")

    if len(RESPONSE_STYLES) != 6:
        raise ValueError("La demo debe empezar con seis estilos de respuesta")

    if len(ANALISIS_SIMULADOS) != len(LEAD_MESSAGES):
        raise ValueError("Cada mensaje debe tener un analisis simulado")

    for mensaje in LEAD_MESSAGES:
        estilos_permitidos = mensaje["allowed_style_ids"]

        if len(estilos_permitidos) == 0:
            raise ValueError("El mensaje no tiene estilos permitidos")

        for id_estilo in estilos_permitidos:
            if id_estilo not in ids_de_estilos:
                raise ValueError("El mensaje usa un estilo que no existe")

    for id_analisis in ids_de_analisis:
        if id_analisis not in ids_de_mensajes:
            raise ValueError("Hay un analisis para un mensaje que no existe")

    for respuesta in RESPUESTAS_SIMULADAS:
        id_mensaje = respuesta["id_mensaje"]
        id_estilo = respuesta["id_estilo"]

        if id_mensaje not in ids_de_mensajes:
            raise ValueError("Hay una respuesta para un mensaje que no existe")

        if id_estilo not in ids_de_estilos:
            raise ValueError("Hay una respuesta con un estilo que no existe")

        if not estilo_esta_permitido(id_mensaje, id_estilo):
            raise ValueError("Hay una respuesta para un estilo no permitido")

    reglas_esperadas = [
        {
            "id_mensaje": "price_question",
            "permitidos": ["friendly", "direct", "ask_more_data"],
            "bloqueados": ["consultative", "schedule_call", "handle_objection"],
        },
        {
            "id_mensaje": "low_budget",
            "permitidos": [
                "friendly",
                "consultative",
                "handle_objection",
            ],
            "bloqueados": ["direct", "ask_more_data", "schedule_call"],
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
    print("Analisis simulados:", len(ANALISIS_SIMULADOS))
    print("Respuestas simuladas:", len(RESPUESTAS_SIMULADAS))
    print("Datos simulados validos")


if __name__ == "__main__":
    mostrar_resumen_de_datos_simulados()
