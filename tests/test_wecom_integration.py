"""Regression checks for the bundled upstream WeCom integration."""

from __future__ import annotations

import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WECOM_SOURCE = {
    "git": "https://github.com/bubbuild/bub-contrib.git",
    "rev": "d9f177145b45d67cc0ca4703a495f062df8e3c32",
    "subdirectory": "packages/bub-wecom",
}


def test_wecom_plugin_is_pinned_to_the_upstream_adapter() -> None:
    """Keep AgentSeek on Bub's maintained channel instead of an in-tree fork."""
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert "bub-wecom" in pyproject["dependency-groups"]["plugins"]
    assert pyproject["tool"]["uv"]["sources"]["bub-wecom"] == WECOM_SOURCE


def test_wecom_env_docs_cover_native_credentials_and_access_policies() -> None:
    env_example = (ROOT / ".env.example").read_text(encoding="utf-8")

    for name in (
        "BUB_WECOM_BOT_ID",
        "BUB_WECOM_SECRET",
        "BUB_WECOM_WEBSOCKET_URL",
        "BUB_WECOM_DM_POLICY",
        "BUB_WECOM_ALLOW_FROM",
        "BUB_WECOM_GROUP_POLICY",
        "BUB_WECOM_GROUP_ALLOW_FROM",
    ):
        assert name in env_example
    assert "AGENTSEEK_WECOM_" not in env_example
