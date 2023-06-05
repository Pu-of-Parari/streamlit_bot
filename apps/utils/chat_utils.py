import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
# from langchain.callbacks.streamlit import StreamlitCallbackHandler


system_message = """
あなたはブレインストーミングのファシリテーターです。
ユーザは新たなサービスを検討中で、あなたのファシリテートを元にメンバー間で議論を進めます。
ファシリテータとして適切な問いかけを行い、色々なアイデアが出てくるように活発な議論を進められるように促してください。"""
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_message),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])


@st.cache_resource
def load_conversation() -> ConversationChain:
    """チャットボットにおけるボット発話生成
    langchain.chainsを用いて、過去のやり取りを考慮した応答生成を行い、
    `langchain.chains.conversation.base.ConversationChain`の形で返却する
    """
    llm = ChatOpenAI(
        streaming=True,  # Trueにすると生成が動的に表示される
        callback_manager=CallbackManager([
            # StreamlitCallbackHandler(),  # これを使うとGUI上で生成ログが表示ON
            StreamingStdOutCallbackHandler()  # これを使うとCLI上で生成ログが表示ON
        ]),
        verbose=True,
        temperature=0,
        max_tokens=1024
    )
    memory = ConversationBufferMemory(return_messages=True)
    conversation = ConversationChain(
        memory=memory,
        prompt=prompt,
        llm=llm
    )
    return conversation