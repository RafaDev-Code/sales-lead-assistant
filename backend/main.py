from fastapi import FastAPI, HTTPException

from backend.mock_data import analizar_mensaje, obtener_ids_de_mensajes


app = FastAPI()


# Endpoints

@app.get("/health")
def verificar_salud():
    return {"status": "ok"}


@app.get("/analizar/{id_mensaje}")
def analizar_lead(id_mensaje):
    if id_mensaje not in obtener_ids_de_mensajes():
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")

    return analizar_mensaje(id_mensaje)
