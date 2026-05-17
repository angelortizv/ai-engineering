---
title: "Evaluation Methodology"
description: "Chapter 3 summary — AI Engineering (Huyen, 2025)"
order: 3
---

## Introduction

The more AI is deployed, the more room there is for **catastrophic failure**. Real cases already made that concrete: a passenger relied on **Air Canada’s chatbot** for bereavement fares and got wrong policy information—the airline had to honor the mistake after a lawsuit. **Lawyers** submitted briefs with **hallucinated case citations** and faced sanctions. A user was encouraged toward self-harm by a chatbot. Without quality control on outputs, risk can outweigh benefit for many applications.

As teams rush to adopt AI, many discover that **evaluation** is often the biggest hurdle—and for some apps it can consume **most of the development effort** (Greg Brockman: “evals are surprisingly often all you need”). This chapter covers **methods** for evaluating open-ended models: how they work and where they break. Chapter 4 turns to **using** those methods to pick models and build an evaluation pipeline for your application.

Evaluation is never isolated: it exists to **mitigate risks** and **surface opportunities**. You must know **where the system fails** and design measurement around those failure modes—sometimes that means **redesigning the system** for visibility. Without that, no metric stack makes the product robust.

---

## Challenges of evaluating foundation models

Evaluating ML was always hard; foundation models made it harder.

**Harder tasks need harder evaluation.** A first-grader’s wrong math answer is obvious; a PhD-level solution is not. Coherent but wrong summaries require reading the source. Terence Tao compared early reasoning models to a “mediocre graduate student”—raising the question of who will evaluate models that exceed most experts.

**Open-ended outputs break ground-truth benchmarks.** Classification has a finite label set; generative tasks admit countless valid answers, so you cannot maintain an exhaustive list of correct outputs.

**Black-box models** limit what you can inspect (architecture, training data, training process). You often judge **only by outputs**, while public benchmarks **saturate quickly** (GLUE → SuperGLUE, NaturalInstructions → SuperNaturalInstructions, MMLU → MMLU-Pro).

**Scope expanded:** task-specific models are judged on one task; general-purpose models must be assessed on known tasks **and** on newly discovered capabilities—including some beyond typical human skill.

The ecosystem responded: papers on LLM evaluation grew sharply in 2023; GitHub hosts dozens of evaluation repos. Yet **investment and tooling still lag** modeling and orchestration—many teams still **eyeball** results or reuse a small ad hoc prompt set. This chapter argues for a **systematic** approach.

---

## The evaluation imperative

High-stakes failures show evaluation is a **business and safety** requirement, not an academic exercise. “Figuring out evaluation” can dominate the calendar.

Not everything reduces to a single number. Hard-to-quantify dimensions include:

- **Nuanced user satisfaction** — technically correct but wrong tone.
- **Factual accuracy in open domains** — no single ground-truth database (e.g. historical analysis).
- **Harm avoidance** — subtle bias or harmful advice.
- **Long-term consequences** — advice that shapes decisions over weeks.

The book focuses on **automatic** evaluation (exact and subjective), while **human evaluation** remains necessary for many apps—and for sanity checks.

---

## Foundational metrics: language modeling

Foundation models often embed a **language model**; LM metrics correlate with downstream performance (though post-training weakens that link).

### Entropy

**Entropy** measures information in the **data**, not the model: how surprising the next token is on average. A language with two position tokens (“upper” / “lower”) has lower entropy (1 bit) than four tokens (“upper-left”, …) at 2 bits. Lower entropy → more predictable language.

### Cross-entropy

**Cross-entropy** measures how hard it is for the **model** to predict the training distribution: `H(P,Q) = H(P) + D_KL(P||Q)`. Training minimizes cross-entropy; a perfect fit matches data entropy. **BPC** and **BPB** normalize across tokenizers for fair comparison. Cross-entropy also relates to **compression efficiency**.

### Perplexity (PPL)

**Perplexity** is `2^H` (or `e^H` with nats in PyTorch/TensorFlow)—intuitively, the **effective number of choices** for the next token. PPL of 10 ≈ choosing among 10 equally likely tokens.

**Interpretation rules:**

- More **structured** text (e.g. HTML) → lower expected PPL.
- Larger **vocabulary** → higher PPL.
- Longer **context** → lower PPL.

**Engineering uses:**

- **Proxy for capability** — lower PPL often correlates with stronger models (when reported).
- **Data contamination** — suspiciously low PPL on a benchmark suggests it was in training data.
- **Abnormal inputs** — gibberish or odd text → very high PPL.
- **Deduplication** — add training samples only if new data has high PPL.

**Critical caveat:** **SFT** and **RLHF** often **increase** PPL—the model optimizes for helpful task completion, not raw next-token prediction. **Quantization** can shift PPL unexpectedly too.

Commercial APIs do not always expose **logprobs**, which are required to compute PPL on arbitrary text.

---

## Exact evaluation metrics

Distinguish **exact** evaluation (unambiguous judgment) from **subjective** evaluation (depends on grader or judge). This section targets **open-ended** generation; close-ended tasks (classification, intent) are well understood elsewhere.

### Functional correctness

The gold standard when automatable: **did the system do what it was supposed to?**

- **Code:** run generated code (unit tests, interpreters). Benchmarks like **HumanEval**, **MBPP**, **Spider**, **BIRD-SQL**, **WikiSQL** use **pass@k**—fraction of problems solved if any of *k* samples passes all test cases.
- **Games / optimization:** score in Tetris, energy saved by a scheduler, etc.

When only part of a workflow is AI-driven, judging the **partial** output can be harder than judging the end outcome (chess: win/lose vs. rating a single move).

### Similarity against reference data

When correctness cannot be executed, compare outputs to **reference** (ground truth) pairs `(input, reference responses)`.

**Ways to compare:**

1. Human or AI judge (“same meaning?”).
2. **Exact match** — works for short factual answers; fragile on formatting; “contains 1929” can accept wrong dates.
3. **Lexical similarity** — overlap of tokens or **n-grams** (BLEU, ROUGE, METEOR++, TER, CIDEr). Penalizes valid paraphrases; needs exhaustive references; **OpenAI found BLEU similar for correct and incorrect HumanEval solutions**.
4. **Semantic similarity** — **embeddings** + cosine similarity (BERTScore, MoverScore). More robust to paraphrase; quality depends on the embedding model and compute cost.

These similarity tools also support retrieval, ranking, clustering, anomaly detection, and deduplication (revisited later in the book).

**Embeddings (sketch):** vectors capturing meaning; specialized models (BERT, CLIP, Sentence Transformers, API embedders). Good embeddings place similar texts closer in space. **CLIP** aligns image and text in a joint space for cross-modal search.

---

## The subjective judge: AI as a judge

Using AI to grade AI (**AI as a judge** / **LLM as a judge**) became practical around **GPT-3 (2020)** and widespread in production by 2023–2024 (e.g. LangChain: ~58% of evals on their platform via AI judges).

### Why use it

- Fast, cheap vs. humans; works **without references** in production.
- Flexible criteria: correctness, toxicity, hallucination, role consistency, image trustworthiness, etc.
- Can **explain** decisions (useful for audits).
- Studies report strong correlation with humans on some benchmarks (e.g. GPT-4 vs. humans on MT-Bench; AlpacaEval vs. Chatbot Arena).

### How to use it

Three common patterns:

1. **Pointwise** — score one answer (e.g. 1–5) given the question.
2. **Reference-based** — True/False or score vs. a reference answer.
3. **Pairwise** — pick A or B; feeds preference data for alignment and comparative ranking.

A judge is a **system** (model + prompt + sampling). Prompts should specify **task**, **criteria**, and **scoring** (classification often beats raw numbers; discrete 1–5 beats wide continuous scales). **Few-shot examples** in the prompt improve consistency (at higher cost).

Built-in criteria vary by tool (Azure: groundedness, relevance…; Ragas: faithfulness…; LangChain: harmfulness, helpfulness…)—**scores are not comparable across tools**.

### Limitations and biases

- **Inconsistency** — same judge, same input, different runs or prompt tweaks.
- **Criteria ambiguity** — “faithfulness” differs across MLflow, Ragas, LlamaIndex (1–5 vs. 0/1 vs. YES/NO).
- **Drift** — judge prompt or model changes break month-over-month trends. **Do not trust a judge if you cannot see model and prompt.**
- **Cost and latency** — judging every response can double API spend; multiple criteria multiply calls; production guardrails add latency.
- **Biases:** **self-bias** (model favors its own outputs), **position bias** (first answer favored; opposite of human recency bias), **verbosity bias** (longer answers win even when wrong). Mitigate with order swapping, specialized judges, or weaker models for spot-checks.

**Which model judges?** Stronger judges correlate better with humans but cost more; **weaker judges** or **specialized** models (reward models, reference-based judges like BLEURT/Prometheus, **preference models** like PandaLM/JudgeLM) can be cheaper and task-specific. **Self-critique** helps sanity checks and revision loops.

AI judges should **supplement** exact metrics and human evaluation—not replace them.

---

## The competitive arena: ranking with comparative evaluation

Often the question is not “What is Model A’s score?” but **“Is Model A better than Model B for us?”**

### Pointwise vs. comparative

- **Pointwise:** each model scored independently (e.g. MMLU accuracy)—like judging skaters on technical and artistic marks separately.
- **Comparative:** side-by-side preference—which performance humans find easier for subjective quality (creativity, helpfulness).

**Chatbot Arena (LMSYS):** anonymous pairwise responses, user votes, then model names revealed. Thousands of **matches** feed rating algorithms (**Elo**, **Bradley–Terry**, **TrueSkill**). Arena moved from Elo to Bradley–Terry partly because Elo was sensitive to match order. Ratings assume: higher rank → should win >50% of future head-to-heads.

**Not the same as A/B testing** — comparative shows multiple outputs at once.

**Caution:** many questions need **correctness**, not preference (“cell phone radiation and brain tumors?”). Preference voting fails when users lack expertise—works when AI assists tasks users already know how to do.

### Engineering challenges

1. **Scalability** — *N* models → *N(N−1)/2* pairs; transitivity (A>B, B>C ⇒ A>C) may not hold for human preference or heterogeneous prompts/evaluators. New models must be matched against many others; **private models** need internal arenas or paid private leaderboards.

2. **Standardization** — crowdsourcing captures diverse prompts but weak **quality control**: no fact-checking, toxic preferences, polluted data (“hi”/“hello” overrepresented, brainteasers repeated). Rankings may not reflect **RAG** with your documents. Mitigations: hard-prompt filtering, trusted evaluators (Scale), or in-product comparisons (noisy if users guess).

3. **“So what?”** — 51% win rate does not state **magnitude** of improvement or absolute quality (both bad vs. both good). Hard to map win rate to business metrics (e.g. % tickets resolved) or **cost–benefit** if Model B costs 2×.

### Why it still matters

Captures **human preference**, resists benchmark saturation, harder to game than training on test sets. Complements exact benchmarks and A/B tests—not a replacement.

---

## Synthesis: building a robust pipeline

No single metric suffices. A practical stack **layers** methods by priority:

**Example — text-to-SQL for a sales database** (accurate SQL, efficient queries, trusted by non-technical users):

| Stage | Role | Methods |
|-------|------|---------|
| **1. Core functionality** | Non-negotiable gate | **Functional correctness** — does the SQL run and return the right result? |
| **2. Scalable quality** | Breadth at lower cost | **AI judges** (and semantic checks where references exist) |
| **3. Gold-standard sanity check** | Final confidence | **Human evaluation** on critical or ambiguous cases |

The same pattern generalizes: **exact / executable checks first**, automated subjective signals second, humans where stakes or ambiguity demand it. Add **language-model metrics** (PPL) for model selection, contamination checks, and data hygiene; add **comparative** evaluation when the business question is relative preference among candidates.

Pair **comparative ranking** with **absolute** thresholds (functional pass rate, latency, cost) before shipping.

---

## Chapter wrap-up

Chapter 3 maps the **evaluation landscape** for foundation models: why failure modes are serious, why open-ended outputs resist classic benchmarks, **LM metrics** (entropy, cross-entropy, perplexity, BPC/BPB), **exact** paths (functional correctness, lexical and semantic similarity), **AI judges** (promise, pitfalls, biases, specialized judges), and **comparative ranking** (Arena-style preference, rating algorithms, scalability and interpretation limits).

Language metrics and hand-designed similarity are mature; **AI-as-judge** and **comparative evaluation** scaled with foundation models. Reliable pipelines **combine** them; Chapter 4 shows how to operationalize that for model choice and application eval.

---

## Closing notes

What I take from this chapter is that evaluation is where AI engineering stops being a demo and becomes **engineering**. The Air Canada and lawyer examples are reminders that wrong outputs have **legal and reputational** cost—not just a bad UX score. That pushes me to name failure modes up front (hallucinated facts, policy errors, harmful advice) instead of optimizing a leaderboard that does not match our users or data.

On **metrics**, I mentally sort tools into layers. **Perplexity** and friends are useful for comparing base LMs and spotting contamination, but I will not treat low PPL after instruction tuning as “worse.” For product tasks, **functional correctness** wins whenever I can run the output (SQL, code, APIs). **Semantic similarity** beats BLEU/ROUGE when references exist but paraphrase is valid; **AI judges** fill gaps at scale, with eyes open to verbosity and position bias—and only with a frozen judge spec I can audit.

For **model selection**, comparative leaderboards answer “A vs. B?” not “good enough?” A slim win against a weak baseline or a 2× price bump needs **absolute** gates and business metrics. Building eval as a **pipeline** (execute → automate judge → human spot-check) matches how I would ship something like text-to-SQL: if the query does not run correctly, nothing else matters.

**Reference:** Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 3: Evaluation Methodology.
