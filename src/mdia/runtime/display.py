"""Display: render run output for a person watching in the terminal."""

from mdia.contracts.trajectory import TurnRecord


def format_turn(record: TurnRecord) -> str:
    stocks = ", ".join(f"{node} {amount}" for node, amount in record.observation.stocks.items())
    seen = f"carrying {record.observation.inventory}; {stocks}"

    if record.intent is None:
        proposed = "no usable action"
        outcome = (record.error or "").partition("\n")[0]
    else:
        proposed = f"gather {record.intent.amount} from {record.intent.node_id}"
        outcome = "accepted" if record.result.accepted else f"rejected: {record.result.reason}"

    return f"tick {record.tick} | {record.agent_id} | {seen} | {proposed} | {outcome} | {record.latency_s:.1f}s"
