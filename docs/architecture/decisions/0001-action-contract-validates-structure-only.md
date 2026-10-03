# ADR 0001 — The action contract validates structure only

**Status:** Accepted
**Date:** 3 October 2026

## Context

A model's proposed action passes two checks: the `AgentAction` contract (Pydantic, at the cognition boundary) and world rules (`simulation/rules.py`). Some constraints could live in either place. For example, `amount > 0` could be a schema constraint, or the world could reject a non-positive gather.

Where a constraint lives decides what gets recorded. A schema failure is a parse error: there is no action, so nothing reaches world resolution or the event journal. A world rejection is an event: the action and the reason are journalled, and they show up in analytics and trajectories.

## Decision

`AgentAction` checks only that model output is well-formed: known action type, required fields present, correct types, no extra fields. Whether an action is possible or sensible (amounts, stock, whether the agent is alive) is decided only by world rules.

This follows from "the LLM is a cognitive component; the simulation owns reality" ([vision.md](../../context/vision.md)). An Ontolette trying to gather −1 berries made a decision. The world should refuse it and record that, not hide it as a formatting error.

## Consequences

- Bad decisions are visible. Rejected actions appear in the journal, the actions section of run analytics and trajectories used for evaluation and training.
- Parse failures mean only "the model did not produce a usable action" and stay a clean model-health metric.
- World rules must handle every value the contract allows (for example, negative amounts). Their tests cover this.
- When tempted to add a value constraint to the contract, add a world rule instead.
