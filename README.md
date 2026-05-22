# Sales Lead Assistant

Sales Lead Assistant es una demo web que simula un asistente comercial para analizar mensajes de leads y generar respuestas de venta en español.

La app trabaja con mensajes predeterminados, analiza la intención del lead, muestra un brief comercial, expone un JSON técnico y habilita solo los estilos de respuesta que aplican al mensaje elegido.

## Qué hace

- Muestra mensajes predeterminados de clientes.
- Analiza el mensaje seleccionado.
- Devuelve un brief comercial para ventas.
- Muestra un JSON técnico con intención, prioridad, datos faltantes y siguiente paso.
- Habilita o bloquea estilos de respuesta según el contexto.
- Genera una respuesta comercial en español.
- Funciona en modo simulado por defecto.

## Stack

- Backend: FastAPI
- Frontend: HTML, CSS y JavaScript
- Modo por defecto: mock mode

## Cómo correr el backend

```bash
source .venv/bin/activate
uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

Probar salud del backend:

```bash
curl http://127.0.0.1:8000/health
```

## Cómo correr el frontend

En otra terminal:

```bash
python3 -m http.server 4173 --directory frontend
```

Abrir:

```text
http://127.0.0.1:4173
```

## Endpoints principales

```text
GET /health
GET /mensajes
GET /estilos
GET /analizar/{id_mensaje}
GET /responder/{id_mensaje}/{id_estilo}
```

## Seguridad y costos

La demo pública usa mock mode por defecto. No necesita API keys reales y no consume créditos de OpenAI.

El modo OpenAI puede agregarse más adelante usando variables de entorno locales. Las claves reales no deben guardarse en el repositorio.

## Decisiones de producto

- No hay input libre ilimitado en la demo pública.
- Los estilos de respuesta inválidos se bloquean en frontend y también se validan en backend.
- La interfaz y las respuestas están en español.
- El JSON técnico queda visible para mostrar cómo responde la API.
