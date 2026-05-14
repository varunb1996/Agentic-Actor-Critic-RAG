from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AdvancedAgenticRAG")


@mcp.tool()
def calculator(expression: str) -> str:

    return str(eval(expression))


if __name__ == "__main__":
    mcp.run()
