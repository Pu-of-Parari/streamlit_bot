import streamlit as st
from streamlit_chat import message

from utils.load_config import load_openai_key
from utils.chat_utils import load_conversation


load_openai_key("../config.ini")

if "generated" not in st.session_state:
    st.session_state.generated = []
if "past" not in st.session_state:
    st.session_state.past = []

st.title("ブレスト支援Botくん")

with st.form("Botくんにブレインストーミングの進行をしてもらいましょう"):
    user_message = st.text_area("発言記録を記入してください")
    submitted = st.form_submit_button("Send")

    if submitted:
        conversation = load_conversation()
        answer = conversation.predict(input=user_message)

        st.session_state.past.append(user_message)
        st.session_state.generated.append(answer)

        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])):
                # user
                message(
                    st.session_state['past'][i],
                    is_user=True,
                    key=str(i) + "_user",
                    avatar_style="thumbs",
                    seed=10
                )

                # bot
                message(
                    st.session_state['generated'][i],
                    key=str(i),
                    avatar_style="shapes",
                    seed=10
                )
