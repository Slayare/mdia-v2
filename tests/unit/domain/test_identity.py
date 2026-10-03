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


def test_identity_starts_at_version_one_unless_given_a_later_version():
    first = Ontolette(id="luma", name="Luma", traits=[], goals=[], beliefs=[])
    revised = Ontolette(id="luma", name="Luma", traits=[], goals=["find shelter"], beliefs=[], version=2)

    assert (first.version, revised.version) == (1, 2)
