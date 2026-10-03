# MDIA V2

Memory-Driven Identity Agent: a closed-world simulation of persistent simulated individuals (Ontolettes) exploring emergent identity, memory and society. Emergence over scripting; the LLM is a cognitive component and the simulation owns reality.

## Always-loaded context

@docs/context/vision.md
@docs/ways-of-working/testing.md
@docs/ways-of-working/tdd.md
@docs/ways-of-working/incremental-commits.md

## Hard rules

- Never run `git commit` (or push). Do the work, then suggest a conventional-commit message for the user to use.
- One commit-sized step at a time: a single thing plus its test. Use TDD (red-green-refactor).

## Read on demand

- Roadmap (ordered build steps and status; update the status when a step lands): docs/plans/roadmap.md
- Architecture (subsystems, cognition workflow, state, memory, persistence): docs/architecture/overview.md
- Provisional tech stack and reference links: docs/architecture/tech-choices.md
- Proposed repo layout and dependency rule: docs/architecture/repo-structure.md
- Proposals (time model, fidelity ladder, build order, society, training): docs/context/future-state.md
- Unresolved decisions and next milestone: docs/context/open-questions.md

Explicit decisions in vision.md take precedence over proposals elsewhere. Items marked "Proposed" or "Provisional" are not settled.
