---
title: "Finetuning"
description: "Resumen del capítulo 7 — AI Engineering (Huyen, 2025)"
order: 7
---

## Introducción

Los capítulos 5–6 adaptan modelos con **instrucciones, contexto y herramientas** sin cambiar pesos. El **finetuning** adapta **entrenando de nuevo** todo el modelo o parte de él—ajustando los pesos.

> Finetuning is the process of adapting a model to a specific task by further training the whole model or part of the model… by adjusting its weights.
>
> — Huyen (2025, p. 307)

Puede mejorar capacidades de **dominio**, **seguridad** y sobre todo **seguimiento de instrucciones** (formatos, estilos). Exige más **inversión inicial** que el prompting: datos, hardware, talento ML, serving y mantenimiento.

Es el capítulo más denso técnicamente del libro. Omite secciones que no apliquen a tu rol; el repositorio GitHub del libro enlaza recursos para repasar ML.

---

## Panorama del finetuning

Partes de un **modelo base** con capacidades parciales; el objetivo es rendimiento suficiente en tu tarea.

### Transfer learning y eficiencia muestral

El finetuning es una forma de **transfer learning** (Bozinovski & Fulgosi, 1976): el conocimiento de una tarea fuente acelera una tarea relacionada—como saber piano ayuda a otro instrumento.

En LLMs, el **pre-entrenamiento** en predicción de tokens (datos abundantes) se transfiere a tareas especializadas (QA legal, text-to-SQL) con **muchos menos ejemplos etiquetados**—a veces cientos frente a millones desde cero.

El marco de **InstructGPT**: el finetuning **desbloquea capacidades ya presentes** difíciles de alcanzar solo con prompts.

La **transferencia basada en características** (embeddings + cabeza clasificadora) es común en visión; el finetuning actualiza pesos directamente.

### Tipos de finetuning

| Tipo | Datos | Propósito |
|------|-------|-----------|
| **Continued pre-training** | Texto crudo del dominio (auto-supervisado) | Lenguaje de dominio antes de etiquetas caras |
| **Supervised finetuning (SFT)** | Pares `(entrada, salida)` | Alinear a instrucciones, formatos, tareas |
| **Preference finetuning** | `(instrucción, ganadora, perdedora)` | Alineación estilo RLHF |
| **Long-context finetuning** | Secuencias largas | Extender contexto (cambios de arquitectura, p. ej. embeddings posicionales) |

**Code Llama** (Rozière et al., 2024) ilustra el apilamiento: Llama 2 base → continued pre-training → extensión de contexto → instruction tuning.

**Quién hace finetuning:** desarrolladores de modelos (post-training antes del release) y **desarrolladores de aplicaciones** (a menudo sobre checkpoints ya post-entrenados).

---

## Cuándo hacer finetuning (y cuándo no)

El finetuning requiere **muchos más recursos** que el prompting—experimenta antes con prompts y RAG. No son mutuamente excluyentes.

### Razones para hacer finetuning

- **Calidad** — estructuras JSON/YAML, SQL dialectal, patrones por cliente.
- **Mitigación de sesgos** — datos curados con cuidado (con límites conocidos).
- **Destilación** — modelo pequeño imitando uno grande en una tarea (capítulo 8).
- **Coste/latencia** — Grammarly reportó Flan-T5 superando una variante GPT-3 a 1/60 del tamaño con ~82k pares de instrucción.

Los modelos abiertos más pequeños hacen el finetuning más atractivo que en la era solo-API.

### Razones para no hacer finetuning

- **Impuesto de alineación** — mejoras en una tarea pueden empeorar otras (fine-tune en todas las tareas relevantes, o modelos separados / merging).
- **Coste alto** — anotación, expertise, serving, monitorización, re-basado cuando salen nuevos modelos fundacionales.
- **Alternativas** — prompts, salidas estructuradas (capítulo 2), RAG para hechos.
- **Modelos generales** — p. ej. GPT-4-0314 superó a **BloombergGPT** en benchmarks financieros pese al costoso entrenamiento 50B de Bloomberg (Li et al., 2023).

Muchos equipos descubren que experimentos de prompt débiles motivaron “necesitamos finetuning”—una evaluación sistemática (capítulo 4) suele bastar.

### Finetuning vs. RAG: forma vs. hechos

> Finetuning is for **form**, and RAG is for **facts**.
>
> — Huyen (2025, p. 317)

| Tipo de fallo | Síntoma | Inclinación |
|---------------|---------|-------------|
| **Basado en información** | Hechos incorrectos u obsoletos; falta conocimiento privado | **RAG** (empezar con BM25, luego embeddings) |
| **Basado en comportamiento** | Correcto pero irrelevante; formato/estilo incorrecto; DSL débil | **Finetuning** |

**Ovadia et al. (2024):** en QA de actualidad, RAG superó al finetuning; RAG sobre base a menudo superó RAG sobre modelo fine-tuned—pero **RAG + finetune** ayudó ~43% de las veces en categorías MMLU.

**Ruta recomendada con ambos problemas:** **RAG** primero para hechos (p. ej. resúmenes de jurisprudencia), luego **finetuning** para formato XML propietario.

**Flujo de trabajo (con pipeline de evaluación):**

1. Prompting (capítulo 5), añadir few-shot.
2. RAG si falta información (retrieval simple primero).
3. RAG avanzado o finetuning según el modo de fallo.
4. Combinar ambos si está justificado.

---

## Cuellos de botella de memoria

> For foundation models, memory is a bottleneck for working with them, both for inference and for finetuning.
>
> — Huyen (2025, p. 320)

La memoria de finetuning ≫ memoria de inferencia porque el **backpropagation** corre en entrenamiento.

### Contribuyentes clave

1. **Número de parámetros** y **parámetros entrenables**
2. **Precisión numérica** (FP32, FP16, BF16, INT8, INT4…)
3. **Optimizador Adam** — **dos valores extra por parámetro entrenable** (estados de momento)

Por parámetro entrenable en backward pass: **gradiente** + estados del optimizador.

### Cálculo rápido

**Inferencia** (solo forward):

`memoria ≈ num_params × bytes_por_param × 1.2`

El factor 1.2 cubre activaciones/KV (aproximado; crece con contexto y batch).

Ejemplo — **modelo 13B, FP16 (2 bytes):**  
13×10⁹ × 2 × 1.2 ≈ **31,2 GB**

**Full finetuning** (todos entrenables, Adam, FP16):

`entrenamiento ≈ pesos + activaciones + gradientes + estados_optimizador`

Por parámetro entrenable con Adam en 16 bits: gradiente (1) + estados (2) → **3 valores × 2 bytes = 6 bytes** por parámetro entrenable (más pesos).

Ejemplo — **7B full finetune, FP16:**

- Pesos: 7B × 2 = **14 GB**
- Gradientes + Adam: 7B × 3 × 2 = **42 GB**
- Subtotal ≈ **56 GB** (las activaciones pueden dominar; usar **gradient checkpointing**)

**PEFT** reduce parámetros entrenables → mucha menos memoria de gradiente/optimizador.

### Cuantización

> Reducing precision, also known as quantization, is a cheap and extremely effective way to reduce a model's memory footprint.
>
> — Huyen (2025, p. 328)

- **PTQ:** cuantizar tras entrenar—común en inferencia (LLM.int8, serving 4-bit).
- **QAT:** simula baja precisión durante entrenamiento para mejor calidad en pocos bits.
- **Entrenamiento en precisión mixta:** mayor precisión en operaciones sensibles (pesos/pérdida), menor en activaciones/gradientes.

**Carga el modelo en el dtype previsto** (p. ej. Llama 2 en **BF16**, no FP16—cae la calidad).

---

## Técnicas de finetuning

### Full vs. parcial vs. PEFT

- **Full finetuning:** todos los parámetros entrenables (memoria como pre-training).
- **Parcial:** congelar capas tempranas—ineficiente en parámetros (~25% de BERT-large para paridad GLUE, Houlsby et al., 2019).
- **PEFT:** rendimiento cercano al full con **órdenes de magnitud menos** parámetros entrenables.

**Cubos PEFT:**

1. **Basado en adaptadores (aditivo)** — módulos pequeños (adaptadores Houlsby; domina **LoRA**).
2. **Soft prompts** — tokens continuos entrenables (prefix-tuning, prompt tuning, P-tuning).

### LoRA (Low-Rank Adaptation)

Matriz de pesos **W** congelada; actualización de bajo rango **ΔW = B × A** (rango **r**). Forward: `h = W₀x + BAx`. Tras entrenar, fusionar: **W′ = W₀ + (α/r)BA** — **sin latencia extra** en inferencia si se fusiona.

**Por qué funciona:** muchos parámetros pero **dimensión intrínseca baja** tras pre-training—modelos más grandes a menudo más fáciles de adaptar con pocos datos (Li et al., 2018; Aghajanyan et al., 2020; Hu et al., 2021).

**Dónde aplicar:** habitualmente **Wq, Wk, Wv, Wo** en atención; Databricks reportó fuertes ganancias con LoRA en **feedforward**. Con presupuesto fijo de parámetros entrenables, importa la asignación de rango (Hu et al., 2021 en GPT-3 175B). **r típico: 4–64** (depende de la tarea).

**Multi-LoRA serving:** una base **W** + muchos adaptadores (A, B) pequeños—mucho menos almacenamiento que 100 modelos fusionados completos.

**QLoRA:** pesos base en **4-bit (NF4)**; forward/backward en BF16; **optimizadores paginados**—**65B en una GPU de 48 GB** (Dettmers et al., 2023). Coste: tiempo de cuantización/desquantización.

### Model merging (experimental)

Combinar varios modelos fine-tuned en uno más útil—no es lo mismo que **ensembling** (varias pasadas forward).

**Casos de uso:** multi-tarea sin olvido catastrófico, memoria en dispositivo, aprendizaje federado, **upscaling** (p. ej. SOLAR 10.7B desde 7B).

**Enfoques:**

| Enfoque | Idea | Notas |
|---------|------|-------|
| **Suma / promedio** | Media ponderada o **vectores de tarea** (fine-tuned − base) | Aritmética de tareas: sumar/restar capacidades |
| **SLERP** | Interpolación esférica entre dos modelos | Útil en pares de checkpoints |
| **TIES / DARE** | Podar parámetros redundantes del vector de tarea antes de fusionar | Menos interferencia |
| **Layer stacking (frankenmerge)** | Apilar capas de distintos modelos | Suele requerir más finetuning (Goliath-120B) |
| **MoE desde denso** | Duplicar capas + router (Komatsuzaki et al.) | Sparse upcycling |
| **Concatenación (LoRA)** | Rango fusionado = r₁ + r₂ | Normalmente **no** recomendada por memoria |

---

## Tácticas prácticas de finetuning

### Modelo base y rutas de desarrollo

**Ruta de progresión** (estilo OpenAI):

1. Modelo más barato — depurar **código**.
2. Modelo intermedio — depurar **datos** (la pérdida debe bajar).
3. Mejor modelo — empujar rendimiento; mapa **precio/rendimiento**.

**Ruta de destilación:**

1. Modelo fuerte + conjunto **pequeño** curado.
2. Generar datos sintéticos de entrenamiento.
3. Entrenar modelo **más barato** estudiante.

### Frameworks

- **APIs** — rápidas, pocos knobs/modelos.
- **Frameworks:** LLaMA-Factory, **PEFT**, **unsloth**, Axolotl, LitGPT; full finetune a menudo desde el repo de entrenamiento del modelo.
- **Distribuido:** DeepSpeed, PyTorch Distributed, ColossalAI.

Empieza con **LoRA**; full finetune cuando esté justificado. LoRA brilla al servir **muchos adaptadores** sobre una base.

### Hiperparámetros clave

| Hiperparámetro | Rol | Notas prácticas |
|----------------|-----|-----------------|
| **Learning rate** | Tamaño del paso de actualización | Probar 1e-7 a 1e-3; pérdida inestable → demasiado alto; descenso lento → demasiado bajo; usar schedules |
| **Batch size** | Ejemplos por paso | Mayor = más estable pero más memoria; **gradient accumulation** simula batch grande |
| **Épocas** | Pasadas sobre los datos | Millones de ejemplos: 1–2 épocas; miles: quizá 4–10; comparar train vs validation para overfitting |
| **Prompt loss weight** | Cuánta pérdida viene del prompt vs la respuesta en SFT | Por defecto ~10% en prompts |

---

## Cierre del capítulo

El finetuning intercambia **actualización de pesos** por **memoria, datos y complejidad operativa**. La práctica moderna se centra en **PEFT (LoRA)** y **cuantización (QLoRA)** para GPUs de consumo y una sola GPU, mientras **RAG** y prompting cubren hechos e iteración rápida.

El **model merging** experimental combina checkpoints especializados para multi-tarea y edge. El capítulo 8 aborda el cuello de botella de **datos**—especialmente datos de instrucción.

---

## Notas finales

Lo que extraigo de este capítulo, alineado con los objetivos de la clase: el finetuning no es el valor por defecto—es la escalada tras trabajo **sistemático** con prompts y RAG. La idea InstructGPT de **desbloquear** comportamientos, no inventarlos desde cero, cambia los criterios de éxito: datasets pequeños de alta calidad y especificaciones de formato claras suelen bastar con LoRA.

La división **forma vs. hechos** es mi árbol de decisión: RAG primero para alucinaciones y conocimiento privado, finetune para dialectos XML/JSON y tono. Internalizaría la **matemática de memoria** antes de elegir hardware: un full finetune 7B en FP16 con Adam ya ronda ~56 GB sin activaciones; LoRA + QLoRA existen porque esa cifra no cabe en 24 GB.

En producción, **multi-LoRA serving** es el caso de negocio: una base, muchos adaptadores por cliente. Seguiría learning rate, batch con acumulación y pérdida de validación—y trataría el merging como investigación salvo vectores de tarea bien definidos.

**Referencia:** Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 7: Finetuning.

---

## Referencias

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 7: Finetuning.

### Artículos fundacionales

- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) — Hu et al. (2021).
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) — Dettmers et al. (2023).
- [Training language models to follow instructions (InstructGPT)](https://arxiv.org/abs/2203.02155) — Ouyang et al. (2022).
- [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) — Lewis et al. (2020) — contraste con finetuning.
- [Fine-Tuning or Retrieval?](https://arxiv.org/abs/2312.05934) — Ovadia et al. (2024) — RAG vs finetune en actualidad.
- [TIES-Merging](https://arxiv.org/abs/2306.01708) — Yadav et al. (2023).
- [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089) — Ilharco et al. (2022).

### Memoria y matemática de entrenamiento

- [Transformer Inference Arithmetic](https://kipp.ly/transformer-inference-arithmetic/) — Carol Chen.
- [Transformer Math 101](https://blog.eleuther.ai/transformer-math-101/) — EleutherAI (Anthony et al., 2023).
- [Reducing Activation Recomputation](https://arxiv.org/abs/2205.05198) — Korthikanti et al. (2022).
- [Mixed Precision Training](https://arxiv.org/abs/1710.03740) — Micikevicius et al. (2017).

### Guías oficiales y cursos

- [OpenAI — Fine-tuning best practices](https://platform.openai.com/docs/guides/fine-tuning) — Rutas de progresión y destilación.
- [Hugging Face — PEFT](https://huggingface.co/docs/peft) — LoRA, adaptadores, soft prompts.
- [Hugging Face — LLaMA-Factory](https://github.com/hiyouga/LlamaFactory) — CLI/UI multi-modelo.
- [unsloth](https://github.com/unslothai/unsloth) — LoRA/QLoRA rápido.
- [DeepSpeed](https://www.deepspeed.ai/) — ZeRO, memoria, entrenamiento distribuido.
- [DeepLearning.AI — Finetuning Large Language Models](https://www.deeplearning.ai/short-courses/finetuning-large-language-models/) — Curso corto.
- [DeepLearning.AI — Efficiently Serving LLMs](https://www.deeplearning.ai/short-courses/efficiently-serving-llms/) — Serving con adaptadores.
- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — Taller en español (stack de adaptación relacionado).

### Protocolos e interoperabilidad (complementario)

- [A Survey of AI Agent Protocols](https://arxiv.org/abs/2504.16736) — Yang et al. (2025) — MCP, A2A.
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

### Model merging y multi-tarea

- [Model soups](https://arxiv.org/abs/2203.05482) — Wortsman et al. (2022).
- [Git Re-Basin](https://arxiv.org/abs/2209.04836) — Ainsworth et al. (2022).
- [MergeKit](https://github.com/arcee-ai/mergekit) — Toolkit práctico.
- [AdapterHub](https://adapterhub.ml/) — Descubrimiento de adaptadores.

### Cuantización e inferencia en pocos bits

- [LLM.int8()](https://arxiv.org/abs/2208.07339) — Dettmers et al. (2022).
- [GPTQ](https://arxiv.org/abs/2210.17323) — Frantar et al. (2022).
- [bitsandbytes](https://github.com/TimDettmers/bitsandbytes) — Utilidades 8/4-bit para QLoRA.

### Vídeos y charlas

- [Hugging Face — tutoriales PEFT + LoRA (YouTube)](https://www.youtube.com/results?search_query=huggingface+peft+lora+tutorial) — Buscar walkthroughs recientes oficiales.
- [Andrej Karpathy — Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) — Intuición de backprop y optimización.

### Repositorio del libro y listas

- [AI Engineering — GitHub (Huyen)](https://github.com/chiphuyen/aie-book) — Walkthroughs de memoria, recursos de finetuning.
- [Llama Police / llm-course](https://github.com/mlabonne/llm-course) — Listas comunitarias (verificar actualidad).
