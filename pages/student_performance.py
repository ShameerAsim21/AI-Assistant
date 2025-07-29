import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

def student_performance_prediction():
    st.header("🎓 Student Performance Prediction")
    st.write("Demo dataset (replaceable)")

    data = pd.DataFrame({
        'StudyHours': [1, 2, 3, 4, 5, 6],
        'Attendance': [60, 70, 75, 80, 85, 90],
        'Score': [50, 60, 65, 70, 80, 90]
    })

    X = data[['StudyHours', 'Attendance']]
    y = data['Score']
    model = LinearRegression()
    model.fit(X, y)

    hours = st.number_input("Study hours per day:", 0, 10, 2)
    attendance = st.number_input("Attendance (%):", 0, 100, 70)
    pred = model.predict([[hours, attendance]])[0]
    st.success(f"Predicted Score: {pred:.2f}")
