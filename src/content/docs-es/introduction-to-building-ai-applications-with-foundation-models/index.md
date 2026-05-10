---
title: "Introducción a la construcción de aplicaciones de IA con modelos fundacionales"
description: "Resumen del capítulo 1 — AI Engineering (Huyen, 2025)"
order: 1
---

## Introducción

Chip Huyen resume la era post-2020 en una palabra: **escala**. Los modelos detrás de ChatGPT, Gemini o Midjourney consumen una parte relevante de la electricidad mundial y el corpus público de internet para entrenamiento es un recurso finito.

Dos consecuencias principales:

1. **Más capacidad y más aplicaciones**: más personas y equipos usan IA para productividad, valor económico y calidad de vida.
2. **Modelo como servicio**: entrenar LLMs exige datos, cómputo y talento concentrados en pocas organizaciones; esos modelos se ofrecen como API, bajando la barrera para quien quiera construir sin financiar un modelo desde cero.

Así, la demanda de aplicaciones de IA crece mientras la barrera de entrada para construirlas baja. **AI engineering** —construir aplicaciones sobre modelos ya disponibles— se convierte en una de las disciplinas de ingeniería que más rápido crece.

Construir sobre ML no es nuevo (recomendaciones, fraude, churn). Muchos principios de producción siguen vigentes; lo nuevo son los **modelos fundacionales** a gran escala y lo que cambian en posibilidades y retos.

---

## Del modelo de lenguaje al modelo fundacional

### Lenguaje y tokens

Un **modelo de lenguaje** codifica estadísticas sobre uno o más idiomas: qué tan probable es una palabra/token en un contexto (p. ej. “My favorite color is ___” → “blue” más que “car”). La unidad básica es el **token** (carácter, palabra o subpalabra); la tokenización y el tamaño del vocabulario los define el desarrollador del modelo.

Hay dos familias principales:

- **Enmascarado (masked)**, p. ej. BERT: predice tokens faltantes usando contexto antes y después; útil en tareas no generativas o que requieren contexto bidireccional.
- **Autoregresivo**: predice el siguiente token solo con lo anterior; hoy es el estándar para **generación de texto**. En el libro, salvo que se diga lo contrario, “language model” = autoregresivo.

Los outputs son **abiertos**: con vocabulario finito se pueden construir infinitas salidas —por eso hablamos de **IA generativa**. Intuitivamente: el modelo es una **máquina de completar**: prompt + continuación probabilística (no garantizada).

Muchas tareas (traducción, resumen, código, clasificación “¿spam?”) pueden plantearse como completación con el prompt adecuado. Completar no es lo mismo que mantener una conversación adaptada al usuario; eso requiere **post-training** u otras técnicas.

### Self-supervision y escalado

La clave del escalado de los LM es la **auto-supervisión**: el propio texto proporciona etiquetas (el siguiente token) y contexto, sin etiquetado manual masivo. Contrasta con **supervisión** clásica (p. ej. ImageNet), cara y lenta a escala.

Los **LLM** se miden sobre todo por **número de parámetros**; “grande” es relativo (GPT-1 ~117M parecía grande; con el tiempo la referencia sube). Modelos más grandes suelen necesitar **más datos** de entrenamiento para aprovechar su capacidad (no se trata de igualar a un modelo pequeño con los mismos datos, sino de maximizar el rendimiento).

### De LLM a foundation models

Los humanos no solo usamos texto; por eso los LM se extienden a **multimodalidad** (imagen, vídeo, etc.). Un modelo que condiciona la generación en varias modalidades encaja mejor como **foundation model** que como “solo LLM”: *foundation* indica que son base para construir encima.

Un modelo multimodal generativo también se llama **large multimodal model (LMM)**. Ejemplo histórico: **CLIP** —no generativo, sino de *embeddings* alineados imagen-texto; backbone de muchos sistemas generativos posteriores.

Los foundation models marcan el paso de modelos **por tarea** a modelos **generalistas**: un mismo modelo puede orientarse a muchas tareas; luego se **adapta** al dominio (voz de marca, formato, etc.).

### Adaptación

Tres técnicas habituales que el libro desarrolla después:

- **Prompt engineering**: instrucciones y ejemplos sin cambiar pesos.
- **RAG**: contexto externo (p. ej. base de conocimiento) para completar mejor.
- **Finetuning**: seguir entrenando el modelo para el caso de uso.

Adaptar un modelo potente suele ser mucho más barato y rápido que entrenar desde cero; aun así pueden seguir siendo interesantes modelos **pequeños y específicos** (velocidad, coste). La decisión **comprar vs construir** modelo sigue siendo central.

---

## Por qué “AI engineering” (y no solo MLOps)

Tres factores que impulsan la disciplina:

1. **Capacidades generalistas**: más tareas posibles, algunas antes “imposibles”; la IA puede automatizar buena parte del trabajo que implica comunicación escrita, creatividad asistida, código, etc.
2. **Inversión**: el éxito de productos como ChatGPT disparó inversión VC y corporativa; costes por caso de uso han bajado órdenes de magnitud en periodos cortos (ejemplos citados en el texto).
3. **Barrera baja**: APIs de **model as a service**, más la posibilidad de prototipar con poco código y hasta en lenguaje natural.

El término **AI engineering** se prefiere frente a agrupar todo en “ML engineering” porque trabajar con foundation models **no es igual** que con ML tradicional; los sufijos “Ops” enfatizan operaciones, pero aquí el foco está en **adaptar** modelos base. En encuestas informales entre profesionales, “AI engineering” fue la etiqueta preferida.

---

## Casos de uso (patrones)

Las taxonomías varían (AWS: experiencia cliente, productividad interna, procesos; O’Reilly: programación, análisis, soporte, marketing, etc.). Huyen sintetiza **ocho categorías** (consumo y empresa): **programación**, **imagen y vídeo**, **escritura**, **educación**, **bots conversacionales**, **agregación de información**, **organización de datos** y **automatización de flujos**.

Ideas transversales del capítulo:

- Ocupaciones muy “expuestas” a la IA (según estudios citados) incluyen interpretación, redacción, diseño web; con baja exposición, oficios muy físicos o manuales.
- Las empresas suelen desplegar antes **aplicaciones internas** (menor riesgo) que **externas**; muchas apps siguen siendo en la práctica **tareas cerradas** (p. ej. clasificación) aunque el modelo sea abierto.
- **Coding**: caso más citado en encuestas; Copilot como hito comercial; McKinsey sugiere grandes ganancias en documentación y moderadas en generación/refactor, menos en tareas muy complejas.
- **Creatividad** (imagen/vídeo): encaja con la naturaleza probabilística de los modelos generativos.
- **Escritura**: alto volumen, tolerancia a errores; estudios (p. ej. MIT sobre ChatGPT) muestran ganancias de tiempo y calidad; también hay abusos (granjas de contenido, spam SEO).
- **Educación**: tutoría personalizada, cuestionarios, debates simulados; tensiones con negocios tradicionales de ayuda con deberes.
- **Bots**: soporte, copilotos de producto, compañía; también voz y personajes 3D/NPC.
- **Agregación**: resúmenes, “talk to your docs”, investigación; en empresa, romper silos de reuniones y correos.
- **Organización de datos**: etiquetado, extracción de PDFs, búsqueda multimodal; IDP como mercado en crecimiento.
- **Automatización y agentes**: tareas que requieren **herramientas externas** y planificación → **agentes** (tema central más adelante en el libro).

---

## Planificar aplicaciones de IA

Antes de construir “porque sí”:

### Evaluación del caso de uso

Motivaciones típicas (de mayor urgencia percibida): **continuidad del negocio** frente a competidores con IA, **captura de valor** (margen, productividad), o **exploración** para no quedarse atrás (con el coste de oportunidad que implica). Decidir **build vs buy** y si el trabajo debe ser **in-house** depende del riesgo estratégico.

### Rol de la IA y de las personas

Dimensiones útiles (inspiradas en documentación de Apple, citada en el libro): **crítico vs complementario**, **reactivo vs proactivo** (latencia y expectativas de calidad distintas), **dinámico vs estático** (personalización continua vs modelo compartido actualizado en releases).

**Human-in-the-loop**: desde sugerencias para agentes humanos hasta automatización total. Marco **Crawl–Walk–Run** (Microsoft): primero humano obligatorio, luego IA con internos, luego más automatización con externos.

### Defensibilidad (“moats”)

APIs y modelos base igualan el playing field: ventajas típicas son **tecnología**, **datos** y **distribución**. El modelo base puede **absorber** capas que antes eran producto (ej. capacidades nuevas del proveedor). Datos de uso y “data flywheel” aparecen como narrativa recurrente en startups.

### Expectativas y métricas

Definir éxito en **métricas de negocio** y umbrales de utilidad: **calidad**, **latencia** (TTFT, TPOT, latencia total), **coste por inferencia**, además de satisfacción de usuario y feedback.

### Plan por hitos y “last mile”

Evaluar modelos **off-the-shelf** antes de comprometer recursos. El salto de demo a producto es largo: la curva **0→60** puede ser rápida; **60→100** es costosa (alucinaciones, detalle). Mantenimiento implica **coste/beneficio** continuo (precios de APIs, proveedores que desaparecen, regulación, IP, hardware).

---

## El stack de AI engineering

### Tres capas

1. **Desarrollo de aplicación**: prompts, contexto, evaluación rigurosa, interfaces.
2. **Desarrollo de modelo**: frameworks de entrenamiento/finetuning, **dataset engineering**, optimización de inferencia.
3. **Infraestructura**: serving, datos, cómputo, monitorización.

En datos de GitHub (repos AI con muchas estrellas), tras ChatGPT/Stable Diffusion explotaron sobre todo **aplicaciones** y **herramientas de aplicación**; la infraestructura crece menos porque muchas necesidades (serving, monitorización) **siguen parecidas** al ML clásico.

Principios que **permanecen**: alinear métricas de negocio con métricas de ML, experimentación sistemática (ahora: modelos, prompts, retrieval, sampling…), feedback loops con datos de producción, eficiencia.

### AI engineering frente a ML “tradicional”

Tres diferencias grandes:

1. **Menos entrenar desde cero, más adaptar** modelos ajenos.
2. **Modelos más grandes**: más presión por coste/latencia de inferencia y por skilled engineers en GPU/clusters.
3. **Salidas abiertas**: la **evaluación** se vuelve un problema mayor.

**Adaptación sin cambiar pesos**: prompt engineering. **Adaptación cambiando pesos**: finetuning (más datos y complejidad, pero necesaria para algunos saltos de calidad o tareas nuevas).

### Desarrollo de modelo (capa media)

- **Pre-training**: desde pesos aleatorios; consume la mayor parte del cómputo en LLMs típicos.
- **Finetuning / post-training**: continuar desde pesos ya entrenados; a menudo “post-training” si lo hace el proveedor del modelo, “finetuning” si lo hace quien construye la aplicación (uso informal solapado).
- **Dataset engineering**: con foundation models hay más **datos no estructurados** y anotar respuestas abiertas es más difícil; más deduplicación, tokenización, recuperación de contexto y control de calidad.
- **Inferencia**: los modelos autoregresivos generan token a token; la latencia acumulada es un reto frente a las expectativas web típicas (~100 ms).

### Desarrollo de aplicación (capa superior)

Con modelos compartidos, la diferenciación viene del **producto**: **evaluación**, **prompt engineering y construcción de contexto**, **interfaz de usuario** (web, extensiones, chat en Slack, plugins…). Las interfaces conversacionales facilitan feedback en lenguaje natural pero complican su **extracción** y análisis.

### AI engineering y full-stack

El peso de interfaces acerca AI engineering al **desarrollo full-stack**: más APIs JavaScript/Node, más iteración rápida demo–feedback. El flujo puede invertirse respecto al ML clásico: **producto primero**, datos/modelos especializados después si el producto lo merece.

---

## Cierre del capítulo

El capítulo intenta explicar **por qué existe AI engineering** como disciplina y **qué implica** construir sobre foundation models: evolución LM → LLM → modelos multimodales/generalistas, auto-supervisión, patrones de uso, planificación antes de codificar, stack en tres capas y diferencias respecto al ML tradicional —con énfasis en **adaptación** y **evaluación**.

La comunidad aporta energía y herramientas a un ritmo difícil de seguir; el libro plantea ofrecer un **marco** para navegar ese espacio, empezando en el capítulo 2 por el bloque fundamental: los propios **foundation models**.

---

## Notas finales

Lo que me queda de este capítulo no es tanto vocabulario como un **cambio de punto de partida**: no voy a entrenar modelos desde cero—voy a **adaptar** modelos generalistas que alguien más ya escaló. La **auto-supervisión** es la pieza técnica que lo hizo viable: el texto (y luego otras modalidades) trae su propia señal de supervisión, así que el crecimiento dejó de estar frenado por etiquetado masivo. En la práctica, la adaptación se apila en **prompting**, **RAG** cuando el conocimiento está fuera de los pesos, y **finetuning** solo cuando ese escalón se justifica. Encaja con un **flujo invertido**: partir del **producto** y del ciclo con usuarios, y **profundizar en datos y modelo** cuando algo demuestre que merece escalarse—lo contrario del hábito clásico “datos → modelo → producto”. La variedad de **casos de uso** (código, escritura, bots, agregación…) también me recuerda que muchas empresas **despliegan primero lo interno** para aprender con menos riesgo antes de exponer al cliente a fallos abiertos.

En el día a día, **mi rol** se inclina hacia la **capa de aplicación**—interfaces, construcción de contexto e iteración—no hacia diseñar transformadores. Lo más difícil no es llamar a una API; es la **evaluación**: las salidas generativas no se resumen en una sola accuracy, así que hay que definir y vigilar qué cuenta como “suficientemente bueno”. Eso obliga a **equilibrar** rendimiento, latencia y coste entre proveedores y técnicas de adaptación. La **planificación** cierra el oficio: aclarar *por qué* existe el proyecto (riesgo, oportunidad o exploración), graduar la automatización (por ejemplo **crawl–walk–run**) y fijar **métricas y umbrales de utilidad** desde el principio—porque un demo de fin de semana no tiene nada que ver con el trecho largo entre “funciona en la demo” y “aguanta producción”.

**Referencia:** Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.
