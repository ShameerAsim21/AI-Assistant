## AI Assistant (Streamlit-based)

An interactive AI-powered assistant built with **Streamlit**, designed to help users with:
- Natural Language Processing (chat & Wikipedia search)
- Data analysis and visualization
- Predictive modeling (House prices & Student performance)
- Session management (reminders & chat history)
- User authentication (login or guest mode)
- Firebase integration for persistence

---

Features

### 1. **AI Chat Assistant**
- Responds to greetings, time/date queries, and calculations.
- Fetches summarized information from Wikipedia.
- Interactive chat interface with chat bubbles.

### 2. **Data Analysis**
- Upload CSV files for analysis.
- View summary statistics.
- Create interactive visualizations (scatter plots) using Plotly.

### 3. **Predictive Modeling**
- **House Price Prediction**: Estimate house prices based on size and bedrooms using a simple ML model.
- **Student Performance Prediction**: Predict student scores based on study hours and attendance.

### 4. **Reminders & History**
- Add session-based reminders.
- View your chat history anytime.

### 5. **Authentication**
- Users can log in with email/password.
- Guest mode for temporary access.
- Firebase integrated for secure backend.

---

## Project Structure

```
AI-Assistant/
│
├── app.py                       # Main application entry point
├── pages/
│   ├── chat.py                  # Chat assistant functionality
│   ├── data_analysis.py         # Data analysis module
│   ├── house_price.py           # House price prediction module
│   ├── student_performance.py   # Student performance prediction
│   ├── reminders.py             # Reminders feature
│   └── history.py               # Chat history display
│
├── utils/
│   └── session_utils.py         # Handles session state initialization
│
├── firebase_key.json            # Firebase service account key (add manually)
├── requirements.txt             # List of dependencies
└── README.md                    # Project documentation
```

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ai-assistant.git
   cd ai-assistant
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Firebase key:
   - Download your `firebase_key.json` from your Firebase console.
   - Place it in the project root directory.

---

## Running the App

Run the following command:
```bash
python -m streamlit run app.py
```

The app will launch in your default browser at:
```
http://localhost:8501
```
---

## Notes
- Ensure your Firebase project is properly set up with Firestore and Authentication.
- The default "login" in this version is basic (for testing); integrate Firebase authentication for production.

-------------------------------
Code by: Muhammad Shameer Asim