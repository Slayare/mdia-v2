# MDIA V2 — Open Decisions and Next Research

**Status:** Open. Update or remove items as they are decided (record decisions as ADRs in [../architecture/decisions/](../architecture/decisions/)).
**Date:** 2 October 2026

Related: [future-state.md](future-state.md) (time model and fidelity ladder proposals) · [../plans/roadmap.md](../plans/roadmap.md) (ordered build steps)

- **Time:** Fixed updates versus discrete events versus a hybrid; custom scheduler versus Mesa versus SimPy.
- **Turn order:** Deterministic ordering and random streams for multiple Ontolettes. Must be decided by roadmap step 7 (second Ontolette).
- **Cognitive scheduling:** Activation rules, per-agent fairness, inference budgets, batching and fidelity bias.
- **Relationship state:** Derive relationships from memory, or hold them as explicit state? Explicit records may conflict with emergence. Start derived (roadmap step 11) and promote only if needed.
- **Representation:** Data-oriented agents, ECS-style components and explicit shared social structures.
- **Demography:** Founder assumptions, reproduction, kinship, mortality and population limits. A three-founder scenario needs explicit modelling assumptions rather than silent defaults.
- **Scale targets:** Cumulative births, peak living population, simulated duration and acceptable wall-clock runtime.
- **Reproducibility:** Stable event ordering, random streams, versioning and the boundary between exact replay and new experimental runs.
- **Emergence:** Which low-level mechanisms permit cooperation, conflict and transmission without scripting institutions?

**Next concrete milestone:** Steps 1-4 are done: a deterministic world with invariants and an in-memory event journal, Ontolette identity, model decisions validated against the action contract, and a turn loop from observation to turn record. Next, make runs watchable with a runnable CLI (4b) and run analytics (5), then add episodic memory (6) to complete the smallest inspectable loop. The scheduling approach must be selected and documented before step 7.
