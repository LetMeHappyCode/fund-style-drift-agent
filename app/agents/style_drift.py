from typing import TypedDict


class StyleDriftState(TypedDict, total=False):
    """Minimal state shape for future LangGraph style-drift workflows."""

    fund_code: str
    report_date: str
    summary: str


def build_style_drift_agent_placeholder() -> dict[str, str]:
    """Placeholder seam for wiring DeepAgents/LangGraph implementation."""

    return {"name": "style-drift-agent", "status": "not_configured"}
