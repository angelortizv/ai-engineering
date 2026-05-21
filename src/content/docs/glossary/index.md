---
title: "Glossary"
description: "Key terms from AI Engineering (Huyen, 2025) and these chapter notes."
order: 11
---

## Introduction

Quick definitions for terms used across the [chapter notes](/ai-engineering/docs). Wording follows *AI Engineering* (Huyen, 2025) unless noted.

Use the **search box** above the list to filter by term or definition (also indexed by site search via Pagefind).

---

## A–C

**AI-as-a-judge** — Using a foundation model to score or compare outputs against rubrics or references; scalable but biased (verbosity, position, self-preference).

**AI engineering** — Building applications on top of readily available foundation models (adaptation, evaluation, product), distinct from training frontier models from scratch.

**Arithmetic intensity** — FLOPs per byte moved; used in **roofline** analysis to see if a workload is compute- or bandwidth-bound.

**Autoregressive LM** — Predicts the next token from prior tokens only; standard for text generation (vs. masked LMs like BERT).

**Bits per byte (BPB)** — Cross-entropy in bits per byte of text; comparable across tokenizers unlike perplexity alone.

**Compute-bound** — Runtime dominated by FLOPs (e.g. LLM **prefill**).

**Context length** — Maximum tokens the model can attend to in one forward pass; drives cost and retrieval design.

**Cross-entropy** — Loss aligned with maximum likelihood for next-token prediction; related to perplexity.

---

## D–G

**Data flywheel** — Product usage → feedback/logs → better data/models → better product.

**Degenerate feedback loop** — Users only see model outputs shaped by past biased feedback, reinforcing errors (Chapter 10).

**Distillation** — Training a smaller model to mimic a larger one (logits or outputs).

**DSPy** — Framework for programmatic prompt optimization and pipelines.

**Embedding** — Dense vector representation of text (or other modality) for similarity search and judges.

**Foundation model** — Large, general-purpose model (often multimodal) others adapt via prompts, RAG, or finetuning.

**Functional correctness** — Evaluation by executing outputs (e.g. run generated SQL/code) rather than string match.

**Goodput** — Useful work per unit time/cost in serving (not raw tokens/s if many are wasted).

**Guardrails** — Input/output filters for safety, PII, policy, and quality before or after the model.

---

## H–M

**Hallucination** — Plausible but false or unsupported content; mitigated with RAG, eval, and guardrails—not sampling alone.

**Human-in-the-loop (HITL)** — Humans review, correct, or approve model outputs in the workflow.

**Instruction finetuning (SFT)** — Supervised training on (instruction, response) pairs after pretraining.

**KV cache** — Stored key/value activations during autoregressive decode to avoid recomputing prefixes.

**LoRA** — Low-rank adapters added to layers; **PEFT** with small trainable footprint.

**MFU (Model FLOP/s Utilization)** — Achieved FLOP/s vs. hardware peak; common in training and inference profiling.

**MBU** — Memory bandwidth utilization analog to MFU.

**Memory bandwidth-bound** — Runtime dominated by moving weights/activations (e.g. LLM **decode**).

**MMLU** — Multi-discipline multiple-choice benchmark; often used as a coarse filter, not a product contract.

**Model-as-a-service** — Using provider APIs instead of self-hosting full training stacks.

---

## N–R

**NIAH (needle in a haystack)** — Long-context test hiding a fact in noise to measure retrieval/recall.

**PEFT** — Parameter-efficient finetuning (LoRA, adapters, etc.) updating a small fraction of weights.

**Perplexity (PPL)** — exp(cross-entropy); lower is better for LMs; interpret carefully after chat tuning.

**Prefill** — Parallel processing of the input prompt to populate KV cache; usually **compute-bound**.

**Prompt caching** — Reusing KV for identical prompt prefixes across requests to cut latency/cost.

**Prompt injection** — Untrusted text in context that overrides intended instructions.

**QLoRA** — LoRA plus quantized base weights for training/serving with less memory.

**RAG** — Retrieval-augmented generation: fetch relevant context, then generate.

**ReAct** — Agent pattern: interleave **Thought → Action → Observation** until the task completes.

**RLHF / preference finetuning** — Train on human or model preferences over completions (DPO, etc.).

**Roofline model** — Plot of achievable FLOP/s vs. arithmetic intensity to locate bottlenecks.

---

## S–Z

**Self-supervision** — Labels derived from the data itself (next-token prediction), enabling web-scale pretraining.

**Speculative decoding** — Draft model proposes tokens; target model verifies in parallel for faster decode.

**Structured output** — JSON/schema-constrained generations (grammar, tools, APIs).

**TTFT (time to first token)** — Latency until the first generated token; dominated by prefill.

**TPOT / TBT** — Time per (output) token after the first; decode smoothness for streaming UX.

**Token** — Subword/word unit in the model vocabulary; drives billing and context limits.

**Tool use / function calling** — Model emits structured calls executed by your runtime (APIs, DB, code).

**Top-p / top-k** — Sampling filters truncating the tail of the next-token distribution.

**Transfer learning** — Starting from pretrained weights instead of random init (finetuning is one form).

---

## Related

- [Overview](/ai-engineering/docs) — chapter index
- [Interview bonus](/ai-engineering/docs/interview-bonus) — interview and system-design Q&A
- [Epilogue](/ai-engineering/docs/epilogue) — closing notes and [book repository](https://github.com/chiphuyen/aie-book)
- [Inference Optimization](/ai-engineering/docs/inference-optimization) — TTFT, TPOT, MFU, prefill/decode
- [Finetuning](/ai-engineering/docs/finetuning) — PEFT, LoRA, QLoRA, memory math

---

## References

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.

- [Book GitHub — aie-book](https://github.com/chiphuyen/aie-book)
