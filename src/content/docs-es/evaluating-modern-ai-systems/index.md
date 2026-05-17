---
title: "Evaluación de sistemas modernos de IA"
description: "Resumen del capítulo 4 — AI Engineering (Huyen, 2025)"
order: 4
---

## Introducción

Un modelo solo sirve si funciona para **tu** aplicación. El capítulo 3 repasó **cómo** evaluar (métricas exactas, jueces IA, ranking comparativo). Este capítulo cubre **qué** medir, **cómo elegir modelos** y **cómo montar un pipeline** confiable en el tiempo.

Tres partes:

1. **Criterios de evaluación** — capacidad de dominio, calidad generativa, seguimiento de instrucciones, coste y latencia.
2. **Selección de modelos** — construir vs. comprar, benchmarks públicos, leaderboards, contaminación.
3. **Pipeline de evaluación** — guías, métodos, *slices* de datos e iteración en producción.

La evaluación debe verse en el **sistema**: saber dónde falla, medir en torno a eso y, a veces, rediseñar para ganar visibilidad.

---

## Filosofía central: desarrollo guiado por evaluación

¿Qué es peor: una app que nunca se despliega o una desplegada **sin saber si funciona**? La mayoría elige lo segundo: cuesta mantenerla y el ROI sigue opaco. Equipos lanzan modelos de valoración de coches sin medir precisión, o chatbots de soporte sin saber si ayudan o perjudican la UX.

Antes de invertir a fondo, define **cómo medirás el éxito**. Huyen llama a esto **evaluation-driven development** (inspirado en TDD): **definir criterios de evaluación antes de construir**.

> En AI engineering, evaluation-driven development significa definir criterios de evaluación antes de construir.
>
> — Huyen (2025, p. 160)

En producción empresarial suelen predominar apps con **métricas claras**: recomendadores (engagement, conversión), fraude (dinero ahorrado), código (corrección funcional). Muchos casos con foundation models siguen siendo **cerrados** en la práctica (intent, sentimiento, siguiente acción)—más fáciles de evaluar que el chat abierto.

Centrarse solo en lo fácil de medir es buscar las llaves bajo el farol: cómodo, no necesariamente donde está el valor. Aun así, **la evaluación es el mayor cuello de botella para adoptar IA**; pipelines fiables desbloquean aplicaciones difíciles de puntuar hoy.

Una aplicación desplegada sin resultados evaluables es un **pasivo**: consume recursos sin valor conocible.

---

## Los cuatro pilares de los criterios de evaluación

Cuatro bloques (ejemplo: resumir un contrato legal):

| Pilar | Pregunta |
|-------|----------|
| **Capacidad de dominio** | ¿Entiende derecho / código / medicina? |
| **Capacidad generativa** | ¿Resumen coherente, fiel, seguro? |
| **Seguimiento de instrucciones** | ¿Formato, longitud, restricciones? |
| **Coste y latencia** | ¿Asequible y rápido para el caso de uso? |

El cap. 3 preguntaba “¿qué mide este **método**?”. Aquí: “dado este **criterio**, ¿qué métodos aplican?”.

### Capacidad específica de dominio

Un agente de código necesita saber programar; una app latín–inglés, ambos idiomas. Las capacidades dependen de **arquitectura, tamaño y datos de entrenamiento**—un modelo sin latín en entrenamiento no lo entenderá.

**Medición:** benchmarks de dominio (públicos o privados). En código suele usarse **corrección funcional** (HumanEval, MBPP, Spider, BIRD-SQL); BIRD-SQL también mide **eficiencia** de consultas (runtime vs. SQL de referencia). La **legibilidad** no tiene métrica exacta—jueces IA.

Otros dominios usan **opción múltiple** (MMLU, AGIEval, ARC-C). Fáciles de verificar; baseline aleatorio con cuatro opciones: 25%. Advertencias: la puntuación cambia con detalles del prompt (espacio extra, “Choices:”); los MCQ miden **clasificar bueno vs. malo**, no **generar**—útiles para conocimiento/razonamiento, débiles para resumen o redacción.

### Capacidad generativa

La NLG clásica medía **fluidez** y **coherencia**; los LM fuertes hicieron la fluidez superficial menos discriminante. Prioridades actuales: **alucinaciones** (indeseables en tareas factuales), **seguridad** (toxicidad, sesgo, daño) y rasgos de producto (controversia, concisión, tono).

**Consistencia factual**

- **Local** — salida respaldada por el **contexto dado** (RAG, soporte, resumen vs. fuente).
- **Global** — salida vs. **conocimiento abierto** (chat general, fact-check); lo más difícil es acordar qué es un hecho.

Técnicas: prompts de **juez IA**; **SelfCheckGPT** (muchas muestras—caro); **SAFE** (descomponer afirmaciones, buscar, verificar); clasificadores **NLI** (entailment / contradicción / neutral); benchmarks como **TruthfulQA**.

Diseña benchmarks donde **tu** modelo alucina (temas de nicho, preguntas sobre cosas que nunca ocurrieron).

**Seguridad**

Incluye lenguaje inapropiado, tutoriales dañinos, discurso de odio, violencia, estereotipos, sesgo ideológico. APIs de moderación, clasificadores de **toxicidad** (Perspective, etc.) o modelos generales bien prompteados. Benchmarks: RealToxicityPrompts, BOLD.

### Capacidad de seguimiento de instrucciones

Si el modelo devuelve HAPPY en lugar de POSITIVE/NEUTRAL en sentimiento, puede dominar el dominio pero fallar en **instrucciones**. Crítico para **JSON**, regex, límites de longitud, vocabulario restringido (p. ej. lectura infantil).

Es difícil separar de dominio o generación—y de la **calidad del prompt** (mala instrucción vs. mal modelo).

**IFEval** — más de 25 reglas de formato **verificables automáticamente** (palabras clave, conteo, JSON, viñetas). **INFOBench** — restricciones de contenido/estilo con criterios sí/no (humano o IA). Ir bien en benchmarks públicos ≠ ir bien con **tus** instrucciones; incluye YAML, “no digas As a language model…”, etc.

**Roleplay** (NPCs, compañeros): difícil de automatizar; RoleLLM, CharacterEval; heurísticas + jueces IA para estilo y **conocimiento** (incluido lo que el personaje *no* debe saber).

### Coste y latencia

Un modelo perfecto pero lento o caro no sirve en producción. Filtra por techos **duros** de latencia y optimiza calidad entre los que pasan. Métricas: **TTFT**, tiempo por token, latencia total; coste por token (API) vs. coste fijo de clúster (self-host—el coste marginal puede bajar al escalar).

Pregunta si la latencia es **obligatoria** o **deseable**; pocos usuarios rechazan menos latencia, pero no siempre es decisiva.

---

## Flujo de selección de modelos

Te importa el **mejor modelo para tu app**, no el #1 global. Re-eliges al cambiar prompts, RAG o finetuning.

**Atributos duros vs. blandos**

- **Duros** — licencia, privacidad, tamaño, API vs. self-host (no cambiables o no quieres cambiarlos).
- **Blandos** — precisión, toxicidad, consistencia factual (prompting, descomposición, finetuning pueden mejorar).

La precisión puede pasar de 20% a 70% tras descomponer la tarea—or seguir inutilizable tras semanas; saber cuándo abandonar un modelo.

### Paso 1: Construir vs. comprar

Primer filtro: **API comercial** vs. **open weights autoalojados** (incluidas APIs en tu VPC).

| Eje | API | Self-host |
|-----|-----|-----------|
| **Privacidad** | Los datos salen; la política puede cambiar (Zoom 2023) | Datos internos; riesgo de linaje en ti |
| **Linaje / IP** | Contratos pueden indemnizar | Quien despliega suele asumir riesgo |
| **Rendimiento** | SOTA top suele ser propietario | Brecha que se cierra; mejor abierto puede ir detrás |
| **Funcionalidad** | Escala, herramientas, salidas estructuradas; a menudo **sin logprobs** | Logprobs, finetuning completo; tú montas guardrails |
| **Coste** | Pago por token | Ingeniería + GPUs; puede ganar a gran volumen |
| **Control** | Límites, actualizaciones opacas, censura | Congelar pesos; tú mantienes serving |
| **Edge** | Requiere red | On-device posible (difícil) |

**Open source vs. open weight vs. open model** — pesos públicos ≠ datos públicos. Licencias: uso comercial, tope de MAU (Llama), destilación desde salidas.

> Un estudio a16z de 2024 muestra que las empresas valoran modelos abiertos sobre todo por **control** y **personalización**.
>
> — Huyen (2025, p. 189)

Los modelos más fuertes suelen quedarse solo en **API**; los más débiles se abren. El mismo modelo en distintos proveedores puede diferir—**prueba al cambiar**.

### Paso 2: Navegar benchmarks públicos

Miles de benchmarks (BIG-bench 214 tareas; lm-evaluation-harness 400+). Úsalos para una **lista corta orientativa**, no como verdad.

Los **leaderboards** agregan pocos benchmarks (límite de cómputo). Open LLM de Hugging Face vs. HELM Lite eligieron conjuntos distintos—la cobertura es subjetiva. **Correlaciona benchmarks**—si dos miden lo mismo, no los dupliques. Promediar trata un 80% en TruthfulQA como un 80% en GSM-8K; HELM usa **mean win rate** entre escenarios.

**Leaderboard privado con benchmarks públicos:** elige los que encajen con tu app (código → HumanEval; escritura → creativos). ¿Sin puntuación? Ejecuta el harness (HELM completo ~80k–100k USD citados para 30 modelos).

**Contaminación de datos** — entrenar con el test infla resultados (sátira “pretraining on the test set is all you need”). Frecuente por scrape web. Detectar: **solapamiento n-gramas** con entrenamiento, **perplejidad** sospechosamente baja en el benchmark. Socava la confianza; quien aprueba exámenes de barra puede dar mal consejo legal.

> La contaminación ocurre cuando el modelo se entrenó con los mismos datos con los que se evalúa, inflando puntuaciones inmerecidas.
>
> — Huyen (2025, p. 197)

**No confíes en benchmarks públicos como única verdad.** Úsalos para **descartar malos modelos** y valida en privado.

Las actualizaciones de modelo mueven puntuaciones (estudio GPT-3.5/4 mar–jun 2023)—“empeoró” a menudo refleja **tu tarea** y la dificultad del eval, no degradación universal.

### Paso 3: Diseñar tu pipeline personalizado

Aquí está tu **fuente de verdad**.

**3a. Evaluar todos los componentes**

De extremo a extremo **y** por paso (PDF → empleador actual). **Por turno** vs. **por tarea** (¿arreglamos el bug en 2 turnos o 20?). Los límites de tarea en chats reales son difusos.

**3b. Crear una guía de evaluación**

Qué debe y **no** debe hacer la app (¿preguntas electorales fuera de alcance en un bot de producto?). **Correcto ≠ bueno**: evaluación de empleo en LinkedIn—“encaje terrible” puede ser correcto pero dañino; lo bueno explica brechas y siguientes pasos.

Por criterio: sistema de puntuación + **rúbrica con ejemplos**; validar con humanos. **Ligar a métricas de negocio**: p. ej. 80% consistencia factual → automatizar 30% de tickets; 98% → 90%. Umbrales de **utilidad** (por debajo de 50% de consistencia, inutilizable incluso para consultas generales).

**3c. Métodos y datos**

Mezcla métodos: clasificador barato de toxicidad al 100%, juez IA caro al 1%. Usa **logprobs** si existen (confianza en clasificación, PPL). Humanos como **estrella polar**—p. ej. LinkedIn revisando cientos de conversaciones al día.

**Curar sets** desde producción; etiquetar con humanos o IA (cap. 8). **Segmentar (*slice*)** datos: pago vs. gratis, móvil vs. web, entradas largas, typos, fallos conocidos, fuera de alcance—evitar **paradoja de Simpson** (A gana en agregado pero pierde en cada subgrupo).

Bootstrap para tamaño de muestra; regla orientativa OpenAI al 95%: ~10 muestras para gap 30%, ~100 para 10%, ~1.000 para 3%, ~10.000 para 1%. Mediana en harness ~1.000 ejemplos.

**Evalúa el evaluador:** ¿más puntuación = mejor salida y negocio? ¿Reproducibilidad (temperatura 0 en jueces)? ¿Correlación entre métricas? ¿Coste/latencia del propio eval?

**Itera** criterios y rúbricas con el producto—pero registra configs para comparar mes a mes.

### Paso 4: Monitorizar en producción

Monitorización continua, detección de fallos y feedback de usuario (cap. 10). Los pasos son **iterativos**—build vs. buy puede cambiar tras eval privado.

---

## Cierre del capítulo

El capítulo 4 une criterios con **selección** y **pipelines**: cuatro pilares, desarrollo guiado por evaluación, flujo en cuatro pasos (filtrar → benchmarks públicos → eval propio → producción), tradeoffs build/buy, contaminación y guías, rúbricas, *slices* y métodos automáticos/humanos mixtos.

Ninguna puntuación resume un sistema de alta dimensión; **combinar métodos** mitiga puntos ciegos. Los capítulos dedicados a eval terminan aquí, pero vuelve en retrieval/agentes (6), finetuning y coste (7–9), calidad de datos (8) y feedback en producción (10). Siguiente: **prompt engineering**.

---

## Notas finales

Lo que me llevo es un cambio de hábito: **definir el éxito antes de construir**. Los cuatro pilares evitan optimizar solo accuracy en un leaderboard—dominio, calidad de salida, instrucciones y economía condicionan el ship.

**Construir vs. comprar** es estratégico: privacidad y control empujan self-host; SOTA y time-to-market empujan API; contaminación y promedios de leaderboard me empujan a un **set privado** con prompts reales, *slices* y umbrales de negocio. MMLU o Arena orientan; no sustituyen.

El ejemplo de LinkedIn (“terrible encaje”) fija que la guía debe codificar **utilidad**, no solo verdad. Montaría un pipeline como el text-to-SQL del cap. 3—funcional primero, jueces escalables después, humanos en la cola—y trataría el harness de eval como producto: bootstrap, juez congelado y mapa explícito de % consistencia → tickets automatizados.

> No tener un pipeline de evaluación fiable es uno de los mayores bloqueos para adoptar IA.
>
> — Huyen (2025, p. 208)

**Referencia:** Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 4: Evaluate AI Systems.
