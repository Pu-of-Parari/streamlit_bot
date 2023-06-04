# streamlit_bot

StreamlitとOpenAI APIを使ったチャットボット開発


## Settings
環境設定方法について

- 前提:
    - poetryがインストールされていること
- 環境準備
    1. 本リポジトリをgit cloneする
        ```
        $ git clone https://github.com/Pu-of-Parari/streamlit_bot.git
        $ cd streamlit_bot
        ```
    2. パッケージ類をインストールする
        ```
        $ poetry config virtualenvs.create false
        $ poetry use env use 3.9
        $ poetry install
        ```

## Run
アプリの起動方法について

- ローカルでの起動方法
    ```
    $ cd apps
    $ poetry run streamlit run home.py
    ```
- Dockerコンテナによる起動方法
    - TBW...