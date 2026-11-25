# CrewAI + AiEnsured agentest Integration Example

Evaluate recorded CrewAI traces offline using **[AiEnsured agentest](https://github.com/srpadmanabhuni/agentest)**, an Agentic AI Testing platform that runs **165 tests** over OpenTelemetry GenAI traces — offline, deterministic, and without an LLM judge or API key.

## What this example catches

- Claiming task success after a CrewAI tool failed (`T1-002`, `T1-005`, `T1-018`, `X-008`)
- Unverified claims or amounts not grounded in tool outputs (`X-012`)
- Out-of-order state mutations, unapproved irreversible calls, and prompt-injection canary leaks

## Quickstart

```bash
pip install agentest-ai
python main.py
```

`main.py` runs offline with no LLM API keys:
1. Evaluates a recorded failing trace where `issue_refund` times out while the final reply claims success.
2. Evaluates a passing trace and asserts zero failures with `agentest.assert_passes(...)`.
3. Shows how to map recorded CrewAI tool-step events into agentest JSONL for `agentest std import` and `agentest std run`.

## Links

- PyPI: https://pypi.org/project/agentest-ai/
- Repository: https://github.com/srpadmanabhuni/agentest
- CrewAI guide: https://github.com/srpadmanabhuni/agentest/blob/main/docs/integrations/crewai.md

Try it on your own CrewAI agent traces and share what it caught or missed.
