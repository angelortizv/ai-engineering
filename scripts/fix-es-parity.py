#!/usr/bin/env python3
"""Translate discussion + Related blocks in docs-es chapters."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ES = ROOT / "src/content/docs-es"

DISCUSSION: dict[str, list[str]] = {
    "introduction-to-building-ai-applications-with-foundation-models": [
        "¿Dónde está tu equipo en **construir vs. comprar** el modelo base—y qué cambiaría eso en 12 meses?",
        "Para un caso de uso interno, ubica **crítico vs. complementario**, **reactivo vs. proactivo** y **dinámico vs. estático**. ¿Qué barra de latencia/calidad sigue?",
        "¿Qué **métrica de negocio** no enviarías sin definir, más allá de «el demo se ve bien»?",
        "¿Qué capa del **stack de tres niveles** es hoy el cuello de botella?",
        "¿Qué **ventaja competitiva** sobrevive si el proveedor de API lanza mañana tu función?",
    ],
    "understanding-foundation-models": [
        "Para tu idioma/región principal, ¿la **mezcla de entrenamiento** del modelo coincide con el tráfico real?",
        "¿Qué modo de fallo ves más: **ruido de muestreo** o **sobreconfianza estructural**?",
        "¿Cuándo subirías **cómputo en inferencia** (best-of-N) frente a cambiar el modelo base?",
        "¿Cómo validas **JSON estructurado**—solo sintaxis o también pruebas semánticas?",
        "¿Qué artefacto de post-entrenamiento (SFT vs. preferencias) explica mejor un mal comportamiento que hayas visto?",
    ],
    "evaluation-methodology": [
        "Nombra tres **modos de fallo** de tu app que ningún leaderboard público captura.",
        "¿Cuándo te sirve la **perplejidad**—y cuándo engaña?",
        "Diseña una comprobación de **corrección funcional** para una tarea generativa que tengas.",
        "¿Qué sesgos probarías si adoptas un **juez IA**?",
        "¿Qué te convencería de que un **+2 % en Arena** vale un **2× en precio**?",
    ],
    "evaluating-modern-ai-systems": [
        "Redacta cuatro **pilares de evaluación** (dominio, generación, instrucciones, coste/latencia) para tu producto.",
        "¿Qué hay en tu **eval privado** que MMLU nunca verá?",
        "¿Dónde podrían **benchmarks públicos contaminados** rankear mal un modelo para ti?",
        "Escribe un párrafo de **guía de evaluación** como el ejemplo de «helpfulness» de LinkedIn.",
        "¿Qué **umbral de utilidad** separa automatización de revisión humana?",
    ],
    "prompt-engineering": [
        "¿Qué tareas quedan **zero-shot** y cuáles necesitan **few-shot**—y por qué?",
        "¿Cómo **versionas** prompts y los ligas a corridas de eval?",
        "¿Cuál es tu política ante **texto no confiable** en el contexto (inyección indirecta)?",
        "¿Cuándo usar **salidas estructuradas** frente a texto libre + parsing?",
        "¿Qué te haría dejar de iterar prompts y probar **RAG** o **finetuning**?",
    ],
    "rag-and-agents": [
        "¿Dónde gana la **recuperación híbrida** frente a solo denso en tu dominio?",
        "¿Cuál es el modo de fallo de tu estrategia de **chunking** hoy?",
        "Esboza un bucle **ReAct** para un flujo—¿qué valida un humano?",
        "¿Qué **fallos de agente** (planificación vs. herramientas) dominan tus logs?",
        "¿Cuándo basta RAG sin agente?",
    ],
    "finetuning": [
        "Enumera **motivos para no hacer finetuning** en tu producto actual.",
        "Estima **parámetros entrenables** y memoria con el cálculo rápido del capítulo.",
        "¿Cuándo basta finetuning de **forma** (tono/formato) sin hechos nuevos?",
        "¿Cambiaría tu historia de **cumplimiento** entre **LoRA y full**?",
        "¿Cómo detectarás **olvido catastrófico** en tareas generales?",
    ],
    "dataset-engineering": [
        "Define dimensiones de **calidad** que importen en tus guías de anotación.",
        "¿Qué ejes de **cobertura** (idioma, tema, longitud) están infrarrepresentados?",
        "¿Cuándo compensa el coste de verificación de **datos sintéticos**?",
        "¿Qué regla de **deduplicación** aplicarías antes del SFT?",
        "¿Cómo difiere tu mezcla entre fases **pretrain / SFT / preferencias**?",
    ],
    "inference-optimization": [
        "¿Tu carga es más **prefill** o **decode**? ¿Qué implica para el hardware?",
        "¿Qué métrica importa más al usuario: **TTFT** o **TPOT**?",
        "¿Ayudaría la **decodificación especulativa** si el MFU ya es alto?",
        "¿Cuándo es seguro el **prompt caching** frente a un fallo de privacidad?",
        "¿Cuál es tu objetivo de **goodput** por dólar?",
    ],
    "ai-engineering-architecture-and-user-feedback": [
        "¿Qué **paso de arquitectura** (contexto, guardrails, router, caché, agentes) falta hoy?",
        "¿Dónde podría una **caché semántica** filtrar respuestas personalizadas a otro usuario?",
        "¿Qué señal de **observabilidad** habría detectado tu último incidente?",
        "¿Cómo evitas un **bucle de feedback degenerado**?",
        "¿Qué feedback recoges sin dañar la UX?",
    ],
}

RELATED: dict[str, str] = {
    "introduction-to-building-ai-applications-with-foundation-models": """## Relacionado

- **Siguiente:** [Entender modelos fundacionales](/ai-engineering/docs/es/understanding-foundation-models) — cómo se entrenan, muestrean y dirigen los LM.
- **Evaluación:** [Metodología de evaluación](/ai-engineering/docs/es/evaluation-methodology) — por qué las salidas abiertas exigen nuevas métricas.
- **Sistemas:** [Evaluar sistemas de IA modernos](/ai-engineering/docs/es/evaluating-modern-ai-systems) — evaluación operativa antes de escalar.
- **Adaptación:** [Ingeniería de prompts](/ai-engineering/docs/es/prompt-engineering) — primera palanca tras elegir un modelo.
- **Repositorio del libro:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glosario:** [Glosario](/ai-engineering/docs/es/glossary) — términos del libro y estas notas.""",
    "understanding-foundation-models": """## Relacionado

- **Anterior:** [Introducción a aplicaciones de IA](/ai-engineering/docs/es/introduction-to-building-ai-applications-with-foundation-models) — por qué existe la ingeniería de IA.
- **Siguiente:** [Metodología de evaluación](/ai-engineering/docs/es/evaluation-methodology) — métricas para lo que acabas de aprender sobre el modelo.
- **Muestreo:** [Ingeniería de prompts](/ai-engineering/docs/es/prompt-engineering) — temperatura, top-p y salidas estructuradas en la práctica.
- **Adaptación:** [Finetuning](/ai-engineering/docs/es/finetuning) — cuándo hay que cambiar pesos, no solo prompts.
- **Repositorio del libro:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glosario:** [Glosario](/ai-engineering/docs/es/glossary) — términos del libro y estas notas.""",
    "evaluation-methodology": """## Relacionado

- **Anterior:** [Entender modelos fundacionales](/ai-engineering/docs/es/understanding-foundation-models) — qué estás midiendo.
- **Siguiente:** [Evaluar sistemas de IA modernos](/ai-engineering/docs/es/evaluating-modern-ai-systems) — pipelines y selección de modelo.
- **Prompts:** [Ingeniería de prompts](/ai-engineering/docs/es/prompt-engineering) — evaluación defensiva ante inyección y fugas.
- **Producción:** [Arquitectura de IA y feedback de usuario](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback) — el feedback como evaluación continua.
- **Repositorio del libro:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glosario:** [Glosario](/ai-engineering/docs/es/glossary) — términos del libro y estas notas.""",
    "evaluating-modern-ai-systems": """## Relacionado

- **Anterior:** [Metodología de evaluación](/ai-engineering/docs/es/evaluation-methodology) — métodos que este capítulo operacionaliza.
- **Siguiente:** [Ingeniería de prompts](/ai-engineering/docs/es/prompt-engineering) — primera capa de adaptación tras elegir modelo.
- **Datos:** [Ingeniería de datos](/ai-engineering/docs/es/dataset-engineering) — construir slices que reflejen producción.
- **Agentes:** [RAG y agentes](/ai-engineering/docs/es/rag-and-agents) — evaluar recuperación y bucles de herramientas.
- **Repositorio del libro:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glosario:** [Glosario](/ai-engineering/docs/es/glossary) — términos del libro y estas notas.""",
    "prompt-engineering": """## Relacionado

- **Anterior:** [Evaluar sistemas de IA modernos](/ai-engineering/docs/es/evaluating-modern-ai-systems) — saber qué es «bueno» antes de iterar prompts.
- **Siguiente:** [RAG y agentes](/ai-engineering/docs/es/rag-and-agents) — contexto más allá de la ventana del prompt.
- **Seguridad:** [Metodología de evaluación](/ai-engineering/docs/es/evaluation-methodology) — elección de juez y métricas para pruebas de safety.
- **Arquitectura:** [Arquitectura de IA y feedback de usuario](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback) — guardrails alrededor de los prompts.
- **Repositorio del libro:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glosario:** [Glosario](/ai-engineering/docs/es/glossary) — términos del libro y estas notas.""",
    "rag-and-agents": """## Relacionado

- **Anterior:** [Ingeniería de prompts](/ai-engineering/docs/es/prompt-engineering) — diseño de instrucciones y contexto.
- **Siguiente:** [Finetuning](/ai-engineering/docs/es/finetuning) — cuando recuperación y herramientas no bastan.
- **Datos:** [Ingeniería de datos](/ai-engineering/docs/es/dataset-engineering) — corpus y calidad de chunks para recuperación.
- **Evaluación:** [Evaluar sistemas de IA modernos](/ai-engineering/docs/es/evaluating-modern-ai-systems) — evaluación end-to-end y por componente.
- **Repositorio del libro:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glosario:** [Glosario](/ai-engineering/docs/es/glossary) — términos del libro y estas notas.""",
    "finetuning": """## Relacionado

- **Anterior:** [RAG y agentes](/ai-engineering/docs/es/rag-and-agents) — adaptación basada en prompt primero.
- **Siguiente:** [Ingeniería de datos](/ai-engineering/docs/es/dataset-engineering) — calidad de datos para SFT y preferencias.
- **Inferencia:** [Optimización de inferencia](/ai-engineering/docs/es/inference-optimization) — coste de serving tras adaptar pesos.
- **Evaluación:** [Evaluar sistemas de IA modernos](/ai-engineering/docs/es/evaluating-modern-ai-systems) — demostrar que el finetuning supera prompts/RAG.
- **Repositorio del libro:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glosario:** [Glosario](/ai-engineering/docs/es/glossary) — términos del libro y estas notas.""",
    "dataset-engineering": """## Relacionado

- **Anterior:** [Finetuning](/ai-engineering/docs/es/finetuning) — para qué sirven los datos.
- **Siguiente:** [Optimización de inferencia](/ai-engineering/docs/es/inference-optimization) — servir el modelo que entrenaste.
- **Evaluación:** [Evaluar sistemas de IA modernos](/ai-engineering/docs/es/evaluating-modern-ai-systems) — slices y rúbricas para calidad de datos.
- **Feedback:** [Arquitectura de IA y feedback de usuario](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback) — logs → *data flywheel* de entrenamiento.
- **Repositorio del libro:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glosario:** [Glosario](/ai-engineering/docs/es/glossary) — términos del libro y estas notas.""",
    "inference-optimization": """## Relacionado

- **Anterior:** [Ingeniería de datos](/ai-engineering/docs/es/dataset-engineering) — modelos que vas a servir.
- **Siguiente:** [Arquitectura de IA y feedback de usuario](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback) — cachés, gateways y UX en producción.
- **Modelos:** [Entender modelos fundacionales](/ai-engineering/docs/es/understanding-foundation-models) — bases de la decodificación autoregresiva.
- **Finetuning:** [Finetuning](/ai-engineering/docs/es/finetuning) — huella de memoria de pesos adaptados.
- **Repositorio del libro:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glosario:** [Glosario](/ai-engineering/docs/es/glossary) — términos del libro y estas notas.""",
    "ai-engineering-architecture-and-user-feedback": """## Relacionado

- **Anterior:** [Optimización de inferencia](/ai-engineering/docs/es/inference-optimization) — latencia y coste bajo carga.
- **Cierre:** [Introducción a aplicaciones de IA](/ai-engineering/docs/es/introduction-to-building-ai-applications-with-foundation-models) — stack y planificación del capítulo 1.
- **Datos de feedback:** [Ingeniería de datos](/ai-engineering/docs/es/dataset-engineering) — convertir logs en conjuntos de entrenamiento.
- **Epílogo:** [Epílogo](/ai-engineering/docs/es/epilogue) — perspectiva de cierre y repositorio del libro.
- **Repositorio del libro:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glosario:** [Glosario](/ai-engineering/docs/es/glossary) — términos del libro y estas notas.""",
}


def discussion_block(items: list[str]) -> str:
    bullets = "\n".join(f"- {x}" for x in items)
    return f"## Preguntas de discusión\n\n{bullets}"


def patch_file(path: Path, slug: str) -> None:
    text = path.read_text(encoding="utf-8")
    disc = discussion_block(DISCUSSION[slug])
    text = re.sub(
        r"## Preguntas de discusión\n\n(?:- .+\n)+",
        disc + "\n",
        text,
        count=1,
    )
    text = re.sub(
        r"## Relacionado\n\n(?:- .+\n)+",
        RELATED[slug] + "\n",
        text,
        count=1,
    )
    path.write_text(text, encoding="utf-8")
    print(f"patched {path.name}")


def main() -> None:
    for slug in DISCUSSION:
        p = ES / slug / "index.md"
        if p.exists():
            patch_file(p, slug)


if __name__ == "__main__":
    main()
