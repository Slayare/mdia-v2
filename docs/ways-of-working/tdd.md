# Test-Driven Development

**Status:** Confirmed way of working.

Use the test to frame what the logic needs to do. Follow red-green-refactor:

1. **Red:** Write a failing test that describes one specific behaviour. Run it and confirm it fails for the expected reason (not an import error or typo).
2. **Green:** Write the minimum code that makes it pass. Do not add behaviour the test does not ask for.
3. **Refactor:** Clean up the implementation and the test with the suite green. Do not change behaviour here.

## Rules of thumb

- One behaviour per cycle. If a test needs several unrelated assertions to describe the change, the step is too big.
- Tests and the code they drive belong to the same unit of work (and the same commit; see [incremental-commits.md](incremental-commits.md)).
- Run the relevant tests after each step and report the actual result, including failures.
- Fix bugs by first writing a test that reproduces them.
- Test categories and what each is for (software, replay, behavioural, experimental) are in [testing.md](testing.md).
- In this project, world-rule invariants (e.g. dead agents cannot act, resources cannot go negative) are good first tests: they pin down what the simulation owns before any model is involved.
