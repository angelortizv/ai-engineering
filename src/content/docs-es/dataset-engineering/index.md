---
title: "Dataset Engineering"
description: "Resumen del capítulo 8 — AI Engineering (Huyen, 2025)"
order: 8
---

## Introducción

> **O'Reilly (1.ª ed.)** — Huyen (2025), **Capítulo 8**, aprox. **pp. 363–404**. Contrasta figuras y tablas con tu PDF.

El mejor equipo ML con cómputo infinito no puede hacer un buen finetuning sin **datos de calidad**. La **ingeniería de datasets** crea conjuntos que entrenan el mejor modelo posible dentro del presupuesto de anotación, cómputo y cumplimiento normativo.

Como menos organizaciones entrenan desde cero, los **datos diferencian** productos de IA. GPT-3 acreditó a dos personas en datos; GPT-4 a **ochenta**—más anotadores externos (OpenAI, 2020 vs 2023). Las operaciones de datos pasaron de tareas laterales a roles dedicados: etiquetadores, creadores de datasets, ingenieros de calidad de datos.

Este capítulo se centra en **datos de post-training** (más relevantes para desarrolladores de aplicaciones), con lecciones de pre-training cuando aportan. Curación, síntesis y procesamiento son **iterativos**, no lineales.

> There are best practices you can follow and tools that you can use to automate parts of the process. However, data will mostly just be toil, tears, and sweat.
>
> — Huyen (2025, cap. 8)

## Objetivos de aprendizaje

Al terminar este capítulo deberías poder:

- Aplicar **calidad, cobertura y cantidad** al plan de datos de finetuning.
- Comparar adquisición **humana, sintética y por destilación**.
- Interpretar cambios de **mezcla por dominio** entre fases (p. ej. Llama 3).
- Diseñar inspección, **deduplicación** y filtrado.
- Definir cómo **evaluarás datos sintéticos** antes de entrenar.

---

## Visión data-centric de la IA

| Enfoque | Prioridad |
|---------|-----------|
| **Model-centric** | Arquitecturas, escala, algoritmos de entrenamiento |
| **Data-centric** | Procesamiento, datasets de calidad, menos recursos |

Los benchmarks evolucionaron: mismo dataset → mejor modelo (era ImageNet) vs mismo modelo → mejor dataset (**DataComp**, **DataPerf**, **dcbench**). La competencia data-centric de Andrew Ng (2021) y **DataComp** para CLIP (Gadre et al., 2023) lo ilustran. El progreso real suele requerir **modelo y datos**.

---

## Curación de datos

Los datos pueden hacer modelos más capaces y seguros—or amplificar sesgos y alucinaciones. Quien construye datasets debe trabajar con desarrollo de aplicación y de modelo (a menudo la misma persona en equipos pequeños).

### Qué datos para cada fase

| Fase | Formato típico | Métrica de cantidad |
|------|----------------|---------------------|
| Auto-supervisado / continued pre-training | Secuencias de texto | Tokens |
| Supervised finetuning (SFT) | `(instrucción, respuesta)` | Ejemplos |
| Preference finetuning | `(instrucción, ganadora, perdedora)` | Ejemplos |
| Modelo de recompensa | Igual que preferencias o `((instrucción, respuesta), score)` | Ejemplos |

Los datos deben **mostrar los comportamientos deseados**—y a veces **eliminar** ejemplos que enseñan malos hábitos (p. ej. reescrituras no solicitadas en fact-checking).

### Comportamientos difíciles de anotar

**Chain-of-thought (CoT):** Respuestas paso a paso en entrenamiento mejoran mucho el CoT (Chung et al., 2024)—pero anotar CoT es tedioso; hay menos datasets CoT.

**Uso de herramientas:** Los expertos ayudan, pero los humanos omiten pasos o prefieren UI frente a APIs. **Simulaciones** y trazas sintéticas encajan mejor con agentes. **Llama 3** usa formato multi-mensaje con cabeceras origen/destino (Dubey et al., 2024).

**Single-turn vs. multi-turn:** Single-turn es más fácil de recoger; multi-turn enseña aclaraciones, correcciones y diálogo real.

### Tres criterios (la “tríada dorada”)

Piensa en entrenar como cocinar:

| Criterio | Analogía | Significado |
|----------|----------|-------------|
| **Calidad** | Ingredientes frescos | Relevante, alineado, consistente, formateado, único, compliant |
| **Cobertura** | Mezcla correcta | Diversidad de tareas, temas, estilos, formatos |
| **Cantidad** | Suficiente volumen | Cuántos ejemplos/tokens—limitado por presupuesto |

---

## Calidad de datos

**10K instrucciones cuidadas** superan cientos de miles ruidosas (Yi, Young et al., 2024). **LIMA** (Zhou et al., 2023): 1.000 pares curados en Llama 65B rivalizaron o ganaron a GPT-4 en ~43% de comparaciones humanas—pero menos robusto que modelos de producto.

**Llama 3** encontró errores en anotaciones humanas en políticas de seguridad; construyeron herramientas de **anotación asistida por IA**.

Seis características (enfoque finetuning):

1. **Relevante** — acorde a la tarea y época.  
2. **Alineado** — cumple requisitos (factual vs creativo vs conciso).  
3. **Consistente** — entre anotadores; requiere **guías de anotación** sólidas.  
4. **Formateado correctamente** — quitar HTML, espacios, tipos erróneos.  
5. **Suficientemente único** — duplicados sesgan y contaminan eval.  
6. **Compliant** — leyes, PII, licencias.

Las guías de anotación coinciden con las de **evaluación** (capítulo 4)—reutiliza ejemplos de eval como semillas de síntesis.

---

## Cobertura de datos

Hace falta datos que reflejen **cómo preguntan los usuarios**—typos, prompts cortos vs largos, todos los lenguajes de programación, diversidad cultural en productos globales.

**Nemotron** (Adler et al., 2024): diversidad de tarea, tema e instrucción. **Shen et al. (2024):** más heterogeneidad a veces **empeora** el rendimiento.

Las ganancias de **Llama 3** vienen sobre todo de **calidad y diversidad de datos**, no de cambios de arquitectura. Las mezclas por dominio difieren por fase (**tabla 8-1**, libro p. 370):

| Dominio | Pre-training | SFT | Preference finetuning |
| --- | ---: | ---: | ---: |
| Conocimiento general (inglés) | 50% | 52,66% | 81,99% |
| Matemáticas y razonamiento | 25% | 21,19% | 5,89% |
| Código | 17% | 14,89% | 6,93% |
| Multilingüe | 8% | 3,01% | 5,19% |
| Tipo examen | — | 8,14% | — |
| Contexto largo | — | 0,11% | — |

Código + matemáticas suman ~la mitad de tokens en pre-training/SFT, muy por encima de su peso en la web típica. **Annealing** con poco código/matemáticas de alta calidad mejora razonamiento; preference finetuning vuelve hacia conocimiento general (~82%).

**Experimento Zhou et al.:** 2.000 ejemplos—solo calidad, solo diversidad, o ambos—gana el conjunto **con ambos**.

---

## Cantidad de datos

Desde demos de **un ejemplo** (Howard & Whitaker) hasta **millones** de pares de finetuning—aún minúsculo frente a los **16 billones** de tokens de pre-training de Llama 3.

**Factores:**

| Factor | Efecto |
|--------|--------|
| **Método de finetuning** | Full finetune exige muchos más datos que LoRA |
| **Complejidad de tarea** | Sentimiento vs QA financiero |
| **Modelo base** | Base más fuerte → menos ejemplos; **osificación** limita adaptación con muchos datos (Hernandez et al., 2021) |

**Patrón OpenAI/SNLI:** con **100** ejemplos, modelos base más fuertes ganan tras finetune; con **550k**, convergen—PEFT + base fuerte con pocos datos; full finetune + modelo más pequeño con muchos.

**Empieza con ~50 ejemplos bien hechos** antes de escalar—si no mejora, revisa hiperparámetros y calidad, no solo tamaño.

**Curvas de escala:** rendimiento vs 25%/50%/100% del dataset—pendiente fuerte implica que más datos ayudan; meseta implica rendimientos decrecientes (habitual).

**Diversidad de tareas:** Flan-T5 saltó de **9 → 282** tareas; la mejora se aplana cerca de **1.836** (Chung et al., 2022).

**Estrategias por etapas:**

- Documentos legales auto-supervisados → pares QA supervisados  
- Sentimiento en tweets → sentimiento en reseñas de producto  
- Datos médicos sintéticos → datos reales (más difícil; dos finetunes)

Ejemplo de presupuesto: 10.000 USD a 2 USD/ejemplo → máximo 5.000 ejemplos—equilibra datos vs cómputo.

---

## Adquisición y anotación

**Mejor fuente:** datos de tu **propia aplicación**—el volante de datos (contenido de usuario, logs, feedback; capítulo 10). Relevancia y distribución ideales.

Si no: mezcla fuentes públicas, compradas, anotadas y sintéticas. Pipeline típico:

1. Datasets públicos (10k ejemplos).  
2. Filtrar instrucciones de baja calidad (9k).  
3. Reescribir respuestas malas en 3k instrucciones buenas.  
4. Rellenar huecos temáticos con plantillas + IA + revisión humana.

**Hubs:** Hugging Face, Kaggle, Google Dataset Search, Data.gov, ICPSR, UCI/OpenML, AWS Open Data, TensorFlow datasets, benchmarks de **lm-evaluation-harness** (400+), SNAP para grafos.

**Inspecciona licencias y procedencia** siempre.

La anotación es de los pasos más duros—equipos abandonan guías y esperan que el modelo “descubra” la respuesta; arriesgado en producción.

---

## Aumento y síntesis de datos

| Proceso | Origen | Ejemplo |
|---------|--------|---------|
| **Aumento** | Datos reales transformados | Voltear imagen; sinónimos |
| **Síntesis** | Generado que imita lo real | Transacciones simuladas; parafraseo con IA |

Librerías como **Faker** empezaron para tests; los LLM permiten notas médicas, contratos, anuncios, etc. **Mezclar humano + sintético** suele ganar a cada uno por separado.

### Por qué sintetizar

- **Cantidad** — escala donde faltan datos reales.  
- **Cobertura** — casos límite, toxicidad, balance de clases, adversariales (**TrueTeacher**, Gekhman et al., 2022).  
- **Calidad** — trazas de herramientas, matemáticas difíciles, preferencias consistentes (evaluaciones escritas por modelos, Perez et al., 2022).  
- **Privacidad** — registros sintéticos de pacientes/reclamaciones.  
- **Destilación** — estudiante entrenado con salidas del maestro.

### Técnicas tradicionales

**Reglas / plantillas:** transacciones, facturas, problemas matemáticos (**AlphaGeometry**, 100M ejemplos sintéticos, Trinh et al., 2024). Texto: sinónimos, swaps de género (tabla 8-2 del libro). **Perturbación** para robustez (ImageNet-C, tokens aleatorios en BERT).

**Simulación:** CARLA, robótica, **StableToolBench** (Guo et al., 2024), eventos raros en finanzas/clima. Persiste la brecha **Sim2Real**.

### Síntesis con IA

- **Self-play** — Dota de OpenAI, AlphaGo.  
- **Parafraseo / traducción** — MetaMath ~400k desde 15k MATH/GSM-8K (Yu et al., 2023); idiomas de bajos recursos con verificación por back-translation.  
- **Traducción de código** — Llama 3 amplía lenguajes.  
- **Reverse instruction** — prompts de IA sobre contenido humano largo de calidad (Köksal, Li, Chen).  
- **Bucle de bootstrapping** — modelo débil → instrucciones sintéticas → finetune → repetir (Li et al., 2023).  
- **SFT long-context** — trocear documentos, Q&A, contexto largo completo.

**Patrones de instrucciones:**

- Temas → subtemas → instrucciones (UltraChat, Ding et al., 2023).  
- **Alpaca:** 175 semillas Self-Instruct → 52k pares con GPT-3 (Taori et al., 2023).

**Pipeline de código Llama 3 (caso de estudio):**

1. Descripciones de problemas con IA.  
2. Soluciones por lenguaje + CoT + reglas de estilo.  
3. Tests unitarios con IA; revisión si falla (~20% autocorrige).  
4. Traducción entre lenguajes + filtro.  
5. Explicaciones/documentación con verificación por **back-translation**.  
→ **Más de 2,7M** ejemplos sintéticos de código.

### Verificación de datos

Prioriza datos **verificables**: parsers, linters, tests, ejecución, back-translation. Si no, **jueces IA** (intercambiar orden para evitar sesgo de posición, NVIDIA 2024). Filtros de consistencia factual (capítulo 4). Heurísticas Self-Instruct: longitud, repetición, instrucciones duplicadas.

Prueba final: **¿mejora el modelo?**

### Límites de datos generados por IA

1. **Calidad** — basura entra, basura sale sin verificación.  
2. **Imitación superficial** — estilo sin razonamiento (**Gudibande et al., 2023**).  
3. **Colapso del modelo** — entrenar recursivamente con sintético olvida eventos raros (Shumailov et al., 2023); mitigable **mezclando real + sintético** (Gerstgrasser et al., 2024).  
4. **Linaje oscuro** — copyright, contaminación de benchmarks.  
5. **Amplificación de sesgos** — bucles de feedback (Taori & Hashimoto, 2023).

**Nemotron-4** usó ~98% sintético en post-training (NVIDIA, 2024)—éxito con verificación rigurosa; no prueba recursión ilimitada.

---

## Destilación de modelos

**Estudiante** pequeño imita **maestro** grande (Hinton et al., 2015)—p. ej. **DistilBERT** (40% más pequeño, ~97% capacidad), **Alpaca** (7B con salidas de davinci-003). Revisa **licencias**—muchas prohíben entrenar competidores con salidas.

No todo entrenamiento sintético es destilación (el estudiante puede superar al maestro, p. ej. Nemotron-4 340B con datos de Mixtral). Datos **autogenerados sin verificar** pueden degradar; bucles sintéticos verificados pueden mejorar (Llama 3).

---

## Procesamiento de datos

Ordena pasos por **eficiencia**; pruebas piloto; **no edites in place**—conserva copia cruda.

### Inspeccionar

Distribuciones: tokens, longitudes, temas, idiomas, sesgo por anotador, desacuerdo inter-anotador. **Inspección manual** (15 minutos) ahorra horas—alto ratio valor/prestigio (Greg Brockman). Verifica hechos en muestras.

### Deduplicar

Duplicados sesgan etiquetas y **filtran** train/test (Lee et al., 2021; Tirumala et al., 2023). Repetir 0,1% de datos 100 veces puede reducir a la mitad el tamaño efectivo del modelo (Anthropic, Hernandez et al., 2022). Métodos: similitud pairwise, **MinHash**, Bloom, embeddings + ANN (dupeGuru, datasketch, lazyNLP).

### Limpiar y filtrar

Quitar HTML/Markdown (Databricks: +20% precisión, −60% tokens). PII/tóxico/copyright (capítulo 4). Active learning / importance sampling / poda de datos (Sorscher et al., 2022). Fatiga de anotadores (Kern et al., 2024).

### Formatear

Alinea **tokenizer y plantilla de chat** (capítulo 5). Convierte few-shot en filas `(entrada, salida)`—inferencia puede usar prompts mínimos (`burger -->` vs 3-shot largo). **Formato train/serve idéntico** (espacios, prefijos).

---

## Cierre del capítulo

El diseño de datasets parte de **comportamientos deseados**, luego calidad, cobertura y cantidad—a menudo con sintético **verificable**. Los datos siguen siendo el cuello de botella donde la automatización se detiene: guías, juicio y compliance siguen necesitando humanos.

El capítulo 9 trata **optimización de inferencia** cuando ya tienes un modelo que merece servirse.

---

## Preguntas de discusión

- Define dimensiones de **calidad** que importen en tus guías de anotación.
- ¿Qué ejes de **cobertura** (idioma, tema, longitud) están infrarrepresentados?
- ¿Cuándo compensa el coste de verificación de **datos sintéticos**?
- ¿Qué regla de **deduplicación** aplicarías antes del SFT?
- ¿Cómo difiere tu mezcla entre fases **pretrain / SFT / preferencias**?

---

## Relacionado

- **Anterior:** [Finetuning](/ai-engineering/docs/es/finetuning) — para qué sirven los datos.
- **Siguiente:** [Optimización de inferencia](/ai-engineering/docs/es/inference-optimization) — servir el modelo que entrenaste.
- **Evaluación:** [Evaluar sistemas de IA modernos](/ai-engineering/docs/es/evaluating-modern-ai-systems) — slices y rúbricas para calidad de datos.
- **Feedback:** [Arquitectura de IA y feedback de usuario](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback) — logs → *data flywheel* de entrenamiento.
- **Repositorio del libro:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glosario:** [Glosario](/ai-engineering/docs/es/glossary) — términos del libro y estas notas.

## Notas finales

Para equipos de aplicación, el capítulo 8 recoloca el finetuning (cap. 7) como **problema de datos primero**. Invertiría pronto en guías de anotación compartidas con eval (cap. 4), un piloto de 50 ejemplos y curvas de escala antes de pagar por 10k etiquetas.

La división **forma vs. hechos** del cap. 7 aplica aquí: el sintético brilla en cobertura y formato; hechos y colas raras siguen necesitando datos reales o pipelines verificables (ejecución de código, back-translation). Trataría **colapso del modelo** e **imitación sin razonamiento** como motivos para limitar la proporción sintética y registrar linaje.

El pipeline de síntesis de código de Llama 3 es la plantilla a copiar en dominios con resultados **comprobables programáticamente**—y extender jueces IA solo donde fallen las comprobaciones.

**Referencia:** Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 8: Dataset Engineering.

---

## Referencias

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 8: Dataset Engineering.

### IA data-centric y competiciones

- [DataPerf](https://dataperf.org/) — MLCommons (2023).
- [DataComp](https://www.datacomp.ai/) — Gadre et al. (2023); escala LM Li et al. (2024).
- [dcbench](https://github.com/stanford-crfm/dcbench) — Eyuboglu & Karlaš (2022).

### Calidad, cobertura y cantidad

- [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) — Zhou et al. (2023).
- [Scaling Instruction-Finetuned Language Models (Flan)](https://arxiv.org/abs/2210.11416) — Chung et al. (2022).
- [The False Promise of Imitating Proprietary LLMs](https://arxiv.org/abs/2305.15717) — Gudibande et al. (2023).
- [Ossification in transfer learning](https://arxiv.org/abs/2102.09574) — Hernandez et al. (2021).
- [Llama 3 paper](https://arxiv.org/abs/2407.21783) — Dubey et al. (2024).
- [Nemotron-4 340B Technical Report](https://arxiv.org/abs/2406.11704) — NVIDIA (2024).

### Datos de instrucción y síntesis

- [Self-Instruct](https://arxiv.org/abs/2212.10560) — Wang et al. (2022).
- [Alpaca](https://arxiv.org/abs/2303.16199) — Taori et al. (2023).
- [UltraChat](https://arxiv.org/abs/2305.14233) — Ding et al. (2023).
- [MetaMath](https://arxiv.org/abs/2309.12288) — Yu et al. (2023).
- [Cosmopedia](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia) — Allal et al. (2024).
- [StableToolBench](https://arxiv.org/abs/2407.08739) — Guo et al. (2024).
- [Discovering LM Behaviors with Model-Written Evaluations](https://arxiv.org/abs/2212.09251) — Perez et al. (2022).
- [The Curse of Recursion / model collapse](https://arxiv.org/abs/2305.17493) — Shumailov et al. (2023).
- [Is Model Collapse Inevitable?](https://arxiv.org/abs/2404.01413) — Gerstgrasser et al. (2024).

### Destilación y deduplicación

- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) — Hinton et al. (2015).
- [DistilBERT](https://arxiv.org/abs/1910.01108) — Sanh et al. (2019).
- [Deduplicating Training Data](https://arxiv.org/abs/2107.06499) — Lee et al. (2021).
- [datasketch (MinHash)](https://github.com/ekzhu/datasketch)

### Hubs y búsqueda de datasets

- [Hugging Face Datasets](https://huggingface.co/datasets)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Data.gov](https://www.data.gov/)
- [OpenML](https://www.openml.org/)
- [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)

### Guías, cursos y herramientas

- [OpenAI — Fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning)
- [Argilla](https://argilla.io/) — Etiquetado humano + IA.
- [Label Studio](https://labelstud.io/)
- [DeepLearning.AI — Data-centric AI](https://www.deeplearning.ai/courses/data-centric-ai/) — Andrew Ng.
- [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) — Huyen.
- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf)

### Repositorio del libro

- [AI Engineering — GitHub (Huyen)](https://github.com/chiphuyen/aie-book) — Recursos de datasets, lazyNLP.
