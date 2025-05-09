from langgraph.prebuilt import create_react_agent
from langchain.tools import Tool, tool
from langchain_openai import AzureChatOpenAI
import asyncio

# 環境変数に関するライブラリ
from dotenv import load_dotenv
import os
### APIキーの取得
load_dotenv()

@tool
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
    )  # stripping away non alphabetic characters just in case

    return len(text)

async def get_llm_response(query: str) -> str:
    # ==== LLMのインスタンスの生成====
    llm = AzureChatOpenAI(
        azure_deployment = os.getenv("AZURE_OPENAI_AZURE_DEPLOYMENT"),
        api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
        model='gpt-4o',
    ) 
    
    # ==== ReActエージェントに対して問い合わせ====
    # 使用できるツールの設定
    tools = [get_text_length]
    
    agent = create_react_agent(llm, tools)
    messages = agent.invoke({"messages": [("user", query)]})
    
    response = messages["messages"][-1].content
    return response

if __name__ == "__main__":
    # LLMのレスポンスを確認する関数
    response = asyncio.run(get_llm_response("What is the length of the word: GOOGLE CLOUD PLATFORM"))
    print(f"LLMのレスポンス: {response}")
    