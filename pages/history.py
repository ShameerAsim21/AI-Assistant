import streamlit as st

def history_page():
    st.header("📝 Chat History")
    for role, text in st.session_state['chat_history']:
        st.write(f"**{role.capitalize()}:** {text}")
