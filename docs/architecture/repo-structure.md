# MDIA V2 — Proposed Repository Structure

**Status:** Proposed conceptual layout, superseding the earlier general-agent-runtime framing. Create components when needed rather than filling every directory with placeholders.
**Date:** 2 October 2026

```text
mdia-v2/
├── pyproject.toml
├── uv.lock
├── .python-version
├── README.md
├── configs/
│   ├── agents/
│   ├── worlds/
│   └── experiments/
├── src/mdia/
│   ├── domain/
│   │   ├── agents/
│   │   ├── memory/
│   │   ├── relationships/
│   │   ├── society/
│   │   ├── world/
│   │   └── events/
│   ├── contracts/
│   ├── cognition/
│   │   ├── scheduler/
│   │   ├── perception/
│   │   ├── context/
│   │   ├── deliberation/
│   │   ├── reflection/
│   │   └── planning/
│   ├── simulation/
│   │   ├── engine/
│   │   ├── time/
│   │   ├── population/
│   │   ├── lifecycle/
│   │   └── systems/
│   ├── models/
│   │   ├── ports/
│   │   └── adapters/
│   ├── memory/
│   │   ├── retrieval/
│   │   ├── consolidation/
│   │   └── storage/
│   ├── persistence/
│   ├── experiments/
│   ├── evaluation/
│   └── runtime/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── replay/
│   └── evals/
├── alembic/
├── training/
├── datasets/evals/
└── docs/
    ├── context/
    ├── ways-of-working/
    ├── architecture/
    │   └── decisions/
    └── plans/
```

`domain/` defines meaning and state; runtime subsystems implement workflows. Domain memory types and the memory service are distinct responsibilities. `runtime/` wires concrete implementations together.

**Dependency rule:** Domain code must not import concrete model servers, database implementations or simulation libraries. Avoid a miscellaneous `brain/` folder and a monolithic Ontolette class. A multi-package uv workspace is unnecessary initially.
