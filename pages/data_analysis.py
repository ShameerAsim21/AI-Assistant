import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def data_analysis():
    st.header("📊 Data Analysis & Visualization")
    file = st.file_uploader("Upload your CSV file", type=['csv'])
    if file:
        df = pd.read_csv(file)
        st.write("### Data Preview", df.head())
        st.write("### Statistical Summary")
        st.write(df.describe())

        st.write("### Interactive Visualization")
        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
        if numeric_cols:
            x_axis = st.selectbox("Select X-axis", numeric_cols)
            y_axis = st.selectbox("Select Y-axis", numeric_cols)
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
            st.plotly_chart(fig)
        else:
            st.info("No numeric columns for visualization.")
