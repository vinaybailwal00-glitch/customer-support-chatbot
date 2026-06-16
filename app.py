import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Customer Support Assistant")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-pro")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Support Assistant")
    st.write("AI-powered customer support bot")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask your question")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = model.generate_content(
        f"""
        You are a professional customer support assistant.

        User Question:
        {prompt}

        Answer professionally and clearly.
        """
    )

    answer = response.text

    with st.chat_message("assistant"):
        st.write(answer)

        col1, col2 = st.columns(2)

        with col1:
            st.button("👍 Helpful")

        with col2:
            st.button("👎 Not Helpful")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
