// Datos simulados del frontend. En el próximo checkpoint se reemplazan por el backend.
const estilos = [
  { id: "friendly", etiqueta: "Amable" },
  { id: "direct", etiqueta: "Directa" },
  { id: "consultative", etiqueta: "Consultiva" },
  { id: "ask_more_data", etiqueta: "Pedir más datos" },
  { id: "schedule_call", etiqueta: "Agendar llamada" },
  { id: "handle_objection", etiqueta: "Manejar objeción" },
];

const mensajes = [
  {
    id: "price_question",
    texto: "Hola, ¿cuánto cuesta este servicio?",
    estilosPermitidos: ["friendly", "direct", "ask_more_data"],
    brief: "El lead quiere entender el precio antes de avanzar.",
    jsonTecnico: {
      intencion: "consultar precio",
      prioridad: "media",
      datos_faltantes: ["alcance del servicio", "plazo esperado"],
      siguiente_paso: "responder claro y pedir datos básicos para cotizar mejor",
    },
    respuestas: {
      friendly: "Hola, gracias por escribir. El precio depende del alcance que necesites. Si me contás qué querés resolver y para cuándo, puedo orientarte mejor.",
      direct: "Hola. Para pasarte un precio necesito saber el alcance del servicio y el plazo esperado. Con esos datos puedo darte una estimación más clara.",
      ask_more_data: "Hola. Para cotizar bien, necesito algunos datos: qué necesitás exactamente, para cuándo y si ya tenés alguna referencia de presupuesto.",
    },
  },
  {
    id: "urgent_deadline",
    texto: "Necesito tener algo funcionando para la semana que viene. ¿Se puede?",
    estilosPermitidos: ["direct", "consultative", "schedule_call"],
    brief: "El lead tiene urgencia y necesita saber si se puede llegar a tiempo.",
    jsonTecnico: {
      intencion: "resolver una necesidad urgente",
      prioridad: "alta",
      datos_faltantes: ["alcance mínimo", "fecha exacta de entrega"],
      siguiente_paso: "validar alcance y proponer una llamada corta",
    },
    respuestas: {
      direct: "Sí, puede ser posible, pero primero habría que definir el alcance mínimo para llegar bien a la semana que viene.",
      consultative: "Podemos evaluarlo. Lo importante es separar qué tiene que estar listo sí o sí y qué puede quedar para una segunda etapa.",
      schedule_call: "Coordinemos una llamada breve para revisar alcance y tiempos. Si te sirve, puedo proponerte dos horarios para hoy o mañana.",
    },
  },
  {
    id: "comparing_providers",
    texto: "Estoy comparando varios proveedores antes de decidir.",
    estilosPermitidos: ["friendly", "consultative", "handle_objection"],
    brief: "El lead está evaluando opciones y todavía no tomó una decisión.",
    jsonTecnico: {
      intencion: "comparar proveedores",
      prioridad: "media",
      datos_faltantes: ["criterios de decisión", "proveedores comparados"],
      siguiente_paso: "diferenciar la propuesta y preguntar qué está priorizando",
    },
    respuestas: {
      friendly: "Perfecto, tiene sentido comparar antes de decidir. Si querés, te puedo contar en qué se diferencia mi propuesta y qué incluye.",
      consultative: "Para ayudarte a comparar mejor, te preguntaría qué estás priorizando: precio, velocidad, soporte, calidad o experiencia previa.",
      handle_objection: "Entiendo que estés comparando. La clave es mirar no solo el precio, sino también el alcance, los tiempos y el acompañamiento incluido.",
    },
  },
  {
    id: "low_budget",
    texto: "Me interesa, pero tengo poco presupuesto.",
    estilosPermitidos: ["friendly", "consultative", "handle_objection"],
    brief: "El lead está interesado, pero tiene una objeción de presupuesto.",
    jsonTecnico: {
      intencion: "validar si el presupuesto alcanza",
      prioridad: "media",
      datos_faltantes: ["presupuesto aproximado", "funcionalidad indispensable"],
      siguiente_paso: "manejar la objeción y proponer un alcance inicial más chico",
    },
    respuestas: {
      friendly: "Gracias por contármelo. Podemos buscar una opción más simple para empezar y dejar mejoras para una segunda etapa.",
      consultative: "Podemos adaptarlo. Primero definiría qué es indispensable para que tengas valor rápido sin gastar de más.",
      handle_objection: "Entiendo la limitación de presupuesto. Una alternativa es empezar con un alcance mínimo que resuelva lo más importante y escalar después.",
    },
  },
  {
    id: "demo_request",
    texto: "¿Podemos coordinar una llamada o demo rápida?",
    estilosPermitidos: ["friendly", "direct", "schedule_call"],
    brief: "El lead ya quiere coordinar una llamada o demo.",
    jsonTecnico: {
      intencion: "agendar una conversación",
      prioridad: "alta",
      datos_faltantes: ["disponibilidad horaria", "objetivo de la llamada"],
      siguiente_paso: "proponer horarios concretos para coordinar",
    },
    respuestas: {
      friendly: "Sí, claro. Podemos coordinar una llamada o demo rápida. Decime qué horarios te quedan cómodos y lo organizamos.",
      direct: "Sí. Pasame dos horarios posibles y coordinamos una llamada breve para revisar tu caso.",
      schedule_call: "Coordinemos una demo rápida. Te propongo una llamada de 20 minutos para entender tu necesidad y mostrarte cómo sería el flujo.",
    },
  },
];

let mensajeElegido = null;
let analisisRealizado = false;

const listaMensajes = document.querySelector("#lista-mensajes");
const listaEstilos = document.querySelector("#lista-estilos");
const textoMensajeElegido = document.querySelector("#mensaje-elegido");
const botonAnalizar = document.querySelector("#boton-analizar");
const botonReiniciar = document.querySelector("#boton-reiniciar");
const textoBrief = document.querySelector("#brief-comercial");
const textoJson = document.querySelector("#json-tecnico");
const textoRespuesta = document.querySelector("#respuesta-sugerida");

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

  return mensajeElegido.estilosPermitidos.includes(idEstilo);
}

function elegirMensaje(idMensaje) {
  mensajeElegido = buscarMensaje(idMensaje);
  analisisRealizado = false;

  textoMensajeElegido.textContent = mensajeElegido.texto;
  botonAnalizar.disabled = false;
  textoBrief.textContent = "Todavía no hay análisis.";
  textoJson.textContent = "{}";
  textoRespuesta.textContent = "Elegí un estilo permitido.";

  mostrarMensajes();
  mostrarEstilos();
}

function analizarLead() {
  if (mensajeElegido === null) {
    return;
  }

  analisisRealizado = true;
  textoBrief.textContent = mensajeElegido.brief;
  textoJson.textContent = JSON.stringify(mensajeElegido.jsonTecnico, null, 2);
  mostrarEstilos();
}

function elegirEstilo(idEstilo) {
  if (!analisisRealizado || !estiloEstaPermitido(idEstilo)) {
    return;
  }

  textoRespuesta.textContent = mensajeElegido.respuestas[idEstilo];
  mostrarEstilos(idEstilo);
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

function mostrarMensajes() {
  listaMensajes.innerHTML = "";

  for (const mensaje of mensajes) {
    const boton = document.createElement("button");
    boton.type = "button";
    boton.className = "message-button";
    boton.textContent = mensaje.texto;

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
    boton.textContent = estilo.etiqueta;
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

botonAnalizar.addEventListener("click", analizarLead);
botonReiniciar.addEventListener("click", reiniciarDemo);

reiniciarDemo();
