# MDIA V2 — Open Decisions and Next Research

**Status:** Open. Update or remove items as they are decided (record decisions as ADRs in [../architecture/decisions/](../architecture/decisions/)).
**Date:** 2 October 2026

Related: [future-state.md](future-state.md) (time model and fidelity ladder proposals)

- **Time:** Fixed updates versus discrete events versus a hybrid; custom scheduler versus Mesa versus SimPy.
- **Cognitive scheduling:** Activation rules, per-agent fairness, inference budgets, batching and fidelity bias.
- **Representation:** Data-oriented agents, ECS-style components and explicit shared social structures.
- **Demography:** Founder assumptions, reproduction, kinship, mortality and population limits. A three-founder scenario needs explicit modelling assumptions rather than silent defaults.
- **Scale targets:** Cumulative births, peak living population, simulated duration and acceptable wall-clock runtime.
- **Reproducibility:** Stable event ordering, random streams, versioning and the boundary between exact replay and new experimental runs.
- **Emergence:** Which low-level mechanisms permit cooperation, conflict and transmission without scripting institutions?

**Next concrete milestone:** Select and document the minimal simulation/scheduling approach, then build the smallest inspectable loop from observation to cognition, world consequence, event and memory.
