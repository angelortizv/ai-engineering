---
title: "RAG and Agents"
description: "Chapter 6 summary — AI Engineering (Huyen, 2025)"
order: 6
---

## Introduction

A model needs **instructions** (Chapter 5) and **context** per query. Chapter 5 covered how to write instructions; this chapter covers **how to build context**—the two dominant patterns are **RAG** (retrieval-augmented generation) and **agents** (tool-using planners).

- **RAG** retrieves from external memory (databases, past chats, the web) and feeds results into the generator.
- **Agents** use tools (search, SQL, code execution, APIs) to perceive and act on an environment.

RAG is mainly **context construction**; agents can do that and more—including **write actions** that change the world. Both extend powerful base models; both need rigorous **evaluation** and **security** (Chapter 5).

---

## Retrieval-Augmented Generation (RAG)

> RAG is a technique that enhances a foundation model's output by first retrieving relevant information from an external data source and then providing that information as context for the generation process.
>
> — Huyen (2025, p. 253)

**Retrieve-then-generate** dates to Chen et al. (2017, Wikipedia QA). Lewis et al. (2020) coined **RAG** for knowledge-intensive tasks: only the most relevant chunks enter the model, improving detail and reducing hallucinations when context is missing.

**Why RAG still matters with long context**

1. Application data often grows **faster** than context limits (“context expands to fill the limit”).
2. Long context ≠ good use of context (**lost in the middle**, cost per token, latency).
3. RAG selects **query-specific** context—useful for per-user data and cost control.

Anthropic (2024) suggests that for Claude, if a knowledge base is under ~200k tokens (~500 pages), you might skip RAG and put everything in the prompt—model-specific guidance varies.

Context construction for foundation models parallels **feature engineering** in classical ML: same purpose, different mechanism.

### RAG architecture

Two components:

1. **Retriever** — **indexing** (prepare data for search) and **querying** (fetch relevant chunks).
2. **Generator** — LLM that answers using the user prompt + retrieved chunks.

Originally Lewis et al. trained retriever and generator jointly; today many systems use **off-the-shelf** parts, though end-to-end finetuning can help. **Retriever quality dominates** system quality.

Typical flow: split documents into **chunks** → retrieve top-*k* for the query → stitch chunks into the final prompt → generate. Whole-document retrieval can blow the context window.

### Retrieval algorithms

Retrieval ranks documents by **relevance**. Two families:

#### Term-based (sparse) retrieval

Keyword matching: **TF** (term frequency in document), **IDF** (inverse document frequency—rare terms matter). **TF-IDF** combines both.

Production tools: **Elasticsearch** (inverted index: term → documents + frequencies), **BM25** (length-normalized TF-IDF variant; strong baseline). Pros: **fast**, cheap, works well out of the box. Cons: **no semantics**—“transformer” matches electrical devices and movies.

Tokenization matters: n-grams (“hot dog”), lowercase, stop words. Lexical overlap retrieval works when query and document lengths are similar.

#### Embedding-based (dense) retrieval

**Semantic retrieval:** embed query and chunks; rank by vector similarity (cosine). Requires **embedding model** quality and a **vector database** with ANN search.

**Vector search:** exact **kNN** for small data; **ANN** (FAISS, HNSW, ScaNN, Annoy, IVF+PQ) for scale—trade recall for speed. Vector DBs are not new to GenAI (search, recommendations use the same ideas).

**SPLADE** uses sparse embeddings—book groups it with embedding-like behavior, not pure lexical.

| Dimension | Term-based | Embedding-based |
|-----------|------------|-----------------|
| Speed | Faster index & query | Embedding + ANN cost |
| Semantics | Weak | Strong (if embedder good) |
| Tuning ceiling | Lower | Finetune embedder/retriever |
| Keyword-heavy queries | Strong | Can miss exact codes/names |
| Cost | Lower | Embeddings, storage, queries |

**Evaluating retrieval:** **context precision** (fraction retrieved that is relevant), **context recall** (fraction of all relevant docs retrieved—expensive at scale). Ranking metrics: NDCG, MAP, MRR. Evaluate **embeddings** (MTEB) and **end-to-end RAG** answers (Chapters 3–4). Vector spend can be a large fraction of total API cost.

#### Hybrid search

Combine approaches:

- **Sequential:** cheap retriever (BM25) → **rerank** with embeddings or cross-encoder.
- **Parallel + fusion:** e.g. **reciprocal rank fusion (RRF)** (Cormack et al., 2009)—merge ranked lists by reciprocal rank scores.

Example: fetch all docs containing “transformer,” then semantic rank for the ML architecture query.

### Retrieval optimization

**Chunking**

- Fixed size (chars, words, sentences, paragraphs) or **recursive** splits (section → paragraph → sentence).
- **Overlap** preserves boundary context (“I left my wife a note” split badly without overlap).
- Size ≤ generator and embedder context limits; token-based chunks tie you to one tokenizer.
- Smaller chunks → more diversity in context but risk splitting coherent topics and **2× index cost** at half size. **Experiment**—no universal best.

**Reranking**

Refine initial rankings; time-decay for news/email; order in context still matters (beginning/end salience) but less than search SERP position.

**Query rewriting**

Ambiguous follow-ups (“How about Emily Doe?”) need standalone queries—LLM rewrite from conversation history, or heuristics in classical search. Hard cases: “his wife” requires identity resolution or admitting unsolvability.

**Contextual retrieval**

Augment chunks with metadata (tags, error codes), **questions the chunk answers**, or **Anthropic-style situating context** (short LLM-generated summary of chunk in parent document, prepended before indexing)—improves discoverability.

### Beyond text

**Multimodal RAG:** retrieve text + images (metadata captions or **CLIP** joint embeddings in a vector DB).

**Tabular RAG:** **text-to-SQL** → execute → generate answer (Kitty Vogue sales example). Schema selection when many tables; functional correctness from Chapter 3–4 applies.

### Choosing a retrieval solution

Check: hybrid support, embedding/ANN algorithms, scale, index latency, query latency, pricing (storage vs queries), enterprise features (ACL, compliance).

---

## AI agents

> An agent is anything that can perceive its environment and act upon that environment.
>
> — Russell & Norvig (1995), as cited in Huyen (2025, p. 275)

Foundation models enable agents that plan and use **tools**. The field lacks a single theory—this chapter is a practical framework.

**Definition:** environment (game, internet, kitchen, codebase) + **actions** (via tools). ChatGPT (browse, code, images) and **RAG systems** (retriever, SQL as tools) are agents.

**Planner (FM)** processes task + feedback → plan → execute → check completion. **Compound error:** 95% per step → ~60% over 10 steps, ~0.6% over 100. **Higher stakes** with write tools.

### Tools

**Read** (perceive): retrievers, web browse, SQL SELECT, email read.  
**Write** (act): SQL UPDATE/DELETE, send email, transfers—require trust, approval, sandboxing (Chapter 5).

Categories:

1. **Knowledge augmentation** — RAG, people search, Slack/email, inventory APIs; web browse prevents staleness but opens untrusted content.
2. **Capability extension** — calculator, calendar, code interpreter, OCR, text-to-image; **Chameleon** (GPT-4 + 13 tools) beats GPT-4 alone on several benchmarks.
3. **Write actions** — automate workflows; never give interns—or unreliable models—delete-on-production without gates.

**Function calling:** declare tools (name, params, docs); per-query subset (`required` / `none` / `auto`); model returns `tool_calls`—validate parameter values in logs.

**Tool selection:** more tools → more capability and harder choice; ablation studies, mistake patterns, usage plots (Chameleon). Prefer fewer, clearer tools; **prompt-engineer tool definitions** with examples and edge cases; **poka-yoke** designs that make common LLM mistakes hard.

### Planning and execution

**Decouple planning from execution:** generate plan → validate (heuristics: invalid tools, max steps; AI judge) → execute. Avoid 1,000 useless steps burning budget.

**Human-in-the-loop** at plan, validate, or execute stages—especially risky DB/git operations.

Typical loop:

1. **Plan** (task decomposition).
2. **Reflect** on plan quality.
3. **Execute** (tools).
4. **Reflect** on outcomes; replan if needed.

**Intent classification** routes tools (billing vs password reset); mark **IRRELEVANT** out-of-scope queries.

**Can LLMs plan?** Debate (LeCun, Kambhampati): autoregressive models may lack true search/backtracking—or we under-tool them. **ReWOO**-style world-model reasoning (Hao et al., 2023) predicts action outcomes. FM and **RL planners** may converge long term.

**Control flows:** sequential, **parallel**, **if/else**, **for** loops—framework support matters for latency (10 parallel browses).

**ReAct** (Yao et al., 2022): interleave **Thought → Act → Observation** until done—planning + reflection in one pattern.

**Reflexion** (Shinn et al., 2023): separate **evaluator** + **self-reflection** → new trajectory. Cost: many tokens per step.

**Granularity:** natural-language plans vs exact function names—NL plans survive API renames but need a **translator** step.

### Advanced agent patterns (Anthropic, 2024)

Patterns for production agents (complement Huyen’s planning discussion):

| Pattern | Idea |
|---------|------|
| **Prompt chaining** | Linear sequence of LLM calls; output of step *n* feeds step *n+1*. |
| **Routing** | Classify intent → specialized downstream prompt or tool set. |
| **Evaluator–optimizer** | Generator + critic LLM iterate until quality threshold. |
| **Orchestrator–workers** | Central LLM delegates subtasks to worker LLMs. |

**Best practices (Anthropic):** crystal-clear tool specs; mistake-proof tool APIs; **start simple**, add complexity only when evals demand it.

### Agent evaluation

Identify failure modes:

**Planning failures**

- Invalid tool name.
- Valid tool, wrong arity of parameters.
- Valid tool, wrong parameter **values**.
- **Goal failure** (wrong city, over budget).
- **False completion** (thinks task done when not).
- **Time** constraints (missed deadline).

Metrics on a `(task, tool_inventory)` dataset: valid plan rate, retries to valid plan, tool-call error rates.

**Tool failures**

- Wrong tool output; translation errors from NL plans; **missing tools** for domain.

**Efficiency**

- Steps, cost, latency per action vs human or baseline.

Benchmarks: Berkeley Function Calling Leaderboard, AgentOps, TravelPlanner; book GitHub simple benchmark.

### Memory

Three mechanisms (Figure 6-16 in book):

| Type | What | Persistence |
|------|------|-------------|
| **Internal knowledge** | Weights from training | Until model update |
| **Short-term** | Context window / conversation | Per session |
| **Long-term** | Vector DB, files, structured stores | Across sessions |

Benefits: overflow handling, **personalization**, consistency of subjective answers, **structured** stores (Excel leads queue) vs unstructured chat.

**Management:** add/delete; FIFO of old messages is easy but can drop critical early context; **summarization** + entity tracking; **reflection** on what to merge/replace (Liu et al., 2023). Long-term holds overflow from short-term (~70/30 split example in book).

Retrieval from long-term memory **is RAG**.

### Supplementary: AI agent protocols

*Not central in Huyen (2025) Chapter 6; included from course material (Yang et al., 2025).*

As agents multiply, **interoperability** needs shared rules for messages and tool calls. **Agent protocols** standardize formats and procedures.

**Taxonomy (Yang et al., 2025):**

- **By orientation:** **context-oriented** (agent ↔ resources, e.g. **MCP** — Model Context Protocol) vs **inter-agent** (agent ↔ agent, e.g. **A2A**).
- **By scenario:** general-purpose vs domain-specific (robotics, etc.).

**Agent communication trilemma** — trade-offs among:

- **Versatility** (rich message types),
- **Efficiency** (cost/latency),
- **Portability** (ease of implementation).

Protocol choice shapes how RAG tools, planners, and external systems plug together in multi-vendor stacks.

---

## Chapter wrap-up

Chapter 6 pairs **RAG** (retrieve → generate; sparse vs dense vs hybrid; chunking, rewrite, contextual retrieval; multimodal and SQL) with **agents** (environment, tools, decoupled planning, ReAct/Reflexion, evaluation, memory). RAG is a special case of an agent whose main tool is retrieval. Both are **prompt-based** adaptations; finetuning is Chapter 7.

Agents need **defensive engineering** from Chapter 5 when tools touch data, code, and the internet—especially **indirect injection** via retrieved or browsed content.

---

## Closing notes

What I take from this chapter is that **context construction is product engineering**: RAG is not “solved” by a 2M token window—you still chunk, hybrid-search, rewrite queries, and measure precision/recall on *your* corpus. I would start with **BM25/Elasticsearch** as a baseline before paying embedding indexing costs, then add semantic reranking where lexical search fails.

For **agents**, the compound-error math is sobering: multi-step autonomy needs **plan validation**, **human gates on writes**, and **reflection** without runaway token burn. Anthropic’s patterns (route → worker, evaluator loop) give a sane growth path from a single prompt chain. I’ll treat **tool definitions** as first-class API design—clear names, few parameters, poka-yoke defaults.

Protocols (MCP, A2A) matter when integrating agents across teams and vendors; the trilemma reminds me I cannot maximize versatility, efficiency, and portability at once—pick two for v1.

**Reference:** Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 6: RAG and Agents.

---

## References

Huyen, C. (2025). *AI engineering: Building applications with foundation models*. O’Reilly Media. Chapter 6: RAG and Agents.

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yau, M., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS*. https://arxiv.org/abs/2005.11401

Yang, Y., Chai, H., Song, Y., Qi, S., Wen, M., Li, N., Liao, J., Hu, H., Lin, J., Chang, G., Liu, W., Wen, Y., Yu, Y., & Zhang, W. (2025). A survey of AI agent protocols. *arXiv*. https://arxiv.org/abs/2504.16736

Anthropic. (2024). Building effective agents. https://www.anthropic.com/engineering/building-effective-agents

Anthropic. (2024). Introducing contextual retrieval. https://www.anthropic.com/news/contextual-retrieval

### Foundational papers (RAG & retrieval)

- [Retrieval-Augmented Generation (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401) — Original RAG paper.
- [Reading Wikipedia to Answer Open-Domain Questions (Chen et al., 2017)](https://arxiv.org/abs/1704.00051) — Retrieve-then-generate precursor.
- [The Probabilistic Relevance Framework: BM25 and Beyond](https://www.nowpublishers.com/article/Details/INR-019) — Robertson & Zaragoza (2009).
- [Reciprocal Rank Fusion](https://plg.uwaterloo.ca/~gvcormac/cormacnorris09a.pdf) — Cormack et al. (2009); hybrid ranking.
- [Lost in the Middle](https://arxiv.org/abs/2307.03172) — Liu et al. (2023); context position effects.

### Agents, planning, and tool use

- [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) — Yao et al. (2022).
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — Shinn et al. (2023).
- [Chameleon: Plug-and-Play Compositional Reasoning](https://arxiv.org/abs/2304.09842) — Lu et al. (2023).
- [Reasoning with Language Model is Planning with World Model](https://arxiv.org/abs/2305.14992) — Hao et al. (2023).
- [Can LLMs Really Reason and Plan?](https://yochan-lab.github.io/papers/llm_reasoning_planning.pdf) — Kambhampati (2023).

### Official guides and tutorials

- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Chaining, routing, evaluator–optimizer, orchestrator–workers.
- [Anthropic — Contextual retrieval](https://www.anthropic.com/news/contextual-retrieval) — Chunk situating for search.
- [OpenAI — Function calling](https://platform.openai.com/docs/guides/function-calling) — Tool use / agents via API.
- [LangChain — RAG conceptual guide](https://python.langchain.com/docs/concepts/rag/) — End-to-end RAG patterns (verify versions).
- [LlamaIndex — RAG](https://docs.llamaindex.ai/en/stable/optimizing/building_rag/) — Indexing, retrieval, evaluation.

### Vector search and databases

- [FAISS (Meta)](https://github.com/facebookresearch/faiss) — Similarity search library.
- [ANN-Benchmarks](https://ann-benchmarks.com/) — Compare ANN algorithms.
- [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — Embedding model evaluation.
- [BEIR](https://github.com/beir-cellar/beir) — Benchmarking IR harness.
- [Zilliz — Vector search explained](https://zilliz.com/learn/what-is-vector-search) — HNSW, IVF, etc.

### Frameworks and orchestration

- [DSPy](https://dspy.ai/) — Programs over prompts (also Ch. 5).
- [LangGraph](https://langchain-ai.github.io/langgraph/) — Stateful agent workflows.
- [AutoGen (Microsoft)](https://microsoft.github.io/autogen/) — Multi-agent conversations.
- [Composio](https://composio.dev/) — Enterprise tool integrations for agents.
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — Context-oriented agent–resource protocol.
- [Google A2A protocol](https://google.github.io/A2A/) — Agent-to-agent interoperability (check current spec).

### Evaluation and security (RAG + agents)

- [Ragas](https://docs.ragas.io/) — RAG evaluation (faithfulness, context precision).
- [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) — Tool-use benchmarks.
- [Microsoft — Plan red teaming for LLMs](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/red-teaming) — Agent safety testing.
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — Injection via RAG/tools.

### Courses, videos, and workshops

- [DeepLearning.AI — Building Applications with Vector Databases](https://www.deeplearning.ai/short-courses/building-applications-vector-databases/) — Embeddings + retrieval basics.
- [DeepLearning.AI — AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) — Agent workflows.
- [Andrew Ng — Agentic AI short course series](https://www.deeplearning.ai/courses/) — Check latest agentic tracks on DeepLearning.AI.
- [UPM — Taller 6: Programación de software con IA (PDF)](https://innovacioneducativa.upm.es/sites/default/files/saga/presentacion-taller6-programacion-software-ia.pdf) — Spanish workshop slides (AI-assisted development).
- [Pinecone — What is RAG?](https://www.pinecone.io/learn/retrieval-augmented-generation/) — Accessible RAG primer (vendor blog).

### Book repository

- [AI Engineering — GitHub (Huyen)](https://github.com/chiphuyen/aie-book) — Chapter 6 code, agent benchmark, extra IR resources.
