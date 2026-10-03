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

Tests that call the local model are skipped by default. To run them (Ollama must be running):

```sh
MDIA_OLLAMA_TESTS=1 uv run pytest tests/integration
```

## Running a simulation

Run the tiny world (one Ontolette, Luma, beside a bush and a tree) against the local model and watch each turn as it completes (Ollama must be running):

```sh
uv run mdia --ticks 5
```

Each line shows the tick, the agent, what it saw, what it proposed, the world's verdict and how long the model took:

```text
tick 2 | luma | carrying 5; bush 0, tree 2 | gather 2 from tree | accepted | 7.1s
```

`uv run mdia --help` lists the options (model, Ollama URL, seed).
