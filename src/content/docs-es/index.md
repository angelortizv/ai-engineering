---
title: "Panorama"
description: "Notas capítulo por capítulo del libro AI Engineering de Chip Huyen (O'Reilly, 2025)—modelos fundacionales hasta producción."
order: 0
---

## De qué trata este sitio

Esta documentación reúne **resúmenes y apuntes organizados por capítulo** a partir de:

**Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.**

El objetivo es tener un solo lugar para repasar el libro en orden de lectura: qué son los modelos fundacionales, cómo evaluarlos y adaptarlos, y cómo llevar aplicaciones fiables a producción.

### Por qué armo este compendio

**Estoy empezando en el mundo del AI engineering.** Este libro es mi base: enlaza modelos de lenguaje (y multimodales) con la práctica—*prompts*, recuperación, *finetuning*, datos, inferencia y arquitectura—sin eludir la **evaluación** ni la **retroalimentación de usuarios**. Escribir estas notas me ayuda a aprender y deja el material a mano junto a los experimentos que voy haciendo.

---

## Capítulos (español)

Cada enlace lleva a la página de notas de ese capítulo (mismo orden que en el libro).

| Cap. | Tema | Página |
| --- | --- | --- |
| 1 | [**Introducción a la construcción de aplicaciones de IA con modelos fundacionales**](/ai-engineering/docs/es/introduction-to-building-ai-applications-with-foundation-models) — Escala, modelo como servicio, de modelos de lenguaje a modelos fundacionales, auto-supervisión, casos de uso, planificación de productos de IA y el stack en tres capas frente al ML clásico. | [→](/ai-engineering/docs/es/introduction-to-building-ai-applications-with-foundation-models) |
| 2 | [**Comprender los modelos fundacionales**](/ai-engineering/docs/es/understanding-foundation-models) — Cómo se comportan los modelos grandes: probabilidades, muestreo, ventana de contexto y qué significa que un LLM “sepa” algo. | [→](/ai-engineering/docs/es/understanding-foundation-models) |
| 3 | [**Metodología de evaluación**](/ai-engineering/docs/es/evaluation-methodology) — Diseñar evaluación alineada con riesgos reales y objetivos de negocio, no solo con tablas de posiciones. | [→](/ai-engineering/docs/es/evaluation-methodology) |
| 4 | [**Evaluación de sistemas modernos de IA**](/ai-engineering/docs/es/evaluating-modern-ai-systems) — Evaluación integral de sistemas (modelo + *prompts* + herramientas + recuperación), *benchmarks* y fallos en escenarios tipo producción. | [→](/ai-engineering/docs/es/evaluating-modern-ai-systems) |
| 5 | [**Ingeniería de prompts**](/ai-engineering/docs/es/prompt-engineering) — Obtener el comportamiento deseado solo con instrucciones y contexto (sin cambiar pesos): patrones, estructura e iteración. | [→](/ai-engineering/docs/es/prompt-engineering) |
| 6 | [**RAG y agentes**](/ai-engineering/docs/es/rag-and-agents) — Generación aumentada por recuperación, herramientas, planificación y bucles tipo agente que conectan modelos con datos y el mundo exterior. | [→](/ai-engineering/docs/es/rag-and-agents) |
| 7 | [**Ajuste fino**](/ai-engineering/docs/es/finetuning) — Adaptar los pesos del modelo para dominio, tono, formato o eficiencia cuando *prompting* y RAG no bastan. | [→](/ai-engineering/docs/es/finetuning) |
| 8 | [**Ingeniería de datasets**](/ai-engineering/docs/es/dataset-engineering) — Curar y generar datos para adaptación: calidad, deduplicación, seguridad y coherencia con la evaluación. | [→](/ai-engineering/docs/es/dataset-engineering) |
| 9 | [**Optimización de inferencia**](/ai-engineering/docs/es/inference-optimization) — Inferencia más rápida y barata: *batching*, cuantización, caché, hardware y equilibrios coste–latencia. | [→](/ai-engineering/docs/es/inference-optimization) |
| 10 | [**Arquitectura de AI Engineering y retroalimentación de usuarios**](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback) — Arquitectura en producción, observabilidad y cierre del ciclo con usuarios para mejorar el sistema con seguridad en el tiempo. | [→](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback) |
| — | [**Glosario**](/ai-engineering/docs/es/glossary) — TTFT, PEFT, RAG, *goodput*, *degenerate feedback loop*, etc. | [→](/ai-engineering/docs/es/glossary) |
| — | [**Epílogo**](/ai-engineering/docs/es/epilogue) — Cierre del libro (~p. 495) y [repositorio](https://github.com/chiphuyen/aie-book). | [→](/ai-engineering/docs/es/epilogue) |
