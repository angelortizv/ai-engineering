---
title: "Epilogue"
description: "Closing notes and what to do after AI Engineering (Huyen, 2025), ~p. 495."
order: 12
---

## Introduction

> **O'Reilly (1st ed.)** — Huyen (2025), **Epilogue**, **p. 495**.

After ten chapters on foundation models, evaluation, adaptation, data, inference, and architecture, the book closes with a short reflection—not new techniques, but perspective on learning and what comes next.

---

## From the book

Chip Huyen notes the scale of the work: on the order of **150,000 words**, **160 illustrations**, **250 footnotes**, and **975 reference links**. Finishing a technical book at that depth is a real investment of attention.

She frames **asking the right questions** as harder than finding correct answers—writing drove her to questions that led to useful discoveries, and she hopes readers leave with questions of their own.

The field already has many strong applications on foundation models, and systematic **AI engineering** (evaluation, adaptation, production architecture, feedback loops) should make the next wave easier to build. She invites readers to share problems and solutions via [X @chipro](https://x.com/chipro), [LinkedIn](https://www.linkedin.com/in/chiphuyen/), or [huyenchip.com](https://huyenchip.com/communication).

**More resources:** [github.com/chiphuyen/aie-book](https://github.com/chiphuyen/aie-book) — companion repository for the O’Reilly edition.

> AI engineering has a lot of challenges. Not all of them are fun, but all of them are opportunities for growth and impact.

---

## What comes after the book?

Finishing the last chapter is not the finish line—it is when **application** starts. The book is a map; you still have to walk the terrain with your own data, users, and constraints.

### 1. Build one end-to-end project

Pick a problem you actually have (internal tool, side project, coursework). A minimal loop that exercises the stack from Chapter 1:

1. **Define success** before coding ([Chapter 4](/ai-engineering/docs/evaluating-modern-ai-systems) — eval criteria, usefulness thresholds).
2. **Start with prompts** on an API model ([Chapter 5](/ai-engineering/docs/prompt-engineering)).
3. Add **RAG** only when facts are missing ([Chapter 6](/ai-engineering/docs/rag-and-agents)).
4. Add **guardrails + logging** before external users ([Chapter 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback)).

Ship something small, measure it, and iterate. A weekend demo that never meets a real user teaches less than a boring internal bot used twice a week.

### 2. Deepen by gap, not by re-reading cover to cover

| If you felt weak on… | Revisit | Then try |
| --- | --- | --- |
| Metrics and shipping bars | [Ch. 3–4](/ai-engineering/docs/evaluation-methodology) | Write a 20-example private eval set from real prompts |
| Model behavior and sampling | [Ch. 2](/ai-engineering/docs/understanding-foundation-models) | A/B temperature and top-p on the same prompt set |
| Cost and latency | [Ch. 9](/ai-engineering/docs/inference-optimization) | Profile TTFT/TPOT; try batch API or prompt caching |
| Data and finetuning | [Ch. 7–8](/ai-engineering/docs/finetuning) | One LoRA run on 500 verified examples—not millions of synthetic pairs |
| Production architecture | [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback) | Sketch your system using the five-step diagram; add only boxes you need |

Use the [book map](/ai-engineering/docs/book-map) to choose a reading path instead of rereading everything.

### 3. Read adjacent work (same author, different lens)

Huyen’s earlier **[Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/)** (2022) complements this book: data flywheels, monitoring, deployment patterns, and ML systems thinking that still apply when the “model” is an API. Many teams need **both** books—foundation models here, classical ML systems there.

### 4. Use the official companion repo

**[github.com/chiphuyen/aie-book](https://github.com/chiphuyen/aie-book)** — extra resources, updates, and community pointers tied to the O’Reilly edition. Check it when a chapter references code or when the field moves faster than your printed page.

### 5. Stay current without chasing every launch

Foundation models change monthly; **principles** from this book age more slowly:

- **Evaluation before scale** (Ch. 3–4)
- **Adapt in order:** prompt → RAG → finetune (Ch. 5–7)
- **Production is eval in motion** (Ch. 10)

Follow a small set of sources (release notes from your provider, one benchmark tracker, one practitioner you trust) instead of every new model announcement.

### 6. How this site fits in

These pages are a **companion**, not a replacement—see the [important note on the overview](/ai-engineering/docs). Use them to:

- Jump back to a chapter when you hit a failure mode in production.
- Search the [glossary](/ai-engineering/docs/glossary) when a metric or acronym slips.
- Pull links from the [bibliography](/ai-engineering/docs/bibliography) when you need the primary paper.

When you learn something the book did not spell out for your domain, consider contributing back (your own notes, issues on [aie-book](https://github.com/chiphuyen/aie-book), or sharing eval patterns with your team).

> **Closing prompt:** What is the one application you will build in the next 30 days—and what eval will tell you it is good enough to keep?

---

## Related

- [Overview](/ai-engineering/docs) — start here if you are reading in order
- [Book map](/ai-engineering/docs/book-map) — reading paths after the book
- [Glossary](/ai-engineering/docs/glossary) — terms used across chapters
- [AI Engineering Architecture and User Feedback](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback) — last technical chapter (pp. 449–494)
- [Book GitHub — aie-book](https://github.com/chiphuyen/aie-book)

---

## References

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Epilogue, p. 495.

- [AI Engineering — book repository](https://github.com/chiphuyen/aie-book)
- [Chip Huyen — communication](https://huyenchip.com/communication)
