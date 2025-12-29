# MCP_AgentLearning

This is mainly to learn about how we configure the MCP server and we are trying to use Fast MCP 2.0

`pip install fastmcp`

Creating a virtual environment
python -m venv .venv

Running a virtual environment
source .venv/bin/activate
If we find some errors, maybe this would be a workaround
.\.venv\Scripts\Activate.ps1

And then with the code that is available in our repository. So we have started using the simple_calculator.py and we have defined it in the MCP servers inside the Claude.
```
{
  "mcpServers": {
    "simple-calculator": {
      "command": "C:\\Users\\shraw\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
      "args": [
        "E:\\MCP_AgentLearning\\simple_calculator.py"
      ]
    }
  }
}
```