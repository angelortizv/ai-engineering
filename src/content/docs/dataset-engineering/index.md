---
title: "Dataset Engineering"
description: "Chapter 8 summary — AI Engineering (Huyen, 2025)"
order: 8
---

## Introduction

The best ML team with infinite compute cannot finetune a strong model without **good data**. **Dataset engineering** creates datasets that train the best model you can afford—within budget for annotation, compute, and compliance.

As fewer organizations train from scratch, **data differentiates** AI products. GPT-3 credited two people for data work; GPT-4 credited **eighty**—plus external annotators (OpenAI, 2020 vs 2023). Data ops moved from side tasks to dedicated roles: labelers, dataset creators, data quality engineers.

This chapter focuses on **post-training data** (most relevant to application developers), with lessons from pre-training when useful. Curation, synthesis, and processing are **iterative**, not linear.

> There are best practices you can follow and tools that you can use to automate parts of the process. However, data will mostly just be toil, tears, and sweat.
>
> — Huyen (2025, Ch. 8)

---

## A data-centric view of AI

| Lens | Focus |
|------|--------|
| **Model-centric** | Architectures, scale, training algorithms |
| **Data-centric** | Processing techniques, high-quality datasets, fewer resources |

Benchmarks shifted: same dataset → best model (ImageNet era) vs same model → best dataset (**DataComp**, **DataPerf**, **dcbench**). Andrew Ng’s data-centric competition (2021) and **DataComp** for CLIP (Gadre et al., 2023) exemplify this. Real progress usually needs **both** model and data investment.

---

## Data curation

Data can make models more capable and safer—or amplify bias and hallucinations. Dataset builders should work with application and model developers (often the same person on small teams).

### What data for which phase?

| Phase | Typical format | Quantity metric |
|-------|----------------|-----------------|
| Self-supervised / continued pre-training | Text sequences | Tokens |
| Supervised finetuning (SFT) | `(instruction, response)` | Examples |
| Preference finetuning | `(instruction, winner, loser)` | Examples |
| Reward model | Same as preference or `((instruction, response), score)` | Examples |

Training data should **exhibit behaviors you want**—and sometimes **remove** data that teaches bad habits (e.g. unsolicited rewrites in fact-check examples).

### Hard-to-annotate behaviors

**Chain-of-thought (CoT):** Step-by-step responses in training data greatly boost CoT performance (Chung et al., 2024)—but CoT annotations are tedious; CoT datasets are rarer.

**Tool use:** Domain experts help, but humans may omit steps or prefer UIs over APIs. **Simulations** and synthetic traces often fit agents better. **Llama 3** uses a multi-message chat format with headers for source/destination (Dubey et al., 2024).

**Single-turn vs. multi-turn:** Single-turn is easier to collect; multi-turn teaches clarification, correction, and real dialogue flows.

### Three criteria (the “golden trio”)

Think of training as cooking:

| Criterion | Cooking analogy | Meaning |
|-----------|-----------------|---------|
| **Quality** | Fresh ingredients | Relevant, aligned, consistent, formatted, unique, compliant |
| **Coverage** | Right mix of ingredients | Diversity across tasks, topics, styles, formats |
| **Quantity** | Enough to feed everyone | How many examples/tokens—budget-limited |

---

## Data quality

**10K careful instructions** beat hundreds of thousands of noisy ones (Yi, Young et al., 2024). **LIMA** (Zhou et al., 2023): 1,000 curated pairs on 65B Llama rivaled or beat GPT-4 in ~43% of human comparisons—but less robust than product models.

**Llama 3** found human annotations error-prone on nuanced safety; they built **AI-assisted annotation** tools.

Six characteristics (finetuning-focused):

1. **Relevant** — matches task and era (19th-century law only if that is the task).
2. **Aligned** — meets task requirements (factual vs creative vs concise).
3. **Consistent** — across annotators; needs strong **annotation guidelines**.
4. **Correctly formatted** — strip HTML, trailing whitespace, wrong dtypes.
5. **Sufficiently unique** — duplicates bias and contaminate eval splits.
6. **Compliant** — laws, PII policies, licenses.

Guidelines for annotation overlap with **evaluation guidelines** (Chapter 4)—reuse eval examples as seeds for synthesis.

---

## Data coverage

Models need data that matches **how users actually ask**—typos, short vs long prompts, all programming languages you support, cultural diversity for global products.

**Nemotron** (Adler et al., 2024): task, topic, and instruction diversity (formats, lengths, open vs yes/no). **Shen et al. (2024):** more heterogeneous data can sometimes **hurt** performance.

**Llama 3** gains came mainly from **data quality and diversity**, not architecture changes. Domain mixes differ by phase (Table 8-1 in book): pre-training ~50% general English; SFT adds exam-like and long-context slices; preference finetuning shifts toward general knowledge (~82%). **Annealing** on small high-quality code/math boosts reasoning benchmarks.

**Zhou et al. experiment:** 2,000 examples each—high-quality only, diverse only, or both—models trained on **both** win on generation quality.

---

## Data quantity

From **one-example** demos (Howard & Whitaker) to **millions** of finetuning pairs—still tiny vs Llama 3’s **16 trillion** pre-training tokens.

**Factors:**

| Factor | Effect |
|--------|--------|
| **Finetuning method** | Full finetune needs orders of magnitude more data than LoRA |
| **Task complexity** | Sentiment vs financial QA |
| **Base model** | Stronger base → fewer examples needed; **ossification** can limit adaptation with lots of data (Hernandez et al., 2021) |

**OpenAI/SNLI pattern:** with **100** examples, stronger base models win after finetune; with **550k**, all models converge—use PEFT + strong base for small data; full finetune + smaller model for large data.

**Start with ~50 well-crafted examples** to validate finetuning helps before scaling—if nothing moves, check hyperparameters and quality, not only size.

**Scaling curves:** plot performance vs 25%/50%/100% of data—steep slope means more data helps; plateau means diminishing returns (typical).

**Task diversity:** Flan-T5 performance jumped from **9 → 282** tasks; gains plateaued near **1,836** tasks (Chung et al., 2022).

**Staged data strategies:**

- Self-supervised legal docs → supervised QA pairs  
- Tweet sentiment → product sentiment  
- Synthetic medical data → real data (harder; two finetunes)

Budget example: $10k at $2/example → max 5,000 examples—balance data vs compute spend.

---

## Data acquisition and annotation

**Best source:** your **application’s own data**—the data flywheel (user content, logs, feedback; Chapter 10). Perfect relevance and distribution.

Otherwise: mix public, purchased, annotated, and synthetic sources. Typical pipeline:

1. Find public datasets (10k examples).
2. Filter low-quality instructions (9k left).
3. Rewrite bad responses for 3k instructions.
4. Fill topic gaps with templates + AI generation + human review.

**Public dataset hubs:** Hugging Face, Kaggle, Google Dataset Search, Data.gov, ICPSR, UCI/ OpenML, AWS Open Data, TensorFlow datasets, **lm-evaluation-harness** benchmarks (400+ sets), SNAP graph data.

**Always inspect licenses and provenance**—commercial licenses may include non-commercial sources.

Annotation is among the hardest pipeline steps—teams abandon guidelines and hope models “figure it out,” which is risky for production.

---

## Data augmentation and synthesis

| Process | Source | Example |
|---------|--------|---------|
| **Augmentation** | Real data transformed | Flip image; synonym swap |
| **Synthesis** | Generated to mimic real | Simulated transactions; AI paraphrase |

Libraries like **Faker** started for test data; LLMs enable doctor notes, contracts, ads, etc. **Mixing human + synthetic** often beats either alone.

### Why synthesize?

- **Quantity** — scale where real data is scarce (rare weather, deep sea, accidents).
- **Coverage** — edge cases, toxicity, class balance, adversarial examples (**TrueTeacher**, Gekhman et al., 2022).
- **Quality** — tool-use traces, hard math, consistent preference labels (Anthropic model-written evals, Perez et al., 2022).
- **Privacy** — synthetic patient/claims records.
- **Distillation** — student trained on teacher outputs.

### Traditional techniques

**Rule-based / templates:** transactions, invoices, regex/math problems (**AlphaGeometry**, 100M synthetic examples, Trinh et al., 2024). Text: synonym replacement, gender debiasing swaps (Table 8-2 in book). **Perturbation** for robustness (ImageNet-C, BERT random tokens).

**Simulation:** CARLA, robotics pour-coffee scenarios, **StableToolBench** API simulation (Guo et al., 2024), finance/climate rare events. **Sim2Real** gap remains.

### AI-powered synthesis

- **Self-play** — OpenAI Dota, AlphaGo.
- **Paraphrase / translate** — MetaMath ~400k from 15k MATH/GSM-8K (Yu et al., 2023); low-resource languages via back-translation check.
- **Code translation** — Llama 3 expands language coverage.
- **Reverse instruction** — AI prompts from high-quality human long-form content (Köksal, Li, Chen)—avoids hallucinated long responses.
- **Bootstrapping loop** — weak model → synthetic instructions on quality text → finetune → repeat (Li et al., 2023).
- **Long-context SFT** — chunk docs, generate Q&A, train with full long doc as context.

**Instruction synthesis patterns:**

- Topics → subtopics → instructions (UltraChat, Ding et al., 2023).
- **Alpaca:** 175 Self-Instruct seeds → 52k pairs via GPT-3 (Taori et al., 2023).

**Llama 3 coding pipeline (case study):**

1. AI problem descriptions (diverse topics).
2. Solutions per language + CoT + lint rules.
3. AI unit tests; revise on failure (~20% self-correct).
4. Cross-language translation + filter.
5. Explanations/docs with **back-translation** verification.  
→ **2.7M+** synthetic coding examples.

### Data verification

Prefer data you can **verify**: parsers, linters, unit tests, execution, back-translation. Else **AI judges** (swap order to avoid position bias, NVIDIA 2024). Factual consistency filters (Chapter 4). Heuristics: length, repetition, duplicate instructions (Self-Instruct filters).

Ultimate test: **does it improve the model?**

### Limitations of AI-generated data

1. **Quality** — garbage in, garbage out without verification.  
2. **Superficial imitation** — style without reasoning (**Gudibande et al., 2023**).  
3. **Model collapse** — training on recursive synthetic data forgets rare events (Shumailov et al., 2023); mitigated by **mixing real + synthetic** (Gerstgrasser et al., 2024).  
4. **Obscure lineage** — copyright, benchmark contamination risks.  
5. **Bias amplification** — feedback loops (Taori & Hashimoto, 2023).

**Nemotron-4** used ~98% synthetic in post-training (NVIDIA, 2024)—success with rigorous verification; not proof for unbounded recursion.

---

## Model distillation

Small **student** mimics large **teacher** (Hinton et al., 2015)—e.g. **DistilBERT** (40% smaller, ~97% capability), **Alpaca** (7B on davinci-003 outputs). Check **licenses**—many prohibit training competitors on outputs.

Not all synthetic training is distillation (student can exceed teacher, e.g. Nemotron-4 340B finetuned with Mixtral-generated data outperforming teacher). **Self-generated unverified data** can degrade; verified synthetic loops can improve (Llama 3).

---

## Data processing

Order steps for **time/compute efficiency**; trial runs; **never edit in place**—keep raw copies.

### Inspect

Distributions: token frequency, lengths, topics, languages, annotator bias, inter-annotator disagreement. **Manual inspection** (15 minutes) often saves hours—high value-to-prestige ratio (Greg Brockman). Fact-check samples.

### Deduplicate

Duplicates skew labels and **leak** train/test (Lee et al., 2021; Tirumala et al., 2023). Repeating 0.1% of data 100× can halve effective model size (Anthropic, Hernandez et al., 2022). Methods: pairwise similarity, **MinHash**, Bloom filters, embedding + ANN (Chapter 3/6 tools: dupeGuru, datasketch, lazyNLP).

### Clean and filter

Remove HTML/Markdown junk (Databricks: +20% accuracy, −60% tokens). PII/toxic/copyright filters (Chapter 4). Active learning / importance sampling / data pruning (Sorscher et al., 2022). Annotator fatigue heuristics (Kern et al., 2024).

### Format

Match **tokenizer and chat template** (Chapter 5). Convert few-shot prompts into `(input, output)` rows—finetuned inference can use minimal prompts (`burger -->` vs long 3-shot). **Train/serve format must match** exactly (spaces, prefixes).

---

## Chapter wrap-up

Dataset design starts from **behaviors you want**, then quality, coverage, and quantity—often with synthetic data you can **verify**. Data remains the bottleneck where automation stops: guidelines, judgment, and compliance still need humans.

Chapter 9 covers **inference optimization** once you have a model worth serving.

---

## Closing notes

For application teams, Chapter 8 reframes finetuning (Chapter 7) as a **data problem first**. I would invest early in annotation guidelines shared with eval (Chapter 4), a 50-example pilot, and scaling curves before paying for 10k labels.

The **form vs. facts** split from Chapter 7 applies here too: synthetic data excels at coverage and format, but factual and rare-tail behavior still needs real data or verifiable pipelines (code execution, back-translation). I treat **model collapse** and **imitation without reasoning** as reasons to cap synthetic share and log data lineage.

The Llama 3 coding synthesis workflow is the template I would copy for any domain where outcomes are **programmatically checkable**—then extend AI judges only where checks fail.

**Reference:** Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 8: Dataset Engineering.

---

## References

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
