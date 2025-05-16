from langgraph.prebuilt import create_react_agent
import mcp
import langchain_mcp_adapters.tools
import asyncio
from langchain_openai import AzureChatOpenAI

# 環境変数に関するライブラリ
from dotenv import load_dotenv
import os
### APIキーの取得
load_dotenv()

async def get_llm_response(query: str) -> str:
    llm = AzureChatOpenAI(
        azure_deployment = os.getenv("AZURE_OPENAI_AZURE_DEPLOYMENT"),
        api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
        model='gpt-4o',
    )

    # tools = [get_text_length]

    params = mcp.StdioServerParameters(
        command="path/to/uv",
        args=["run", "path/to/practice-mcp-server/Les3-Benefit-of-mcp-server/mcp-server.py"],
    )

    

    # MCP サーバを実行
    async with mcp.client.stdio.stdio_client(params) as (read, write):
        async with mcp.ClientSession(read, write) as session:
            await session.initialize()
            tools = await langchain_mcp_adapters.tools.load_mcp_tools(session)

            print(tools)

            agent = create_react_agent(llm, tools)
            agent_response = await agent.ainvoke({"messages": query})
            response = agent_response["messages"][-1].content
            return response

if __name__ == "__main__":
    # LLMのレスポンスを確認する関数
    response = asyncio.run(get_llm_response("What is the length of the word: GOOGLE CLOUD PLATFORM"))
    print(f"LLMのレスポンス: {response}")
    
