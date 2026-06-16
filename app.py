import streamlit as st

st.set_page_config(page_title="AI Customer Support Assistant")

st.title("🤖 AI Customer Support Assistant")

question = st.text_input("Ask a support question")

if question:

    q = question.lower()

    if "password" in q:
        st.success("""
To reset your password:

1. Click Forgot Password
2. Enter your registered email
3. Open the reset link sent to your email
4. Create a new password
        """)

    elif "login" in q:
        st.success("""
Login Troubleshooting:

1. Check your email and password
2. Turn off Caps Lock
3. Clear browser cache
4. Try logging in again
        """)

    elif "account locked" in q:
        st.success("""
Your account is temporarily locked.

Please wait 15 minutes and try again.
        """)

    else:
        st.warning(
            "I don't have information about that. Please contact support."
        )