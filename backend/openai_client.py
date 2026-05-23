from openai import OpenAI

from backend.config import OPENAI_API_KEY, OPENAI_MODEL


# Cliente de OpenAI

def crear_cliente_openai():
    return OpenAI(api_key=OPENAI_API_KEY)


# Funciones principales

def generar_respuesta_openai(mensaje, estilo):
    cliente = crear_cliente_openai()

    prompt = (
        "Generá una respuesta comercial breve en español.\n"
        "Mensaje del lead: " + mensaje + "\n"
        "Estilo de respuesta: " + estilo + "\n"
        "La respuesta debe sonar natural, clara y profesional."
    )

    resultado = cliente.responses.create(
        model=OPENAI_MODEL,
        input=prompt,
    )

    return resultado.output_text
