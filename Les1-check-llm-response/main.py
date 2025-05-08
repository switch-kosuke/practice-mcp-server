from langchain_openai import AzureChatOpenAI


from langchain_ollama import ChatOllama
# llm = ChatOllama(model = "llama3")

# 環境変数に関するライブラリ
from dotenv import load_dotenv
import os
### APIキーの取得
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI



llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def get_llm_response(request : str) -> str:   
    prompt = llm.invoke(input = request)
    return prompt.content

if __name__ == "__main__":
    # LLMのレスポンスを確認する関数
    response = get_llm_response("こんにちは!")
    print(f"LLMのレスポンス: {response}")