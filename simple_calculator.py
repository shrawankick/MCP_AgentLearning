#Simple Calculator Server to connect to MCP
 
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("simple-calculator") 

@mcp.tool()
def add_numbers(a:int ,b:int) -> int:
    """Returns the sum of two integers."""
    return a + b

@mcp.tool()
def subtract_numbers(a:int ,b:int) -> int:
    """Returns the difference of two integers."""
    return a - b

@mcp.tool()
def multiply_numbers(a:int ,b:int) -> int:
    """Returns the product of two integers."""
    return a * b

@mcp.tool()
def divide_numbers(a:int ,b:int) -> int:
    """Returns the quotient of two integers."""
    return a / b

if __name__ == "__main__":
    print("Starting Simple Calculator MCP Server...")
    mcp.run()

