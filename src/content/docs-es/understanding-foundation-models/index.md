---
title: "Comprender los modelos fundacionales"
description: "Resumen del capítulo 2 — AI Engineering (Huyen, 2025)"
order: 2
---

## Comprender los modelos fundacionales

> While you don't need to know how to develop a model to use it, a high-level understanding will help you decide what model to use and how to adapt it to your needs.
>
> — Huyen (2025, p. 49)

Este capítulo se sitúa **por encima de la receta de entrenamiento** que una API propietaria nunca revelará por completo. Aun así explica las palancas que moldean el comportamiento en producción: **de dónde salieron los datos**, **cómo se modeló y escaló el stack**, **cómo el post-training convirtió la completación cruda en producto** y **cómo el muestreo convierte logits en experiencia**—incluidas la inconsistencia y la alucinación.

---

## Datos

### Los datos definen la capacidad

Un modelo fundacional **hereda** sesgos, fortalezas y puntos ciegos de su mezcla de entrenamiento. Si un idioma o dominio casi no aparece en el pre-entrenamiento, el modelo no lo compensa por arte de magia en inferencia—la calidad, la latencia y el coste en idiomas “de cola” suelen seguir esa escasez.

> An AI model is only as good as the data it was trained on. If there's no Vietnamese in the training data, the model won't be able to translate from English into Vietnamese.
>
> — Huyen (2025, p. 50)

Los **corpus a escala web** (p. ej. Common Crawl y subconjuntos filtrados como C4) son atractivos por estar **disponibles**, no por ser limpios: *clickbait*, propaganda, toxicidad y fuentes poco fiables aparecen en análisis de dominios frecuentes. Las heurísticas (p. ej. filtrar enlaces de Reddit para GPT-2) mejoran el rendimiento pero no borran el sesgo.

### Distribución de idiomas (ilustrativa)

El inglés domina muchos rastreos; las lenguas de cola pueden ser **órdenes de magnitud** más raras—lo que marca diferencias en calidad, cobertura de evaluación y economía de productos multilingües. Cuotas orientativas de análisis tipo Common Crawl (véase la tabla 2-1 del libro; cifras redondeadas):

| Idioma | Cuota aproximada |
| --- | ---: |
| Inglés | 45,8% |
| Ruso | 6,0% |
| Alemán | 5,9% |
| Chino | 4,9% |
| Punyabí | menos del 0,01% |

**Implicación de ingeniería:** antes de comprometer un modelo, pregunta por la **receta de datos** con la que se entrenó (divulgada o inferida) y si los idiomas y dominios de tus usuarios están **en distribución**. El capítulo 8 profundiza en curación y datos sintéticos cuando debas cerrar tú mismo la brecha.

---

## Modelado

### Arquitectura: dominio del transformador

Los transformadores ganaron en modelado de lenguaje porque la **auto-atención** mezcla representaciones a lo largo de la secuencia y **paraleliza** mucho más que las pilas recurrentes clásicas—a costa de un coste de atención **cuadrático** en formulaciones ingenuas al crecer el contexto. Ese coste motiva una línea amplia de trabajo en **atención eficiente**, **trucos de contexto largo** y **capas de secuencia alternativas**.

El libro repasa el panorama más allá del “solo transformador”, incluyendo **Mamba** (modelado de secuencia selectivo / tiempo lineal) e híbridos como **Jamba** (bloques intercalados transformador–Mamba)—contexto útil cuando los proveedores anuncian arquitecturas nuevas.

> With transformers, the input tokens can be processed in parallel, significantly speeding up input processing.
>
> — Huyen (2025, p. 60) (discusión del capítulo sobre transformadores frente a modelos secuenciales)

### Tamaño y leyes de escalado

La calidad del modelo no es “solo parámetros”: acopla **parámetros**, **tokens vistos en entrenamiento** y **FLOPs**. Para un **presupuesto de cómputo fijo**, la ley de escalado **Chinchilla** (DeepMind, 2022) sugiere un óptimo mucho más **rico en datos** que la práctica de eras anteriores: del orden de **~20 tokens de entrenamiento por parámetro** en pre-entrenamiento *compute-optimal* (p. ej. un modelo de ~3B parámetros del orden de ~60B tokens), escalando parámetros y tokens a la par al duplicar presupuesto.

> Given a fixed amount of FLOPs, what model size and dataset size would give the best performance? A model that can achieve the best performance given a fixed compute budget is **compute-optimal**.
>
> — Huyen (2025, p. 72) (encuadre de Chinchilla / *compute-optimal* en el capítulo)

**Matiz de producto:** Chinchilla optimiza la **pérdida de pre-entrenamiento** bajo presupuesto de entrenamiento. Los equipos reales también optimizan **coste de inferencia**, **latencia** y **usabilidad**—el libro señala que algunas familias ampliamente adoptadas se sitúan de forma deliberada “sub-óptima” en pérdida bruta para lanzar modelos más pequeños y baratos de servir.

---

## Post-training

El pre-entrenamiento produce una **máquina de completar** entrenada en texto a escala de internet—potente pero no alineada con chat, rechazos, formatos de herramientas ni la voz de tu marca. El **post-training** es el puente entre “capacidad cruda” y “producto”.

Un **modelo mental de tres fases** habitual (figuras 2-10 y 2-11 del libro):

1. **Pre-entrenamiento** — aprendizaje auto-supervisado sobre datos amplios (comportamiento base “indómito”).
2. **Supervised finetuning (SFT)** — demostraciones de alta calidad `(prompt, response)` para que el modelo **siga instrucciones** y converse en lugar de solo completar prosa.
3. **Ajuste por preferencias** — p. ej. tuberías tipo **RLHF** o alternativas como **DPO**, con señales de preferencia humana (o asistida por modelo) y a menudo un **modelo de recompensa** para empujar hacia regiones **útiles, honestas e inofensivas**.

El meme del **Shoggoth con carita** resume la intuición: el pre-entrenamiento es la masa alienígena; el SFT y las preferencias esculpen algo **apto para cliente**.

> You can think of post-training as unlocking the capabilities that the pre-trained model already has but are hard for users to access via prompting alone.
>
> — Huyen (2025, pp. 78–79)

La alineación **no está resuelta**: las preferencias son plurales, los modelos de recompensa mal-especifican objetivos y algunas intervenciones de seguridad cruzan trade-offs con factualidad o capacidad—sigue haciendo falta criterio de ingeniería.

---

## Muestreo

Cada paso de decodificación produce una **distribución sobre todo el vocabulario**; el **muestreo** es la regla para convertir esos logits en el siguiente token. Ese mecanismo explica tanto la **variación agradable** como la **inconsistencia frustrante**.

### Temperatura y perillas afines

La **temperatura** reescala los logits antes del *softmax*: valores bajos **aguzan** la distribución (más determinista, “aburrida”, fiable); valores altos la **aplanan**, subiendo tokens raros y la **creatividad** a riesgo de coherencia.

> Intuitively, a higher temperature reduces the probabilities of common tokens, and as a result, increases the probabilities of rarer tokens. This enables models to create more creative responses.
>
> — Huyen (2025, p. 91)

En la práctica, `temperature = 0` (estilo *argmax* / codicioso) es habitual cuando se necesita repetibilidad—las APIs lo simulan sin dividir literalmente entre cero. **Top-*p*** (núcleo), **top-*k*** y otros muestreadores moldean la cola; la perilla adecuada depende de la tarea (escritura creativa frente a JSON estricto).

### Cómputo en tiempo de inferencia (*test-time compute*)

El **test-time compute** gasta **inferencia extra** para mejorar la calidad: muestrear **muchas** completaciones y **seleccionar** con un verificador, modelo de recompensa, heurística (p. ej. la respuesta más corta) o voto de consistencia (**self-consistency** / mayoría en matemáticas). El libro da ejemplos llamativos: los verificadores pueden rivalizar con saltos enormes de parámetros en algunos regímenes, y las curvas “mejor de *N*” saturan (p. ej. ganancias que se aplastan tras cientos de muestras). Es la palanca explícita **cómputo ↔ calidad** en despliegue.

### Salidas estructuradas

Para **agentes**, **llamadas a herramientas** y **pipelines legibles por máquina**, a menudo hace falta generación **restringida**: modos JSON, decodificadores guiados por gramática, restricciones tipo regex o marcos (p. ej. estilo Guidance—véase el libro). Ojo: “JSON válido” ≠ “JSON semánticamente correcto”. Las mitigaciones se apilan: mejores *prompts*, decodificación restringida, *finetuning* y evaluación.

### Alucinaciones frente a ruido de muestreo

> If inconsistency arises from randomness in the sampling process, the cause of hallucination is more nuanced… A model can output something that is believed to have never been seen before in the training data.
>
> — Huyen (2025, p. 107)

Así: **bajar la temperatura** reduce varianza, pero la **alucinación** también enlaza con objetivos de entrenamiento, límites de conocimiento, autoengaño / efecto bola de nieve en generaciones largas y contexto faltante—lo abordan después **RAG**, la **evaluación** y las **barreras de producto**, no el muestreo aislado.

---

## Enseñanzas clave

1. **Los datos dictan el destino** — capacidades y sesgos se heredan de la mezcla de entrenamiento; lee la **receta de datos** antes de elegir proveedor o *checkpoint* abierto.
2. **Respeta las leyes de escalado** — en pre-entrenamiento con presupuesto de FLOPs, el balance estilo **Chinchilla** (tokens ≈ 20 × parámetros) es la guía canónica; valida aparte la economía de **servicio**.
3. **La alineación crea usabilidad** — el **SFT** más el ajuste por **preferencias** convierte la completación pre-entrenada en algo que el usuario puede dirigir; ahí se fijan muchos comportamientos de seguridad y formato.
4. **Domina el dial de muestreo** — temperatura, **top-*p***, **top-*k*** moldean creatividad frente a determinismo; el **test-time compute** y la **decodificación restringida** son herramientas de primera clase junto al *prompting*.
5. **Probabilístico por construcción** — planifica inconsistencia y alucinación con **evaluación**, **recuperación** y **arquitectura**, no solo con intuición.

---

## Cierre del capítulo

El capítulo 2 conecta **datos de entrenamiento → arquitectura y escala → post-training → decodificación** con lo que ves en una API. Los capítulos siguientes construyen la **disciplina de evaluación** que necesitas antes de confiar en esos comportamientos en producción.

---

## Notas finales

Leo este capítulo como recordatorio de que “elegir modelo” es en realidad un **paquete de decisiones**: la **mezcla del rastreo** detrás del multilingüe justo, el trade **tipo Chinchilla** (o no) que fijó el *cutoff* y la pérdida, la capa **SFT/RLHF** que lo volvió *conversable*, y el **muestreador** que activo en tiempo de inferencia. Nada de eso cabe en una celda de *leaderboard*, pero explica por qué dos modelos con puntuaciones parecidas se comportan distinto con *mis* prompts.

Lo que llevo a la práctica: (1) **auditar encaje de datos** primero—sobre todo fuera del inglés y en dominios de nicho; (2) tratar **temperatura**, **top-*p*** y **mejor de *N*** como perillas de producto con curva de coste, no como detalle; (3) asumir que el **modo JSON** solo garantiza sintaxis hasta demostrar lo contrario con pruebas; (4) mantener separado el modelo mental de **alucinación**—ruido de muestreo frente a sobreconfianza estructural—para no “arreglar” con la herramienta equivocada. El hilo del libro es que nada sustituye la **evaluación**; este capítulo motiva por qué existe el capítulo 3.

---

## Referencias

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.

### Materiales adicionales para repasar

- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — guía visual de Jay Alammar sobre atención y el bloque transformador.
- [Intro to large language models](https://www.youtube.com/watch?v=zjkBMFhNj_g) — Andrej Karpathy (2023): visión compacta de cómo se entrenan y usan los LLM; complementa bien **transformadores**, ***prompting*** y la narrativa de **retroalimentación humana**. (Si tienes una conferencia concreta titulada *“LLM Lecture: A Deep Dive into Transformers, Prompts, and Human Feedback”*, enlázala aquí en paralelo: el título exacto varía entre cursos.)
