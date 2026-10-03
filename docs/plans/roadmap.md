# MDIA V2 — Roadmap

**Status:** Proposed working order. Refines the build order in [../context/future-state.md](../context/future-state.md). Explicit decisions in [../context/vision.md](../context/vision.md) take precedence.
**Date:** 3 October 2026

Update the status column as each step lands. Each step is one commit-sized unit with its test (see [../ways-of-working/incremental-commits.md](../ways-of-working/incremental-commits.md)); a step may split into several commits.

| # | Step | Status |
|---|---|---|
| 1 | Tiny deterministic world, invariants and in-memory event journal (scripted fake decider) | todo |
| 2 | Ontolette identity as a small data object (id, name, traits, goals, beliefs) | todo |
| 3 | Decision port and Ollama structured-output adapter, validated against `AgentAction` | todo |
| 4 | Turn loop emitting a turn record | todo |
| 5 | In-memory episodic memory (recency and keyword retrieval) | todo |
| 6 | Second Ontolette and deterministic turn order | todo |
| 7 | Two-way conversation (speech delivered as an observation) | todo |
| 8 | First behavioural eval (e.g. B recalls what A promised) | todo |
| 9 | SQLite journal, snapshots, replay and resume | todo |
| 10 | Relationship state, derived from memory first | todo |
| 11 | Embedding-based retrieval behind the memory port | todo |
| 12 | Lifecycle basics (hunger, death, birth) | todo |
| 13 | Dataset export, then first QLoRA fine-tune | todo |

## Rationale for the order

- **World before decision (1 before 3).** The world owns reality, so its invariants (dead agents cannot act, resources cannot go negative) are tested first with no model involved. Invalid actions are rejected by the world and recorded, not crashed on.
- **Event journal first (1).** Each turn is an event. Memory, persistence, replay and training data are all derived from events. SQLite (9) replaces the in-memory journal behind the same interface.
- **Eval early (8).** [testing.md](../ways-of-working/testing.md) says evaluation starts with the first slice. The same scenario later judges embedding retrieval (11).
- **Identity stays small (2).** No monolithic Ontolette class; mutable state is separate from identity (see [../architecture/repo-structure.md](../architecture/repo-structure.md)).
- **Relationships derived first (10).** Explicit relationship records may conflict with emergence. Promote to explicit state only if derivation proves insufficient.

## Turn record

Two records, not one:

- **Event journal:** canonical world truth, used for replay.
- **Trajectory record:** derived, agent-subjective view used for evals and later training.

Fields the trajectory record needs beyond agent, observation, retrieved memories, identity, action and world result:

- tick / simulated time, run id, seed
- model id and version, prompt hash
- raw model output (replay needs recorded inference, not only the parsed action)
- parse or validation error, fallback used
- identity version, config version

`reward` is deliberately omitted. It does not fit emergence over scripting. Step 13 curates and filters trajectories for supervised fine-tuning; add a reward only if preference or RL methods are adopted.

## Known gaps and risks

- **Turn order and scheduling** is undecided ([../context/open-questions.md](../context/open-questions.md)). It becomes unavoidable at step 6: use deterministic ordering and one random stream per run.
- **Lifecycle** (step 12) is the route to the primary goal of generations; do not let it slip behind training.
- **Replay and resume** need explicit tests in step 9, not just a working database.
- **QLoRA feasibility** must be benchmarked on the actual hardware before step 13 is committed to.
