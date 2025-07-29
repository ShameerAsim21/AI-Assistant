import streamlit as st

def add_reminder(reminder):
    st.session_state['reminders'].append(reminder)
    st.success(f"Reminder added: {reminder}")

def show_reminders():
    if st.session_state['reminders']:
        st.write("### Your Reminders:")
        for r in st.session_state['reminders']:
            st.write(f"- {r}")
    else:
        st.info("No reminders set.")

def reminders_page():
    st.header("⏰ Reminders")
    reminder = st.text_input("Add a reminder:")
    if st.button("Add Reminder"):
        add_reminder(reminder)
    show_reminders()
