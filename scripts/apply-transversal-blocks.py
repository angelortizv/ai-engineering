#!/usr/bin/env python3
"""One-off helper: inject transversal blocks into chapter index.md files."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "/ai-engineering/docs"

CHAPTERS = {
    "introduction-to-building-ai-applications-with-foundation-models": {
        "num": 1,
        "title_en": "Introduction",
        "pages": "1–48",
        "objectives": False,
        "refs": True,
        "related_en": [
            ("Next", "understanding-foundation-models", "how LMs are trained, sampled, and steered"),
            ("Evaluation", "evaluation-methodology", "why open-ended outputs need new metrics"),
            ("Systems", "evaluating-modern-ai-systems", "operational eval before you scale"),
            ("Adaptation", "prompt-engineering", "first lever after choosing a model"),
        ],
        "discussion_en": [
            "Where does your team sit on **build vs. buy** for the base model—and what would change that in 12 months?",
            "For one internal use case, map **critical vs. complementary**, **reactive vs. proactive**, and **dynamic vs. static**. What latency/quality bar follows?",
            "What **business metric** would you refuse to ship without, beyond “the demo looks good”?",
            "Which layer of the **three-layer stack** is the bottleneck today?",
            "What **moat** survives if the API provider ships your feature tomorrow?",
        ],
    },
    "understanding-foundation-models": {
        "num": 2,
        "pages": "49–112",
        "objectives": False,
        "refs": False,
        "related_en": [
            ("Back", "introduction-to-building-ai-applications-with-foundation-models", "why AI engineering exists"),
            ("Next", "evaluation-methodology", "metrics for what you just learned models can do"),
            ("Sampling", "prompt-engineering", "temperature, top-p, and structured outputs in practice"),
            ("Adaptation", "finetuning", "when weights must change, not just prompts"),
        ],
        "discussion_en": [
            "For your primary language/locale, does the model’s **training mix** match user traffic?",
            "Which failure mode do you see more: **sampling noise** or **structural overconfidence**?",
            "When would you raise **test-time compute** (best-of-N) vs. change the base model?",
            "How do you validate **structured JSON**—syntax only or semantic tests?",
            "What post-training artifact (SFT vs. preference) best explains a bad behavior you’ve seen?",
        ],
    },
    "evaluation-methodology": {
        "num": 3,
        "pages": "113–158",
        "objectives": True,
        "refs": True,
        "related_en": [
            ("Back", "understanding-foundation-models", "what you are measuring"),
            ("Next", "evaluating-modern-ai-systems", "pipelines and model selection"),
            ("Prompts", "prompt-engineering", "defensive eval for injection and leakage"),
            ("Production", "ai-engineering-architecture-and-user-feedback", "feedback as ongoing eval"),
        ],
        "discussion_en": [
            "Name three **failure modes** for your app that no public leaderboard captures.",
            "When is **perplexity** useful for you—and when is it misleading?",
            "Design a **functional correctness** check for one generative task you own.",
            "What biases will you test for if you adopt an **AI judge**?",
            "What would convince you a **2% Arena win** is worth a 2× price increase?",
        ],
        "objectives_en": [
            "Explain why **open-ended** outputs break classic accuracy metrics.",
            "Choose among **perplexity**, exact checks, similarity, and **AI-as-judge** for a given task.",
            "List failure modes and biases of **comparative** leaderboards.",
            "Describe when **functional correctness** is the right primary metric.",
            "Connect evaluation design to **risk** (legal, safety, reputation).",
        ],
    },
    "evaluating-modern-ai-systems": {
        "num": 4,
        "pages": "159–210",
        "objectives": True,
        "refs": True,
        "related_en": [
            ("Back", "evaluation-methodology", "methods this chapter operationalizes"),
            ("Next", "prompt-engineering", "first adaptation layer after you pick a model"),
            ("Data", "dataset-engineering", "building slices that match production"),
            ("Agents", "rag-and-agents", "evaluating retrieval and tool loops"),
        ],
        "discussion_en": [
            "Draft four **evaluation pillars** (domain, generation, instruction, cost/latency) for your product.",
            "What is on your **private eval set** that MMLU will never see?",
            "Where could **contaminated** public benchmarks mis-rank models for you?",
            "Write a one-paragraph **evaluation guideline** like the LinkedIn “helpfulness” example.",
            "What **usefulness threshold** gates automation vs. human review?",
        ],
        "objectives_en": [
            "Apply the **four evaluation criteria** to a real use case.",
            "Outline a **model selection workflow** (filter → public → custom → production).",
            "Argue **build vs. buy** with privacy, latency, and capability tradeoffs.",
            "Design a three-step **evaluation pipeline** with human spot-checks.",
            "Map benchmark scores to **business thresholds**, not leaderboard rank alone.",
        ],
    },
    "prompt-engineering": {
        "num": 5,
        "pages": "211–252",
        "objectives": False,
        "refs": False,
        "related_en": [
            ("Back", "evaluating-modern-ai-systems", "know what “good” means before iterating prompts"),
            ("Next", "rag-and-agents", "context beyond the prompt window"),
            ("Security", "evaluation-methodology", "judge and metric choices for safety tests"),
            ("Architecture", "ai-engineering-architecture-and-user-feedback", "guardrails around prompts"),
        ],
        "discussion_en": [
            "Which tasks stay **zero-shot** vs. need **few-shot** examples—and why?",
            "How do you **version** prompts and tie them to eval runs?",
            "What is your policy for **untrusted text** inside context (indirect injection)?",
            "When do you reach for **structured outputs** vs. free text + parsing?",
            "What would make you stop prompt tuning and try **RAG** or **finetuning**?",
        ],
    },
    "rag-and-agents": {
        "num": 6,
        "pages": "253–306",
        "objectives": False,
        "refs": False,
        "related_en": [
            ("Back", "prompt-engineering", "instructions and context design"),
            ("Next", "finetuning", "when retrieval and tools are not enough"),
            ("Data", "dataset-engineering", "corpora and chunk quality for retrieval"),
            ("Eval", "evaluating-modern-ai-systems", "end-to-end and component eval"),
        ],
        "discussion_en": [
            "Where does **hybrid retrieval** beat dense-only for your domain?",
            "What is the failure mode of your **chunking** strategy today?",
            "Sketch a **ReAct** loop for one workflow—what is human-verified?",
            "Which **agent failures** (planning vs. tools) dominate your logs?",
            "When is RAG “enough” without an agent?",
        ],
    },
    "finetuning": {
        "num": 7,
        "pages": "307–362",
        "objectives": True,
        "refs": False,
        "related_en": [
            ("Back", "rag-and-agents", "prompt-based adaptation first"),
            ("Next", "dataset-engineering", "data quality for SFT and preferences"),
            ("Inference", "inference-optimization", "serving cost after you adapt weights"),
            ("Eval", "evaluating-modern-ai-systems", "prove finetuning beat prompts/RAG"),
        ],
        "discussion_en": [
            "List **reasons not to finetune** for your current product.",
            "Estimate **trainable params** and memory with the chapter’s napkin math.",
            "When is **form** (tone/format) finetuning enough without new facts?",
            "Would **LoRA vs. full** change your compliance story?",
            "How will you detect **catastrophic forgetting** on general tasks?",
        ],
        "objectives_en": [
            "Decide **when to finetune** vs. prompt/RAG using the book’s criteria.",
            "Estimate **memory** for inference vs. full finetune vs. **PEFT**.",
            "Contrast **PTQ** and **QAT** for deployment.",
            "Explain **model merging** use cases and risks.",
            "Plan hyperparameter and data tactics that avoid **overfitting** small sets.",
        ],
    },
    "dataset-engineering": {
        "num": 8,
        "pages": "363–404",
        "objectives": True,
        "refs": False,
        "related_en": [
            ("Back", "finetuning", "what the data is for"),
            ("Next", "inference-optimization", "serving the model you trained"),
            ("Eval", "evaluating-modern-ai-systems", "slices and rubrics for data quality"),
            ("Feedback", "ai-engineering-architecture-and-user-feedback", "logs → training data flywheel"),
        ],
        "discussion_en": [
            "Define **quality** dimensions that matter for your annotation guidelines.",
            "Which **coverage** axes (language, topic, length) are underrepresented?",
            "When is **synthetic data** worth the verification cost?",
            "What **dedup** rule would you apply before SFT?",
            "How does your mix differ across **pretrain / SFT / preference** phases?",
        ],
        "objectives_en": [
            "Apply **quality, coverage, quantity** to a finetuning dataset plan.",
            "Compare **human, synthetic, and distillation** sourcing.",
            "Interpret **domain mix** shifts across training phases (e.g. Llama 3).",
            "Design inspection, **dedup**, and filtering steps.",
            "State how you will **evaluate synthetic data** before training.",
        ],
    },
    "inference-optimization": {
        "num": 9,
        "pages": "405–448",
        "objectives": True,
        "refs": False,
        "related_en": [
            ("Back", "dataset-engineering", "models you will serve"),
            ("Next", "ai-engineering-architecture-and-user-feedback", "caches, gateways, production UX"),
            ("Models", "understanding-foundation-models", "autoregressive decode basics"),
            ("Finetuning", "finetuning", "memory footprint of adapted weights"),
        ],
        "discussion_en": [
            "Is your workload **prefill-** or **decode-heavy**? What does that imply for hardware?",
            "Which metric matters more to users: **TTFT** or **TPOT**?",
            "Would **speculative decoding** help if MFU is already high?",
            "When is **prompt caching** safe vs. a privacy bug?",
            "What is your **goodput** target per dollar?",
        ],
        "objectives_en": [
            "Classify bottlenecks as **compute-bound** vs. **bandwidth-bound**.",
            "Relate **TTFT, TPOT, throughput**, MFU/MBU to product SLAs.",
            "Explain **prefill vs. decode** and why fleets decouple them.",
            "Choose among **quantization, KV cache, batching, speculative decoding**.",
            "Negotiate provider features (**prompt cache**, routing) with eval data.",
        ],
    },
    "ai-engineering-architecture-and-user-feedback": {
        "num": 10,
        "pages": "449–494",
        "objectives": True,
        "refs": False,
        "related_en": [
            ("Back", "inference-optimization", "latency/cost under load"),
            ("Capstone", "introduction-to-building-ai-applications-with-foundation-models", "stack and planning from Chapter 1"),
            ("Feedback data", "dataset-engineering", "turning logs into training sets"),
            ("Epilogue", "epilogue", "closing perspective and book repo"),
        ],
        "discussion_en": [
            "Which **architecture step** (context, guardrails, router, cache, agents) is missing today?",
            "Where could **semantic caching** leak personalized answers?",
            "What **observability** signal would have caught your last incident?",
            "How do you avoid a **degenerate feedback loop**?",
            "What feedback do you collect without hurting UX?",
        ],
        "objectives_en": [
            "Walk through the **five-step progressive architecture** with tradeoffs.",
            "Place **guardrails** on input vs. output for your risk model.",
            "Explain **router vs. gateway** responsibilities.",
            "Design **feedback** capture that feeds the data flywheel safely.",
            "Connect monitoring to **new failure modes** of foundation models.",
        ],
    },
}

REFERENCES_EN = {
    1: """## References

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
""",
    3: """## References

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
""",
    4: """## References

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
""",
}

REFERENCES_ES = {
    1: """## Referencias

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
""",
    3: """## Referencias

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
""",
    4: """## Referencias

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
""",
}

SLUG_TITLES = {
    "introduction-to-building-ai-applications-with-foundation-models": {
        "en": "Introduction to Building AI Applications",
        "es": "Introducción a aplicaciones de IA",
    },
    "understanding-foundation-models": {"en": "Understanding Foundation Models", "es": "Entender modelos fundacionales"},
    "evaluation-methodology": {"en": "Evaluation Methodology", "es": "Metodología de evaluación"},
    "evaluating-modern-ai-systems": {"en": "Evaluating Modern AI Systems", "es": "Evaluar sistemas de IA modernos"},
    "prompt-engineering": {"en": "Prompt Engineering", "es": "Ingeniería de prompts"},
    "rag-and-agents": {"en": "RAG and Agents", "es": "RAG y agentes"},
    "finetuning": {"en": "Finetuning", "es": "Finetuning"},
    "dataset-engineering": {"en": "Dataset Engineering", "es": "Ingeniería de datos"},
    "inference-optimization": {"en": "Inference Optimization", "es": "Optimización de inferencia"},
    "ai-engineering-architecture-and-user-feedback": {
        "en": "AI Engineering Architecture and User Feedback",
        "es": "Arquitectura de IA y feedback de usuario",
    },
    "glossary": {"en": "Glossary", "es": "Glosario"},
    "epilogue": {"en": "Epilogue", "es": "Epílogo"},
}

def book_note(num: int, pages: str, lang: str) -> str:
    if lang == "es":
        return (
            f"> **O'Reilly (1.ª ed.)** — Huyen (2025), **Capítulo {num}**, "
            f"aprox. **pp. {pages}**. Contrasta figuras y tablas con tu PDF.\n\n"
        )
    return (
        f"> **O'Reilly (1st ed.)** — Huyen (2025), **Chapter {num}**, "
        f"approximately **pp. {pages}**. Cross-check figures and tables in your PDF.\n\n"
    )


def objectives_block(items: list[str], lang: str) -> str:
    title = "## Objetivos de aprendizaje" if lang == "es" else "## Learning objectives"
    bullets = "\n".join(f"- {x}" for x in items)
    intro = (
        "Al terminar este capítulo deberías poder:"
        if lang == "es"
        else "After this chapter, you should be able to:"
    )
    return f"{title}\n\n{intro}\n\n{bullets}\n\n---\n\n"


def discussion_block(items: list[str], lang: str) -> str:
    title = "## Preguntas de discusión" if lang == "es" else "## Discussion questions"
    bullets = "\n".join(f"- {x}" for x in items)
    return f"\n---\n\n{title}\n\n{bullets}\n"


def related_block(links: list[tuple], lang: str, locale_prefix: str) -> str:
    title = "## Relacionado" if lang == "es" else "## Related"
    lines = [title, ""]
    for label, slug, desc in links:
        href = f"{BASE}{locale_prefix}/{slug}"
        name = SLUG_TITLES.get(slug, {}).get(lang, slug)
        lines.append(f"- **{label}:** [{name}]({href}) — {desc}.")
    book_label = "Repositorio del libro" if lang == "es" else "Book repository"
    glossary_label = "Glosario" if lang == "es" else "Glossary"
    lines.append(f"- **{book_label}:** [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).")
    lines.append(f"- **{glossary_label}:** [{BASE}{locale_prefix}/glossary]({BASE}{locale_prefix}/glossary).")
    return "\n".join(lines) + "\n\n"


def process_file(path: Path, slug: str, lang: str) -> None:
    cfg = CHAPTERS[slug]
    text = path.read_text(encoding="utf-8")
    if "## Discussion questions" in text or "## Preguntas de discusión" in text:
        return

    locale_prefix = "/es" if lang == "es" else ""
    num = cfg["num"]
    pages = cfg["pages"]

    # Book note after ## Introduction / Introducción
    intro_pat = r"(## (Introduction|Introducción)\n\n)"
    note = book_note(num, pages, lang)
    if note.strip() not in text:
        text = re.sub(intro_pat, r"\1" + note, text, count=1)

    # Learning objectives after book note block (before first --- following intro)
    if cfg.get("objectives"):
        key = "objectives_es" if lang == "es" and "objectives_es" in cfg else "objectives_en"
        obj = objectives_block(cfg[key], lang)
        if "## Learning objectives" not in text and "## Objetivos de aprendizaje" not in text:
            # insert after book note, before first ---
            text = re.sub(
                r"(> \*\*O'Reilly.*?\n\n)(---\n\n)",
                r"\1" + obj + r"\2",
                text,
                count=1,
                flags=re.DOTALL,
            )

    # Discussion before closing notes (after chapter wrap-up / cierre)
    disc_key = "discussion_es" if lang == "es" and "discussion_es" in cfg else "discussion_en"
    disc = discussion_block(cfg[disc_key], lang)
    closing = "## Notas finales" if lang == "es" else "## Closing notes"
    if f"\n---\n\n{closing}" in text:
        text = text.replace(f"\n---\n\n{closing}", disc + f"\n---\n\n{closing}", 1)

    # Related before closing
    rel_links = cfg.get("related_es", cfg["related_en"]) if lang == "es" else cfg["related_en"]
    if lang == "es":
        rel_links = [
            ("Anterior" if l == "Back" else "Siguiente" if l == "Next" else l, s, d)
            for l, s, d in rel_links
        ]
    rel = related_block(rel_links, lang, locale_prefix)
    if f"\n---\n\n{closing}" in text:
        text = text.replace(f"\n---\n\n{closing}", f"\n---\n\n{rel}{closing}", 1)

    # References for ch 1,3,4
    if cfg.get("refs"):
        ref_marker = "## Referencias" if lang == "es" else "## References"
        if ref_marker not in text:
            ref_body = REFERENCES_ES.get(num) if lang == "es" else REFERENCES_EN.get(num)
            if ref_body:
                # remove inline **Reference:** at end of closing notes
                text = re.sub(
                    r"\n\*\*Reference:\*\* Huyen.*?\n",
                    "\n",
                    text,
                )
                text = re.sub(
                    r"\n\*\*Referencia:\*\* Huyen.*?\n",
                    "\n",
                    text,
                )
                text = text.rstrip() + "\n\n---\n\n" + ref_body

    path.write_text(text, encoding="utf-8")
    print(f"updated {path}")


def main() -> None:
    for lang, sub in [("en", "docs"), ("es", "docs-es")]:
        for slug in CHAPTERS:
            p = ROOT / "src/content" / sub / slug / "index.md"
            if p.exists():
                process_file(p, slug, lang)


if __name__ == "__main__":
    main()
