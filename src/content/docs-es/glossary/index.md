---
title: "Glosario"
description: "Términos clave de AI Engineering (Huyen, 2025) y de estas notas."
order: 11
---

## Introducción

Definiciones breves de términos usados en las [notas por capítulo](/ai-engineering/docs/es). La redacción sigue *AI Engineering* (Huyen, 2025) salvo que se indique lo contrario.

Usa la **caja de búsqueda** sobre la lista para filtrar por término o definición (también indexado por la búsqueda del sitio con Pagefind).

---

## A–C

**AI-as-a-judge** — Usar un modelo fundacional para puntuar o comparar salidas según rúbricas o referencias; escala bien pero introduce sesgos (verbosidad, posición, auto-preferencia).

**AI engineering** — Construir aplicaciones sobre modelos fundacionales disponibles (adaptación, evaluación, producto), distinto de entrenar modelos frontera desde cero.

**Intensidad aritmética** — FLOPs por byte movido; en análisis **roofline** para ver si el cuello de botella es cómputo o ancho de banda.

**LM autoregresivo** — Predice el siguiente token solo con tokens previos; estándar en generación de texto (frente a modelos enmascarados como BERT).

**Bits por byte (BPB)** — Entropía cruzada en bits por byte; más comparable entre tokenizadores que la perplejidad sola.

**Compute-bound** — Tiempo dominado por FLOPs (p. ej. **prefill** del LLM).

**Longitud de contexto** — Máximo de tokens en un forward; condiciona coste y diseño de recuperación.

**Entropía cruzada** — Pérdida alineada con máxima verosimilitud del siguiente token; relacionada con perplejidad.

---

## D–G

**Data flywheel** — Uso del producto → feedback/logs → mejores datos/modelos → mejor producto.

**Bucle de feedback degenerado** — Los usuarios solo ven salidas moldeadas por feedback sesgado pasado, reforzando errores (cap. 10).

**Destilación** — Entrenar un modelo pequeño imitando uno grande (logits o salidas).

**Embedding** — Vector denso de texto (u otra modalidad) para búsqueda por similitud y jueces.

**Modelo fundacional** — Modelo grande y general (a menudo multimodal) que otros adaptan con prompts, RAG o *finetuning*.

**Corrección funcional** — Evaluar ejecutando la salida (p. ej. SQL/código generado), no solo comparando cadenas.

**Goodput** — Trabajo útil por tiempo/coste en serving (no solo tokens/s si muchos se desperdician).

**Guardrails** — Filtros de entrada/salida para seguridad, PII, política y calidad.

---

## H–M

**Alucinación** — Contenido plausible pero falso o sin soporte; se mitiga con RAG, evaluación y guardrails.

**Human-in-the-loop (HITL)** — Humanos revisan, corrigen o aprueban salidas del modelo.

**Instruction finetuning (SFT)** — Entrenamiento supervisado en pares (instrucción, respuesta) tras el preentrenamiento.

**KV cache** — Activaciones K/V guardadas en decodificación autoregresiva para no recomputar prefijos.

**LoRA** — Adaptadores de bajo rango; **PEFT** con pocos parámetros entrenables.

**MFU** — Utilización de FLOP/s del modelo frente al pico del hardware.

**MBU** — Analogía de utilización de ancho de banda de memoria.

**Memory bandwidth-bound** — Tiempo dominado por mover pesos/activaciones (p. ej. **decode** del LLM).

**MMLU** — Benchmark multichoice multidisciplinar; filtro grueso, no contrato de producto.

**Model-as-a-service** — APIs de proveedor en lugar de autoalojar todo el stack de entrenamiento.

---

## N–R

**NIAH (needle in a haystack)** — Prueba de contexto largo con un dato oculto en ruido.

**PEFT** — *Finetuning* eficiente en parámetros (LoRA, adaptadores, etc.).

**Perplejidad (PPL)** — exp(entropía cruzada); menor suele ser mejor; interpretar con cuidado tras chat tuning.

**Prefill** — Procesamiento paralelo del prompt para llenar KV cache; suele ser **compute-bound**.

**Prompt caching** — Reutilizar KV de prefijos idénticos entre peticiones.

**Prompt injection** — Texto no confiable en contexto que anula instrucciones previstas.

**QLoRA** — LoRA con pesos base cuantizados para menos memoria.

**RAG** — Generación aumentada por recuperación: buscar contexto y luego generar.

**ReAct** — Patrón de agente: alternar **Thought → Action → Observation** hasta terminar.

**RLHF / preference finetuning** — Entrenar con preferencias humanas o de modelo (DPO, etc.).

**Roofline** — Gráfica de FLOP/s alcanzable vs. intensidad aritmética para localizar cuellos de botella.

---

## S–Z

**Autosupervisión** — Etiquetas del propio dato (siguiente token); permite preentrenamiento a escala web.

**Decodificación especulativa** — Modelo borrador propone tokens; el objetivo verifica en paralelo.

**Salida estructurada** — JSON/esquema forzado (gramática, herramientas, APIs).

**TTFT** — Latencia hasta el primer token generado; dominada por prefill.

**TPOT / TBT** — Tiempo por token de salida tras el primero.

**Token** — Subpalabra/palabra en el vocabulario; base de facturación y límites de contexto.

**Uso de herramientas** — El modelo emite llamadas estructuradas ejecutadas por tu runtime.

**Top-p / top-k** — Filtros de muestreo que recortan la cola de la distribución del siguiente token.

**Transfer learning** — Partir de pesos preentrenados (el *finetuning* es una forma).

---

## Relacionado

- [Resumen](/ai-engineering/docs/es) — índice de capítulos
- [Bonus entrevistas](/ai-engineering/docs/es/interview-bonus) — preguntas tipo entrevista
- [Epílogo](/ai-engineering/docs/es/epilogue) — cierre y [repositorio del libro](https://github.com/chiphuyen/aie-book)
- [Optimización de inferencia](/ai-engineering/docs/es/inference-optimization) — TTFT, TPOT, MFU, prefill/decode
- [Finetuning](/ai-engineering/docs/es/finetuning) — PEFT, LoRA, QLoRA, memoria

---

## Referencias

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.

- [Repositorio del libro — aie-book](https://github.com/chiphuyen/aie-book)
