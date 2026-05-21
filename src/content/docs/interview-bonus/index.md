---
title: "Interview bonus"
description: "FAQ-style questions for interviews and general AI engineering knowledge, aligned with Chip Huyen's AI Engineering (2025) and these chapter notes."
order: 11.5
sidebar:
  label: "Interview bonus"
---

## Introduction

**Bonus page** — questions that often show up in **technical interviews**, system-design discussions, or “explain it like I’m hiring you” conversations. Answers are concise and tied to ideas from *AI Engineering* (Huyen, 2025) and the [chapter notes](/ai-engineering/docs) on this site—not a substitute for the book.

> **Sanity check:** *“How would you solve this without using an LLM at all?”* If the honest answer is “you can’t,” the problem may be poorly scoped. Classical software, rules, retrieval without generation, or smaller specialized models often belong in the design.

Use site **search** (Pagefind) to jump to a topic. For definitions, see the [Glossary](/ai-engineering/docs/glossary).

---

## LLM fundamentals

### What is tokenization, and how does it affect generation?

**Tokenization** splits text into subword units the model was trained on (BPE, SentencePiece, etc.). It affects **vocabulary size**, **context budget** (tokens ≠ words), **cost** (billing is per token), and **multilingual behavior** (some languages need more tokens per idea). Rare strings can split into many tokens and burn context. Generation always operates in token space: the model predicts the next token; decoding maps tokens back to text. See [Ch. 2](/ai-engineering/docs/understanding-foundation-models).

### How do embeddings really work?

An **embedding** is a dense vector from an encoder (or an embedding model) that places similar meaning close in vector space. For LLMs, “embedding” often means **text vectors for retrieval** (dual encoders, late interaction) rather than the model’s internal hidden states. Quality depends on **training objective**, **domain**, and **language**. Same text can get different vectors if the embedding model changes—plan migrations. See [Ch. 6](/ai-engineering/docs/rag-and-agents) and [Glossary](/ai-engineering/docs/glossary).

### What’s the role of attention and positional encoding?

**Self-attention** lets each token attend to others so the model builds contextual representations. Cost scales ~quadratically with sequence length in vanilla transformers (mitigated in production with FlashAttention, sliding windows, etc.). **Positional encoding** (absolute, RoPE, ALiBi…) tells the model **order**—attention alone is permutation-invariant without it. Long-context models still face **effective** attention limits and cost. See [Ch. 2](/ai-engineering/docs/understanding-foundation-models).

### What changes during fine-tuning? (optimizers, schedulers, layer freezing)

**Fine-tuning** updates some or all weights on task-specific data. You choose **what to train** (full model vs. adapters vs. last layers), **optimizer** (often AdamW), **learning rate schedule** (warmup, cosine decay), **batch size** (memory-limited), and **regularization** (dropout, early stopping on a **held-out eval**). **Layer freezing** stabilizes early layers (general features) and trains later layers or heads—common in PEFT. Wrong data or no eval → **overfitting** and **forgetting**. See [Ch. 7](/ai-engineering/docs/finetuning) and [Ch. 8](/ai-engineering/docs/dataset-engineering).

### LoRA vs QLoRA vs full fine-tune — tradeoffs?

| Approach | Trainable params | Memory | Quality / flexibility | When |
| --- | --- | --- | --- | --- |
| **Full fine-tune** | All | Highest | Maximum adaptation | Lots of domain data, you own the stack |
| **LoRA** | Low-rank adapters | Lower | Strong for style/format/domain | Default PEFT for many apps |
| **QLoRA** | LoRA on **quantized** base | Lowest GPU footprint | Good; watch eval on hard tasks | Consumer GPUs, many adapters |

Full fine-tune is costly and risks **catastrophic forgetting**; LoRA/QLoRA ship faster and compose multiple adapters. Always compare on a **private eval**, not vibes. See [Ch. 7](/ai-engineering/docs/finetuning).

### What is the difference between prefill and decode latency?

**Prefill** processes the prompt (often compute-bound, parallel). **Decode** generates tokens one-by-one (often memory-bandwidth-bound). Users feel **TTFT** (prefill + scheduling) and **TPOT** (per output token). Optimizations differ: batching prefill, KV cache for decode, speculative decoding. See [Ch. 9](/ai-engineering/docs/inference-optimization).

### Why does temperature affect “creativity” and reliability?

**Temperature** scales logits before softmax: higher → flatter distribution → more random tokens; lower → sharper → more deterministic. It does **not** fix factual errors; for facts use **RAG**, **constraints**, and **eval**. For reproducibility, fix `temperature=0` (or low), `seed` if supported, and structured outputs. See [Ch. 2](/ai-engineering/docs/understanding-foundation-models) and [Ch. 5](/ai-engineering/docs/prompt-engineering).

---

## Prompting and context engineering

### Few-shot vs zero-shot — which works better where?

**Zero-shot** relies on instructions + model priors—cheap, fast to iterate, good for well-defined tasks the model already knows. **Few-shot** adds exemplars in-context—helps **format**, **tone**, **edge cases**, and **tool-use patterns** without weight updates; costs tokens and can **bias** toward examples. Prefer zero-shot + clear schema first; add few-shot when eval shows systematic errors. Cap examples to fit context and watch **ordering bias**. See [Ch. 5](/ai-engineering/docs/prompt-engineering).

### How do you design system prompts that are robust across users?

Treat the system prompt as **product spec**: role, constraints, output format, refusal rules, and what **not** to do. Keep it **short and testable**; avoid conflicting instructions. Version it like code; run **regression evals** when it changes. Separate **stable policy** (system) from **volatile facts** (RAG/user message). Layer **guardrails** outside the prompt for safety/PII. See [Ch. 5](/ai-engineering/docs/prompt-engineering) and [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

### How do you make output deterministic?

Combine **low temperature**, **fixed seed** (if API supports), **JSON/schema mode** or constrained decoding, **canonical prompts** (no unnecessary timestamps), and **post-validation** (parse JSON, retry on failure). Log prompt hash + model version. “Deterministic enough” for prod often means **same distribution** on eval sets, not bitwise identical strings. See [Ch. 5](/ai-engineering/docs/prompt-engineering) and [Ch. 9](/ai-engineering/docs/inference-optimization).

### How do you track, version, and backfill changing context?

Store **prompt templates** and **context snapshots** with IDs in your observability stack. When docs or policies change: **version** corpora, **re-embed** in batches, **dual-write** or **blue/green** index, run **retrieval eval** before cutover. For user-specific context, timestamp **memory entries** and expire stale facts. See [Ch. 6](/ai-engineering/docs/rag-and-agents) and [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

### How do you build and maintain memory?

Split **short-term** (conversation in context window) from **long-term** (vector store, profile DB, summaries). Write memory only from **verified** user facts or tool results; summarize periodically to save tokens. Tag entries with **source**, **time**, and **confidence**; let users delete/update (privacy). Avoid unbounded growth—**decay** or roll up old threads. See [Ch. 6](/ai-engineering/docs/rag-and-agents) and [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

### When should you use chain-of-thought (CoT) in production?

CoT helps **multi-step reasoning** and debugging but adds **latency and tokens**. In prod: use CoT when eval proves lift; hide scratchpad from users if needed; prefer **structured steps** or **tool calls** for reliability. Don’t rely on CoT alone for **factual** grounding—pair with RAG. See [Ch. 5](/ai-engineering/docs/prompt-engineering).

---

## RAG systems

### What’s your chunking strategy — by length, semantics, or structure?

**Structure-aware** chunks (headings, sections, records) usually beat naive fixed-size splits for citations. **Length-based** chunks (with overlap) are a solid baseline. **Semantic** chunking (split when embedding similarity drops) helps heterogeneous docs but costs compute. Match chunk size to **retrieval granularity** and **context window**; tune with **retrieval eval** (precision@k, nDCG). See [Ch. 6](/ai-engineering/docs/rag-and-agents).

### How do you choose a vector DB (Chroma, Pinecone, OpenSearch…)?

Decide on **scale**, **latency SLO**, **metadata filters**, **hybrid search** (BM25 + vectors), **ops model** (managed vs. self-hosted), **cost**, and **compliance**. Pinecone/Weaviate simplify ops; OpenSearch/Elasticsearch excel at **hybrid** and existing search teams; Chroma/pgvector are fine for prototypes. The DB matters less than **chunking, embeddings, and eval**. See [Ch. 6](/ai-engineering/docs/rag-and-agents).

### Can you update or backfill embeddings with zero downtime?

Yes, with **versioned indexes**: build **index v2** in parallel, **dual-query** during validation, switch traffic with a flag, retire v1. Re-embed in **batches** with rate limits; store `embedding_model_version` on each vector. For large corpora, **incremental** updates per doc ID plus periodic compaction. See [Ch. 6](/ai-engineering/docs/rag-and-agents).

### How do you evaluate retrieval quality (precision@k, reranking, citation)?

Build a **labeled set** of (query, relevant doc IDs). Measure **precision@k**, **recall@k**, **MRR**, **nDCG**. Add a **reranker** (cross-encoder) when bi-encoder retrieval is noisy. End-to-end **answer faithfulness** and **citation match** catch failures retrieval metrics miss. Log **which chunks** were used per answer. See [Ch. 3](/ai-engineering/docs/evaluation-methodology), [Ch. 4](/ai-engineering/docs/evaluating-modern-ai-systems), [Ch. 6](/ai-engineering/docs/rag-and-agents).

### RAG vs fine-tuning — when do you pick which?

| Need | Prefer |
| --- | --- |
| Fresh/factual/private docs | **RAG** |
| Style, format, tool patterns, domain phrasing | **Prompting** → then **finetune** |
| Behavior baked into weights (offline, same every call) | **Finetune** (often LoRA) |

Often **both**: RAG for facts, LoRA for tone/format. Finetuning won’t fix a missing knowledge base. See [Ch. 6](/ai-engineering/docs/rag-and-agents) and [Ch. 7](/ai-engineering/docs/finetuning).

### How do agents differ from a single RAG call?

**Agents** loop: plan → act (tools/APIs) → observe → repeat. They trade **latency and cost** for **flexibility**. Risks: tool errors, loops, insecure actions. Start with **retrieve-then-generate**; add agents when eval shows multi-step tool use is required. See [Ch. 6](/ai-engineering/docs/rag-and-agents).

---

## MLOps and LLMOps

### Sketch a pipeline: from raw data → model → serving → feedback

1. **Define metrics** tied to product (Ch. 3–4).  
2. **Ingest** docs/events → clean/dedupe (Ch. 8).  
3. **Adapt**: prompts → RAG → finetune if needed (Ch. 5–7).  
4. **Serve** with gateway, caching, autoscaling (Ch. 9–10).  
5. **Observe** traces, costs, errors (Ch. 10).  
6. **Collect feedback** → label failures → update eval/data → redeploy.  

That loop is the **data flywheel** when done safely (avoid degenerate feedback). See [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

### How would you monitor performance drift or hallucinations?

Track **online** proxies: user thumbs, edits, escalation rate, **groundedness** checks, retrieval hit rate, latency, cost per success. **Offline**: periodic runs on golden sets; compare across **model/prompt/index versions**. Segment by **locale, product area, user cohort**. Alert on **statistical shifts**, not single bad answers. See [Ch. 4](/ai-engineering/docs/evaluating-modern-ai-systems) and [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

### How do you log prompts and outputs for debugging and auditing?

Log **request ID**, model version, prompt template version, retrieved chunk IDs, latency, token counts, output, tool calls, and **PII-redacted** copies where required. Separate **debug** (full prompts) from **analytics** (hashed). Retention and access control for compliance. Use OpenTelemetry-style traces across retrieval → LLM → post-process. See [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

### CI/CD for LLM workflows — what’s different from classic ML?

Pipelines gate on **eval suites** and **prompt/index artifacts**, not only unit tests. Non-determinism → **threshold-based** promotion. Version **prompts, embeddings, indexes, and models** together. Load-test **inference** separately. Human review for safety/policy changes. Canary by **traffic %** with rollback. See [Ch. 4](/ai-engineering/docs/evaluating-modern-ai-systems) and [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

### How do you evaluate LLM apps without golden answers?

Use **rubric-based** scoring, **AI-as-judge** (with bias checks), **pairwise** comparison, **functional tests** (run code/SQL), and **human spot-checks** on stratified samples. Combine metrics: usefulness, faithfulness, safety, latency, cost. See [Ch. 3](/ai-engineering/docs/evaluation-methodology) and [Ch. 4](/ai-engineering/docs/evaluating-modern-ai-systems).

---

## Cost and latency tradeoffs

### How do you reduce token usage?

Shorter prompts, **summarize** history, retrieve only needed chunks, **compress** tool outputs, cheaper models for routing/draft, **structured** outputs (less rambling), cache **prefixes** (prompt caching), and fix **max tokens**. Measure tokens per successful task, not per request. See [Ch. 9](/ai-engineering/docs/inference-optimization).

### When should you quantize a model?

When **self-hosting** and **memory or cost** dominates, and eval shows acceptable quality loss (INT8/INT4, GPTQ/AWQ, etc.). Quantize for **inference**; **QLoRA** uses quantization for training adapters. Re-benchmark **your** tasks after quantizing. See [Ch. 9](/ai-engineering/docs/inference-optimization).

### What’s your batching and caching strategy to reduce latency?

**Continuous batching** for serving; separate **prefill** and **decode** queues. **KV cache** reuse for shared prefixes; **prompt caching** on APIs. **Semantic cache** only with caution (staleness). Right-size **max concurrent** requests to avoid thrashing. See [Ch. 9](/ai-engineering/docs/inference-optimization).

### When to use hosted APIs vs open-source models?

| Hosted API | Open-source / self-host |
| --- | --- |
| Fastest path, frontier quality | Data residency, cost at scale, custom adapters |
| Pay per token | CapEx/ops for GPUs, team skill |

Hybrid: **router** sends easy queries to small/local models and hard ones to frontier APIs. See [Ch. 1](/ai-engineering/docs/introduction-to-building-ai-applications-with-foundation-models) and [Ch. 9](/ai-engineering/docs/inference-optimization).

---

## System design thinking

### How do you make an AI system more deterministic and less brittle?

Narrow the task, **schema-locked** outputs, validation + **retry**, retrieval with citations, **feature flags** for model versions, and **fallback models**. Reduce degrees of freedom in the agent loop; prefer **workflow** over open-ended autonomy when stakes are high. See [Ch. 5](/ai-engineering/docs/prompt-engineering) and [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

### What fallback do you use if the LLM fails mid-task?

**Retries** with backoff; **smaller/cheaper backup model**; **cached answer**; **degraded UX** (“try again”, human handoff); **rule-based** path; return **partial** result with clear status. For agents, **checkpoint** state per step. Never infinite loops—max steps/timeouts. See [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

### Can you solve this without an LLM or vector DB?

Often yes: **SQL + full-text search**, **rules**, **templates**, **classification** with small models, **graph** of verified facts. LLMs excel at language-heavy, ambiguous, or rapidly changing tasks—not at being the only database. Vector DBs help **semantic** search; keyword + metadata may suffice. See [Ch. 1](/ai-engineering/docs/introduction-to-building-ai-applications-with-foundation-models).

### What’s the right database for this task — SQL, NoSQL, or vector?

**SQL** for transactions, joins, reporting. **NoSQL** for flexible schemas, high write rates, documents. **Vector** for similarity search on unstructured text—usually **alongside** SQL/ES, not instead of them. Hybrid **BM25 + vector** is common in RAG. See [Ch. 6](/ai-engineering/docs/rag-and-agents).

### How do guardrails fit in the architecture?

**Input**: PII scrub, injection checks, policy filters. **Output**: moderation, format validation, blocklists. Run **outside** the model when possible for auditability. Log violations and sample for eval. See [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

---

## Real-world scenarios

### What happens if your embedding model changes — how do you migrate safely?

1. Pin `embedding_model_id` on every vector.  
2. Build **new index** with the new model (full re-embed).  
3. Compare **retrieval eval** old vs. new on the same query set.  
4. **Canary** traffic; dual-read if needed.  
5. Decommission old index after SLOs hold.  

Never swap models in place without re-embedding. See [Ch. 6](/ai-engineering/docs/rag-and-agents).

### How would you fine-tune a model on user behavior and deploy it?

Collect **opt-in** interaction data; **filter PII**; dedupe and balance; define **target behavior** (not raw clicks if biased). Train **LoRA** on curated pairs; evaluate on **held-out** real prompts. **Version** adapters; deploy behind flag; monitor **regressions** and **feedback loops**. Consider privacy/regulatory review before training on user content. See [Ch. 7](/ai-engineering/docs/finetuning), [Ch. 8](/ai-engineering/docs/dataset-engineering), [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

### How would you make this system cheaper without killing quality?

Measure **cost per successful task**. Cheaper model for **routing/draft**; cache prompts; shorten context; better retrieval (fewer tokens); batch offline jobs; **quantize** self-hosted paths; reduce agent steps. A/B each change on **quality metrics**, not cost alone. See [Ch. 9](/ai-engineering/docs/inference-optimization).

### Can you walk me through debugging incorrect LLM outputs?

1. Reproduce with **saved trace** (prompt, retrieval IDs, model version).  
2. Classify failure: **retrieval miss**, **prompt ambiguity**, **model hallucination**, **tool error**, **post-process bug**.  
3. Check **chunk relevance** and citations.  
4. A/B **temperature / prompt / model**.  
5. Add case to **regression eval**; fix root cause (data > prompt > model).  

See [Ch. 4](/ai-engineering/docs/evaluating-modern-ai-systems) and [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

### Users report “the bot forgot what I said yesterday” — what do you check?

Context window truncation, missing **long-term memory** write, wrong **session ID**, cache serving stale profile, or summarization dropping entities. Verify what was actually in the **last request payload**. See [Ch. 6](/ai-engineering/docs/rag-and-agents).

### Leadership wants “100% accurate AI.” How do you respond?

Set **measurable** targets per risk class (e.g. citation required for medical claims, human review for high stakes). Explain **residual error**, monitoring, and **escalation** paths. Evaluation methodology is negotiation, not magic. See [Ch. 3](/ai-engineering/docs/evaluation-methodology).

---

## Extra questions (evaluation, safety, product)

### What is “goodput” and why does it matter in interviews?

**Goodput** is useful work per dollar or second—not raw tokens/sec. Optimizing TPOT while answers are wrong wastes money. Tie infra metrics to **task success**. See [Glossary](/ai-engineering/docs/glossary) and [Ch. 9](/ai-engineering/docs/inference-optimization).

### How do you detect eval contamination or benchmark overfitting?

Hold out **time-split** and **source-split** data; private **user-like** prompts; avoid tuning repeatedly on the same public benchmark. Watch **verbosity bias** in AI judges. See [Ch. 3](/ai-engineering/docs/evaluation-methodology).

### What is a degenerate feedback loop?

When the product only shows model outputs and users adapt to errors, **logs reinforce bad behavior** (e.g. clickbait summaries). Mitigate with **human labels**, **diverse** sampling, and **offline** eval before retraining. See [Ch. 10](/ai-engineering/docs/ai-engineering-architecture-and-user-feedback).

### Build vs buy for foundation models?

**Buy (API)** for speed, frontier quality, and low ops. **Build/self-host** for data control, predictable unit economics at scale, and custom adapters. Most teams **buy first**, then hybridize. See [Ch. 4](/ai-engineering/docs/evaluating-modern-ai-systems).

### How do you scope an MVP AI feature?

**Crawl–walk–run**: one user journey, clear **success metric**, smallest model that passes eval, manual review for edge cases, then add RAG/agents only when eval proves need. See [Ch. 1](/ai-engineering/docs/introduction-to-building-ai-applications-with-foundation-models).

---

## Related

- [Book map](/ai-engineering/docs/book-map) — reading paths by goal (RAG, finetune, cost, eval)
- [Glossary](/ai-engineering/docs/glossary) — definitions (TTFT, LoRA, goodput, …)
- [Study mode](/ai-engineering/docs/introduction-to-building-ai-applications-with-foundation-models/study) — per-chapter quizzes
- [Epilogue](/ai-engineering/docs/epilogue) — what to do after finishing the book

---

## References

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media.

- [O’Reilly — *AI Engineering*](https://www.oreilly.com/library/view/ai-engineering/9781098166304/)
- [Book repository — aie-book](https://github.com/chiphuyen/aie-book)
