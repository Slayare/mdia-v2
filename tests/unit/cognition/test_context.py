from mdia.cognition.context import build_prompt
from mdia.contracts.observations import Observation
from mdia.domain.agents.identity import Ontolette


def _on_one_line(text: str, *parts: str) -> bool:
    return any(all(part in line for part in parts) for line in text.splitlines())


def test_prompt_carries_the_identity_and_everything_observed():
    ada = Ontolette(
        id="ada",
        name="Ada",
        traits=["curious", "cautious"],
        goals=["find food"],
        beliefs=["the tree is barren"],
    )
    observation = Observation(inventory=3, stocks={"bush": 5, "tree": 2})

    prompt = build_prompt(ada, observation)

    for detail in ["Ada", "curious", "cautious", "find food", "the tree is barren"]:
        assert detail in prompt
    assert _on_one_line(prompt, "carrying", "3")
    assert _on_one_line(prompt, "bush", "5")
    assert _on_one_line(prompt, "tree", "2")
