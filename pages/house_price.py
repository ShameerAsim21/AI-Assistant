import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

def house_price_prediction():
    st.header("🏠 House Price Prediction")
    st.write("Demo dataset (replace with your own)")

    data = pd.DataFrame({
        'Size': [1000, 1500, 2000, 2500, 3000],
        'Bedrooms': [2, 3, 3, 4, 4],
        'Price': [200000, 300000, 400000, 500000, 600000]
    })

    X = data[['Size', 'Bedrooms']]
    y = data['Price']
    model = LinearRegression()
    model.fit(X, y)

    size = st.number_input("Enter house size (sq ft):", 500, 5000, 1500)
    bedrooms = st.number_input("Number of bedrooms:", 1, 10, 3)
    pred = model.predict([[size, bedrooms]])[0]
    st.success(f"Estimated Price: ${pred:,.2f}")
