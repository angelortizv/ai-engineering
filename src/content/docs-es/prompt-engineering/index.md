---
title: "Ingeniería de prompts"
description: "Resumen del capítulo 5 — AI Engineering (Huyen, 2025)"
order: 5
---

## Introducción

> **O'Reilly (1.ª ed.)** — Huyen (2025), **Capítulo 5**, aprox. **pp. 211–252**. Contrasta figuras y tablas con tu PDF.

La **ingeniería de prompts** es la forma más fácil y habitual de adaptar foundation models: redactar una instrucción que provoque el comportamiento deseado **sin cambiar pesos**. Muchas aplicaciones se lanzan solo con prompting, pero lo fácil del inicio esconde dificultad real.

> Prompt engineering se refiere al proceso de elaborar una instrucción que haga que el modelo genere el resultado deseado… Puedes pensarlo como comunicación humano–IA.
>
> — Huyen (2025, p. 211)

Cualquiera escribe un prompt; pocos escriben uno **eficaz**. Trata los experimentos de prompt con el mismo rigor que un experimento de ML: pruebas y evaluación sistemáticas (capítulo 4). En producción hacen falta estadística, ingeniería y datos—not solo prompts.

Un responsable de investigación de OpenAI, citado en el libro: el problema no es el prompt engineering como habilidad; es cuando **el prompt engineering es lo único que la gente sabe**.

Este capítulo cubre **prompting efectivo** y diseño **defensivo** frente a ataques de prompt.

---

## El arte y la ciencia del prompting

### Anatomía de un prompt

Un **prompt** es una instrucción para realizar una tarea—desde “¿Quién inventó el cero?” hasta investigación o código en varios pasos. Partes típicas:

1. **Descripción de la tarea** — rol, restricciones, formato de salida.
2. **Ejemplo(s)** — demostraciones del comportamiento deseado.
3. **La tarea** — entrada concreta (pregunta, documento, etc.).

El prompting solo funciona si el modelo **sigue instrucciones** (capítulo 4). La **robustez** a perturbaciones pequeñas (“5” vs. “five”, mayúsculas, saltos de línea) correlaciona con la capacidad global; modelos más fuertes exigen menos retoques. En la práctica, muchos modelos rinden mejor con la descripción al **inicio**; otros (p. ej. Llama 3) al **final**—experimenta.

### Aprendizaje en contexto (ICL)

**In-context learning** (Brown et al., 2020, GPT-3): el modelo aprende del comportamiento mostrado en el **prompt** sin actualizar pesos. Permite refrescar conocimiento (p. ej. documentación nueva de JavaScript en contexto vs. reentrenar).

Cada ejemplo es un **shot**. **Zero-shot** = sin ejemplos; **few-shot** = uno o más. Más ejemplos suelen ayudar hasta el límite de **contexto** y el coste. GPT-3 ganó mucho con few-shot; en modelos tipo GPT-4, Microsoft (2023) vio menos mejora en tareas generales—but few-shot sigue importando en **APIs de nicho** (p. ej. Ibis) poco vistas en entrenamiento.

**Terminología:** En este libro, **prompt** = entrada completa al modelo; **contexto** = información necesaria para la tarea (no siempre igual que “prompt” en otros sitios).

Analogía de François Chollet: el foundation model es una **biblioteca de programas**; el prompt engineering encuentra el prompt que **activa** el programa que quieres.

### Prompt de sistema vs. de usuario

Las APIs suelen separar:

- **System prompt** — persona, reglas, formato (definido por el desarrollador).
- **User prompt** — consulta del usuario + **contexto** recuperado o subido (la tarea).

Ejemplo: chatbot de disclosures inmobiliarios—agente en system; PDF + pregunta en user.

El proveedor concatena ambos con una **plantilla de chat** (específica del modelo y versión). Plantilla incorrecta (salto de línea, tokens especiales) → **fallos silenciosos**.

**Buenas prácticas:**

- Seguir exactamente la plantilla documentada del modelo.
- Verificar que librerías de terceros usen la plantilla correcta para tu versión.
- **Imprimir el prompt final** antes de enviar.

El system prompt puede rendir mejor que el mismo texto en user porque va **primero** y porque el **post-training** puede priorizar mensajes de sistema (jerarquía de instrucciones de OpenAI, Wallace et al., 2024)—también para seguridad.

### Longitud de contexto y eficiencia

Las ventanas pasaron de ~1K tokens a millones, pero **no todas las posiciones valen igual**. **Needle in a haystack (NIAH):** ocultar un dato en distintas posiciones; el modelo recuerda mejor al **inicio y al final**, peor en el **medio** (Liu et al., 2023). Usa agujas de prueba privadas para no confundir con memorización del entrenamiento.

Si el rendimiento cae con contexto largo → acorta o reestructura. Pon instrucciones críticas y retrieval en posiciones de **alta saliencia**.

---

## Buenas prácticas para prompts efectivos

Destiladas de OpenAI, Anthropic, Meta, Google y equipos en producción—técnicas que envejecen mejor que trucos (“propina de 300 $”, “Q:” vs “Questions:”).

### Escribe instrucciones claras y explícitas

- Define la tarea **sin ambigüedad** (escala 1–5 vs 1–10; solo enteros si aparecen decimales).
- La **persona** orienta la perspectiva (ensayo 2/5 genérico vs 4/5 como maestro de primaria).
- Los **ejemplos** reducen ambigüedad (bot de Papá Noel: sin ejemplos, “personaje ficticio”; con hada de los dientes, respuesta mágica afirmativa).
- Formatos de ejemplo **eficientes en tokens** si el rendimiento es igual.
- **Formato de salida** — conciso, sin preámbulos, claves JSON; **marcadores finales** en clasificación para que el modelo no continúe la entrada.

### Proporciona contexto suficiente

El contexto mejora respuestas y **reduce alucinaciones** cuando el modelo de otro modo adivinaría con conocimiento interno desactualizado. Documentos directos o **construcción de contexto** (RAG, búsqueda web—capítulo 6).

Responder **solo con el contexto** (NPC de Skyrim, políticas internas) es difícil: instrucciones claras, “cita la fuente”, ejemplos de lo no respondible—but **sin garantía** sin finetuning o corpus cerrado.

### Descompón tareas complejas

Encadena **prompts pequeños** en lugar de uno gigante:

1. Clasificación de intent → categorías JSON.
2. Prompts de respuesta por intent.

Ventajas: **monitorizar** salidas intermedias, **depurar** un paso, **paralelizar**, redactar más fácil. Costes: más consultas, mayor **latencia hasta el primer token** si el usuario espera el paso final. GoDaddy (2024): prompt de soporte **>1.500 tokens**; la descomposición mejoró calidad y bajó tokens. Modelo débil en pasos baratos (intent), fuerte en generación.

### Dale al modelo “tiempo para pensar”

- **Chain-of-thought (CoT)** — “piensa paso a paso”, pasos fijados o ejemplos (Wei et al., 2022). Ayuda en razonamiento; LinkedIn reportó menos alucinaciones.
- **Autocrítica** — el modelo revisa su salida (capítulo 3).

Ambos suben latencia y coste. Equilibra calidad vs. experiencia visible.

### Itera, evalúa y organiza

El prompting es iterativo. **Versiona prompts**, registra experimentos, evalúa en el **sistema completo**.

Herramientas de optimización (DSPy, OpenPrompt, Promptbreeder)—cuidado con **explosión de llamadas API** ocultas. Inspecciona prompts generados; errores de plantilla en herramientas (ejemplo LangChain en el libro).

**Separa prompts del código**: reutilización, tests, legibilidad, colaboración de expertos de dominio. Metadatos y **catálogo de prompts** con versionado explícito cuando varias apps comparten uno.

---

## Ingeniería de prompts defensiva: panorama de amenazas

Apps desplegadas tienen **usuarios legítimos** y **atacantes**. Tres familias:

| Ataque | Objetivo |
|--------|----------|
| **Extracción de prompt** | Robar el system prompt para replicar o manipular la app |
| **Jailbreak / inyección** | Violar políticas o ejecutar acciones no deseadas |
| **Extracción de información** | Filtrar datos de entrenamiento o **contexto** privado |

**Riesgos:** ejecución SQL/herramientas no autorizada, fugas, tutoriales dañinos, desinformación, denegación de servicio, **daño de marca**.

Mejor seguimiento de instrucciones mejora UX **y** éxito de ataques.

### Extracción y reverse engineering

Prompts valiosos circulan en GitHub y marketplaces; algunos equipos los tratan como IP.

> Los prompts propietarios son más un **pasivo** que una ventaja competitiva.
>
> — Huyen (2025, p. 238)

Asume que el system prompt puede hacerse público; el **contexto** (PII en RAG) también puede filtrarse. Los prompts requieren mantenimiento en cada cambio de modelo.

### Jailbreak e inyección de prompt

**Jailbreak** — saltarse seguridad. **Inyección** — instrucciones maliciosas en contenido de usuario o herramientas. Huyen usa **jailbreaking** para ambos en el libro.

Trucos históricos (cada vez menos efectivos en modelos fuertes): ofuscación, formato (poema sobre forzar coches), **DAN** / abuela. Ataques **automatizados** (PAIR, etc.).

**Inyección indirecta** — instrucciones en **salidas de herramientas** (email, web, documento RAG, nombre de usuario malicioso en SQL). Pasiva vs. activa. Crítica para agentes y RAG.

### Extracción de información

Robo de datos de entrenamiento, **privacidad**, **copyright**. Ataque de **divergencia** (repetir “poem” indefinidamente, Nasr et al., 2023); modelos grandes memorizan más. Filtros de PII en entrada/salida.

### Defensa: enfoque multicapa

Métricas: **tasa de violación** y **tasa de rechazo falso**.

**1. Nivel modelo** — Jerarquía: **system > user > salida del modelo > salida de herramienta**. Entrenar casos límite (cerradura propia → cerrajero).

**2. Nivel prompt** — Prohibiciones explícitas; **repetir instrucciones de sistema** tras el usuario; advertir sobre DAN/abuela. Revisar plantillas por defecto de frameworks.

**3. Nivel sistema** — **Aislamiento** (sandbox de código); **aprobación humana** en SQL destructivo; filtros de alcance; **guardrails** entrada/salida (capítulo 10); detectar patrones de sondeo repetido.

La seguridad sigue siendo **gato y ratón**; adopción de alto riesgo irá más lenta.

---

## Cierre del capítulo

El capítulo 5 plantea el prompting como **comunicación humano–IA**: anatomía, ICL, system/user, eficiencia de contexto, buenas prácticas y **defensa en profundidad** frente a extracción, inyección y filtrado de datos.

Las instrucciones solas no bastan: hace falta el **contexto** adecuado (capítulo 6). El finetuning queda cuando el prompting se estanca (capítulo 7).

---

## Preguntas de discusión

- ¿Qué tareas quedan **zero-shot** y cuáles necesitan **few-shot**—y por qué?
- ¿Cómo **versionas** prompts y los ligas a corridas de eval?
- ¿Cuál es tu política ante **texto no confiable** en el contexto (inyección indirecta)?
- ¿Cuándo usar **salidas estructuradas** frente a texto libre + parsing?
- ¿Qué te haría dejar de iterar prompts y probar **RAG** o **finetuning**?

---

## Relacionado

- **Anterior:** [Evaluar sistemas de IA modernos](/ai-engineering/docs/es/evaluating-modern-ai-systems) — saber qué es «bueno» antes de iterar prompts.
- **Siguiente:** [RAG y agentes](/ai-engineering/docs/es/rag-and-agents) — contexto más allá de la ventana del prompt.
- **Seguridad:** [Metodología de evaluación](/ai-engineering/docs/es/evaluation-methodology) — elección de juez y métricas para pruebas de safety.
- **Arquitectura:** [Arquitectura de IA y feedback de usuario](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback) — guardrails alrededor de los prompts.
- **Repositorio del libro:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glosario:** [Glosario](/ai-engineering/docs/es/glossary) — términos del libro y estas notas.

## Notas finales

Me queda una doble actitud: **diseñar** prompts como superficie de producto (claros, con ejemplos, descompuestos, evaluados) y **asumir compromiso** como en seguridad (jerarquía, sandboxes, guardrails, sin secretos en el system prompt).

El ICL explica el “solo hazle prompt”, pero plantillas de chat y needle-in-haystack me recuerdan que **dónde** está la información en la ventana importa tanto como **qué** dice. Iteraría con evaluación (cap. 4) antes que automatizar con DSPy, y trataría prompts propietarios como **deuda operativa**.

En producción apilaría **jerarquía de instrucciones + guardrails + confirmación humana en acciones irreversibles** y reservaría red team cuando herramientas o RAG ingieran texto no confiable—la inyección indirecta es la amenaza que más creció en mi modelo mental.

**Referencia:** Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 5: Prompt Engineering.

---

## Referencias

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 5: Prompt Engineering.

### Guías oficiales y tutoriales (proveedores de modelos)

- [OpenAI — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) — Prácticas base: claridad, ejemplos, descomposición, salidas estructuradas.
- [OpenAI Cookbook](https://cookbook.openai.com/) — Recetas y patrones para prompting y APIs en producción.
- [Anthropic — Prompt engineering (overview)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) — Guía para Claude, personas y ejemplos.
- [Anthropic — Moderación de contenido con Claude](https://docs.anthropic.com/en/docs/build-with-claude/content-moderation) — Uso de modelos como moderadores (citado en el capítulo 5).
- [Google Cloud — Estrategias de diseño de prompts](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies) — Vertex AI / Gemini.
- [Meta — Llama: guía de prompting](https://www.llama.com/docs/how-to-guides/prompting/) — Plantillas de chat y consejos para Llama.
- [Microsoft Learn — Técnicas de prompt engineering](https://learn.microsoft.com/es-es/azure/ai-foundry/openai/concepts/prompt-engineering) — Patrones en Azure OpenAI (documentación en español disponible).

### Artículos, papers y conceptos clave

- [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165) — Brown et al. (2020); aprendizaje en contexto.
- [Chain-of-Thought Prompting Elicits Reasoning](https://arxiv.org/abs/2201.11903) — Wei et al. (2022).
- [The Instruction Hierarchy](https://arxiv.org/abs/2404.19756) — Wallace et al., OpenAI (2024); prioridad system > user > herramientas.
- [Understanding In-Context Learning](https://ai.stanford.edu/blog/understanding-incontext/) — Resumen Stanford AI Lab.
- [Lost in the Middle](https://arxiv.org/abs/2307.03172) — Liu et al. (2023); efecto “aguja en el pajar”.
- [Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — Greshake et al. (2023).
- [Extracción de datos de entrenamiento en modelos en producción](https://arxiv.org/abs/2311.17035) — Nasr et al. (2023); ataques de repetición / divergencia.

### Herramientas, frameworks y automatización de prompts

- [DSPy](https://dspy.ai/) — Optimización programática de prompts y pipelines.
- [Guidance](https://github.com/guidance-ai/guidance) — Generación estructurada / restringida.
- [Instructor](https://github.com/instructor-ai/instructor) — Salidas estructuradas desde APIs de LLM.
- [Outlines](https://github.com/dottxt-ai/outlines) — Generación de texto con restricciones.
- [Promptbreeder](https://arxiv.org/abs/2309.16797) — Optimización evolutiva de prompts (DeepMind).
- [TextGrad](https://arxiv.org/abs/2406.07496) — Refinamiento tipo gradiente de prompts.
- [Firebase Genkit — Dotprompt](https://firebase.google.com/docs/genkit/dotprompt) — Archivos `.prompt` versionados con esquema.
- [LangSmith / LangChain Hub](https://smith.langchain.com/hub) — Plantillas compartidas (revisar defaults de seguridad).

### Bibliotecas, catálogos y listas comunitarias

- [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) — Colección comunitaria (inglés).
- [PlexPt/awesome-chatgpt-prompts-zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) — Colección en chino.
- [PromptHero](https://prompthero.com/) — Descubrimiento público de prompts.
- [PromptBase](https://promptbase.com/) — Marketplace de prompts.
- [Cursor Directory](https://cursor.directory/) — Prompts y reglas para asistentes de código.

### Seguridad, jailbreak y red teaming

- [Microsoft — Plan de red teaming para aplicaciones LLM](https://learn.microsoft.com/es-es/azure/ai-foundry/openai/concepts/red-teaming) — Guía empresarial.
- [Azure PyRIT](https://github.com/Azure/PyRIT) — Toolkit de identificación de riesgos en IA generativa.
- [garak (NVIDIA)](https://github.com/NVIDIA/garak) — Escáner de vulnerabilidades en LLM.
- [llm-security (Greshake)](https://github.com/greshake/llm-security) — Utilidades de prueba de seguridad.
- [OWASP Top 10 para aplicaciones LLM](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — Marco estándar (inyección de prompt, etc.).
- [Dropbox — Evolución de ataques por token repetido](https://dropbox.tech/machine-learning/bye-bye-bye-evolution-of-repeated-token-attacks-on-chatgpt-models) — Breitenbach & Wood (2024).

### Blogs y notas de práctica

- [Hamel Husain — “Show Me the Prompt”](https://hamel.dev/blog/posts/prompt/) — Inspeccionar prompts generados por herramientas.
- [Brex — Guía de prompt engineering](https://www.brex.com/journal/prompt-engineering-guide) — Patrones empresariales (incluye ejemplos de fuga de contexto).
- [Shreya Shankar](https://shreya-shankar.github.io/) — Pruebas NIAH en escenarios tipo producción (buscar el post más reciente en su sitio).

### Cursos y talleres

- [DeepLearning.AI — ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) — Curso corto (OpenAI + Isa Fulford).
- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — *Innovación Educativa UPM*: presentación del taller sobre desarrollo de software asistido por IA y prompting.
