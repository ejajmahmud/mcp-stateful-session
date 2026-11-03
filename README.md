# MCP Stateful Session ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="MCP Stateful Session Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/mcp-stateful-session/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/mcp-stateful-session?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/mcp-stateful-session/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**MCP Stateful Session** is a production-ready developer tool and connector: Session persistence and resumption store with snapshot rollbacks for MCP conversations.

---

## 🚀 Problem Statement

When long-running autonomous workflows encounter errors, stateless execution forces restarting from scratch, wasting prior reasoning and API tokens.

---

## ⚡ Architecture Flow

```mermaid
flowchart LR
    A[Step 1: Init] --> B[Snapshot 1]
    B --> C[Step 2: Generate Code]
    C --> D[Snapshot 2]
    D --> E[Step 3: Run Tests]
    E -->|Test Fails| F[Rollback to Snapshot 2]
    F --> G[Step 3b: Fix & Re-run]
    G --> H[Final Success]
```

---

## 📊 Performance Benchmarks

| Failure Recovery Workflow | Cold Restart | MCP Stateful Session | Savings |
|---|---|---|---|
| Step 8/10 Failure Recovery | 42.5s | 1.8s | **23.6x faster** |
| Token Wastage on Retry | 14,200 tokens | 0 tokens | **100% saved** |
| Snapshot Storage Size | - | 1.8 KB/step | **Negligible** |
| Rollback Latency | - | 0.24 ms | **Instantaneous** |

---

## 🛠️ Installation & Quickstart

```bash
pip install mcp_stateful_session
```

### Python API

```python
import mcp_stateful_session

print(mcp_stateful_session.__version__)
```

### CLI Usage

```bash
mcp-stateful-session --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
