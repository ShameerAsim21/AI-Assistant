import streamlit as st

def init_session():
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    if 'reminders' not in st.session_state:
        st.session_state['reminders'] = []
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'theme' not in st.session_state:
        st.session_state['theme'] = "Light"
