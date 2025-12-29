# MCP_AgentLearning 🚀

**A small experimental repository for learning and experimenting with Fast MCP (MCP server) integrations.** This repo contains small example MCP servers (tools) that demonstrate how to expose functions to an external controller (an LLM, automation agent, or custom client) using `fastmcp`.

---

## 🔍 Project Overview

- `simple_calculator.py` — A minimal MCP server that exposes basic math tools (`add`, `subtract`, `multiply`, `divide`). Great for testing and learning how to register and run synchronous tools.
- `Playwright_mcp.py` — An async MCP server exposing common Playwright browser automation actions (navigate, click, fill, screenshot, etc.). Useful for exploring browser automation from an MCP-controlled agent.
- `File_system_reader.py` — A small server to read and list files from a configurable base directory (protected to avoid directory traversal).
- `test.py` — placeholder for adding tests and examples.

---

## ✅ Goals

- Provide clear, runnable examples of MCP servers using `fastmcp`.
- Make it easy for others to run the examples locally and extend them.
- Document next steps to improve the project (tests, CI, docker, examples).

---

## Prerequisites

- **Python 3.10+** (3.11 recommended)
- Git
- On Windows: PowerShell (to use the recommended activation commands)

---

## Quick Start (Local)

1. Clone the repository

```bash
git clone <repo-url>
cd MCP_AgentLearning
```

2. Create & activate a virtual environment

- macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

- Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

- Windows (cmd)

```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

3. Install dependencies

```bash
pip install fastmcp
pip install playwright      # required only if you plan to use Playwright example
python -m playwright install   # installs browser binaries for Playwright
```

> Tip: Add a `requirements.txt` later to make installs reproducible.

---

## Running the examples

- Start the simple calculator MCP server

```bash
python simple_calculator.py
# you should see: "Starting Simple Calculator MCP Server..."
```

- Start the Playwright MCP server (requires Playwright and browsers installed)

```bash
python Playwright_mcp.py
```

- Start the File System Reader server

```bash
# Optionally set BASE directory (default: ./documents)
setx File_DirectoryReader "C:\\path\\to\\documents"
python File_system_reader.py
```

Each script will call `mcp.run()` and begin serving tools under the configured MCP name (example names: `simple-calculator`, `playwright-automation`, `file-system-reader`).

---

## Example: MCP Server Configuration (for external controller)

If you are using an external controller that starts MCP servers via a config file, a simple example JSON could look like this:

```json
{
  "mcpServers": {
    "simple-calculator": {
      "command": "C:\\path\\to\\python.exe",
      "args": ["E:\\MCP_AgentLearning\\simple_calculator.py"]
    }
  }
}
```

Notes:
- Prefer using a Python executable from the virtual environment to ensure dependency isolation.
- Use absolute paths for reliability.

---

## How to test / interact

- There is no example client in this repo yet — to test, you can:
  - Run a server locally and connect it from your preferred MCP-capable controller (LLM client or agent).
  - Add a small client script that uses your controller tooling or `fastmcp` client (see Fast MCP docs).
  - Write unit tests (recommended): import tool functions directly and validate their behavior.

Example quick test (local import for `simple_calculator` functions):

```python
from simple_calculator import add_numbers
assert add_numbers(2, 3) == 5
```

---

## Troubleshooting & Tips ⚠️

- "Module not found": ensure you activated the virtual environment and installed `fastmcp`.
- Playwright UI not opening: run `python -m playwright install` and confirm the browser binaries were installed.
- Path / permission issues with `File_system_reader`: set `File_DirectoryReader` environment variable to a safe base directory and ensure files exist.
- If tools return unexpected types (e.g., division returning float), check Python version and function signatures.

---

## Next action steps (short-term roadmap) 🔭

1. **Add `requirements.txt`** with pinned versions (e.g., `fastmcp`, `playwright`).
2. **Add unit tests** for each tool in `tests/` (use pytest) and a simple CI workflow (GitHub Actions) to run them.
3. **Add a simple client example** that connects to a running MCP server and calls tools.
4. **Add a CONTRIBUTING.md** and coding guidelines for contributors.
5. **Add logging and better error handling** in servers, and input validation for tools.
6. **Containerize** servers with a `Dockerfile` for reproducible runs and deployment testing.

---

## Contributing ✨

- Fork the repo, create a branch, add tests, and open a Pull Request.
- Keep changes small and include tests for new behavior.

---

## Files & Purpose

- `simple_calculator.py` — example synchronous MCP server (math tools).
- `Playwright_mcp.py` — example async MCP server (browser automation).
- `File_system_reader.py` — example file reading tools with a base directory guard.
- `test.py` — placeholder for future tests and example scripts.

---

## License & Author

This is a learning project. Add a license file (`LICENSE`) if you want to share it beyond personal/experimental use.

---
