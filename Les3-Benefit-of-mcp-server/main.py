from langchain import hub
# from langchain_community.llms import OpenAI
from langchain.agents import AgentExecutor, create_react_agent
import langchain.agents
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import Tool, tool
import mcp
import langchain_mcp_adapters.tools
import asyncio

# 環境変数に関するライブラリ
from dotenv import load_dotenv
import os
### APIキーの取得
load_dotenv()

async def get_llm_response(request: str) -> str:
    prompt = hub.pull("hwchase17/react")
    model = ChatOllama(model="llama3")
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    # tools = [get_text_length]

    params = mcp.StdioServerParameters(
        command="/root/.local/bin/uv",
        args=["run", "/home/practice-mcp-server/Les3-Benefit-of-mcp-server/mcp-server.py"],
    )

    # MCP サーバを実行
    async with mcp.client.stdio.stdio_client(params) as (read, write):
        async with mcp.ClientSession(read, write) as session:
            await session.initialize()
            tools = await langchain_mcp_adapters.tools.load_mcp_tools(session)

            print(tools)

            agent = create_react_agent(model, tools, prompt)
            agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

            result = await agent_executor.ainvoke({"input": "What is the length of the word: GOOGLE CLOUD PLATFORM"})
            print(f"STEP3 LLMの応答: {result['output']}\n")

if __name__ == "__main__":
    # LLMのレスポンスを確認する関数
    asyncio.run(get_llm_response("こんにちは!"))

    
import langchain_core.prompts
import langchain.agents
from langchain_google_genai import ChatGoogleGenerativeAI
# async def main():

#     # model = ChatOllama(model="llama3")
#     model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

#     # プロンプトを準備
#     prompt = hub.pull("hwchase17/react")
#     print(f"STEP0 LLMの応答: {prompt}\n")
#     prompt = langchain_core.prompts.chat.ChatPromptTemplate.from_template(
#     """Question: {input}
#     Thought: Let's think step by step.
#     Use one of registered tools to answer the question.
#     Answer: {agent_scratchpad}"""
#     )

#     print(f"STEP1 LLMの応答: {prompt}\n")

#     # MCP サーバ呼出の設定
#     params = mcp.StdioServerParameters(
#         command="/root/.local/bin/uv",
#         args=["run", "/home/practice-mcp-server/Les3-Benefit-of-mcp-server/mcp-server.py"],
#     )

#     # MCP サーバを実行
#     async with mcp.client.stdio.stdio_client(params) as (read, write):
#         async with mcp.ClientSession(read, write) as session:
#             await session.initialize()
#             tools = await langchain_mcp_adapters.tools.load_mcp_tools(session)

#             print(tools)
#             # エージェントを用意
#             agent = langchain.agents.create_tool_calling_agent(model, tools, prompt)
#             executor = langchain.agents.AgentExecutor(agent=agent, tools=tools, verbose=True)

#             query = "What is the length of the word: GOOGLE CLOUD PLATFORM"

#             # 推論を実行
#             output = await executor.ainvoke({"input": query})
#             print(output)

# asyncio.run(main())