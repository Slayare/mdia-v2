# MDIA V2 — Roadmap

**Status:** Proposed working order. Refines the build order in [../context/future-state.md](../context/future-state.md). Explicit decisions in [../context/vision.md](../context/vision.md) take precedence.
**Date:** 3 October 2026

Update the status column as each step lands. Each step is one commit-sized unit with its test (see [../ways-of-working/incremental-commits.md](../ways-of-working/incremental-commits.md)); a step may split into several commits.

| # | Step | Status |
|---|---|---|
| 1 | Tiny deterministic world, invariants and in-memory event journal (scripted fake decider) | done |
| 2 | Ontolette identity as a small data object (id, name, traits, goals, beliefs) | done |
| 3 | Decision port and Ollama structured-output adapter, validated against `AgentAction` | done |
| 4 | Turn loop emitting a turn record | todo |
| 4b | Runnable CLI in `runtime/`: tiny world, one Ontolette, N ticks against Ollama, printing each turn record | todo |
| 5 | Run analytics report, derived from the journal and turn records (see [Analytics](#analytics)) | todo |
| 6 | In-memory episodic memory (recency and keyword retrieval) | todo |
| 7 | Second Ontolette and deterministic turn order | todo |
| 8 | Two-way conversation (speech delivered as an observation) | todo |
| 9 | First behavioural eval (e.g. B recalls what A promised) | todo |
| 10 | SQLite journal, snapshots, replay and resume | todo |
| 11 | Relationship state, derived from memory first | todo |
| 12 | Embedding-based retrieval behind the memory port | todo |
| 13 | Lifecycle basics (hunger, death, birth) | todo |
| 14 | Dataset export, then first QLoRA fine-tune | todo |

## Rationale for the order

- **World before decision (1 before 3).** The world owns reality, so its invariants (dead agents cannot act, resources cannot go negative) are tested first with no model involved. Invalid actions are rejected by the world and recorded, not crashed on.
- **Event journal first (1).** Each turn is an event. Memory, persistence, replay and training data are all derived from events. SQLite (10) replaces the in-memory journal behind the same interface.
- **Eval early (9).** [testing.md](../ways-of-working/testing.md) says evaluation starts with the first slice. The same scenario later judges embedding retrieval (12).
- **Identity stays small (2).** No monolithic Ontolette class; mutable state is separate from identity (see [../architecture/repo-structure.md](../architecture/repo-structure.md)).
- **Relationships derived first (11).** Explicit relationship records may conflict with emergence. Promote to explicit state only if derivation proves insufficient.
- **Watch it run before growing it (4b, 5).** A CLI and an analytics report arrive as soon as a real turn exists, so every later step can be checked by running it, not only by unit tests.

## Turn record

Two records, not one:

- **Event journal:** canonical world truth, used for replay.
- **Trajectory record:** derived, agent-subjective view used for evals and later training.

Fields the trajectory record needs beyond agent, observation, retrieved memories, identity, action and world result:

- tick / simulated time, run id, seed
- model id and version, prompt hash
- raw model output (replay needs recorded inference, not only the parsed action)
- parse or validation error, fallback used
- inference latency (wall-clock, kept apart from simulated time)
- identity version, config version

`reward` is deliberately omitted. It does not fit emergence over scripting. Step 14 curates and filters trajectories for supervised fine-tuning; add a reward only if preference or RL methods are adopted.

## Analytics

Analytics are computed from the event journal and turn records, never from separate state tables, so they describe exactly what happened in a run. Metrics are pure functions over records (unit-tested); printing is a thin layer on top. A report is per run; once runs are persisted (step 10) it defaults to the latest one.

Step 5 covers what exists then. Each later step adds the section for what it introduces:

| Section | Contents | From step |
|---|---|---|
| Run overview | Run id, seed, config and model versions, ticks, agents | 5 |
| Actions | Actions per agent, accepted versus rejected, rejection reasons, resource flow over ticks | 5 |
| Model health | Parse and validation failures, fallbacks used, latency | 5 |
| Identity | Latest goals, beliefs and traits per agent, and changes between identity versions | 5 |
| Memory | Memories per agent, retrieval hits per turn | 6 |
| Interactions | Who spoke to whom: pair counts and unique partners | 8 |
| Relationships | Derived relationship strength per pair, over time | 11 |
| Population | Births, deaths, living population over time | 13 |

Sentiment or emotional tagging of memories (from the earlier MDIA analysis) is added only once a mechanism produces it; the report does not invent tags.

## Known gaps and risks

- **Turn order and scheduling** is undecided ([../context/open-questions.md](../context/open-questions.md)). It becomes unavoidable at step 7: use deterministic ordering and one random stream per run.
- **Lifecycle** (step 13) is the route to the primary goal of generations; do not let it slip behind training.
- **Replay and resume** need explicit tests in step 10, not just a working database.
- **QLoRA feasibility** must be benchmarked on the actual hardware before step 14 is committed to.
