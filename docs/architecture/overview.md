# MDIA V2 — Architecture Overview

**Status:** Design direction (not an implementation specification). Principles live in [../context/vision.md](../context/vision.md); technology choices in [tech-choices.md](tech-choices.md); layout in [repo-structure.md](repo-structure.md).
**Date:** 2 October 2026

## Major subsystems

| Subsystem | Responsibility |
|---|---|
| Simulation kernel | Time, scheduling, world state, resources, environment rules and population lifecycle |
| Ontolette cognition | Perception, goals, beliefs, emotions, deliberation, planning and reflection |
| Cognition scheduler | Decide when cognition is needed, choose fidelity and manage inference requests |
| Memory | Working, episodic, semantic, social and autobiographical memory; retrieval and consolidation |
| Social systems | Relationships, communication, households, groups and persistent shared structures |
| Model infrastructure | Shared local inference behind a replaceable provider interface |
| Persistence and history | Events, snapshots, current read models and model trajectories |
| Experimentation and evaluation | Run configurations, invariants, behavioural scenarios and comparisons |
| Analysis and visualisation | Inspect individuals, lineages, relationships, world changes and long-term outcomes |

Use a **modular Python monolith** initially. Separate responsibilities through interfaces and data contracts without introducing microservices.

Ports and adapters remain useful for model inference, persistence, embeddings and simulation implementations. The simulation itself stays a first-class MDIA subsystem, rather than merely one arbitrary environment alongside desktop control.

## Agent decisions and world consequences

The cognitive workflow is:

1. Observe the world through the agent's available perception.
2. Retrieve relevant memories.
3. Build a bounded context package.
4. Deliberate when the cognition policy requires it.
5. Validate the proposed action's structure.
6. Let world rules resolve whether the action is possible and what happens.
7. Expose the appropriate outcome to the agent.
8. Form memories and update subjective state.
9. Reflect when warranted; schedule subsequent activity.

An engine orchestrates this workflow. The Ontolette is primarily state, rather than a giant class that also runs the database, world and model.

### Example: chopping a tree

An Ontolette proposes `ActionIntent(CHOP, tree_72)`. The world checks that the tree exists, the person can reach it, the required tool or capability is available, and the action's time and resource costs can be met.

Only world resolution may produce a result such as `tree_72 = FELLED`, wood gained and stamina spent. The agent's declaration does not make the event true. Its perceived outcome may also differ from complete objective state.

## Ontolette state

| State category | Candidate contents |
|---|---|
| Biology | Age, sex, health, hunger, fatigue and inherited traits |
| Identity | Personality, values, self-concept, preferences and worldview |
| Cognition | Goals, intentions, beliefs, emotional state and active thoughts |
| Memory | Working, episodic, semantic and autobiographical records |
| Social | Parents, children, kinship, relationships, reputation, groups and roles |
| Material | Possessions, home, resources and occupation |
| Spatial | Location and current activity |

Systems operate on this state. Persistent facts about the world and subjective claims held by an agent must remain distinguishable.

## Individual and cultural memory

| Memory concept | Example | Persistence mechanism |
|---|---|---|
| Working | Current concerns and active thoughts | Short-term agent context |
| Episodic | “My father taught me to fish.” | Personal experience records |
| Semantic | “This river floods after heavy rain.” | Learned knowledge or beliefs |
| Autobiographical/self-model | “Loyalty matters to me.” | Reflection and identity continuity |
| Social | “I trust Mara because she kept her promise.” | Subjective relationship knowledge |
| Cultural | Stories, skills, customs and shared beliefs | Teaching, imitation, conversation and artefacts |

The LLM receives a small relevant context package, not the entire memory store. Start with simple retrieval if adequate; embeddings and vector stores can be introduced behind an interface later.

Cultural transmission may change information: an event becomes an eyewitness account, then a story, oral tradition, legend or myth. Preserve provenance where useful so analysis can compare transmitted belief with recorded reality.

Private memories may remain archived for researcher inspection after death. That does not make them accessible to living Ontolettes.

Inheritance has separate possible channels:

- **Biological:** physique, health and predispositions.
- **Cultural:** language, skills, customs, beliefs, knowledge and stories acquired through transmission.
- **Material:** property, tools, resources and wealth transferred under world rules.

## Persistence, replay and observability

Use an initial **event-history-plus-snapshots** approach:

- Immutable events record meaningful causal changes.
- Snapshots provide practical restore points.
- Current tables/read models support inspection and queries.

Candidate tables include `runs`, `agents`, `events`, `snapshots`, `memories`, `relationships`, `model_calls`, `tool_calls` for any world capabilities, and `evaluations`. Treat this as a starting sketch, not a final schema.

Record model trajectories with run/agent/decision identifiers, model name and available digest, parameters, prompt version, request, retrieved memories, response, validated output, latency and available token counts.

A `RecordedModelAdapter` can return recorded outputs during debugging without new inference. Replay also requires controlled event ordering, random-number state, world rules and relevant version information; a seed alone does not guarantee identical LLM outputs.

Trace perception, retrieval, context construction, deliberation, validation, world resolution and memory updates. Keep simulation time distinct from inference wall-clock time.
