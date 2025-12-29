import os 
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("file-system-reader")

BASE_DIR = Path(os.getenv("File_DirectoryReader","./documents "))

# Read file content
@mcp.tool()
def read_file(file_path: str) -> str:
    "Read file from the document or any directory."

    try:
        file_path = BASE_DIR / file_path
        if not str(file_path).startswith(str(BASE_DIR.resolve())):
            return "Error: Access denied: invalid path."
        
        content = file_path.read_text(encoding="utf-8")
        return f"file:{file_path}\n\n{content}"
    except Exception as e:
        return f"Error reading file: {e}"

#
# List files in a directory    
@mcp.tool()
def list_files(directory: str = ".") -> str:
    "List files in a directory."

    try:
        dir_path = BASE_DIR / directory
        if not str(dir_path).startswith(str(BASE_DIR.resolve())):
            return "Error: Access denied: invalid path."

        files = [f for f in dir_path.iterdir() if f.is_file()]
        return "\n".join([f.name for f in files])
    except Exception as e:
        return f"Error listing files: {e}"
    

if __name__ == "__main__":
    print("Starting File System Reader MCP Server...")
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    mcp.run()