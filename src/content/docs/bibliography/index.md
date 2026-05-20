---
title: "Bibliography"
description: "Aggregated references from all chapter notes (Huyen, 2025)."
order: 12
---

## Introduction

Aggregated links from each chapter's **## References** section. Edit the chapter pages first, then run `python scripts/build-bibliography.py`.

---

## By chapter

### [Introduction to Building AI Applications with Foundation Models](/ai-engineering/docs/introduction-to-building-ai-applications-with-foundation-models)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 1: Introduction to Building AI Applications with Foundation Models.

### Book and author resources

- [AI Engineering — GitHub (aie-book)](https://github.com/chiphuyen/aie-book) — Companion repo for the O’Reilly edition.
- [Chip Huyen — Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) — Prior book on ML systems (many principles still apply).
- [O’Reilly — AI Engineering product page](https://www.oreilly.com/library/view/ai-engineering/9781098166304/)

### Scaling and foundation models

- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — Kaplan et al. (2020).
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — Brown et al., GPT-3 (2020).
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) — Hoffmann et al., Chinchilla (2022).

### Industry framing

- [OpenAI — Models documentation](https://platform.openai.com/docs/models) — Model-as-a-service APIs (evolving catalog).
- [McKinsey — The state of AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) — Enterprise adoption surveys (periodic).

### Courses

- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — Workshop slides (Spanish) on AI-assisted development.

### [Understanding Foundation Models](/ai-engineering/docs/understanding-foundation-models)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 2: Understanding Foundation Models.

### Foundational papers

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Vaswani et al. (2017), Transformer.
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — Brown et al., GPT-3 (2020).
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) — Hoffmann et al., Chinchilla (2022).
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — Ouyang et al., InstructGPT / RLHF (2022).

### Additional materials

- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar.
- [Intro to large language models](https://www.youtube.com/watch?v=zjkBMFhNj_g) — Andrej Karpathy (2023).

### [Evaluation Methodology](/ai-engineering/docs/evaluation-methodology)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 3: Evaluation Methodology.

### Metrics and similarity

- [BLEU](https://arxiv.org/abs/2109.11346) — Papineni et al.; see also [sacreBLEU](https://github.com/mjpost/sacrebleu).
- [ROUGE](https://aclanthology.org/W04-1013/) — Lin (2004).
- [BERTScore](https://arxiv.org/abs/1904.09675) — Zhang et al. (2020).
- [BLEURT](https://arxiv.org/abs/2004.04696) — Sellam et al. (2020).

### Benchmarks and contamination

- [MMLU](https://arxiv.org/abs/2009.03300) — Hendrycks et al. (2020).
- [MMLU-Pro](https://arxiv.org/abs/2406.01574) — Wang et al. (2024).
- [Chatbot Arena](https://chat.lmsys.org/) — LMSYS comparative evaluation platform.
- [Data Contamination in LLMs](https://arxiv.org/abs/2310.17589) — Sainz et al. (2023).

### AI as judge

- [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685) — Zheng et al. (2023).
- [G-Eval](https://arxiv.org/abs/2303.16634) — Liu et al. (2023).

### Functional correctness

- [HumanEval](https://arxiv.org/abs/2107.03374) — Chen et al. (2021).
- [SWE-bench](https://www.swebench.com/) — Jimenez et al. (2024).

### Courses

- [UPM — Taller 6 PDF](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — Spanish workshop on AI-assisted software.

### [Evaluating Modern AI Systems](/ai-engineering/docs/evaluating-modern-ai-systems)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 4: Evaluate AI Systems.

### Holistic evaluation

- [HELM](https://crfm.stanford.edu/helm/latest/) — Liang et al., Stanford holistic benchmarking.
- [OpenAI — Evals guide](https://platform.openai.com/docs/guides/evals) — Product-oriented eval workflows.

### Model selection and benchmarks

- [MMLU](https://arxiv.org/abs/2009.03300) — Hendrycks et al. (2020).
- [Chatbot Arena](https://chat.lmsys.org/) — Comparative ranking (LMSYS).
- [Data Contamination in LLMs](https://arxiv.org/abs/2310.17589) — Sainz et al. (2023).

### Build vs. buy and production

- [Hugging Face — Model Hub](https://huggingface.co/models) — Open weights and cards.
- [vLLM](https://github.com/vllm-project/vllm) — High-throughput serving for self-hosting comparisons.

### Practitioner essays

- [Greg Brockman on evals](https://x.com/gdb) — “Evals are surprisingly often all you need” (search talks/posts for context).

### Courses

- [UPM — Taller 6 PDF](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — Spanish workshop on AI-assisted software.

### [Prompt Engineering](/ai-engineering/docs/prompt-engineering)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 5: Prompt Engineering.

### Official guides and tutorials (model providers)

- [OpenAI — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) — Core practices: clarity, examples, decomposition, structured outputs.
- [OpenAI Cookbook](https://cookbook.openai.com/) — Recipes and patterns for production prompting and APIs.
- [Anthropic — Prompt engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) — Claude-specific guidance, personas, and examples.
- [Anthropic — Content moderation with Claude](https://docs.anthropic.com/en/docs/build-with-claude/content-moderation) — Using models as moderators (cited in Chapter 5).
- [Google Cloud — Prompt design strategies](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies) — Vertex AI / Gemini prompt design.
- [Meta — Llama prompting how-to](https://www.llama.com/docs/how-to-guides/prompting/) — Chat templates and Llama-specific tips.
- [Microsoft Learn — Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/prompt-engineering) — Azure OpenAI prompting patterns.

### Papers and conceptual deep dives

- [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165) — Brown et al. (2020); introduces in-context learning.
- [Chain-of-Thought Prompting Elicits Reasoning](https://arxiv.org/abs/2201.11903) — Wei et al. (2022).
- [The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions](https://arxiv.org/abs/2404.19756) — Wallace et al., OpenAI (2024); system vs. user vs. tool priority.
- [Understanding In-Context Learning in Foundation Models](https://ai.stanford.edu/blog/understanding-incontext/) — Stanford AI Lab overview.
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — Liu et al. (2023); needle-in-a-haystack motivation.
- [Not What You’ve Signed Up For: Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — Greshake et al. (2023).
- [Scalable Extraction of Training Data from Production Language Models](https://arxiv.org/abs/2311.17035) — Nasr et al. (2023); divergence / repeated-token attacks.

### Tools, frameworks, and prompt automation

- [DSPy](https://dspy.ai/) — Programmatic prompt optimization and pipelines (Khattab et al.).
- [Guidance](https://github.com/guidance-ai/guidance) — Constrained / structured generation.
- [Instructor](https://github.com/instructor-ai/instructor) — Structured outputs from LLM APIs.
- [Outlines](https://github.com/dottxt-ai/outlines) — Structured text generation.
- [Promptbreeder](https://arxiv.org/abs/2309.16797) — Evolutionary prompt optimization (DeepMind).
- [TextGrad](https://arxiv.org/abs/2406.07496) — Gradient-style prompt refinement (Stanford).
- [Firebase Genkit — Dotprompt](https://firebase.google.com/docs/genkit/dotprompt) — Versioned `.prompt` files with schema.
- [LangSmith / LangChain Hub](https://smith.langchain.com/hub) — Shared prompt templates (inspect defaults for safety).

### Prompt libraries, catalogs, and community lists

- [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) — Large community prompt collection (English).
- [PlexPt/awesome-chatgpt-prompts-zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) — Chinese prompt collection.
- [PromptHero](https://prompthero.com/) — Public prompt discovery (image and text).
- [PromptBase](https://promptbase.com/) — Marketplace for buying/selling prompts.
- [Cursor Directory](https://cursor.directory/) — Prompts and rules for coding assistants.

### Security, jailbreaking, and red teaming

- [Microsoft — Plan red teaming for LLM applications](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/red-teaming) — Enterprise red-team playbook.
- [Azure PyRIT](https://github.com/Azure/PyRIT) — Python Risk Identification Toolkit for generative AI.
- [garak (NVIDIA)](https://github.com/NVIDIA/garak) — LLM vulnerability scanner.
- [llm-security (Greshake)](https://github.com/greshake/llm-security) — Security probing utilities.
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — Prompt injection and related risks in a standard framework.
- [Dropbox — Evolution of repeated token attacks](https://dropbox.tech/machine-learning/bye-bye-bye-evolution-of-repeated-token-attacks-on-chatgpt-models) — Breitenbach & Wood (2024).

### Blogs and practitioner write-ups

- [Hamel Husain — “Show Me the Prompt”](https://hamel.dev/blog/posts/prompt/) — Why you should inspect tool-generated prompts.
- [Brex — Prompt engineering guide](https://www.brex.com/journal/prompt-engineering-guide) — Practical enterprise patterns (includes leakage examples).
- [Shreya Shankar — Practical needle-in-a-haystack for doctor visits](https://shreya-shankar.github.io/) — NIAH testing in production-like settings (2024; search author site for latest post).

### Courses and workshops

- [DeepLearning.AI — ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) — Short course (OpenAI + Isa Fulford).
- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — *Innovación Educativa UPM*: workshop slides on AI-assisted software development and prompting (Spanish).

### [RAG and Agents](/ai-engineering/docs/rag-and-agents)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 6: RAG and Agents.

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yau, M., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS*. https://arxiv.org/abs/2005.11401

Yang, Y., Chai, H., Song, Y., Qi, S., Wen, M., Li, N., Liao, J., Hu, H., Lin, J., Chang, G., Liu, W., Wen, Y., Yu, Y., & Zhang, W. (2025). A survey of AI agent protocols. *arXiv*. https://arxiv.org/abs/2504.16736

Anthropic. (2024). Building effective agents. https://www.anthropic.com/engineering/building-effective-agents

Anthropic. (2024). Introducing contextual retrieval. https://www.anthropic.com/news/contextual-retrieval

### Foundational papers (RAG & retrieval)

- [Retrieval-Augmented Generation (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401) — Original RAG paper.
- [Reading Wikipedia to Answer Open-Domain Questions (Chen et al., 2017)](https://arxiv.org/abs/1704.00051) — Retrieve-then-generate precursor.
- [The Probabilistic Relevance Framework: BM25 and Beyond](https://www.nowpublishers.com/article/Details/INR-019) — Robertson & Zaragoza (2009).
- [Reciprocal Rank Fusion](https://plg.uwaterloo.ca/~gvcormac/cormacnorris09a.pdf) — Cormack et al. (2009); hybrid ranking.
- [Lost in the Middle](https://arxiv.org/abs/2307.03172) — Liu et al. (2023); context position effects.

### Agents, planning, and tool use

- [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) — Yao et al. (2022).
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — Shinn et al. (2023).
- [Chameleon: Plug-and-Play Compositional Reasoning](https://arxiv.org/abs/2304.09842) — Lu et al. (2023).
- [Reasoning with Language Model is Planning with World Model](https://arxiv.org/abs/2305.14992) — Hao et al. (2023).
- [Can LLMs Really Reason and Plan?](https://yochan-lab.github.io/papers/llm_reasoning_planning.pdf) — Kambhampati (2023).

### Official guides and tutorials

- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Chaining, routing, evaluator–optimizer, orchestrator–workers.
- [Anthropic — Contextual retrieval](https://www.anthropic.com/news/contextual-retrieval) — Chunk situating for search.
- [OpenAI — Function calling](https://platform.openai.com/docs/guides/function-calling) — Tool use / agents via API.
- [LangChain — RAG conceptual guide](https://python.langchain.com/docs/concepts/rag/) — End-to-end RAG patterns (verify versions).
- [LlamaIndex — RAG](https://docs.llamaindex.ai/en/stable/optimizing/building_rag/) — Indexing, retrieval, evaluation.

### Vector search and databases

- [FAISS (Meta)](https://github.com/facebookresearch/faiss) — Similarity search library.
- [ANN-Benchmarks](https://ann-benchmarks.com/) — Compare ANN algorithms.
- [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — Embedding model evaluation.
- [BEIR](https://github.com/beir-cellar/beir) — Benchmarking IR harness.
- [Zilliz — Vector search explained](https://zilliz.com/learn/what-is-vector-search) — HNSW, IVF, etc.

### Frameworks and orchestration

- [DSPy](https://dspy.ai/) — Programs over prompts (also Ch. 5).
- [LangGraph](https://langchain-ai.github.io/langgraph/) — Stateful agent workflows.
- [AutoGen (Microsoft)](https://microsoft.github.io/autogen/) — Multi-agent conversations.
- [Composio](https://composio.dev/) — Enterprise tool integrations for agents.
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — Context-oriented agent–resource protocol.
- [Google A2A protocol](https://google.github.io/A2A/) — Agent-to-agent interoperability (check current spec).

### Evaluation and security (RAG + agents)

- [Ragas](https://docs.ragas.io/) — RAG evaluation (faithfulness, context precision).
- [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) — Tool-use benchmarks.
- [Microsoft — Plan red teaming for LLMs](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/red-teaming) — Agent safety testing.
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — Injection via RAG/tools.

### Courses, videos, and workshops

- [DeepLearning.AI — Building Applications with Vector Databases](https://www.deeplearning.ai/short-courses/building-applications-vector-databases/) — Embeddings + retrieval basics.
- [DeepLearning.AI — AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) — Agent workflows.
- [Andrew Ng — Agentic AI short course series](https://www.deeplearning.ai/courses/) — Check latest agentic tracks on DeepLearning.AI.
- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — Spanish workshop slides (AI-assisted development).
- [Pinecone — What is RAG?](https://www.pinecone.io/learn/retrieval-augmented-generation/) — Accessible RAG primer (vendor blog).

### Book repository

- [AI Engineering — GitHub (Huyen)](https://github.com/chiphuyen/aie-book) — Chapter 6 code, agent benchmark, extra IR resources.

### [Finetuning](/ai-engineering/docs/finetuning)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 7: Finetuning.

### Foundational papers

- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) — Hu et al. (2021).
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) — Dettmers et al. (2023).
- [Training language models to follow instructions (InstructGPT)](https://arxiv.org/abs/2203.02155) — Ouyang et al. (2022).
- [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) — Lewis et al. (2020) — cited for contrast with finetuning.
- [Fine-Tuning or Retrieval? Comparing Knowledge Injection](https://arxiv.org/abs/2312.05934) — Ovadia et al. (2024) — RAG vs finetune on current events.
- [TIES-Merging](https://arxiv.org/abs/2306.01708) — Yadav et al. (2023).
- [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089) — Ilharco et al. (2022).

### Memory and training math

- [Transformer Inference Arithmetic](https://kipp.ly/transformer-inference-arithmetic/) — Carol Chen.
- [Transformer Math 101](https://blog.eleuther.ai/transformer-math-101/) — EleutherAI (Anthony et al., 2023).
- [Reducing Activation Recomputation in Large Transformer Models](https://arxiv.org/abs/2205.05198) — Korthikanti et al. (2022).
- [Mixed Precision Training](https://arxiv.org/abs/1710.03740) — Micikevicius et al. (2017).

### Official guides and courses

- [OpenAI — Fine-tuning best practices](https://platform.openai.com/docs/guides/fine-tuning) — Progression and distillation paths.
- [Hugging Face — PEFT documentation](https://huggingface.co/docs/peft) — LoRA, adapters, soft prompts.
- [Hugging Face — LLaMA-Factory](https://github.com/hiyouga/LlamaFactory) — Multi-model finetuning UI/CLI.
- [unsloth](https://github.com/unslothai/unsloth) — Fast LoRA/QLoRA training.
- [DeepSpeed](https://www.deepspeed.ai/) — ZeRO, memory optimization, distributed training.
- [DeepLearning.AI — Finetuning Large Language Models](https://www.deeplearning.ai/short-courses/finetuning-large-language-models/) — Short course (Andrew Ng / Sharon Zhou).
- [DeepLearning.AI — Efficiently Serving LLMs](https://www.deeplearning.ai/short-courses/efficiently-serving-llms/) — Serving including adapters.
- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — Spanish workshop (related adaptation stack).

### Agent protocols and interoperability (supplementary)

- [A Survey of AI Agent Protocols](https://arxiv.org/abs/2504.16736) — Yang et al. (2025) — MCP, A2A; complements deployment of finetuned adapters.
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

### Model merging and multi-task

- [Model soups](https://arxiv.org/abs/2203.05482) — Wortsman et al. (2022).
- [Git Re-Basin](https://arxiv.org/abs/2209.04836) — Ainsworth et al. (2022) — alignment before merge.
- [MergeKit](https://github.com/arcee-ai/mergekit) — Practical merging toolkit.
- [AdapterHub](https://adapterhub.ml/) — Adapter discovery and sharing.

### Quantization and low-bit inference

- [LLM.int8()](https://arxiv.org/abs/2208.07339) — Dettmers et al. (2022).
- [GPTQ](https://arxiv.org/abs/2210.17323) — Frantar et al. (2022).
- [bitsandbytes](https://github.com/TimDettmers/bitsandbytes) — 8-bit/4-bit utilities used by QLoRA.

### Videos and talks

- [Hugging Face — PEFT + LoRA tutorial (YouTube)](https://www.youtube.com/results?search_query=huggingface+peft+lora+tutorial) — Search for latest official walkthroughs.
- [Andrej Karpathy — Let's build GPT (training intuition)](https://www.youtube.com/watch?v=kCc8FmEb1nY) — Backprop and optimization basics.

### Book repository and lists

- [AI Engineering — GitHub (Huyen)](https://github.com/chiphuyen/aie-book) — Memory calc walkthroughs, finetuning resources.
- [Llama Police — finetuning frameworks list](https://github.com/mlabonne/llm-course) — Community-maintained pointers (verify freshness).

### [Dataset Engineering](/ai-engineering/docs/dataset-engineering)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 8: Dataset Engineering.

### Data-centric AI and competitions

- [DataPerf](https://dataperf.org/) — MLCommons (2023).
- [DataComp](https://www.datacomp.ai/) — Gadre et al. (2023); language-model scale Li et al. (2024).
- [dcbench](https://github.com/stanford-crfm/dcbench) — Eyuboglu & Karlaš (2022).

### Quality, coverage, and quantity

- [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) — Zhou et al. (2023).
- [Scaling Instruction-Finetuned Language Models (Flan)](https://arxiv.org/abs/2210.11416) — Chung et al. (2022).
- [The False Promise of Imitating Proprietary LLMs](https://arxiv.org/abs/2305.15717) — Gudibande et al. (2023).
- [Ossification in transfer learning](https://arxiv.org/abs/2102.09574) — Hernandez et al. (2021).
- [Llama 3 paper](https://arxiv.org/abs/2407.21783) — Dubey et al. (2024) — data mixes, synthesis, ChatML.
- [Nemotron-4 340B Technical Report](https://arxiv.org/abs/2406.11704) — NVIDIA (2024).

### Instruction and synthetic data

- [Self-Instruct](https://arxiv.org/abs/2212.10560) — Wang et al. (2022).
- [Alpaca](https://arxiv.org/abs/2303.16199) — Taori et al. (2023).
- [UltraChat](https://arxiv.org/abs/2305.14233) — Ding et al. (2023).
- [MetaMath](https://arxiv.org/abs/2309.12288) — Yu et al. (2023).
- [Cosmopedia](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia) — Allal et al. (2024).
- [StableToolBench](https://arxiv.org/abs/2407.08739) — Guo et al. (2024).
- [Discovering LM Behaviors with Model-Written Evaluations](https://arxiv.org/abs/2212.09251) — Perez et al. (2022).
- [The Curse of Recursion / model collapse](https://arxiv.org/abs/2305.17493) — Shumailov et al. (2023).
- [Is Model Collapse Inevitable?](https://arxiv.org/abs/2404.01413) — Gerstgrasser et al. (2024).

### Distillation and deduplication

- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) — Hinton et al. (2015).
- [DistilBERT](https://arxiv.org/abs/1910.01108) — Sanh et al. (2019).
- [Deduplicating Training Data](https://arxiv.org/abs/2107.06499) — Lee et al. (2021).
- [datasketch (MinHash)](https://github.com/ekzhu/datasketch) — Library for near-duplicate detection.

### Dataset hubs and search

- [Hugging Face Datasets](https://huggingface.co/datasets)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Data.gov](https://www.data.gov/)
- [OpenML](https://www.openml.org/)
- [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)

### Guides, courses, and tools

- [OpenAI — Fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning) — Data size experiments (SNLI).
- [Argilla — data labeling for LLMs](https://argilla.io/) — Human + AI annotation workflows.
- [Label Studio](https://labelstud.io/) — Annotation UI.
- [DeepLearning.AI — Data-centric AI](https://www.deeplearning.ai/courses/data-centric-ai/) — Andrew Ng.
- [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) — Huyen — weak supervision, augmentation (Ch. 4).
- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — Spanish workshop context.

### Related book repository

- [AI Engineering — GitHub (Huyen)](https://github.com/chiphuyen/aie-book) — Dataset resources, lazyNLP deduplication notes.

### [Inference Optimization](/ai-engineering/docs/inference-optimization)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 9: Inference Optimization.

### Roofline, metrics, and profiling

- [Roofline: An Insightful Visual Performance Model](https://people.eecs.berkeley.edu/~kubitron/cs252/handouts/papers/RooflineVyNoYellow.pdf) — Williams et al. (2009).
- [NVIDIA Nsight](https://developer.nvidia.com/nsight-systems) — Profiling and roofline charts.
- [Anyscale — LLM inference performance](https://www.anyscale.com/blog/llm-inference-performance) — Kadous et al. (2023); input vs output token latency.
- [LinkedIn — Generative AI deployment reflections](https://www.linkedin.com/blog/engineering/generative-ai) — Throughput vs TTFT trade-offs (2024).

### Prefill/decode and serving systems

- [DistServe: Disaggregating Prefill and Decoding](https://arxiv.org/abs/2401.09670) — Zhong et al. (2024).
- [Orca: Continuous Batching](https://www.usenix.org/conference/osdi22/presentation/yu) — Yu et al. (2022).
- [vLLM / PagedAttention](https://arxiv.org/abs/2309.06180) — Kwon et al. (2023).
- [Efficient Memory Management for LLM Serving](https://github.com/vllm-project/vllm) — vLLM project.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) — NVIDIA inference stack.
- [llama.cpp](https://github.com/ggerganov/llama.cpp) — Edge/local inference.

### Decoding acceleration

- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.10438) — Leviathan et al. (2022); Chen et al. (2023) Chinchilla draft model.
- [Inference with Reference](https://arxiv.org/abs/2304.04487) — Yang et al. (2023).
- [Medusa: Simple Framework for Accelerating LLM Generation](https://arxiv.org/abs/2401.10774) — Cai et al. (2024).
- [Lookahead Decoding](https://arxiv.org/abs/2402.02057) — Fu et al. (2024).

### Attention and KV cache

- [FlashAttention](https://arxiv.org/abs/2205.14135) — Dao et al. (2022).
- [FlashAttention-3](https://arxiv.org/abs/2407.08608) — Shah et al. (2024).
- [Efficiently Scaling Transformer Inference](https://arxiv.org/abs/2211.05102) — Pope et al. (2022) — KV cache at scale.
- [GQA: Grouped-Query Attention](https://arxiv.org/abs/2305.13245) — Ainslie et al. (2023).

### Hardware and utilization

- [PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311) — Chowdhery et al. (2022) — MFU.
- [ML Accelerator Survey](https://arxiv.org/abs/2303.04608) — Desislavov et al. (2023).
- [PyTorch — torch.compile Llama throughput blog](https://pytorch.org/blog/accelerating-generative-ai/) — (2023).
- [OpenAI Triton](https://github.com/triton-lang/triton) — Kernel language.

### API pricing, caching, and batch

- [OpenAI — Batch API](https://platform.openai.com/docs/guides/batch) — Cost/latency trade-off.
- [Google Gemini — Context caching](https://ai.google.dev/gemini-api/docs/caching) — Cached token pricing.
- [Anthropic — Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) — Cost and latency examples.
- [OpenAI — Prompt caching](https://platform.openai.com/docs/guides/prompt-caching) — Provider feature parity evolves—check current docs.

### Compilers and optimization frameworks

- [Apache TVM](https://tvm.apache.org/)
- [MLIR](https://mlir.llvm.org/)
- [torch.compile](https://pytorch.org/docs/stable/torch.compiler.html)
- [NVIDIA TensorRT](https://developer.nvidia.com/tensorrt)

### Courses and talks

- [Full Stack LLM Bootcamp — LLM serving (YouTube)](https://www.youtube.com/results?search_query=full+stack+llm+bootcamp+serving) — Berkeley/full-stack content on inference.
- [Meta — Llama inference at scale (talks, 2024)](https://engineering.fb.com/) — Prefill/decode fleet ratios (search Meta engineering blog).
- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — Spanish workshop (deployment context).

### Book repository

- [AI Engineering — GitHub (Huyen)](https://github.com/chiphuyen/aie-book) — Inference resources and kernel tutorials.

### [AI Engineering Architecture and User Feedback](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 10: AI Engineering Architecture and User Feedback.

### Architecture, gateways, and guardrails

- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) — NVIDIA.
- [Purple Llama](https://ai.meta.com/purple-llama/) — Meta safety stack.
- [Portkey AI Gateway](https://github.com/Portkey-AI/gateway)
- [MLflow AI Gateway](https://mlflow.org/docs/latest/llms/gateway/index.html)
- [OpenAI Moderation API](https://platform.openai.com/docs/guides/moderation)
- [Perspective API](https://perspectiveapi.com/) — Toxicity scoring.

### Orchestration and observability

- [LangChain](https://www.langchain.com/)
- [LlamaIndex](https://www.llamaindex.ai/)
- [LangSmith](https://www.langchain.com/langsmith) — Tracing (Figure 10-11 in book).
- [OpenTelemetry](https://opentelemetry.io/) — Traces/metrics/logs standard.
- [Weights & Biases — LLM monitoring](https://wandb.ai/site/solutions/llmops)
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) — LLM eval and tracing.

### Caching and routing

- [GPTCache](https://github.com/zilliztech/GPTCache) — Semantic cache community patterns.
- [Semantic cache discussion — LangChain](https://python.langchain.com/docs/how_to/semantic_cache/)

### User feedback and preference learning

- [FITS: Feedback for Interactive Talk & Search](https://arxiv.org/abs/2204.10091) — Xu et al. (2022).
- [Learning from Natural Language Feedback](https://arxiv.org/abs/2306.08899) — Yuan et al. (2023).
- [RL from Human Feedback survey](https://arxiv.org/abs/2203.02155) — Ouyang et al. (2022) — InstructGPT context.
- [Towards Understanding Sycophancy in LLMs](https://arxiv.org/abs/2310.13581) — Sharma et al. (2023).
- [Aligning AI with shared human values (RLHF risks)](https://www.alignmentforum.org/) — Stray (2023) and related discourse.

### Model drift and versioning

- [How Is ChatGPT’s Behavior Changing?](https://arxiv.org/abs/2307.09009) — Chen et al. (2023) — GPT-3.5/4 version drift.
- [Voiceflow — model version performance](https://www.voiceflow.com/blog) — GPT-3.5-turbo version notes (cited in book).

### Product design and HCI

- [Apple Human Interface Guidelines — Ratings and reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews)
- [Midjourney documentation](https://docs.midtrourney.com/) — Implicit feedback workflow.
- [GitHub Copilot — inline suggestions](https://docs.github.com/en/copilot)

### Monitoring (general)

- [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) — Huyen (2022) — Monitoring chapter; blog draft on distribution shift.
- [Datadog / Splunk / Dynatrace](https://www.datadoghq.com/) — Enterprise observability (market context in book).

### Courses and workshops

- [Full Stack LLM Bootcamp — production LLM apps](https://fullstackdeeplearning.com/llm-bootcamp/) — Architecture patterns.
- [DeepLearning.AI — Building Systems with the ChatGPT API](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/) — Pipelines and guardrails intro.
- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — Spanish deployment context.

### Book repository

- [AI Engineering — GitHub (Huyen)](https://github.com/chiphuyen/aie-book) — Observability resources, architecture examples.

### [Glossary](/ai-engineering/docs/glossary)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.

- [Book GitHub — aie-book](https://github.com/chiphuyen/aie-book)

### [Epilogue](/ai-engineering/docs/epilogue)

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Epilogue, p. 495.

- [AI Engineering — book repository](https://github.com/chiphuyen/aie-book)
- [Chip Huyen — communication](https://huyenchip.com/communication)

---

## Related

- [Book map](/ai-engineering/docs/book-map) — reading order and prerequisites
- [Overview](/ai-engineering/docs) — chapter index
- [Glossary](/ai-engineering/docs/glossary) — key terms
