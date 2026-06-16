import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🤖",
    layout="wide"
)

# Configure Gemini API
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("Gemini API key not found. Please add GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()

# Initialize Model
try:
    model = genai.GenerativeModel("gemini-2.0-flash")
except Exception as e:
    st.error(f"Model Error: {e}")
    st.stop()

# Title
st.title("🤖 AI Customer Support Assistant")
st.markdown("Ask any customer support question and get AI-powered assistance.")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("### About")
    st.write(
        "This chatbot uses Google's Gemini AI to answer customer support questions."
    )

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User Input
prompt = st.chat_input("Type your question here...")

if prompt:

    # Save User Message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = model.generate_content(
                    f"""
                    You are a professional customer support assistant.

                    Guidelines:
                    - Be polite and professional.
                    - Give clear step-by-step instructions.
                    - Keep answers concise.
                    - If you do not know the answer, recommend contacting support.

                    Customer Question:
                    {prompt}
                    """
                )

                answer = response.text

            except Exception as e:
                answer = f"❌ Error: {str(e)}"

            st.write(answer)

            col1, col2 = st.columns(2)

            with col1:
                st.button("👍 Helpful")

            with col2:
                st.button("👎 Not Helpful")

    # Save Assistant Message
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
