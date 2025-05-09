# 環境変数に関するライブラリ
from dotenv import load_dotenv
import os
### APIキーの取得
load_dotenv()

from langchain_openai import AzureChatOpenAI

def get_llm_response(query : str) -> str: 
    # ==== LLMのインスタンスの生成====
    llm = AzureChatOpenAI(
        azure_deployment = os.getenv("AZURE_OPENAI_AZURE_DEPLOYMENT"),
        api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
        model='gpt-4o',
    )  
    
    # ==== LLMに対して問い合わせ====
    response = llm.invoke(input = query)
    return response.content

if __name__ == "__main__":
    # LLMのレスポンスを確認する関数
    response = get_llm_response("こんにちは!")
    print(f"LLMのレスポンス: {response}")