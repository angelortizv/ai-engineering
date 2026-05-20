---
title: "Overview"
description: "Chapter-by-chapter notes from Chip Huyen's AI Engineering (O'Reilly, 2025)—foundation models through production."
order: 0
---

## What this site is

This documentation collects **chapter-oriented summaries and notes** based on:

**Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.**

The goal is a single place to revisit ideas from the book in reading order: what foundation models are, how to evaluate and adapt them, and how to ship reliable applications.

### The book (read this first)

| | |
| --- | --- |
| **Author** | [Chip Huyen](https://huyenchip.com/) — writer and ML systems engineer; taught ML systems at Stanford; author of *Designing Machine Learning Systems* (2022). |
| **Get the book** | [O’Reilly — *AI Engineering*](https://www.oreilly.com/library/view/ai-engineering/9781098166304/) (print, ebook, or subscription). |
| **Companion repo** | [github.com/chiphuyen/aie-book](https://github.com/chiphuyen/aie-book) — extra materials from the publisher. |
| **After chapter 10** | [What comes next →](/ai-engineering/docs/epilogue) — practice paths and how this site fits in. |

### Why I’m building this compendium

I’m **getting started in AI engineering**. This book is how I’m grounding myself: it connects language models and multimodal systems to the practical stack—prompting, retrieval, finetuning, data, inference, and architecture—without skipping **evaluation** or **user feedback**. Writing these notes helps me learn and keeps the material searchable alongside experiments I run in code.

> **Important note:** This site is only a **reading guide** and a **short summary** of the book—not a substitute for it. Figures, proofs, nuance, and the full argument live in Huyen’s text. **Nothing here replaces reading the book itself**; use these pages to orient yourself, revisit ideas, and link experiments back to the source.

---

## Navigation

| Resource | Description |
| --- | --- |
| [**Book map**](/ai-engineering/docs/book-map) | Chapter → themes → tools → prerequisites and suggested reading paths. |
| [**Bibliography**](/ai-engineering/docs/bibliography) | All chapter `## References` sections in one page. |
| [**Glossary**](/ai-engineering/docs/glossary) | Searchable definitions (filter box on the glossary page). |

---

## Chapters (English)

Each link opens the notes page for that chapter (same order as in the book).

| Ch. | Topic | Page |
| --- | --- | --- |
| 1 | [**Introduction to Building AI Applications with Foundation Models**](/ai-engineering/docs/introduction-to-building-ai-applications-with-foundation-models) — Scale, model-as-a-service, from language models to foundation models, self-supervision, common use cases, planning AI products, and the three-layer AI engineering stack versus classic ML engineering. | [→](/ai-engineering/docs/introduction-to-building-ai-applications-with-foundation-models) |
| 2 | [**Understanding Foundation Models**](/ai-engineering/docs/understanding-foundation-models) — How large models behave under the hood: probabilities, sampling, context windows, and what “knowing” means for an LLM. | [→](/ai-engineering/docs/understanding-foundation-models) |
| 3 | [**Evaluation Methodology**](/ai-engineering/docs/evaluation-methodology) — How to design evaluation that matches real risks and business goals, not only leaderboard scores. | [→](/ai-engineering/docs/evaluation-methodology) |
| 4 | [**Evaluating Modern AI Systems**](/ai-engineering/docs/evaluating-modern-ai-systems) — Holistic evaluation of systems (models + prompts + tools + retrieval), benchmarks, and failure modes in production-like settings. | [→](/ai-engineering/docs/evaluating-modern-ai-systems) |
| 5 | [**Prompt Engineering**](/ai-engineering/docs/prompt-engineering) — Getting desired behavior from instructions and context alone (no weight updates): patterns, structure, and iteration. | [→](/ai-engineering/docs/prompt-engineering) |
| 6 | [**RAG and Agents**](/ai-engineering/docs/rag-and-agents) — Retrieval-augmented generation, tools, planning, and agent-style loops that connect models to data and the outside world. | [→](/ai-engineering/docs/rag-and-agents) |
| 7 | [**Finetuning**](/ai-engineering/docs/finetuning) — Adapting model weights for domain, tone, format, or efficiency when prompting and RAG are not enough. | [→](/ai-engineering/docs/finetuning) |
| 8 | [**Dataset Engineering**](/ai-engineering/docs/dataset-engineering) — Curating and generating data for adaptation: quality, deduplication, safety, and alignment with evaluation. | [→](/ai-engineering/docs/dataset-engineering) |
| 9 | [**Inference Optimization**](/ai-engineering/docs/inference-optimization) — Making inference faster and cheaper: batching, quantization, caching, hardware, and cost–latency tradeoffs. | [→](/ai-engineering/docs/inference-optimization) |
| 10 | [**AI Engineering Architecture and User Feedback**](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback) — Production architecture, observability, and closing the loop with users so the system improves safely over time. | [→](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback) |
| — | [**Glossary**](/ai-engineering/docs/glossary) — TTFT, PEFT, RAG, goodput, degenerate feedback loop, and related terms. | [→](/ai-engineering/docs/glossary) |
| — | [**Epilogue**](/ai-engineering/docs/epilogue) — Closing notes (~p. 495) and [book repository](https://github.com/chiphuyen/aie-book). | [→](/ai-engineering/docs/epilogue) |
