# MDIA V2 — Vision, Decisions and Principles

**Status:** Confirmed direction (decisions) plus guiding principles. Explicit user decisions take precedence over provisional recommendations in other docs.
**Date:** 2 October 2026

Related: [future-state.md](future-state.md) · [open-questions.md](open-questions.md) · [../architecture/overview.md](../architecture/overview.md)

## Quick reference

MDIA means **Memory-Driven Identity Agent**. MDIA V2 is a closed-world simulation framework exploring emergent artificial identity, memory, social behaviour and long-term civilisation dynamics.

The fundamental unit is an **Ontolette**: a persistent simulated individual whose behaviour develops through its own experiences, memories, goals, beliefs, preferences, personality and relationships. Many Ontolettes share a base cognitive model, but have independent state and subjective experiences.

The guiding principle is **emergence over scripting**. Provide foundational cognitive, biological, material and social mechanisms, then observe what develops through interaction. Complex behaviours, norms, culture and institutions should not appear because a script decides that society has reached the appropriate year.

**The LLM is a cognitive component. The simulation owns reality.** Ontolettes propose actions; world rules determine their consequences. MDIA explores identity-like behaviour without assuming its agents are conscious or sentient.

## Confirmed project direction

| Question | User decision | Architectural consequence |
|---|---|---|
| Primary goal | Populations interacting and changing over generations | Design for persistent individuals within a shared causal world |
| Starting scenario | Roughly three founders | Begin with a small population, then study descendants and society |
| Long-term ambition | Approximately 4,000–5,000 simulated years; earlier concept involved 4,000–5,000 people generated | Keep elapsed years, cumulative births and simultaneous population as separate quantities |
| Environment | Only their sandbox world, perceived as reality | Agents receive world observations and world actions; no real-PC or web capabilities |
| Models | Shared base model, independent identities and memory | One model plays many people using separate context and state |
| Deployment | Local first; expansion later | Start with the existing local model setup |
| Execution | Manually run on the current machine initially; dedicated hardware eventually | Support pause, persistence and resume before unattended operation |
| Mesa | Starting fresh; Mesa need not remain central | Evaluate it as a simulation implementation, not an architectural dependency |

**Scale clarification:** Thousands of people generated across an experiment does not necessarily mean thousands alive at once. The previous 5,000-agent examples illustrate a possible throughput challenge, not a settled concurrent population requirement.

## Architectural principles

1. **The world owns reality.** Agents perceive it and attempt actions within its constraints.
2. **Ontolettes own subjective experience.** Beliefs, memories and interpretations may be wrong.
3. **Identity belongs to persistent state**, rather than separate model weights per person.
4. **A shared cognitive model can portray many individuals.** Context must preserve separation between their knowledge and experiences.
5. **Meaningful cognition is activated by events and needs**, rather than an LLM call for every person on every tick.
6. **Routine behaviour should be cheap; consequential deliberation receives inference.** Fidelity policies must be evaluated for behavioural bias.
7. **Higher-order society should emerge where practical.** Represent what develops without predetermining its form.
8. **Meaningful causal changes should be observable**, with replay and reproducibility supported where possible.
9. **Knowledge can outlive individuals through transmission.** Descendants do not automatically receive a dead person's private memories.
10. **The sandbox defines the Ontolette's available world.** External computer tools are outside the current scope.
