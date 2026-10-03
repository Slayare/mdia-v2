# Incremental Commits and Conventional Commit Names

**Status:** Confirmed way of working.

## Who commits

**Claude does not commit.** Do the work up to the point of a commit, then stop and give the user a commit message for what was done. The user reviews and commits.

## Shape of a commit

Each commit covers one specific thing and only that thing, plus its associated test. Prefer many small, independently understandable commits over one large one. If a change spans layers, split it by layer and do the layers in dependency order, one commit each.

Illustrative example (frontend, API, backend, DB), working from the bottom up:

1. DB migration
2. Backend service reads from the DB
3. API controller calls the service
4. Frontend calls the endpoint
5. Frontend component uses the data

For MDIA the equivalent order is usually: domain types/contracts, then the subsystem that uses them, then persistence, then wiring in `runtime/`. Each step is its own commit with its own tests.

## Workflow per piece of work

1. Agree the next single step (small enough for one commit).
2. Implement it with TDD ([tdd.md](tdd.md)).
3. Make sure the tests pass and nothing unrelated is changed.
4. Report what was done and suggest the commit message. Do not run `git commit`.
5. Wait for the user before starting the next step.

If a step turns out to need unrelated changes (a refactor, a fix elsewhere), say so and propose them as separate commits rather than folding them in.

## Commit message format

Use [Conventional Commits](https://www.conventionalcommits.org/): `type(scope): summary`

- Imperative, lowercase summary, no trailing full stop, ideally under about 72 characters.
- Add a body only when the *why* is not obvious from the summary.
- Mark breaking changes with `!` and a `BREAKING CHANGE:` footer.

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `build`, `ci`, `perf`.

Scope names the area touched so history is easy to trace. Proposed scopes mirror `src/mdia/`: `domain`, `contracts`, `cognition`, `simulation`, `models`, `memory`, `persistence`, `experiments`, `evaluation`, `runtime`, plus `docs` and `deps` where useful. Use a narrower scope when it helps (e.g. `simulation/time`).

Examples:

- `feat(domain): add Ontolette state and lifecycle status`
- `feat(simulation): resolve CHOP intent against world rules`
- `test(persistence): cover snapshot restore with event replay`
- `docs(ways-of-working): add tdd and commit conventions`
