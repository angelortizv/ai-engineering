# AI Engineering — field notes

> *A chapter-by-chapter compendium in progress, built around [Chip Huyen](https://huyenchip.com/)'s book.*

```
  eval ──► adapt ──► ship
    ▲         │         │
    └─────────┴─────────┘   (the loop the book keeps you honest about)
```

**[Read the site →](https://angelortizv.github.io/ai-engineering/)** · [Repository](https://github.com/angelortizv/ai-engineering) · [Book on O'Reilly](https://www.oreilly.com/library/view/ai-engineering/9781098166304/)

---

## What this is (and what it isn't)

This repository powers a **static documentation site**: **chapter-oriented summaries and notes** based on:

**Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O'Reilly Media.**

The goal matches the [site overview](https://angelortizv.github.io/ai-engineering/docs): one place to revisit the book **in reading order** — foundation models, evaluation, adaptation (prompts, RAG, finetuning, data), inference, and production architecture — and tie those ideas back to experiments in code.

| Yes | No |
| --- | --- |
| Reading guide and mental map | A substitute for the book |
| Glossary, aggregated bibliography, suggested paths | Huyen's figures, proofs, and full nuance |
| Bilingual notes (EN / ES) for review | Official course or publisher materials |

I'm **getting started in AI engineering**; this book is how I'm grounding myself. It connects LLMs (and multimodal systems) to the practical stack without skipping **evaluation** or **user feedback**. Writing here is how I make what I read stick.

---

## The book route (10 rungs)

Each chapter has its own notes page. Order follows the book:

| | Chapter | In one line |
| ---: | --- | --- |
| 1 | [Introduction to Building AI Applications with Foundation Models](https://angelortizv.github.io/ai-engineering/docs/introduction-to-building-ai-applications-with-foundation-models) | Scale, model-as-a-service, use cases, planning, three-layer stack |
| 2 | [Understanding Foundation Models](https://angelortizv.github.io/ai-engineering/docs/understanding-foundation-models) | Probabilities, sampling, context window, what "knowing" means for an LLM |
| 3 | [Evaluation Methodology](https://angelortizv.github.io/ai-engineering/docs/evaluation-methodology) | Match evaluation to risks and business goals, not only leaderboards |
| 4 | [Evaluating Modern AI Systems](https://angelortizv.github.io/ai-engineering/docs/evaluating-modern-ai-systems) | Model + prompts + tools + retrieval, in production-like settings |
| 5 | [Prompt Engineering](https://angelortizv.github.io/ai-engineering/docs/prompt-engineering) | Desired behavior from instructions and context alone (no weight updates) |
| 6 | [RAG and Agents](https://angelortizv.github.io/ai-engineering/docs/rag-and-agents) | Retrieval, tools, planning, agent-style loops |
| 7 | [Finetuning](https://angelortizv.github.io/ai-engineering/docs/finetuning) | Adapt weights when prompting and RAG are not enough |
| 8 | [Dataset Engineering](https://angelortizv.github.io/ai-engineering/docs/dataset-engineering) | Quality, deduplication, synthetic data, alignment with evaluation |
| 9 | [Inference Optimization](https://angelortizv.github.io/ai-engineering/docs/inference-optimization) | Latency, cost, quantization, caching, batching |
| 10 | [AI Engineering Architecture and User Feedback](https://angelortizv.github.io/ai-engineering/docs/ai-engineering-architecture-and-user-feedback) | Observability, guardrails, closing the loop with users |

**Satellites:** [Book map](https://angelortizv.github.io/ai-engineering/docs/book-map) · [Glossary](https://angelortizv.github.io/ai-engineering/docs/glossary) · [Bibliography](https://angelortizv.github.io/ai-engineering/docs/bibliography) · [Epilogue](https://angelortizv.github.io/ai-engineering/docs/epilogue) (after ch. 10)

Spanish version: `/docs/es/` prefix — e.g. [Panorama](https://angelortizv.github.io/ai-engineering/docs/es).

---

## What the site adds (beyond Markdown)

- **Book map** — themes, tools cited, prerequisites, and reading paths (RAG, finetune, cost, etc.).
- **Study mode** — per-chapter quizzes (`/docs/.../study` and `/docs/es/.../study`).
- **Search** — [Pagefind](https://pagefind.app/) indexes the site after build.
- **Diagrams** — `mermaid` blocks in the notes.
- **i18n** — content in `src/content/docs` (EN) and `src/content/docs-es` (ES).
- **RSS, sitemap, `llms.txt`** — for readers and agents that prefer plain text.

---

## Official book sources

| Resource | Link |
| --- | --- |
| Author | [Chip Huyen](https://huyenchip.com/) |
| Book | [O'Reilly — *AI Engineering*](https://www.oreilly.com/library/view/ai-engineering/9781098166304/) |
| Publisher repo | [github.com/chiphuyen/aie-book](https://github.com/chiphuyen/aie-book) |

---

## Local development

Requirements: **Node.js** (LTS) and **npm**.

```bash
git clone https://github.com/angelortizv/ai-engineering.git
cd ai-engineering
npm ci
npm run dev
```

Open the URL Vite prints (the project uses `base: '/ai-engineering'`; locally that's usually `http://localhost:5173/ai-engineering`).

| Command | Purpose |
| --- | --- |
| `npm run dev` | Development server |
| `npm run build` | Static build + Pagefind index |
| `npm run preview` | Preview the production build |
| `npm run check` | Type checking (Svelte) |
| `npm run lint` | ESLint + Prettier |

**GitHub Pages** deploys on every push to `main` (see `.github/workflows/deploy.yml`).

### Stack

SvelteKit · Svelte 5 · mdsvex · Tailwind CSS 4 · Shiki · Mermaid · adapter-static

Content lives under `src/content/docs*`; doc components in `src/lib/components/docs` and `src/lib/docs`.

---

## Quick layout

```
src/content/
  docs/          # English notes (chapters, glossary, map, bibliography)
  docs-es/       # same structure in Spanish
  study/         # quiz JSON (en / es)
src/routes/      # SvelteKit routes, incl. /docs/[lang]/...
static/          # assets and Pagefind output after build
```

---

## License and author

**MIT** — see [LICENSE](LICENSE).

**Angelo Ortiz Vega** — personal notes; the book's copyright belongs to its authors and publisher.

If this compendium helps you orient yourself while reading Huyen, great. If these pages are all you use, **buy or subscribe to the book** — that's where the full argument lives.

---

<p align="center">
  <sub>Built with curiosity, Markdown, and the conviction that evaluating before you scale is not optional.</sub>
</p>
