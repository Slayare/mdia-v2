from mdia.domain.agents.identity import Ontolette


def test_identity_is_unaffected_by_later_changes_to_the_lists_it_was_built_from():
    traits, goals, beliefs = ["curious"], ["find food"], ["the bush has berries"]
    luma = Ontolette(id="luma", name="Luma", traits=traits, goals=goals, beliefs=beliefs)

    traits.append("reckless")
    goals.clear()
    beliefs[0] = "the bush is empty"

    assert luma == Ontolette(
        id="luma",
        name="Luma",
        traits=("curious",),
        goals=("find food",),
        beliefs=("the bush has berries",),
    )
