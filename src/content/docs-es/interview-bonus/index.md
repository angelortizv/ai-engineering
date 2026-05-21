---
title: "Bonus entrevistas"
description: "Preguntas frecuentes tipo entrevista y conocimiento general de AI engineering, alineadas con AI Engineering de Chip Huyen (2025) y estas notas."
order: 11.5
sidebar:
  label: "Bonus entrevistas"
---

## Introducción

**Página bonus** — preguntas que suelen salir en **entrevistas técnicas**, diseño de sistemas o conversaciones del tipo “explícamelo como si me fueras a contratar”. Las respuestas son concisas y enlazan ideas de *AI Engineering* (Huyen, 2025) y las [notas por capítulo](/ai-engineering/docs/es)—no sustituyen el libro.

> **Comprobación de cordura:** *«¿Cómo resolverías esto sin usar un LLM?»* Si la respuesta honesta es «no se puede», quizá el problema está mal acotado. Software clásico, reglas, recuperación sin generación o modelos pequeños especializados suelen tener sitio en el diseño.

Usa la **búsqueda** del sitio (Pagefind) para saltar a un tema. Definiciones: [Glosario](/ai-engineering/docs/es/glossary).

---

## Fundamentos de LLM

### ¿Qué es la tokenización y cómo afecta la generación?

La **tokenización** divide el texto en subpalabras con las que se entrenó el modelo (BPE, SentencePiece, etc.). Impacta **tamaño de vocabulario**, **presupuesto de contexto** (tokens ≠ palabras), **coste** (facturación por token) y **multilingüe** (algunos idiomas necesitan más tokens por idea). Cadenas raras pueden partirse en muchos tokens y consumir contexto. La generación opera en espacio de tokens: el modelo predice el siguiente; el decodificador vuelve a texto. Ver [Cap. 2](/ai-engineering/docs/es/understanding-foundation-models).

### ¿Cómo funcionan realmente los embeddings?

Un **embedding** es un vector denso de un codificador (o modelo de embeddings) que acerca significados similares en el espacio vectorial. En LLM, «embedding» suele referirse a **vectores de texto para recuperación** (encoders duales, etc.), no solo a estados internos. La calidad depende del **objetivo de entrenamiento**, **dominio** e **idioma**. El mismo texto puede tener vectores distintos si cambia el modelo de embeddings—planifica migraciones. Ver [Cap. 6](/ai-engineering/docs/es/rag-and-agents) y [Glosario](/ai-engineering/docs/es/glossary).

### ¿Qué papel tienen la atención y la codificación posicional?

La **autoatención** permite que cada token atienda a otros y construya representaciones contextuales. El coste escala ~cuadráticamente con la longitud (mitigado con FlashAttention, ventanas, etc.). La **codificación posicional** (RoPE, ALiBi…) aporta **orden**—sin ella la atención es invariante a permutaciones. Los modelos de contexto largo siguen teniendo **límites efectivos** y coste. Ver [Cap. 2](/ai-engineering/docs/es/understanding-foundation-models).

### ¿Qué cambia en el fine-tuning? (optimizadores, schedulers, congelar capas)

El **fine-tuning** actualiza parte o todo el modelo con datos de tarea. Eliges **qué entrenar** (modelo completo vs. adaptadores vs. últimas capas), **optimizador** (a menudo AdamW), **schedule de learning rate**, **batch** (limitado por memoria) y **regularización**. **Congelar capas** estabiliza capas tempranas y entrena las posteriores o cabezas—habitual en PEFT. Sin eval → **sobreajuste** y **olvido**. Ver [Cap. 7](/ai-engineering/docs/es/finetuning) y [Cap. 8](/ai-engineering/docs/es/dataset-engineering).

### LoRA vs QLoRA vs fine-tune completo — ¿tradeoffs?

| Enfoque | Parámetros entrenables | Memoria | Calidad / flexibilidad | Cuándo |
| --- | --- | --- | --- | --- |
| **Fine-tune completo** | Todos | Máxima | Máxima adaptación | Muchos datos de dominio, stack propio |
| **LoRA** | Adaptadores de bajo rango | Menor | Fuerte en estilo/formato/dominio | PEFT por defecto en muchas apps |
| **QLoRA** | LoRA sobre base **cuantizada** | Menor huella GPU | Buena; evaluar tareas difíciles | GPUs modestas, varios adaptadores |

El fine-tune completo es caro y arriesga **olvido catastrófico**; LoRA/QLoRA despliegan más rápido. Compara siempre con **eval privado**. Ver [Cap. 7](/ai-engineering/docs/es/finetuning).

### ¿Diferencia entre latencia de prefill y decode?

**Prefill** procesa el prompt (a menudo limitado por cómputo). **Decode** genera token a token (a menudo limitado por ancho de banda de memoria). El usuario nota **TTFT** y **TPOT**. Las optimizaciones difieren: batching de prefill, KV cache en decode, decodificación especulativa. Ver [Cap. 9](/ai-engineering/docs/es/inference-optimization).

### ¿Por qué la temperatura afecta «creatividad» y fiabilidad?

**Temperatura** escala los logits antes del softmax: más alta → distribución más plana → más aleatoriedad; más baja → más determinismo. **No corrige** alucinaciones; para hechos usa **RAG**, restricciones y **eval**. Para reproducibilidad: `temperature` baja, `seed` si existe, salidas estructuradas. Ver [Cap. 2](/ai-engineering/docs/es/understanding-foundation-models) y [Cap. 5](/ai-engineering/docs/es/prompt-engineering).

---

## Prompting e ingeniería de contexto

### Few-shot vs zero-shot — ¿dónde funciona mejor cada uno?

**Zero-shot**: instrucciones + priors del modelo—barato, iteración rápida, tareas que el modelo ya domina. **Few-shot**: ejemplos en contexto—ayuda **formato**, **tono**, **casos límite** y **uso de herramientas** sin actualizar pesos; cuesta tokens y puede **sesgar** hacia los ejemplos. Empieza con zero-shot + esquema claro; añade few-shot cuando el eval muestre errores sistemáticos. Ver [Cap. 5](/ai-engineering/docs/es/prompt-engineering).

### ¿Cómo diseñar system prompts robustos entre usuarios?

Trata el system prompt como **especificación de producto**: rol, restricciones, formato, reglas de rechazo. Corto y **testeable**; versiona como código; **eval de regresión** al cambiar. Separa **política estable** (system) de **hechos volátiles** (RAG/mensaje usuario). **Guardrails** fuera del prompt para PII/seguridad. Ver [Cap. 5](/ai-engineering/docs/es/prompt-engineering) y [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

### ¿Cómo hacer la salida determinista?

**Temperatura baja**, **semilla fija**, modo **JSON/esquema**, decodificación restringida, prompts **canónicos**, **validación** posterior (parsear JSON, reintentar). Registra hash de prompt + versión de modelo. En producción suele bastar **misma distribución** en el eval, no strings idénticos bit a bit. Ver [Cap. 5](/ai-engineering/docs/es/prompt-engineering) y [Cap. 9](/ai-engineering/docs/es/inference-optimization).

### ¿Cómo versionar y rellenar contexto que cambia?

Guarda **plantillas** y **snapshots** con IDs en observabilidad. Al cambiar docs o políticas: **versiona** corpus, **re-embed** por lotes, índice **blue/green**, **eval de recuperación** antes del corte. En contexto de usuario: **marca de tiempo** y caducidad. Ver [Cap. 6](/ai-engineering/docs/es/rag-and-agents) y [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

### ¿Cómo construir y mantener memoria?

**Corto plazo** (conversación en ventana) vs. **largo plazo** (vector store, perfil, resúmenes). Escribe memoria solo de hechos **verificados** o herramientas; resume para ahorrar tokens. Etiqueta **fuente**, **tiempo**, **confianza**; permite borrar (privacidad). **Decae** hilos viejos. Ver [Cap. 6](/ai-engineering/docs/es/rag-and-agents) y [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

### ¿Cuándo usar chain-of-thought (CoT) en producción?

CoT ayuda en **razonamiento multi-paso** pero suma **latencia y tokens**. Úsalo si el eval lo justifica; oculta el scratchpad si hace falta; prefiere **pasos estructurados** o **herramientas** para fiabilidad. No sustituye **RAG** para hechos. Ver [Cap. 5](/ai-engineering/docs/es/prompt-engineering).

---

## Sistemas RAG

### Estrategia de chunking — ¿por longitud, semántica o estructura?

Chunks **conscientes de estructura** (títulos, secciones) suelen citar mejor que trozos fijos ciegos. **Por longitud** con solapamiento es un buen baseline. **Semántico** ayuda en documentos heterogéneos pero cuesta cómputo. Ajusta con **eval de recuperación** (precision@k, nDCG). Ver [Cap. 6](/ai-engineering/docs/es/rag-and-agents).

### ¿Cómo elegir vector DB (Chroma, Pinecone, OpenSearch…)?

Mira **escala**, **SLO de latencia**, **filtros de metadatos**, **búsqueda híbrida**, **operación** (managed vs. propio), **coste** y **cumplimiento**. OpenSearch/Elasticsearch brillan en **híbrido**; Chroma/pgvector valen para prototipos. Importan más **chunking, embeddings y eval** que la marca del DB. Ver [Cap. 6](/ai-engineering/docs/es/rag-and-agents).

### ¿Actualizar embeddings con cero downtime?

Sí: **índices versionados**, construye **v2** en paralelo, **doble consulta** en validación, conmuta con flag, retira v1. Re-embed por **lotes**; guarda `embedding_model_version` en cada vector. Ver [Cap. 6](/ai-engineering/docs/es/rag-and-agents).

### ¿Cómo evaluar calidad de recuperación?

Conjunto **etiquetado** (consulta, docs relevantes). **precision@k**, **recall@k**, **MRR**, **nDCG**. **Reranker** si el bi-encoder es ruidoso. Métricas end-to-end de **fidelidad** y **citas**. Registra chunks usados. Ver [Cap. 3](/ai-engineering/docs/es/evaluation-methodology), [Cap. 4](/ai-engineering/docs/es/evaluating-modern-ai-systems), [Cap. 6](/ai-engineering/docs/es/rag-and-agents).

### RAG vs fine-tuning — ¿cuándo cada uno?

| Necesidad | Preferir |
| --- | --- |
| Docs frescos/privados | **RAG** |
| Estilo, formato, patrones de herramientas | **Prompts** → luego **finetune** |
| Comportamiento en pesos, offline | **Finetune** (a menudo LoRA) |

A menudo **ambos**. El finetune no sustituye una base de conocimiento ausente. Ver [Cap. 6](/ai-engineering/docs/es/rag-and-agents) y [Cap. 7](/ai-engineering/docs/es/finetuning).

### ¿En qué se diferencian agentes de una sola llamada RAG?

Los **agentes** iteran: planificar → actuar (herramientas) → observar. Cambian **latencia y coste** por **flexibilidad**. Riesgos: errores de herramientas, bucles. Empieza con **recuperar-y-generar**; añade agentes si el eval exige multi-paso. Ver [Cap. 6](/ai-engineering/docs/es/rag-and-agents).

---

## MLOps y LLMOps

### Bosqueja un pipeline: datos → modelo → serving → feedback

1. **Métricas** de producto (Cap. 3–4).  
2. **Ingesta** y limpieza (Cap. 8).  
3. **Adaptación**: prompts → RAG → finetune (Cap. 5–7).  
4. **Serving** con gateway y caché (Cap. 9–10).  
5. **Observabilidad** (Cap. 10).  
6. **Feedback** → eval/datos → redespliegue (**flywheel** con cuidado). Ver [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

### ¿Cómo monitorizar deriva o alucinaciones?

Proxies **online**: valoraciones, ediciones, escalaciones, groundedness, hit rate de recuperación, latencia, coste por éxito. **Offline**: golden sets por versión de modelo/prompt/índice. Alertas por **cambios estadísticos**. Ver [Cap. 4](/ai-engineering/docs/es/evaluating-modern-ai-systems) y [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

### ¿Cómo registrar prompts y salidas?

**Request ID**, versión de modelo, plantilla, IDs de chunks, latencia, tokens, salida, llamadas a herramientas, copias **sin PII** donde aplique. Retención y control de acceso. Trazas estilo OpenTelemetry. Ver [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

### CI/CD en flujos LLM — ¿qué cambia respecto al ML clásico?

Promoción por **suites de eval** y artefactos de **prompt/índice**, no solo tests unitarios. Umbral por **no determinismo**. Versionar **prompts, embeddings, índices y modelos** juntos. Canary y rollback. Ver [Cap. 4](/ai-engineering/docs/es/evaluating-modern-ai-systems) y [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

### ¿Evaluar sin respuestas doradas?

**Rúbricas**, **AI-as-judge** (con sesgos controlados), comparación **por pares**, tests **funcionales** (ejecutar código/SQL), revisión humana estratificada. Ver [Cap. 3](/ai-engineering/docs/es/evaluation-methodology) y [Cap. 4](/ai-engineering/docs/es/evaluating-modern-ai-systems).

---

## Coste y latencia

### ¿Cómo reducir uso de tokens?

Prompts más cortos, **resumir** historial, menos chunks, comprimir salidas de herramientas, modelos baratos para routing, salidas **estructuradas**, **caché de prefijos**. Mide tokens por **tarea exitosa**. Ver [Cap. 9](/ai-engineering/docs/es/inference-optimization).

### ¿Cuándo cuantizar?

Al **autoalojar** cuando **memoria o coste** dominan y el eval acepta la pérdida (INT8/INT4, etc.). **QLoRA** cuantiza para entrenar adaptadores. Re-benchmark **tus** tareas. Ver [Cap. 9](/ai-engineering/docs/es/inference-optimization).

### Estrategia de batching y caché

**Batching continuo**, colas separadas prefill/decode, **KV cache**, **prompt caching** en APIs. **Caché semántica** con cuidado (obsolescencia). Ver [Cap. 9](/ai-engineering/docs/es/inference-optimization).

### APIs hospedadas vs modelos open source

| API | Open source / propio |
| --- | --- |
| Ruta rápida, calidad frontera | Residencia de datos, coste a escala, adaptadores |

Híbrido: **router** a modelo pequeño vs. frontera. Ver [Cap. 1](/ai-engineering/docs/es/introduction-to-building-ai-applications-with-foundation-models) y [Cap. 9](/ai-engineering/docs/es/inference-optimization).

---

## Diseño de sistemas

### ¿Cómo hacer el sistema más determinista y menos frágil?

Acota la tarea, salidas con **esquema**, validación + **reintento**, RAG con citas, **feature flags**, modelos de respaldo. Prefiere **workflow** a autonomía abierta en alto riesgo. Ver [Cap. 5](/ai-engineering/docs/es/prompt-engineering) y [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

### ¿Fallback si el LLM falla a mitad de tarea?

**Reintentos**, modelo **backup** más pequeño, respuesta **cacheada**, UX degradada, **reglas**, resultado **parcial** con estado claro. En agentes: **checkpoint** y límites de pasos/tiempo. Ver [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

### ¿Resolver sin LLM ni vector DB?

A menudo sí: **SQL + búsqueda full-text**, **reglas**, **plantillas**, clasificadores pequeños. Los LLM brillan en lenguaje ambiguo o cambiante—not en ser la única base de datos. Ver [Cap. 1](/ai-engineering/docs/es/introduction-to-building-ai-applications-with-foundation-models).

### ¿SQL, NoSQL o vector?

**SQL**: transacciones e informes. **NoSQL**: esquemas flexibles, alto volumen de escritura. **Vector**: similitud en texto—casi siempre **junto** a SQL/ES. **BM25 + vector** es habitual. Ver [Cap. 6](/ai-engineering/docs/es/rag-and-agents).

### ¿Dónde encajan los guardrails?

**Entrada**: PII, inyección, política. **Salida**: moderación, formato, listas de bloqueo. Fuera del modelo cuando sea posible. Ver [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

---

## Escenarios reales

### Cambia el modelo de embeddings — ¿migración segura?

1. Fijar `embedding_model_id`.  
2. **Índice nuevo** con re-embed completo.  
3. Comparar **eval** viejo vs. nuevo.  
4. **Canary**; lectura dual si hace falta.  
5. Retirar índice antiguo. Ver [Cap. 6](/ai-engineering/docs/es/rag-and-agents).

### Fine-tune con comportamiento de usuario y despliegue

Datos con **opt-in**; filtrar **PII**; definir comportamiento objetivo (no clicks crudos sesgados). **LoRA** + eval held-out; **versionar** adaptadores; flag y monitorizar **regresiones** y bucles de feedback. Revisión legal/privacidad. Ver [Cap. 7](/ai-engineering/docs/es/finetuning), [Cap. 8](/ai-engineering/docs/es/dataset-engineering), [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

### ¿Más barato sin matar calidad?

**Coste por tarea exitosa**. Modelo barato para routing/borrador; caché; menos contexto; mejor recuperación; lotes offline; **cuantización**; menos pasos de agente. A/B con métricas de **calidad**. Ver [Cap. 9](/ai-engineering/docs/es/inference-optimization).

### Depurar salidas incorrectas del LLM

1. Reproducir con **traza** guardada.  
2. Clasificar: **recuperación**, **prompt**, **alucinación**, **herramienta**, **post-proceso**.  
3. Revisar **chunks** y citas.  
4. A/B temperatura / prompt / modelo.  
5. Añadir caso al **eval de regresión**. Ver [Cap. 4](/ai-engineering/docs/es/evaluating-modern-ai-systems) y [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

### «El bot olvidó lo de ayer»

Truncado de ventana, memoria larga no escrita, **session ID** incorrecto, caché obsoleta, resumen que pierde entidades. Revisa el **payload** real de la última petición. Ver [Cap. 6](/ai-engineering/docs/es/rag-and-agents).

### Quieren «IA 100% precisa»

Metas **medibles** por riesgo (citas obligatorias, revisión humana en alto impacto). Error residual, monitorización y escalación. Ver [Cap. 3](/ai-engineering/docs/es/evaluation-methodology).

---

## Preguntas extra (evaluación, seguridad, producto)

### ¿Qué es goodput?

Trabajo **útil** por dólar o segundo—not tokens/s en bruto. Ver [Glosario](/ai-engineering/docs/es/glossary) y [Cap. 9](/ai-engineering/docs/es/inference-optimization).

### Contaminación de eval y sobreajuste a benchmarks

Hold-out por **tiempo** y **fuente**; prompts tipo usuario privados; cuidado con **sesgo de verbosidad** en jueces IA. Ver [Cap. 3](/ai-engineering/docs/es/evaluation-methodology).

### Bucle de feedback degenerado

El producto refuerza errores en los logs. Mitiga con **etiquetas humanas**, muestreo diverso y eval **offline**. Ver [Cap. 10](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback).

### ¿Construir o comprar modelos?

**Comprar (API)** por velocidad y calidad. **Autoalojar** por datos, economía unitaria y adaptadores. **Comprar primero**, luego híbrido. Ver [Cap. 4](/ai-engineering/docs/es/evaluating-modern-ai-systems).

### Acotar un MVP de IA

**Crawl–walk–run**: un flujo, métrica clara, modelo mínimo que pase eval, revisión manual en bordes; RAG/agentes solo si el eval lo exige. Ver [Cap. 1](/ai-engineering/docs/es/introduction-to-building-ai-applications-with-foundation-models).

---

## Relacionado

- [Mapa del libro](/ai-engineering/docs/es/book-map) — rutas por objetivo
- [Glosario](/ai-engineering/docs/es/glossary) — TTFT, LoRA, goodput, …
- [Modo estudio](/ai-engineering/docs/es/introduction-to-building-ai-applications-with-foundation-models/study) — cuestionarios por capítulo
- [Epílogo](/ai-engineering/docs/es/epilogue) — después del libro

---

## Referencias

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.

- [O’Reilly — *AI Engineering*](https://www.oreilly.com/library/view/ai-engineering/9781098166304/)
- [Repositorio del libro — aie-book](https://github.com/chiphuyen/aie-book)
