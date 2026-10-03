"""Ollama adapter: a LanguageModel served by a local Ollama instance, using structured output."""

from typing import Any

import httpx


class OllamaModel:
    def __init__(self, client: httpx.Client, model: str) -> None:
        self._client = client
        self._model = model

    def generate(self, prompt: str, schema: dict[str, Any]) -> str:
        response = self._client.post(
            "/api/generate",
            json={"model": self._model, "prompt": prompt, "format": schema, "stream": False},
        )
        response.raise_for_status()
        return response.json()["response"]
