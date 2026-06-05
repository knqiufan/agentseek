# Skills

Curated skills for agent-assisted development with AgentSeek templates.

## Install

### All skills (recommended)

```bash
npx skills add ob-labs/agentseek --all --global
```

This installs every skill globally via symlink so they're available across all projects and agents. Updates via `npx skills update -g` take effect immediately.

### Specific skills

```bash
npx skills add ob-labs/agentseek --skill langsmith-trace --global --yes
npx skills add ob-labs/agentseek --skill langchain-dev-guide --global --yes
npx skills add ob-labs/agentseek --skill langchain-cn-models --global --yes
npx skills add ob-labs/agentseek --skill github-repo-cards --global --yes
```

### Specific agent only

```bash
npx skills add ob-labs/agentseek --all --global --agent claude-code
npx skills add ob-labs/agentseek --all --global --agent cursor
```

### Project-local (for shared repos)

```bash
npx skills add ob-labs/agentseek --all
```

Omit `--global` to install into the current project only.

### Standalone copies (CI / airgapped)

```bash
npx skills add ob-labs/agentseek --all --global --copy
```

## Available Skills

| Skill | Purpose |
|-------|---------|
| `langsmith-trace` | LangSmith CLI setup, tracing, and trace debugging for AgentSeek backends |
| `langchain-dev-guide` | Engineering pitfalls and verified fixes for LangChain/LangGraph |
| `langchain-cn-models` | Integrating Chinese LLM providers (Qwen, GLM, DeepSeek) with LangChain |
| `github-repo-cards` | Generate visual repo cards for documentation and social sharing |

## Update & Remove

```bash
npx skills update -g              # update all global skills
npx skills remove --all --global  # remove everything
```
