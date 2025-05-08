from langchain import hub
# from langchain_community.llms import OpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain_ollama import ChatOllama
from langchain.tools import Tool, tool

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

def get_llm_response(request: str) -> str:
    prompt = hub.pull("hwchase17/react")
    print(f"prompt: {prompt}")
    model = ChatOllama(model="llama3")
    tools = [get_text_length]

    agent = create_react_agent(model, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    result = agent_executor.invoke({"input": "What is the length of the word: GOOGLE CLOUD PLATFORM"})
    print(f"STEP3 LLMの応答: {result['output']}\n")

if __name__ == "__main__":
    # LLMのレスポンスを確認する関数
    response = get_llm_response("こんにちは!")
    print(f"LLMのレスポンス: {response}")