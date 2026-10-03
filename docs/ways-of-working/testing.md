# Testing and Scientific Evaluation

**Status:** Direction. Seed for a fuller TDD / definition-of-done doc. Tooling: pytest; Hypothesis where stateful invariants justify it (see [../architecture/tech-choices.md](../architecture/tech-choices.md)).
**Date:** 2 October 2026

| Category | Question | Examples |
|---|---|---|
| Software tests | Is the implementation correct? | Dead agents cannot act; resources cannot become negative; references are valid |
| Replay tests | Can recorded execution be reconstructed? | Restored snapshots plus events yield the same state under the recorded configuration |
| Behavioural evaluations | Do mechanisms produce the intended capabilities? | Remembering promises, handling contradictions, identity continuity, effects of reflection |
| Experimental runs | What happened in this society? | Lineages, knowledge transmission, group formation and long-term changes |

Compare configurations with explicit versions and assumptions. For example, compare reflection enabled versus disabled across controlled runs. Reusing a seed supports comparison but does not establish causality by itself; stochastic variation and model variability need consideration.

Correctness and evaluation begin with the first vertical slice and continue through every later stage.
