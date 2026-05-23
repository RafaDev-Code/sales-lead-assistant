const API_URL = "http://127.0.0.1:8000";

// Estado de la pantalla

let mensajes = [];
let estilos = [];
let mensajeElegido = null;
let analisisRealizado = false;

// Elementos del HTML que vamos a modificar

const listaMensajes = document.querySelector("#lista-mensajes");
const listaEstilos = document.querySelector("#lista-estilos");
const textoMensajeElegido = document.querySelector("#mensaje-elegido");
const botonAnalizar = document.querySelector("#boton-analizar");
const botonReiniciar = document.querySelector("#boton-reiniciar");
const textoBrief = document.querySelector("#brief-comercial");
const textoJson = document.querySelector("#json-tecnico");
const textoRespuesta = document.querySelector("#respuesta-sugerida");
const textoModoApp = document.querySelector("#modo-app");

// Funciones auxiliares

function buscarMensaje(idMensaje) {
  for (const mensaje of mensajes) {
    if (mensaje.id === idMensaje) {
      return mensaje;
    }
  }

  return null;
}

function estiloEstaPermitido(idEstilo) {
  if (mensajeElegido === null) {
    return false;
  }

  return mensajeElegido.allowed_style_ids.includes(idEstilo);
}

function mostrarError(mensaje) {
  textoRespuesta.textContent = mensaje;
}

function mostrarModoApp(configuracion) {
  if (configuracion.app_mode === "openai" && configuracion.openai_configurado) {
    textoModoApp.textContent = "Modo OpenAI";
    return;
  }

  textoModoApp.textContent = "Modo mock";
}

// Pedidos al backend

async function pedirJson(url) {
  const respuesta = await fetch(url);

  if (!respuesta.ok) {
    throw new Error("El backend devolvió un error");
  }

  return respuesta.json();
}

async function cargarDatosIniciales() {
  try {
    const configuracion = await pedirJson(API_URL + "/config");
    mostrarModoApp(configuracion);

    mensajes = await pedirJson(API_URL + "/mensajes");
    estilos = await pedirJson(API_URL + "/estilos");
    reiniciarDemo();
  } catch (error) {
    mostrarError("No se pudo conectar con el backend.");
  }
}

// Acciones principales del usuario

function elegirMensaje(idMensaje) {
  mensajeElegido = buscarMensaje(idMensaje);
  analisisRealizado = false;

  textoMensajeElegido.textContent = mensajeElegido.text;
  botonAnalizar.disabled = false;
  textoBrief.textContent = "Todavía no hay análisis.";
  textoJson.textContent = "{}";
  textoRespuesta.textContent = "Elegí un estilo permitido.";

  mostrarMensajes();
  mostrarEstilos();
}

async function analizarLead() {
  if (mensajeElegido === null) {
    return;
  }

  try {
    textoBrief.textContent = "Analizando lead...";
    const resultado = await pedirJson(API_URL + "/analizar/" + mensajeElegido.id);

    analisisRealizado = true;
    textoBrief.textContent = resultado.brief;
    textoJson.textContent = JSON.stringify(resultado.json_tecnico, null, 2);
    mostrarEstilos();
  } catch (error) {
    mostrarError("No se pudo analizar el mensaje.");
  }
}

async function elegirEstilo(idEstilo) {
  if (!analisisRealizado || !estiloEstaPermitido(idEstilo)) {
    return;
  }

  try {
    textoRespuesta.textContent = "Generando respuesta...";
    const resultado = await pedirJson(
      API_URL + "/responder/" + mensajeElegido.id + "/" + idEstilo
    );

    textoRespuesta.textContent = resultado.respuesta;
    mostrarEstilos(idEstilo);
  } catch (error) {
    mostrarError("No se pudo generar la respuesta.");
  }
}

function reiniciarDemo() {
  mensajeElegido = null;
  analisisRealizado = false;

  textoMensajeElegido.textContent = "Elegí un mensaje para empezar.";
  botonAnalizar.disabled = true;
  textoBrief.textContent = "Todavía no hay análisis.";
  textoJson.textContent = "{}";
  textoRespuesta.textContent = "Elegí un estilo permitido.";

  mostrarMensajes();
  mostrarEstilos();
}

// Funciones que dibujan datos en pantalla

function mostrarMensajes() {
  listaMensajes.innerHTML = "";

  for (const mensaje of mensajes) {
    const boton = document.createElement("button");
    boton.type = "button";
    boton.className = "message-button";
    boton.textContent = mensaje.text;

    if (mensajeElegido !== null && mensaje.id === mensajeElegido.id) {
      boton.classList.add("active");
    }

    boton.addEventListener("click", function () {
      elegirMensaje(mensaje.id);
    });

    listaMensajes.appendChild(boton);
  }
}

function mostrarEstilos(idEstiloActivo) {
  listaEstilos.innerHTML = "";

  for (const estilo of estilos) {
    const boton = document.createElement("button");
    const permitido = estiloEstaPermitido(estilo.id);

    boton.type = "button";
    boton.className = "style-button";
    boton.textContent = estilo.label;
    boton.disabled = !analisisRealizado || !permitido;

    if (permitido) {
      boton.classList.add("allowed");
    } else {
      boton.classList.add("blocked");
    }

    if (estilo.id === idEstiloActivo) {
      boton.classList.add("active");
    }

    boton.addEventListener("click", function () {
      elegirEstilo(estilo.id);
    });

    listaEstilos.appendChild(boton);
  }
}

// Eventos iniciales

botonAnalizar.addEventListener("click", analizarLead);
botonReiniciar.addEventListener("click", reiniciarDemo);

cargarDatosIniciales();
