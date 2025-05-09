from mcp.server.fastmcp import FastMCP

mcp = FastMCP("文字列の文字数を数えるMCPサーバー")

@mcp.tool()
def get_text_length(text: str) -> int:
    """
    テキストの文字数を取得するツール
    Args:
        text (str): 文字数を取得したいテキスト
    Returns:
        int: テキストの文字数
    """
    print(f"get_text_length enter with {text=}")
    text = text.strip("'\n").strip(
        '"'
    )  
    return len(text)

if __name__ == "__main__":
    print("Starting MCP server in stdio mode")
    mcp.run(transport="stdio")
    # mcp.run(transport="sse")