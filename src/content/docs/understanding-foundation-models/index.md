---
title: "Understanding Foundation Models"
description: "Chapter 2 summary — AI Engineering (Huyen, 2025)"
order: 2
---

## Understanding Foundation Models

> While you don't need to know how to develop a model to use it, a high-level understanding will help you decide what model to use and how to adapt it to your needs.
>
> — Huyen (2025, p. 49)

This chapter stays **above the training recipe** you will never fully see inside a proprietary API. It still explains the levers that shape behavior in production: **where the data came from**, **how the stack was modeled and scaled**, **how post-training turned raw completion into a product**, and **how sampling turns logits into experience**—including inconsistency and hallucination.

---

## Data

### Data defines capability

A foundation model **inherits** the biases, strengths, and blind spots of its training mixture. If a language or domain barely appears in pre-training, the model will not magically compensate at inference time—latency, cost, and quality for “tail” languages often track that scarcity.

> An AI model is only as good as the data it was trained on. If there's no Vietnamese in the training data, the model won't be able to translate from English into Vietnamese.
>
> — Huyen (2025, p. 50)

**Web-scale corpora** (e.g. Common Crawl and filtered subsets like C4) are attractive because they are available, not because they are clean: clickbait, propaganda, toxicity, and untrustworthy sources show up in analyses of top domains. Heuristics (e.g. Reddit link filtering for GPT-2) improve yield but do not erase skew.

### Language distribution (illustrative)

English dominates many crawls; long-tail languages can be **orders of magnitude** rarer—driving disparities in quality, evaluation coverage, and the economics of serving multilingual products. Representative shares from Common Crawl–style analyses (see Table 2-1 in the book; figures rounded):

| Language | Approx. share |
| --- | ---: |
| English | 45.8% |
| Russian | 6.0% |
| German | 5.9% |
| Chinese | 4.9% |
| Punjabi | under 0.01% |

**Engineering implication:** before committing to a model, ask what **data recipe** it was trained on (disclosed or inferred) and whether your users’ languages and domains are **in-distribution**. Chapter 8 goes deeper on curation and synthetic data when you must close the gap yourself.

---

## Modeling

### Architecture: transformer dominance

Transformers won language modeling because **self-attention** lets representations mix across the sequence while **parallelizing** token processing far more aggressively than classic recurrent stacks—at the cost of **quadratic** attention cost in naive formulations as context grows. That cost motivates a rich line of work on **efficient attention**, **long-context tricks**, and **alternative sequence layers**.

The book surveys the competitive landscape beyond “transformer-only,” including **Mamba** (selective state-space / linear-time sequence modeling) and hybrids like **Jamba** (interleaved transformer and Mamba blocks)—useful context when vendors advertise new architectures.

> With transformers, the input tokens can be processed in parallel, significantly speeding up input processing.
>
> — Huyen (2025, p. 60) (chapter discussion of transformers vs sequential models)

### Size and scaling laws

Model quality is not “parameters alone”—it couples **parameters**, **tokens seen in training**, and **FLOPs**. For a **fixed compute budget**, the **Chinchilla** scaling law (DeepMind, 2022) suggests a much more **data-heavy** optimum than earlier-era practice: roughly **~20 training tokens per parameter** for compute-optimal pre-training (e.g. a 3B model on the order of ~60B tokens), scaling parameters and tokens together when you double budget.

> Given a fixed amount of FLOPs, what model size and dataset size would give the best performance? A model that can achieve the best performance given a fixed compute budget is **compute-optimal**.
>
> — Huyen (2025, p. 72) (paraphrasing the Chinchilla / compute-optimal framing in the chapter)

**Product caveat:** Chinchilla optimizes **training loss under a pre-training budget**. Real teams also optimize **inference cost**, **latency**, and **usability**—the book notes that some widely adopted families deliberately sit “sub-Chinchilla-optimal” on raw loss to ship smaller, cheaper-to-serve models.

---

## Post-training

Pre-training produces a **completion machine** trained on internet-scale text—powerful but not aligned to chat, refusals, tool formats, or your brand voice. **Post-training** is the bridge from “raw capability” to “product.”

A common **three-stage mental model** (see Figures 2-10 and 2-11 in the book):

1. **Pre-training** — self-supervised learning on broad data (the “untamed” base behavior).
2. **Supervised finetuning (SFT)** — high-quality `(prompt, response)` demonstrations so the model **follows instructions** and acts conversational rather than only completing prose.
3. **Preference finetuning** — e.g. **RLHF**-style pipelines or alternatives such as **DPO**, using human (or model-assisted) preference signals and often a **reward model** to push outputs toward **helpful, honest, harmless** regions.

The **Shoggoth with a smiley face** meme captures the intuition: pre-training is the alien bulk; SFT and preference steps sculpt something **customer-appropriate**.

> You can think of post-training as unlocking the capabilities that the pre-trained model already has but are hard for users to access via prompting alone.
>
> — Huyen (2025, pp. 78–79)

Alignment is **not solved**: preferences are plural, reward models mis-specify objectives, and some safety interventions trade off factuality or capability—engineering judgment still matters.

---

## Sampling

Each decode step produces a **distribution over the full vocabulary**; **sampling** is the rule for turning those logits into the next token. That single mechanism explains both **delightful variation** and **maddening inconsistency**.

### Temperature and related knobs

**Temperature** rescales logits before softmax: lower values **sharpen** the distribution (more deterministic, “boring,” reliable); higher values **flatten** it, boosting rare tokens and **creativity** at the risk of coherence.

> Intuitively, a higher temperature reduces the probabilities of common tokens, and as a result, increases the probabilities of rarer tokens. This enables models to create more creative responses.
>
> — Huyen (2025, p. 91)

In practice, `temperature = 0` (argmax / greedy-style decoding) is common when you need repeatability—APIs simulate it without literally dividing by zero. **Top-*p*** (nucleus), **top-*k***, and custom samplers further shape tail behavior; the right dial depends on the task (creative writing vs strict JSON).

### Test-time compute

**Test-time compute** means spending **extra inference** to improve quality: sample **many** completions, then **select** with a verifier, reward model, heuristic (e.g. shortest answer), or consistency vote (**self-consistency** / majority for math). The book gives striking examples: verifiers can dwarf raw parameter scaling in some settings, and “best-of-*N*” curves saturate (e.g. gains taper after hundreds of samples in cited experiments). This is the explicit **compute ↔ quality** knob at deployment time.

### Structured outputs

For **agents**, **tool calling**, and **machine-readable** pipelines, you often need **constrained** generation: JSON modes, grammar-guided decoders, regex constraints, or frameworks (e.g. Guidance-style constraints—see the book’s discussion). Note: “valid JSON” ≠ “semantically correct JSON.” Mitigations stack: better prompts, constrained decoding, finetuning, and evaluation.

### Hallucinations vs sampling noise

> If inconsistency arises from randomness in the sampling process, the cause of hallucination is more nuanced… A model can output something that is believed to have never been seen before in the training data.
>
> — Huyen (2025, p. 107)

So: **turn down temperature** to tame variance, but **hallucination** also ties to training objectives, knowledge boundaries, self-delusion / snowballing on long generations, and missing context—addressed later with **RAG**, **evaluation**, and **product guardrails**, not sampling alone.

---

## Key takeaways

1. **Data dictates destiny** — capabilities and biases are inherited from the training mixture; read the **data recipe** before choosing a provider or open-weight checkpoint.
2. **Respect scaling laws** — for pre-training under a FLOPs budget, **Chinchilla-style** token–parameter balance is the canonical guide; still validate **serve-time** economics separately.
3. **Alignment creates usability** — **SFT** plus **preference tuning** turn pre-trained completion into something users can steer; it is also where many safety and format behaviors are baked in.
4. **Master the sampling dial** — temperature / top-*p* / top-*k* shape creativity vs determinism; **test-time compute** and **structured decoding** are first-class engineering tools beside prompting.
5. **Probabilistic by construction** — plan for inconsistency and hallucination with **evaluation**, **retrieval**, and **architecture**—not vibes alone.

---

## Chapter wrap-up

Chapter 2 connects **training data → architecture & scale → post-training → decoding** to what you actually see in an API. The next chapters build the **evaluation discipline** you need before you trust those behaviors in production.

---

## Discussion questions

- For your primary language/locale, does the model’s **training mix** match user traffic?
- Which failure mode do you see more: **sampling noise** or **structural overconfidence**?
- When would you raise **test-time compute** (best-of-N) vs. change the base model?
- How do you validate **structured JSON**—syntax only or semantic tests?
- What post-training artifact (SFT vs. preference) best explains a bad behavior you’ve seen?

---

## Related

- **Back:** [Introduction to Building AI Applications](/ai-engineering/docs/introduction-to-building-ai-applications-with-foundation-models) — why AI engineering exists.
- **Next:** [Evaluation Methodology](/ai-engineering/docs/evaluation-methodology) — metrics for what you just learned models can do.
- **Sampling:** [Prompt Engineering](/ai-engineering/docs/prompt-engineering) — temperature, top-p, and structured outputs in practice.
- **Adaptation:** [Finetuning](/ai-engineering/docs/finetuning) — when weights must change, not just prompts.
- **Book repository:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- **Glossary:** [Glossary](/ai-engineering/docs/glossary) — key terms from the book and these notes.

## Closing notes

I read this chapter as a reminder that a “model pick” is really a **bundle of decisions**: the **crawl mix** behind multilingual fairness, the **Chinchilla-ish** (or not) compute trade that set its knowledge cutoff and loss, the **SFT/RLHF** layer that made it *chatty*, and the **sampler** I turn on at runtime. None of those are visible in a leaderboard cell, but they explain why two models with similar scores behave differently on *my* prompts.

What I’m taking into practice: (1) **audit data fit** first—especially for non-English and niche domains; (2) treat **temperature**, **top-*p***, and **best-of-*N*** as real product knobs with cost curves, not afterthoughts; (3) assume **JSON mode** is only syntax unless I verify semantics with tests; (4) keep the **hallucination** mental model split—sampling noise vs structural overconfidence—so I don’t “fix” with the wrong tool. The book’s through-line is that none of this replaces **evaluation**; it motivates why Chapter 3 exists.

---

## References

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.

### Additional materials to review

- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar’s visual walkthrough of attention and the transformer block.
- [Intro to large language models](https://www.youtube.com/watch?v=zjkBMFhNj_g) — Andrej Karpathy (2023): a compact deep dive on how LLMs are trained and used; strong complement on **transformers**, **prompting**, and the **human-feedback** alignment story. (If you have a specific lecture titled *“LLM Lecture: A Deep Dive into Transformers, Prompts, and Human Feedback”*, add it alongside—naming varies across courses.)
