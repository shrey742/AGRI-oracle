import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Title
st.title("🌾 AGRI-oracle App(AI based crop yield predictor)")

# Description
st.write("""
Welcome! This app uses simple AI logic (Linear Regression) to predict **crop yield (kg/hectare)** 
based on rainfall, temperature, and area cultivated.
""")

# Input Fields
rainfall = st.number_input("Enter Rainfall (mm)", min_value=0.0)
temperature = st.number_input("Enter Temperature (°C)", min_value=-10.0)
area = st.number_input("Enter Area Cultivated (hectares)", min_value=0.0)

# Button to Predict
if st.button("Predict Yield"):
    # Dummy AI Model: Just for demonstration (normally trained on real data)
    # Example training data (rainfall, temperature, area) → yield
    X = np.array([[100, 25, 1], [200, 30, 2], [150, 27, 1.5]])
    y = np.array([2000, 4000, 3000])  # Example yields

    # Train the model
    model = LinearRegression()
    model.fit(X, y)

    # Make prediction
    input_data = np.array([[rainfall, temperature, area]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Crop Yield: {prediction[0]:.2f} kg")

# Footer
st.markdown("---")
st.caption("Developed by AI-innovators • Supporting SDG 2: Zero Hunger 🌍")