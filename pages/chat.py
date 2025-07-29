import streamlit as st
from utils.wikipedia_utils import wikipedia_search
import datetime

def greet_user():
    hour = datetime.datetime.now().hour
    return "Good morning!" if hour < 12 else ("Good afternoon!" if hour < 18 else "Good evening!")

def chat_assistant():
    st.header("💬 AI Chat Assistant")

    for role, text in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(text)

    user_input = st.chat_input("Ask me anything...")
    if user_input:
        st.session_state.chat_history.append(("user", user_input))

        if any(word in user_input.lower() for word in ["hi", "hello", "hey"]):
            response = greet_user()
        elif "time" in user_input.lower():
            response = f"🕒 The current time is **{datetime.datetime.now().strftime('%H:%M:%S')}**"
        elif "date" in user_input.lower():
            response = f"📅 Today's date is **{datetime.datetime.now().strftime('%Y-%m-%d')}**"
        elif "calculate" in user_input.lower():
            try:
                expression = user_input.lower().replace("calculate", "").strip()
                result = eval(expression)
                response = f"🧮 **Result:** `{result}`"
            except:
                response = "⚠️ Sorry, I couldn't calculate that."
        else:
            page, response = wikipedia_search(user_input)
            if page and page.images:
                st.image(page.images[0], caption=page.title, use_column_width=True)

        st.session_state.chat_history.append(("assistant", response))
        with st.chat_message("assistant"):
            st.markdown(response)
