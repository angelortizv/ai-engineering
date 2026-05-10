---
title: "Introduction to Building AI Applications with Foundation Models"
description: "Chapter 1 summary — AI Engineering (Huyen, 2025)"
order: 1
---

## Introduction

Chip Huyen sums up the post-2020 era in one word: **scale**. The models behind ChatGPT, Gemini, or Midjourney consume a meaningful share of global electricity, and the public internet corpus available for training is a finite resource.

Two main consequences:

1. **More capability and more applications**: more people and teams use AI for productivity, economic value, and quality of life.
2. **Model as a service**: training LLMs requires data, compute, and talent concentrated in a few organizations; those models are exposed via APIs, lowering the barrier for anyone who wants to build without funding a model from scratch.

Thus, demand for AI applications rises while the barrier to building them falls. **AI engineering**—building applications on top of readily available models—becomes one of the fastest-growing engineering disciplines.

Building on ML is not new (recommendations, fraud, churn). Many production principles still apply; what is new is **large-scale foundation models** and how they change possibilities and challenges.

---

## From language models to foundation models

### Language and tokens

A **language model** encodes statistics about one or more languages: how likely a word or token is in a context (e.g. “My favorite color is ___” → “blue” rather than “car”). The basic unit is the **token** (character, word, or subword); tokenization and vocabulary size are defined by the model developer.

There are two main families:

- **Masked** (e.g. BERT): predicts missing tokens using context before and after; useful for non-generative tasks or tasks that need bidirectional context.
- **Autoregressive**: predicts the next token using only prior tokens; today this is the standard for **text generation**. In the book, unless stated otherwise, “language model” means autoregressive.

Outputs are **open-ended**: with a finite vocabulary you can still compose infinitely many outputs—hence **generative AI**. Intuitively, the model is a **completion machine**: prompt plus probabilistic continuation (not guaranteed).

Many tasks (translation, summarization, code, “is this spam?” classification) can be framed as completion with the right prompt. Completion is not the same as a user-aligned conversation; that requires **post-training** or other techniques.

### Self-supervision and scaling

The key to scaling LMs is **self-supervision**: the text itself provides labels (the next token) and context, without massive manual labeling. This contrasts with classical **supervision** (e.g. ImageNet), which is expensive and slow at scale.

**LLMs** are measured mainly by **parameter count**; “large” is relative (GPT-1 at ~117M once seemed large; the bar rises over time). Larger models generally need **more training data** to use their capacity (the goal is not to match a small model on the same data, but to maximize performance).

### From LLMs to foundation models

Humans do not live on text alone; LMs therefore extend to **multimodality** (images, video, etc.). A model that conditions generation on several modalities fits **foundation model** better than “LLM only”: *foundation* signals that others build on top.

A generative multimodal model is also called a **large multimodal model (LMM)**. A historical example is **CLIP**—not generative, but image–text aligned *embeddings*; a backbone for many later generative systems.

Foundation models mark the shift from **task-specific** models to **general-purpose** ones: the same model can be steered across many tasks, then **adapted** to a domain (brand voice, format, etc.).

### Adaptation

Three common techniques the book develops later:

- **Prompt engineering**: instructions and examples without changing weights.
- **RAG**: external context (e.g. a knowledge base) to complete more accurately.
- **Finetuning**: continued training of the model for the use case.

Adapting a strong model is usually far cheaper and faster than training from scratch; smaller **specialized** models can still win on speed and cost. The **buy vs build** decision for models remains central.

---

## Why “AI engineering” (and not just MLOps)

Three factors driving the discipline:

1. **General-purpose capabilities**: more tasks become possible, including some once seen as impossible; AI can automate much work that involves written communication, assisted creativity, code, and more.
2. **Investment**: hits like ChatGPT spurred VC and corporate spending; per–use-case costs have dropped by orders of magnitude over short periods (examples cited in the book).
3. **Low barrier**: **model-as-a-service** APIs plus the ability to prototype with little code—or even in natural language.

The term **AI engineering** is preferred over folding everything into “ML engineering” because working with foundation models **differs** from traditional ML; “Ops” suffixes emphasize operations, but here the focus is **adapting** base models. Informal surveys among practitioners favored “AI engineering.”

---

## Use cases (patterns)

Taxonomies vary (AWS: customer experience, employee productivity, process optimization; O’Reilly: programming, analysis, support, marketing, etc.). Huyen groups **eight categories** (consumer and enterprise): **coding**, **image and video**, **writing**, **education**, **conversational bots**, **information aggregation**, **data organization**, and **workflow automation**.

Cross-cutting ideas from the chapter:

- Highly “exposed” occupations (per cited studies) include interpreting, writing, web design; low exposure includes very physical trades.
- Enterprises often ship **internal** applications first (lower risk) before **external** ones; many apps are still effectively **closed-ended** tasks (e.g. classification) even when the base model is open-ended.
- **Coding**: top cited use case in surveys; Copilot as a commercial milestone; McKinsey suggests large gains on documentation and moderate gains on generation/refactoring, less so on highly complex tasks.
- **Creativity** (image/video): fits the probabilistic nature of generative models.
- **Writing**: high volume, tolerance for errors; studies (e.g. MIT on ChatGPT) show time and quality gains; abuse exists too (content farms, SEO spam).
- **Education**: personalized tutoring, quizzes, simulated debates; tension with traditional homework-help businesses.
- **Bots**: support, product copilots, companionship; also voice and 3D/NPC characters.
- **Aggregation**: summaries, talk-to-your-docs, research; in enterprises, breaking meeting/email silos.
- **Data organization**: labeling, PDF extraction, multimodal search; IDP as a growing market.
- **Automation and agents**: tasks needing **external tools** and planning → **agents** (a central topic later in the book).

---

## Planning AI applications

Before building “because we can”:

### Use case evaluation

Typical motivations (from highest perceived urgency): **business continuity** against AI-enabled competitors, **value capture** (margin, productivity), or **exploration** so as not to fall behind (with opportunity cost). **Build vs buy** and whether work must be **in-house** depend on strategic risk.

### Role of AI and humans

Useful dimensions (inspired by Apple documentation cited in the book): **critical vs complementary**, **reactive vs proactive** (different latency and quality expectations), **dynamic vs static** (continuous personalization vs a shared model updated on releases).

**Human-in-the-loop**: from suggestions for human agents to full automation. Microsoft’s **Crawl–Walk–Run**: humans required first, then AI with internals, then more automation with external users.

### Defensibility (moats)

APIs and base models level the playing field; typical advantages are **technology**, **data**, and **distribution**. The base model can **subsume** layers that used to be standalone products (e.g. new provider capabilities). Usage data and “data flywheel” narratives recur at startups.

### Expectations and metrics

Define success with **business metrics** and usefulness thresholds: **quality**, **latency** (TTFT, TPOT, total latency), **cost per inference**, plus user satisfaction and feedback.

### Milestones and the “last mile”

Evaluate **off-the-shelf** models before committing resources. The jump from demo to product is long: **0→60** can be fast; **60→100** is costly (hallucinations, polish). Maintenance means ongoing **cost/benefit** tradeoffs (API pricing, vendors disappearing, regulation, IP, hardware).

---

## The AI engineering stack

### Three layers

1. **Application development**: prompts, context, rigorous evaluation, interfaces.
2. **Model development**: training/finetuning frameworks, **dataset engineering**, inference optimization.
3. **Infrastructure**: serving, data, compute, monitoring.

GitHub data (high-star AI repos) shows that after ChatGPT/Stable Diffusion, **applications** and **application tooling** exploded; infrastructure grows less because needs (serving, monitoring) **still resemble** classical ML.

Principles that **remain**: align business and ML metrics, systematic experimentation (now: models, prompts, retrieval, sampling…), production feedback loops, efficiency.

### AI engineering versus traditional ML

Three major differences:

1. **Less train-from-scratch, more adapt** others’ models.
2. **Larger models**: more pressure on inference cost/latency and on engineers skilled with GPUs/clusters.
3. **Open-ended outputs**: **evaluation** becomes a harder problem.

**Adaptation without weight updates**: prompt engineering. **Adaptation with weight updates**: finetuning (more data and complexity, but needed for some quality jumps or new tasks).

### Model development (middle layer)

- **Pre-training**: from random weights; dominates compute for typical LLMs.
- **Finetuning / post-training**: continue from pretrained weights; “post-training” often means the model vendor’s phase, “finetuning” often means the application developer’s phase (informal overlap).
- **Dataset engineering**: foundation models lean on **unstructured** data; annotating open-ended outputs is harder; more deduplication, tokenization, context retrieval, and quality control.
- **Inference**: autoregressive models generate token by token; accumulated latency conflicts with typical web expectations (~100 ms).

### Application development (top layer)

With shared models, differentiation comes from the **product**: **evaluation**, **prompt engineering and context construction**, **user interface** (web, extensions, Slack chat, plugins…). Conversational UIs make natural-language feedback easier but **harder to extract** and analyze.

### AI engineering and full-stack

Interface weight pulls AI engineering toward **full-stack** development: more JavaScript/Node APIs, faster demo–feedback loops. The workflow can invert classical ML: **product first**, specialized data/models only if the product earns them.

---

## Chapter wrap-up

The chapter explains **why AI engineering exists** as a discipline and **what it takes** to build on foundation models: LM → LLM → multimodal/general models, self-supervision, usage patterns, planning before coding, a three-layer stack, and differences from traditional ML—with emphasis on **adaptation** and **evaluation**.

The community contributes energy and tools at a pace that is hard to match; the book aims to provide a **framework** for navigating that space, starting in Chapter 2 with the foundational piece: **foundation models** themselves.

---

## Closing notes

What sticks with me from this chapter is less jargon than a **shift in default**: I’m not training models from scratch—I’m **adapting** general-purpose ones that someone else scaled. **Self-supervision** is the technical reason that became possible: text (and later multimodal data) carries its own supervision signal, so models could grow without a labeling bottleneck. Practically, adaptation stacks **prompting**, **RAG** when facts live outside the weights, and **finetuning** only when that tier is justified. That stacks cleanly with an **inverted workflow**: start from the **product** and user loop, then deepen data and model investment once something proves worth scaling—the opposite of the classical “data → model → product” habit. The breadth of **use cases** (coding, writing, bots, aggregation, etc.) also reminds me that organizations often **ship internal tools first** to learn safely before exposing customers to open-ended failure modes.

Day to day, **my role** tilts toward the **application layer**—interfaces, context construction, and iteration—not toward designing transformers. The hardest part isn’t wiring an API; it’s **evaluation**: generative outputs don’t reduce to a single accuracy score, so “good enough” has to be defined and guarded continuously. That forces explicit **tradeoffs** among performance, latency, and cost across providers and adaptation strategies. **Planning** rounds out the craft: clarify *why* the project exists (risk, opportunity, or exploration), stage automation with something like **crawl–walk–run**, and set **metrics and usefulness thresholds** early—because a weekend demo is nothing like the long slog from “works in the demo” to “survives production.”

**Reference:** Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.
