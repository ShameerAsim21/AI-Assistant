import streamlit as st
from utils.session_utils import init_session
from pages.chat import chat_assistant
from pages.data_analysis import data_analysis
from pages.house_price import house_price_prediction
from pages.student_performance import student_performance_prediction
from pages.reminders import reminders_page
from pages.history import history_page

# ---------------- Dashboard ----------------
def dashboard():
    st.markdown("## 🤖 Welcome to AI Assistant!")
    st.write("""
    Your AI-powered assistant can help you with:
    - 💬 **Chat and query knowledge** (Wikipedia powered).
    - 📊 **Analyze and visualize your CSV data**.
    - 🏠 **Predict house prices** with a simple ML model.
    - 🎓 **Estimate student performance** using study data.
    - ⏰ **Set reminders** and track your session.
    - 📝 **Review your chat history anytime**.
    """)

# ---------------- Landing/Login Page ----------------
def login_screen():
    # Hide sidebar using CSS
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {display: none;}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Big title
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap" rel="stylesheet">
        <style>
        .title {
            text-align: center;
            font-size: 70px;
            font-family: 'Orbitron', sans-serif;
            font-weight: 900;
            color: #6A0DAD;
            margin-top: 20%;
        }
        </style>
        <div class="title">AI Assistant</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h4 style='text-align: center;'>Login to continue</h4>", unsafe_allow_html=True)

    # Login inputs
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login"):
            if email and password:
                st.session_state['logged_in'] = True
                st.session_state['user'] = email
                st.experimental_rerun()
            else:
                st.error("Please enter both email and password.")
    with col2:
        if st.button("Continue as Guest"):
            st.session_state['logged_in'] = True
            st.session_state['user'] = "Guest"
            st.experimental_rerun()

# ---------------- Main App ----------------
def main():
    init_session()

    if not st.session_state['logged_in']:
        # Only login page, no sidebar
        login_screen()
    else:
        # Show sidebar after login
        with st.sidebar:
            st.markdown(f"### Welcome, {st.session_state['user']}")
            menu = ["Main Dashboard", "Chat Assistant", "Data Analysis",
                    "House Price Prediction", "Student Performance Prediction",
                    "Reminders", "History"]
            choice = st.selectbox("Go to", menu)

            if st.button("Logout"):
                st.session_state['logged_in'] = False
                st.session_state.pop('user', None)
                st.experimental_rerun()

        # Routing
        if choice == "Main Dashboard":
            dashboard()
        elif choice == "Chat Assistant":
            chat_assistant()
        elif choice == "Data Analysis":
            data_analysis()
        elif choice == "House Price Prediction":
            house_price_prediction()
        elif choice == "Student Performance Prediction":
            student_performance_prediction()
        elif choice == "Reminders":
            reminders_page()
        elif choice == "History":
            history_page()

if __name__ == "__main__":
    main()
