# MDIA V2 — Future State and Proposals

**Status:** Proposed. Nothing here is validated, benchmarked or decided; see [open-questions.md](open-questions.md). Explicit decisions in [vision.md](vision.md) take precedence.
**Date:** 2 October 2026

## Time and cognitive scale

### Proposed time model

Evaluate a **hybrid discrete-event simulation**: jump between scheduled events while retaining periodic updates where they suit world systems. Examples include waking, work, encounters, weather, resource production, births, deaths and reflection.

Compare a purpose-built scheduler, Mesa and SimPy before selecting an implementation. The previous discussion favoured this direction, but no engine has been chosen or benchmarked.

### Proposed cognitive fidelity ladder

| Level | Mode | Example | Model use |
|---|---|---|---|
| C0 | Mechanical | Ageing, hunger, sleeping, travel progression | None |
| C1 | Routine | Established work, meals and household tasks | Usually none |
| C2 | Reactive | Unexpected encounter, minor conflict or opportunity | Conditional |
| C3 | Deliberative | Partner choice, migration or occupation change | Normally required |
| C4 | Reflective | Bereavement, betrayal or changing worldview | Deeper context/reasoning |
| C5 | Highly consequential | Major collective crisis or consequential innovation | Richer deliberation where justified |

This ladder is a **proposal**, not a validated theory of human cognition. Historic importance may only become apparent afterwards; activation should use information available at the time, rather than an oracle announcing future historical significance.

Routine policies should depend on individual state and remain revisable. Otherwise the cheap layer could script away the emergence the project aims to study.

### Why daily inference is unsuitable

At a hypothetical constant population of 5,000, over 5,000 years:

`5,000 × 365 × 5,000 = 9,125,000,000 agent-days`

An LLM call per agent-day would therefore require billions of calls. Actual cost depends on population over time, activation frequency, context length and output length.

Start with Ollama. Consider another serving adapter, such as vLLM, if measured demand justifies batching and throughput work. Parallel inference must not let response arrival order determine simulation outcomes.

## Society outside the individual

World-level state may eventually represent households, lineages, settlements, organisations, cultures, languages, economies, laws, technologies and institutions.

These are candidate representations, not a required starting catalogue or progression tree. Shared rituals and beliefs could develop into group identity, specialised roles and institutional continuity. Software may recognise and represent that pattern once supported by behaviour.

Avoid automatic milestones such as “Year 150: unlock religion”. Distinguish researcher labels from structures that agents actually recognise and act upon.

## Learning versus model training

Ontolettes can learn through memories, beliefs, goals, relationships and changing context without modifying neural weights.

Later weight training is a separate workflow: export trajectories, curate/filter them, version the dataset, train an adapter/model, evaluate it, and accept or reject the new build.

The prospective target is “portray a person given their identity, memories, beliefs and circumstances”, rather than one separate fine-tuned model per Ontolette. Training feasibility must be benchmarked on actual hardware; do not infer it from inference success alone.

## Recommended build order

> The current working order, with status per step, is in [../plans/roadmap.md](../plans/roadmap.md). The list below is the original coarse proposal.

1. **Simulation design pass:** Compare time/scheduling options, cognition activation and representation of individual/social state.
2. **Foundation:** Package layout, configuration, typed contracts, ports and composition root.
3. **Vertical slice:** One Ontolette, one deterministic toy world, validated model action, resolved consequence, saved event and memory.
4. **Persistence and replay:** Migrations, journal, snapshots, recorded inference and resume support.
5. **Small social simulation:** A few individuals with independent memory, communication, relationships and goals.
6. **Lifecycle and transmission:** Birth, ageing, death, parenting and cultural/material transfer under explicit assumptions.
7. **Evaluation and scale:** Behavioural scenarios, fidelity-policy comparisons and measured throughput; expand time horizons gradually.
8. **World expansion:** Richer resources, settlements and representations of emergent social structures as justified.
9. **Training experiments:** Curated data and accepted model builds after the runtime produces useful trajectories.

Correctness and evaluation begin with the first slice and continue through these stages.
