import os


# Configuracion de la app

APP_MODE = os.getenv("APP_MODE", "mock")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


# Funciones auxiliares

def usar_openai():
    return APP_MODE == "openai" and OPENAI_API_KEY != ""


def obtener_config_publica():
    return {
        "app_mode": APP_MODE,
        "openai_configurado": usar_openai(),
        "openai_model": OPENAI_MODEL,
    }
