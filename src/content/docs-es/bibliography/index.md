---
title: "Bibliografía"
description: "Referencias agregadas de todas las notas por capítulo (Huyen, 2025)."
order: 12
---

## Introduction

Enlaces agregados de la sección **## References** de cada capítulo. Edita primero las páginas de capítulo y luego ejecuta `python scripts/build-bibliography.py`.

---

## By chapter

### [Introducción a la construcción de aplicaciones de IA con modelos fundacionales](/ai-engineering/docs/es/introduction-to-building-ai-applications-with-foundation-models)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 1: Introduction to Building AI Applications with Foundation Models.

### Libro y autor

- [AI Engineering — GitHub (aie-book)](https://github.com/chiphuyen/aie-book) — Repositorio complementario de la edición O’Reilly.
- [Chip Huyen — Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) — Libro previo sobre sistemas de ML.
- [O’Reilly — AI Engineering](https://www.oreilly.com/library/view/ai-engineering/9781098166304/)

### Escalamiento y modelos fundacionales

- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — Kaplan et al. (2020).
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — Brown et al., GPT-3 (2020).
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) — Hoffmann et al., Chinchilla (2022).

### Cursos

- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — Taller (español) sobre desarrollo asistido por IA.

### [Comprender los modelos fundacionales](/ai-engineering/docs/es/understanding-foundation-models)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.

### Materiales adicionales para repasar

- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — guía visual de Jay Alammar sobre atención y el bloque transformador.
- [Intro to large language models](https://www.youtube.com/watch?v=zjkBMFhNj_g) — Andrej Karpathy (2023): visión compacta de cómo se entrenan y usan los LLM; complementa bien **transformadores**, ***prompting*** y la narrativa de **retroalimentación humana**. (Si tienes una conferencia concreta titulada *“LLM Lecture: A Deep Dive into Transformers, Prompts, and Human Feedback”*, enlázala aquí en paralelo: el título exacto varía entre cursos.)

### [Metodología de evaluación](/ai-engineering/docs/es/evaluation-methodology)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 3: Evaluation Methodology.

### Métricas y similitud

- [BERTScore](https://arxiv.org/abs/1904.09675) — Zhang et al. (2020).
- [BLEURT](https://arxiv.org/abs/2004.04696) — Sellam et al. (2020).
- [sacreBLEU](https://github.com/mjpost/sacrebleu) — Implementación estándar de BLEU.

### Benchmarks y contaminación

- [MMLU](https://arxiv.org/abs/2009.03300) — Hendrycks et al. (2020).
- [MMLU-Pro](https://arxiv.org/abs/2406.01574) — Wang et al. (2024).
- [Chatbot Arena](https://chat.lmsys.org/) — Evaluación comparativa (LMSYS).
- [Data Contamination in LLMs](https://arxiv.org/abs/2310.17589) — Sainz et al. (2023).

### AI como juez

- [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685) — Zheng et al. (2023).
- [G-Eval](https://arxiv.org/abs/2303.16634) — Liu et al. (2023).

### Corrección funcional

- [HumanEval](https://arxiv.org/abs/2107.03374) — Chen et al. (2021).
- [SWE-bench](https://www.swebench.com/) — Jimenez et al. (2024).

### Cursos

- [UPM — Taller 6 PDF](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — Taller en español.

### [Evaluación de sistemas modernos de IA](/ai-engineering/docs/es/evaluating-modern-ai-systems)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 4: Evaluate AI Systems.

### Evaluación holística

- [HELM](https://crfm.stanford.edu/helm/latest/) — Liang et al., Stanford.
- [OpenAI — Guía de evals](https://platform.openai.com/docs/guides/evals)

### Selección de modelo

- [MMLU](https://arxiv.org/abs/2009.03300) — Hendrycks et al. (2020).
- [Chatbot Arena](https://chat.lmsys.org/)
- [Data Contamination in LLMs](https://arxiv.org/abs/2310.17589) — Sainz et al. (2023).

### Producción

- [Hugging Face — Model Hub](https://huggingface.co/models)
- [vLLM](https://github.com/vllm-project/vllm)

### Cursos

- [UPM — Taller 6 PDF](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf)

### [Ingeniería de prompts](/ai-engineering/docs/es/prompt-engineering)

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

### [RAG y agentes](/ai-engineering/docs/es/rag-and-agents)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 6: RAG and Agents.

Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. https://arxiv.org/abs/2005.11401

Yang, Y., et al. (2025). A survey of AI agent protocols. https://arxiv.org/abs/2504.16736

Anthropic. (2024). Building effective agents. https://www.anthropic.com/engineering/building-effective-agents

Anthropic. (2024). Introducing contextual retrieval. https://www.anthropic.com/news/contextual-retrieval

### Artículos fundacionales (RAG y recuperación)

- [RAG (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401)
- [Reading Wikipedia to Answer Questions (Chen et al., 2017)](https://arxiv.org/abs/1704.00051)
- [BM25 and Beyond (Robertson & Zaragoza, 2009)](https://www.nowpublishers.com/article/Details/INR-019)
- [Reciprocal Rank Fusion](https://plg.uwaterloo.ca/~gvcormac/cormacnorris09a.pdf)
- [Lost in the Middle (Liu et al., 2023)](https://arxiv.org/abs/2307.03172)

### Agentes, planificación y herramientas

- [ReAct (Yao et al., 2022)](https://arxiv.org/abs/2210.03629)
- [Reflexion (Shinn et al., 2023)](https://arxiv.org/abs/2303.11366)
- [Chameleon (Lu et al., 2023)](https://arxiv.org/abs/2304.09842)
- [Planning with World Model (Hao et al., 2023)](https://arxiv.org/abs/2305.14992)
- [Can LLMs Really Reason and Plan? (Kambhampati, 2023)](https://yochan-lab.github.io/papers/llm_reasoning_planning.pdf)

### Guías oficiales y tutoriales

- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Anthropic — Contextual retrieval](https://www.anthropic.com/news/contextual-retrieval)
- [OpenAI — Function calling](https://platform.openai.com/docs/guides/function-calling)
- [LangChain — Conceptos RAG](https://python.langchain.com/docs/concepts/rag/)
- [LlamaIndex — Construir RAG](https://docs.llamaindex.ai/en/stable/optimizing/building_rag/)

### Búsqueda vectorial y bases de datos

- [FAISS](https://github.com/facebookresearch/faiss)
- [ANN-Benchmarks](https://ann-benchmarks.com/)
- [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)
- [BEIR](https://github.com/beir-cellar/beir)
- [Zilliz — Vector search](https://zilliz.com/learn/what-is-vector-search)

### Frameworks y orquestación

- [DSPy](https://dspy.ai/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- [AutoGen](https://microsoft.github.io/autogen/)
- [Composio](https://composio.dev/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [Google A2A](https://google.github.io/A2A/)

### Evaluación y seguridad

- [Ragas](https://docs.ragas.io/)
- [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)
- [Microsoft — Red teaming LLM](https://learn.microsoft.com/es-es/azure/ai-foundry/openai/concepts/red-teaming)
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

### Cursos, vídeos y talleres

- [DeepLearning.AI — Vector Databases](https://www.deeplearning.ai/short-courses/building-applications-vector-databases/)
- [DeepLearning.AI — AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/)
- [DeepLearning.AI — Cursos de agentes](https://www.deeplearning.ai/courses/) — Revisar rutas agentic actuales.
- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf)
- [Pinecone — What is RAG?](https://www.pinecone.io/learn/retrieval-augmented-generation/)

### Repositorio del libro

- [AI Engineering — GitHub (Huyen)](https://github.com/chiphuyen/aie-book) — Código cap. 6, benchmark de agentes, recursos IR.

### [Finetuning](/ai-engineering/docs/es/finetuning)

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

### [Dataset Engineering](/ai-engineering/docs/es/dataset-engineering)

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

### [Inference Optimization](/ai-engineering/docs/es/inference-optimization)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 9: Inference Optimization.

### Roofline, métricas y perfilado

- [Roofline](https://people.eecs.berkeley.edu/~kubitron/cs252/handouts/papers/RooflineVyNoYellow.pdf) — Williams et al. (2009).
- [NVIDIA Nsight](https://developer.nvidia.com/nsight-systems)
- [Anyscale — LLM inference performance](https://www.anyscale.com/blog/llm-inference-performance) — Kadous et al. (2023).
- [LinkedIn — reflexiones despliegue GenAI](https://www.linkedin.com/blog/engineering/generative-ai) — (2024).

### Prefill/decode y sistemas de serving

- [DistServe](https://arxiv.org/abs/2401.09670) — Zhong et al. (2024).
- [Orca: Continuous Batching](https://www.usenix.org/conference/osdi22/presentation/yu) — Yu et al. (2022).
- [vLLM / PagedAttention](https://arxiv.org/abs/2309.06180) — Kwon et al. (2023).
- [vLLM](https://github.com/vllm-project/vllm)
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)
- [llama.cpp](https://github.com/ggerganov/llama.cpp)

### Aceleración de decodificación

- [Speculative Decoding](https://arxiv.org/abs/2211.10438) — Leviathan et al. (2022); Chen et al. (2023).
- [Inference with Reference](https://arxiv.org/abs/2304.04487) — Yang et al. (2023).
- [Medusa](https://arxiv.org/abs/2401.10774) — Cai et al. (2024).
- [Lookahead Decoding](https://arxiv.org/abs/2402.02057) — Fu et al. (2024).

### Atención y KV cache

- [FlashAttention](https://arxiv.org/abs/2205.14135) — Dao et al. (2022).
- [FlashAttention-3](https://arxiv.org/abs/2407.08608) — Shah et al. (2024).
- [Efficiently Scaling Transformer Inference](https://arxiv.org/abs/2211.05102) — Pope et al. (2022).
- [GQA](https://arxiv.org/abs/2305.13245) — Ainslie et al. (2023).

### Hardware y utilización

- [PaLM](https://arxiv.org/abs/2204.02311) — Chowdhery et al. (2022) — MFU.
- [ML Accelerator Survey](https://arxiv.org/abs/2303.04608) — Desislavov et al. (2023).
- [PyTorch — torch.compile Llama](https://pytorch.org/blog/accelerating-generative-ai/) — (2023).
- [OpenAI Triton](https://github.com/triton-lang/triton)

### APIs, caching y batch

- [OpenAI — Batch API](https://platform.openai.com/docs/guides/batch)
- [Google Gemini — Context caching](https://ai.google.dev/gemini-api/docs/caching)
- [Anthropic — Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
- [OpenAI — Prompt caching](https://platform.openai.com/docs/guides/prompt-caching)

### Compiladores

- [Apache TVM](https://tvm.apache.org/)
- [MLIR](https://mlir.llvm.org/)
- [torch.compile](https://pytorch.org/docs/stable/torch.compiler.html)
- [NVIDIA TensorRT](https://developer.nvidia.com/tensorrt)

### Cursos y talleres

- [Full Stack LLM Bootcamp — serving (YouTube)](https://www.youtube.com/results?search_query=full+stack+llm+bootcamp+serving)
- [Meta — Llama inference (engineering blog)](https://engineering.fb.com/)
- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf)

### Repositorio del libro

- [AI Engineering — GitHub (Huyen)](https://github.com/chiphuyen/aie-book)

### [AI Engineering Architecture and User Feedback](/ai-engineering/docs/es/ai-engineering-architecture-and-user-feedback)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Capítulo 10: AI Engineering Architecture and User Feedback.

### Arquitectura, gateways y guardrails

- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) — NVIDIA.
- [Purple Llama](https://ai.meta.com/purple-llama/) — Meta.
- [Portkey AI Gateway](https://github.com/Portkey-AI/gateway)
- [MLflow AI Gateway](https://mlflow.org/docs/latest/llms/gateway/index.html)
- [OpenAI Moderation API](https://platform.openai.com/docs/guides/moderation)
- [Perspective API](https://perspectiveapi.com/)

### Orquestación y observabilidad

- [LangChain](https://www.langchain.com/)
- [LlamaIndex](https://www.llamaindex.ai/)
- [LangSmith](https://www.langchain.com/langsmith)
- [OpenTelemetry](https://opentelemetry.io/)
- [Arize Phoenix](https://github.com/Arize-ai/phoenix)

### Caché y routing

- [GPTCache](https://github.com/zilliztech/GPTCache)

### Feedback y preferencias

- [FITS dataset](https://arxiv.org/abs/2204.10091) — Xu et al. (2022).
- [Learning from Natural Language Feedback](https://arxiv.org/abs/2306.08899) — Yuan et al. (2023).
- [InstructGPT / RLHF](https://arxiv.org/abs/2203.02155) — Ouyang et al. (2022).
- [Sycophancy in LLMs](https://arxiv.org/abs/2310.13581) — Sharma et al. (2023).

### Deriva de modelos

- [How Is ChatGPT’s Behavior Changing?](https://arxiv.org/abs/2307.09009) — Chen et al. (2023).

### Diseño de producto

- [Apple HIG — Ratings](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews)
- [Midjourney docs](https://docs.midjourney.com/)
- [GitHub Copilot](https://docs.github.com/en/copilot)

### Monitorización general

- [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) — Huyen (2022).

### Cursos

- [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/)
- [DeepLearning.AI — Building Systems with the ChatGPT API](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/)
- [UPM — Taller 6 (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf)

### Repositorio del libro

- [AI Engineering — GitHub (Huyen)](https://github.com/chiphuyen/aie-book)

### [Glosario](/ai-engineering/docs/es/glossary)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.

- [Repositorio del libro — aie-book](https://github.com/chiphuyen/aie-book)

### [Epílogo](/ai-engineering/docs/es/epilogue)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Epílogo, p. 495.

- [AI Engineering — repositorio del libro](https://github.com/chiphuyen/aie-book)
- [Chip Huyen — comunicación](https://huyenchip.com/communication)

---

## Relacionado

- [Mapa del libro](/ai-engineering/docs/es/book-map) — orden y prerequisitos
- [Overview](/ai-engineering/docs/es) — índice de capítulos
- [Glosario](/ai-engineering/docs/es/glossary) — términos clave
