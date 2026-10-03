# MDIA V2 — Provisional Technical Choices

**Status:** Provisional. These choices were recommended in the discussion; they are not all installed, implemented or newly verified. Convert to ADRs in [decisions/](decisions/) as they are confirmed.
**Date:** 2 October 2026

| Concern | Initial direction |
|---|---|
| Language and environment | Python 3.12 in WSL2 Ubuntu |
| Project management | `uv`, `pyproject.toml`, `src/` layout and committed lockfile |
| Architecture | Modular monolith with ports and adapters |
| Boundary contracts | Pydantic validation and JSON schemas |
| LLM integration | Model port; optional Pydantic AI behind that boundary |
| Local serving/model | Existing Ollama and `gpt-oss:20b` setup |
| Persistence | SQLite, SQLAlchemy and Alembic |
| Simulation scheduling | Evaluate custom scheduler, Mesa and SimPy |
| Testing | pytest; Hypothesis where stateful invariants justify it |
| Behavioural evaluation | Controlled scenarios, trajectory inspection and ablations |
| Observability | Structured logs/traces; OpenTelemetry is a candidate |
| Training | Separate later pipeline using curated trajectories |

Pydantic belongs at boundaries: observations, context packages, deliberations, action intents/results, memory candidates, reflections and goal updates. Schema-valid output still needs semantic validation against world rules.

Do not equate a library's model-call `Agent` object with an Ontolette. MDIA owns simulated identity and cognition orchestration.

## Links retained from the earlier discussion

These are reference links from the discussion, not a fresh verification of package versions or capabilities.

- [Python protocols](https://typing.python.org/en/latest/reference/protocols.html)
- [uv project guide](https://docs.astral.sh/uv/guides/projects/)
- [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/)
- [Pydantic AI](https://ai.pydantic.dev/)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [Event sourcing](https://martinfowler.com/eaaDev/EventSourcing.html)
- [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/20/)
- [Mesa event scheduling](https://mesa.readthedocs.io/latest/tutorials/3_event_scheduling.html)
- [SimPy documentation](https://simpy.readthedocs.io/)
- [vLLM documentation](https://docs.vllm.ai/)
- [OpenAI gpt-oss introduction](https://openai.com/index/introducing-gpt-oss/)
- [Hypothesis stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html)
- [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/)
- [Hugging Face PEFT](https://huggingface.co/docs/peft/index)
