---
title: "Book map"
description: "Reading order, themes, tools, and prerequisites for each chapter (Huyen, 2025)."
order: 0
sidebar:
  label: "Book map"
---

## Introduction

Use this page to plan a path through the [chapter notes](/ai-engineering/docs). It mirrors the book’s arc: **what each chapter covers**, **which tools appear**, and **what to read first**.

---

## Chapter map

| Ch. | Chapter | Core themes | Tools & frameworks (in notes) | Read first |
| --- | --- | --- | --- | --- |
| 1 | [Introduction](/ai-engineering/docs/introduction-to-building-ai-applications-with-foundation-models) | LM → foundation models, self-supervision, use cases, crawl–walk–run, three-layer stack | Provider APIs, planning frameworks | — |
| 2 | [Understanding foundation models](/ai-engineering/docs/understanding-foundation-models) | Architecture, Chinchilla scaling, post-training (SFT, preferences), sampling, hallucination types | Hugging Face ecosystem (context), OpenAI/Anthropic APIs | 1 |
| 3 | [Evaluation methodology](/ai-engineering/docs/evaluation-methodology) | PPL, functional correctness, AI judges, Arena-style ranking, contamination | LangChain eval patterns, Ragas/MLflow (refs), MT-Bench | 2 |
| 4 | [Evaluating modern AI systems](/ai-engineering/docs/evaluating-modern-ai-systems) | Four pillars, EDD, build vs buy, private eval, production monitoring link | MMLU, HELM, LMSYS Arena, HumanEval, moderation APIs | 3 |
| 5 | [Prompt engineering](/ai-engineering/docs/prompt-engineering) | Instructions, CoT, defensive prompting, OWASP LLM | Instructor, JSON mode, DSPy, NeMo/Purple Llama (refs) | 2, 3 |
| 6 | [RAG and agents](/ai-engineering/docs/rag-and-agents) | Retrieve-then-generate, hybrid search, ReAct, tools, MCP/A2A | Elasticsearch/BM25, vector DBs, LangChain/LlamaIndex | 5 |
| 7 | [Finetuning](/ai-engineering/docs/finetuning) | PEFT/LoRA/QLoRA, memory math, RAG vs finetune | Hugging Face PEFT, DeepSpeed, bitsandbytes | 2, 5, 6 |
| 8 | [Dataset engineering](/ai-engineering/docs/dataset-engineering) | Quality, Llama 3 mix, synthetic data, flywheel | Faker, Self-Instruct patterns, verification pipelines | 4, 7 |
| 9 | [Inference optimization](/ai-engineering/docs/inference-optimization) | Prefill/decode, KV cache, quantization, serving | vLLM, TensorRT-LLM, llama.cpp, torch.compile | 2, 7 |
| 10 | [Architecture & feedback](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback) | Progressive architecture, guardrails, observability, feedback loops | Gateways (Portkey, etc.), OpenTelemetry, LangSmith | 4, 6, 9 |
| — | [Glossary](/ai-engineering/docs/glossary) | Terms used across chapters | — | any |
| — | [Bibliography](/ai-engineering/docs/bibliography) | Aggregated chapter references | — | any |
| — | [Epilogue](/ai-engineering/docs/epilogue) | Closing notes, book repo | [aie-book](https://github.com/chiphuyen/aie-book) | 10 |

---

## Suggested reading paths

```mermaid
flowchart LR
  C1[Ch 1–2 Models] --> C3[Ch 3–4 Eval]
  C3 --> C5[Ch 5 Prompts]
  C5 --> C6[Ch 6 RAG/Agents]
  C6 --> C7[Ch 7–8 Adapt weights]
  C7 --> C9[Ch 9 Inference]
  C9 --> C10[Ch 10 Production]
```

| Goal | Path |
| --- | --- |
| **Ship a RAG product** | 1 → 2 → 3 → 4 → 5 → 6 → 10 (skim 9 for cost) |
| **Finetune for format/tone** | 1 → 2 → 3 → 5 → 7 → 8 → 9 |
| **Evaluation lead** | 1 → 2 → 3 → 4 → 10 |
| **Platform / serving** | 2 → 9 → 10 (+ 4 for SLOs) |

---

## Related

- [Overview](/ai-engineering/docs) — short chapter blurbs
- [Bibliography](/ai-engineering/docs/bibliography) — all `## References` in one place
- [Glossary](/ai-engineering/docs/glossary) — searchable terms

---

## References

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.

- [AI Engineering — GitHub (aie-book)](https://github.com/chiphuyen/aie-book)
