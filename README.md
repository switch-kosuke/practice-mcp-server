# MCPサーバー練習用コード

本コードは下記のQiita記事の実装コードです。  
先に記事をご覧ください。  

## 環境構築
1. リポジトリクローン
    ```bash
    git clone https://github.com/switch-kosuke/practice-mcp-server.git
    ```

2. `.env`ファイルを作成して、使用したいLLMモデルのAPIを記載:  
    筆者は、Azure OpenAI Servicesのモデルを使用しております.  
    ```bash
    cp .env.sample .env
    ```

3. Python開発環境は、uvを用います. インストールされていない方は以下を実行.  
    > 参考:  
    > [uvを使ってPython環境を効率的に管理！](https://qiita.com/piapepper/items/d48939dd42a7420efcd1)  

    #### Linux/Mac  
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh

    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```

    #### Windows
    ```bash
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

4. uvを使って依存関係をインストール  
    ```bash
    # 仮想環境を作成
    uv venv

    # 仮想環境を有効化（Linux/Mac）
    source .venv/bin/activate

    # 仮想環境を有効化（Windows）
    .venv\Scripts\activate

    # 依存関係をインストール
    uv pip install -e .
    ```