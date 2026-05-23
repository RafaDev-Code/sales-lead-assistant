from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.config import obtener_config_publica, usar_openai
from backend.mock_data import (
    analizar_mensaje,
    buscar_estilo,
    buscar_mensaje,
    estilo_esta_permitido,
    generar_respuesta,
    LEAD_MESSAGES,
    RESPONSE_STYLES,
    obtener_ids_de_estilos,
    obtener_ids_de_mensajes,
)
from backend.openai_client import generar_respuesta_openai


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:4173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Endpoints

@app.get("/health")
def verificar_salud():
    return {"status": "ok"}


@app.get("/config")
def ver_configuracion():
    return obtener_config_publica()


@app.get("/mensajes")
def listar_mensajes():
    return LEAD_MESSAGES


@app.get("/estilos")
def listar_estilos():
    return RESPONSE_STYLES


@app.get("/analizar/{id_mensaje}")
def analizar_lead(id_mensaje):
    if id_mensaje not in obtener_ids_de_mensajes():
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")

    return analizar_mensaje(id_mensaje)


@app.get("/responder/{id_mensaje}/{id_estilo}")
def responder_lead(id_mensaje, id_estilo):
    if id_mensaje not in obtener_ids_de_mensajes():
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")

    if id_estilo not in obtener_ids_de_estilos():
        raise HTTPException(status_code=404, detail="Estilo no encontrado")

    if not estilo_esta_permitido(id_mensaje, id_estilo):
        raise HTTPException(
            status_code=400,
            detail="Este estilo no aplica al mensaje elegido",
        )

    if usar_openai():
        mensaje = buscar_mensaje(id_mensaje)
        estilo = buscar_estilo(id_estilo)
        respuesta = generar_respuesta_openai(mensaje["text"], estilo["label"])

        return {
            "id_mensaje": id_mensaje,
            "id_estilo": id_estilo,
            "mensaje": mensaje["text"],
            "respuesta": respuesta,
        }

    return generar_respuesta(id_mensaje, id_estilo)
