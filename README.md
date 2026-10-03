# MDIA V2

Memory-Driven Identity Agent: a closed-world simulation of persistent simulated individuals (Ontolettes) exploring emergent identity, memory and society.

See [CLAUDE.md](CLAUDE.md) for the project summary, [docs/context/vision.md](docs/context/vision.md) for decisions and principles, and [docs/plans/roadmap.md](docs/plans/roadmap.md) for the build order.

## Development environment

MDIA V2 is developed on Windows using WSL2/Ubuntu as the primary environment. The repository, Python runtime, virtual environment and dependencies all live inside WSL, and the IDE connects to WSL, so running, debugging and dependency management happen in Linux rather than Windows.

Prerequisites:

- WSL2 with Ubuntu, with the repository cloned inside the WSL filesystem (not under `/mnt/c`).
- [uv](https://docs.astral.sh/uv/) for Python and dependency management. Python 3.12 is pinned in `.python-version`.
- [Ollama](https://ollama.com/) running locally with the `gpt-oss:20b` model pulled (`ollama pull gpt-oss:20b`). An NVIDIA GPU is exposed to WSL through the Windows NVIDIA driver, which Ollama uses for inference.

Setup and tests:

```sh
uv sync
uv run pytest
```
