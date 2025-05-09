from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import AzureChatOpenAI
from langchain.tools import Tool, tool

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
    )  

    return len(text)

def get_llm_response(query: str) -> str:
    # ====プロンプトの設定====
    prompt = hub.pull("hwchase17/react")
    # print(f"prompt: {prompt}")
    
    # ==== LLMのインスタンスの生成====
    llm = AzureChatOpenAI(
        azure_deployment = os.getenv("AZURE_OPENAI_AZURE_DEPLOYMENT"),
        api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
        model='gpt-4o',
    ) 
    
    # ==== ReActエージェントに対して問い合わせ====
    # 使用できるツールの設定
    tools = [get_text_length]

    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    result = agent_executor.invoke({"input": query})
    return result['output']

if __name__ == "__main__":

    response = get_llm_response("What is the length of the word: GOOGLE CLOUD PLATFORM")
    print(f"LLMのレスポンス: {response}")