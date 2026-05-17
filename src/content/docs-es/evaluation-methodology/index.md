---
title: "Metodología de evaluación"
description: "Resumen del capítulo 3 — AI Engineering (Huyen, 2025)"
order: 3
---

## Introducción

Cuanto más se despliega la IA, más margen hay para **fallos catastróficos**. Casos reales ya lo demostraron: un pasajero confió en el **chatbot de Air Canada** sobre tarifas por duelo y recibió información falsa; la aerolínea tuvo que cumplir el error tras una demanda. **Abogados** presentaron escritos con **citas de casos inventadas** por un LLM y fueron sancionados. Un usuario fue empujado al suicidio por un chatbot. Sin control de calidad en las salidas, el riesgo puede superar el beneficio en muchas aplicaciones.

Al adoptar IA con prisa, muchos equipos descubren que la **evaluación** es a menudo el mayor obstáculo; en algunas apps puede consumir **la mayor parte del esfuerzo de desarrollo** (Greg Brockman: “evals are surprisingly often all you need”). Este capítulo cubre **métodos** para evaluar modelos abiertos: cómo funcionan y dónde fallan. El capítulo 4 pasa a **usar** esos métodos para elegir modelos y montar un pipeline de evaluación en tu aplicación.

La evaluación no va aislada: sirve para **mitigar riesgos** y **detectar oportunidades**. Hay que saber **dónde falla el sistema** y diseñar la medición en torno a esos modos de fallo; a veces hace falta **rediseñar el sistema** para ganar visibilidad. Sin eso, ninguna pila de métricas hace el producto robusto.

---

## Retos de evaluar modelos fundacionales

Evaluar ML siempre fue difícil; los foundation models lo complicaron más.

**Tareas más difíciles exigen evaluación más difícil.** Un error de matemáticas de primaria es obvio; uno de nivel doctorado, no. Un resumen coherente pero incorrecto obliga a leer la fuente. Terence Tao comparó modelos de razonamiento tempranos con un “estudiante de posgrado mediocre”; surge la pregunta de quién evaluará modelos que superen a la mayoría de expertos.

**Salidas abiertas rompen benchmarks con ground truth.** La clasificación tiene etiquetas finitas; la generación admite infinitas respuestas válidas, así que no existe una lista exhaustiva de salidas correctas.

**Modelos caja negra** limitan lo inspeccionable (arquitectura, datos, entrenamiento). A menudo solo se juzga por **salidas**, mientras benchmarks públicos **saturan rápido** (GLUE → SuperGLUE, NaturalInstructions → SuperNaturalInstructions, MMLU → MMLU-Pro).

**El alcance se amplió:** modelos por tarea se miden en una tarea; los generalistas deben evaluarse en tareas conocidas **y** en capacidades nuevas —algunas por encima del humano medio.

El ecosistema reaccionó: papers sobre evaluación de LLM crecieron mucho en 2023; GitHub alberga decenas de repos de evaluación. Aun así, **inversión y herramientas siguen por detrás** del modelado y la orquestación; muchos equipos aún hacen **vibe check** o reutilizan un set pequeño de prompts. Este capítulo defiende un enfoque **sistemático**.

---

## El imperativo de la evaluación

Los fallos de alto impacto muestran que evaluar no es académico: es **negocio y seguridad**. “Resolver la evaluación” puede dominar el calendario.

No todo se reduce a un número. Dimensiones difíciles de cuantificar:

- **Satisfacción matizada** — técnicamente correcto pero tono inadecuado.
- **Exactitud factual en dominios abiertos** — sin una base de verdad única (p. ej. análisis histórico).
- **Evitar daño** — sesgos sutiles o consejos perjudiciales.
- **Consecuencias a largo plazo** — consejos que moldean decisiones durante semanas.

El libro se centra en evaluación **automática** (exacta y subjetiva); la **evaluación humana** sigue siendo necesaria en muchas apps —y para sanity checks.

---

## Métricas fundacionales: modelado de lenguaje

Muchos foundation models llevan un **modelo de lenguaje**; las métricas del LM correlacionan con el rendimiento aguas abajo (aunque el post-training debilita ese vínculo).

### Entropía

La **entropía** mide información en los **datos**, no en el modelo: cuán sorprendente es el siguiente token en promedio. Un idioma con dos tokens de posición (“upper” / “lower”) tiene menor entropía (1 bit) que cuatro tokens (“upper-left”, …) con 2 bits. Menor entropía → lenguaje más predecible.

### Entropía cruzada (cross-entropy)

La **entropía cruzada** mide qué tan difícil le resulta al **modelo** predecir la distribución de entrenamiento: `H(P,Q) = H(P) + D_KL(P||Q)`. El entrenamiento la minimiza; un ajuste perfecto iguala la entropía de los datos. **BPC** y **BPB** normalizan entre tokenizadores para comparar modelos. También se relaciona con **eficiencia de compresión**.

### Perplejidad (PPL)

La **perplejidad** es `2^H` (o `e^H` con nats en PyTorch/TensorFlow): de forma intuitiva, el **número efectivo de opciones** para el siguiente token. PPL = 10 ≈ elegir entre 10 tokens igualmente probables.

**Reglas de interpretación:**

- Texto más **estructurado** (p. ej. HTML) → menor PPL esperada.
- **Vocabulario** mayor → mayor PPL.
- **Contexto** más largo → menor PPL.

**Usos en ingeniería:**

- **Proxy de capacidad** — menor PPL suele correlacionar con modelos más fuertes (cuando se reporta).
- **Contaminación de datos** — PPL sospechosamente baja en un benchmark sugiere que estaba en entrenamiento.
- **Entradas anómalas** — texto sin sentido → PPL muy alta.
- **Deduplicación** — añadir datos solo si la PPL del material nuevo es alta.

**Advertencia crítica:** **SFT** y **RLHF** suelen **subir** la PPL: el modelo optimiza utilidad en la tarea, no predicción cruda del siguiente token. La **cuantización** también puede alterar la PPL.

Las APIs comerciales no siempre exponen **logprobs**, necesarios para calcular PPL en texto arbitrario.

---

## Métricas de evaluación exacta

Conviene distinguir evaluación **exacta** (juicio sin ambigüedad) de **subjetiva** (depende del evaluador o del juez). Esta sección trata **generación abierta**; tareas cerradas (clasificación, intent) están mejor resueltas en otros sitios.

### Corrección funcional

El estándar de oro cuando se puede automatizar: **¿el sistema hizo lo que debía?**

- **Código:** ejecutar el código generado (tests, intérprete). Benchmarks como **HumanEval**, **MBPP**, **Spider**, **BIRD-SQL**, **WikiSQL** usan **pass@k** — fracción de problemas resueltos si alguna de *k* muestras pasa todos los tests.
- **Juegos / optimización:** puntuación en Tetris, energía ahorrada por un planificador, etc.

Cuando la IA solo cubre parte del flujo, juzgar la **parte** puede ser más difícil que el resultado final (ajedrez: ganar/perder vs. puntuar una jugada).

### Similitud frente a datos de referencia

Si no se puede ejecutar la corrección, se compara con **referencias** (ground truth) en pares `(entrada, respuestas de referencia)`.

**Formas de comparar:**

1. Humano o juez IA (“¿mismo significado?”).
2. **Coincidencia exacta** — útil en respuestas cortas; frágil con formato; “contiene 1929” puede aceptar fechas incorrectas.
3. **Similitud léxica** — solapamiento de tokens o **n-gramas** (BLEU, ROUGE, METEOR++, TER, CIDEr). Penaliza paráfrasis válidas; exige referencias exhaustivas; **OpenAI encontró BLEU similar en soluciones correctas e incorrectas en HumanEval**.
4. **Similitud semántica** — **embeddings** + similitud coseno (BERTScore, MoverScore). Más robusta a la paráfrasis; depende del modelo de embeddings y del coste de cómputo.

Esas medidas también sirven para retrieval, ranking, clustering, detección de anomalías y deduplicación (el libro las retoma después).

**Embeddings (bosquejo):** vectores que capturan significado; modelos especializados (BERT, CLIP, Sentence Transformers, APIs de embedding). Buenos embeddings acercan textos similares. **CLIP** alinea imagen y texto en un espacio conjunto para búsqueda multimodal.

---

## El juez subjetivo: IA como evaluador

Usar IA para calificar IA (**AI as a judge** / **LLM as a judge**) se volvió práctico con **GPT-3 (2020)** y muy extendido en producción hacia 2023–2024 (p. ej. LangChain: ~58% de evals en su plataforma con jueces IA).

### Por qué usarlo

- Rápido y barato frente a humanos; funciona **sin referencias** en producción.
- Criterios flexibles: corrección, toxicidad, alucinación, coherencia con un rol, confianza en una imagen, etc.
- Puede **explicar** decisiones (útil para auditoría).
- Estudios reportan alta correlación con humanos en algunos benchmarks (p. ej. GPT-4 en MT-Bench; AlpacaEval vs. Chatbot Arena).

### Cómo usarlo

Tres patrones habituales:

1. **Puntuación individual** — calificar una respuesta (p. ej. 1–5) dada la pregunta.
2. **Con referencia** — True/False o score frente a una respuesta canónica.
3. **Por pares** — elegir A o B; alimenta datos de preferencia para alineación y ranking comparativo.

Un juez es un **sistema** (modelo + prompt + muestreo). El prompt debe definir **tarea**, **criterios** y **puntuación** (clasificación suele ir mejor que números crudos; 1–5 discreto mejor que escalas continuas amplias). **Ejemplos en el prompt** mejoran consistencia (a mayor coste).

Los criterios integrados varían por herramienta (Azure: groundedness, relevance…; Ragas: faithfulness…; LangChain: harmfulness, helpfulness…) — **las puntuaciones no son comparables entre herramientas**.

### Limitaciones y sesgos

- **Inconsistencia** — mismo juez, misma entrada, distintas ejecuciones o prompts.
- **Ambigüedad de criterios** — “faithfulness” difiere entre MLflow, Ragas, LlamaIndex (1–5 vs. 0/1 vs. YES/NO).
- **Deriva** — cambios en prompt o modelo rompen tendencias mes a mes. **No confíes en un juez si no ves modelo y prompt.**
- **Coste y latencia** — juzgar cada respuesta puede duplicar gasto de API; varios criterios multiplican llamadas; guardrails en producción suman latencia.
- **Sesgos:** **auto-sesgo** (el modelo favorece sus respuestas), **sesgo de posición** (favorece la primera respuesta; opuesto al sesgo de recencia humano), **sesgo de verbosidad** (respuestas largas ganan aunque sean incorrectas). Mitigar con orden alternado, jueces especializados o modelos débiles en spot-check.

**¿Qué modelo juzga?** Jueces más fuertes correlacionan mejor con humanos pero cuestan más; **jueces débiles** o **especializados** (reward models, jueces con referencia como BLEURT/Prometheus, **modelos de preferencia** como PandaLM/JudgeLM) pueden ser más baratos y específicos. La **autocrítica** ayuda en sanity checks y bucles de revisión.

Los jueces IA deben **complementar** métricas exactas y evaluación humana — no sustituirlas.

---

## La arena competitiva: ranking con evaluación comparativa

A menudo la pregunta no es “¿cuánto saca el modelo A?” sino **“¿A es mejor que B para nosotros?”**

### Evaluación puntual vs. comparativa

- **Puntual:** cada modelo se puntúa por separado (p. ej. accuracy en MMLU) — como puntuar patinadores en técnica y arte por separado.
- **Comparativa:** preferencia lado a lado — más fácil para calidad subjetiva (creatividad, utilidad).

**Chatbot Arena (LMSYS):** respuestas anónimas por pares, voto del usuario, luego se revelan los modelos. Miles de **matches** alimentan algoritmos de rating (**Elo**, **Bradley–Terry**, **TrueSkill**). La arena pasó de Elo a Bradley–Terry por sensibilidad al orden de partidas. Se asume: mayor ranking → debería ganar >50% de enfrentamientos futuros.

**No es lo mismo que A/B testing** — en comparativa se ven varias salidas a la vez.

**Precaución:** muchas preguntas exigen **corrección**, no preferencia (“¿relación entre radiación móvil y tumores?”). El voto por preferencia falla si el usuario no es experto — encaja cuando la IA asiste tareas que el usuario ya sabe hacer.

### Problemas de ingeniería

1. **Escalabilidad** — *N* modelos → *N(N−1)/2* pares; la transitividad (A>B, B>C ⇒ A>C) puede no cumplirse con preferencias humanas o prompts/evaluadores distintos. Modelos nuevos deben enfrentarse a muchos existentes; **modelos privados** requieren arenas internas o leaderboards de pago.

2. **Estandarización** — el crowdsourcing captura diversidad pero con poco **control de calidad**: sin fact-check, preferencias tóxicas, datos contaminados (“hola”/“hi” sobrerepresentados, acertijos repetidos). El ranking puede no reflejar **RAG** con tus documentos. Mitigaciones: filtrar prompts difíciles, evaluadores de confianza (Scale), comparaciones dentro del producto (ruidosas si el usuario adivina).

3. **“¿Y qué?”** — un 51% de victorias no dice **magnitud** ni calidad absoluta (ambos malos vs. ambos buenos). Es difícil traducir win rate a métricas de negocio (p. ej. % de tickets resueltos) o **coste–beneficio** si B cuesta el doble.

### Por qué sigue importando

Captura **preferencia humana**, no satura como benchmarks fijos, es más difícil de “entrenar para el test”. Complementa benchmarks exactos y A/B — no los reemplaza.

---

## Síntesis: construir un pipeline robusto

Ninguna métrica basta sola. Un stack práctico **superpone** métodos por prioridad:

**Ejemplo — text-to-SQL sobre base de ventas** (SQL correcto, consultas eficientes, confianza de usuarios no técnicos):

| Etapa | Rol | Métodos |
|-------|-----|---------|
| **1. Funcionalidad núcleo** | Puerta no negociable | **Corrección funcional** — ¿el SQL ejecuta y devuelve el resultado correcto? |
| **2. Calidad escalable** | Amplitud a menor coste | **Jueces IA** (y similitud semántica donde haya referencias) |
| **3. Gold standard** | Confianza final | **Evaluación humana** en casos críticos o ambiguos |

El mismo patrón generaliza: **comprobaciones exactas/ejecutables primero**, señales subjetivas automáticas después, humanos donde el riesgo o la ambigüedad lo exijan. Añadir **métricas de LM** (PPL) para selección de modelo, contaminación e higiene de datos; **evaluación comparativa** cuando la pregunta de negocio es preferencia relativa entre candidatos.

Combinar **ranking comparativo** con **umbrales absolutos** (tasa de pass funcional, latencia, coste) antes de desplegar.

---

## Cierre del capítulo

El capítulo 3 traza el **mapa de evaluación** para foundation models: por qué los fallos importan, por qué las salidas abiertas resisten benchmarks clásicos, **métricas de LM** (entropía, entropía cruzada, perplejidad, BPC/BPB), vías **exactas** (corrección funcional, similitud léxica y semántica), **jueces IA** (promesa, límites, sesgos, jueces especializados) y **ranking comparativo** (preferencia estilo Arena, algoritmos de rating, escalabilidad e interpretación).

Las métricas de lenguaje y la similitud diseñada a mano son maduras; **IA como juez** y **evaluación comparativa** escalaron con los foundation models. Los pipelines fiables las **combinan**; el capítulo 4 muestra cómo operacionalizarlo para elegir modelo y evaluar la aplicación.

---

## Notas finales

Lo que me queda de este capítulo es que la evaluación es donde el AI engineering deja de ser demo y pasa a ser **ingeniería**. Los ejemplos de Air Canada y los abogados recuerdan que una salida incorrecta tiene **coste legal y reputacional**, no solo una mala puntuación de UX. Eso me empuja a nombrar modos de fallo al inicio (hechos alucinados, errores de política, consejo dañino) en lugar de optimizar un leaderboard que no refleja a nuestros usuarios ni nuestros datos.

En **métricas**, ordeno mentalmente por capas. **Perplejidad** y afines sirven para comparar LMs base y detectar contaminación, pero no interpretaré PPL alta tras instruction tuning como “peor.” En producto, gana la **corrección funcional** cuando puedo ejecutar la salida (SQL, código, APIs). La **similitud semántica** supera a BLEU/ROUGE cuando hay referencias pero vale la paráfrasis; los **jueces IA** cubren huecos a escala, con sesgo de verbosidad y posición en mente —y solo con una especificación de juez congelada y auditable.

Para **elegir modelo**, los leaderboards comparativos responden “¿A vs. B?” no “¿suficientemente bueno?”. Una victoria estrecha frente a un baseline débil o un precio 2× exigen **umbrales absolutos** y métricas de negocio. Montar la evaluación como **pipeline** (ejecutar → juez automático → humano puntual) es como desplegaría algo tipo text-to-SQL: si la consulta no corre bien, lo demás no compensa.

**Referencia:** Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 3: Evaluation Methodology.
