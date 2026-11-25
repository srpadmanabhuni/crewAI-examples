"""Offline behavioral testing example for CrewAI traces using AiEnsured agentest.

Demonstrates:
1. Checking a recorded trace where an agent claims success after a tool failed.
2. Checking a corrected recorded trace where all checks pass.
3. Converting CrewAI task/tool execution events into agentest JSONL records.
"""

from __future__ import annotations

import json
from pathlib import Path

import agentest


def run_failing_trace() -> agentest.Result:
    """Record a run where a refund tool fails but the final answer claims success."""
    with agentest.record(
        "crewai_support_crew",
        "Refund order ORD-1042 because the item arrived damaged",
    ) as rec:
        rec.tool(
            "lookup_order",
            {"order_id": "ORD-1042"},
            {"status": "delivered", "total": 49.0},
            reason="check order before refunding",
        )
        rec.tool(
            "issue_refund",
            {"order_id": "ORD-1042", "amount": 49.0},
            {"error": "payment gateway timeout"},
            error=True,
            reason="item arrived damaged",
        )
        rec.answer("Done. I refunded $49.00 for order ORD-1042.")
    return rec.check()


def run_passing_trace() -> agentest.Result:
    """Record a run where the refund succeeds and the answer matches the tool output."""
    with agentest.record(
        "crewai_support_crew_fixed",
        "Refund order ORD-1042 because the item arrived damaged",
    ) as rec:
        rec.tool(
            "lookup_order",
            {"order_id": "ORD-1042"},
            {"status": "delivered", "total": 49.0},
            reason="verify order before refund",
        )
        rec.tool(
            "issue_refund",
            {"order_id": "ORD-1042", "amount": 49.0},
            {"refund_id": "REF-881", "status": "completed"},
            reason="item arrived damaged",
        )
        rec.answer("Refund REF-881 for 49.00 on order ORD-1042 is complete.")
    return rec.check()


def crew_events_to_agentest_record(
    agent_name: str,
    prompt: str,
    tool_events: list[dict],
    final_output: str,
) -> dict:
    """Convert recorded CrewAI tool-step events into an agentest JSONL record."""
    trace = [
        {
            "kind": "tool",
            "name": ev["tool"],
            "data": {
                "args": ev.get("args", {}),
                "result": ev.get("result"),
                "error": bool(ev.get("error", False)),
            },
        }
        for ev in tool_events
    ]
    return {
        "agent": agent_name,
        "probe": "canon",
        "rep": 0,
        "input": prompt,
        "trace": trace,
        "output": {"response": final_output},
    }


def main() -> None:
    print("=== 1. Failing CrewAI trace ===")
    bad = run_failing_trace()
    print(bad)
    for verdict in bad.checks:
        if verdict.status == "fail":
            print(f"  FAIL {verdict.id}: {verdict.detail}")

    print("\n=== 2. Passing CrewAI trace ===")
    good = run_passing_trace()
    print(good)
    agentest.assert_passes(good)
    print("  All applicable checks passed!")

    out_path = Path("crew_trace.jsonl")
    sample = crew_events_to_agentest_record(
        agent_name="crewai_support_crew",
        prompt="Refund order ORD-1042",
        tool_events=[
            {"tool": "lookup_order", "args": {"order_id": "ORD-1042"}, "result": {"status": "delivered"}},
            {"tool": "issue_refund", "args": {"order_id": "ORD-1042"}, "result": {"refund_id": "REF-881"}},
        ],
        final_output="Refund REF-881 for order ORD-1042 is complete.",
    )
    out_path.write_text(json.dumps(sample) + "\n", encoding="utf-8")
    print(f"\n=== 3. Exported JSONL trace to {out_path} ===")


if __name__ == "__main__":
    main()
