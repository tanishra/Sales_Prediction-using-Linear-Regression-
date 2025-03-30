import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("sales_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the input feature scaler (X)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Streamlit UI
st.title("📈 Sales Prediction App")
st.markdown("Predict sales based on TV, Radio, and Newspaper ad spend using Multiple Linear Regression.")

# User input fields
tv = st.number_input("Enter TV Ad Spend ($)", min_value=0.0, step=0.1, value=100.0)
radio = st.number_input("Enter Radio Ad Spend ($)", min_value=0.0, step=0.1, value=50.0)
newspaper = st.number_input("Enter Newspaper Ad Spend ($)", min_value=0.0, step=0.1, value=30.0)

# Prediction Button
if st.button("Predict Sales 🚀"):
    # Convert input to array
    input_data = np.array([[tv, radio, newspaper]])

    # Normalize input data using the same scaler as training
    input_data_scaled = scaler.transform(input_data)

    # Predict using the trained model
    prediction_scaled = model.predict(input_data_scaled)

    # Display result
    st.success(f"📊 Predicted Sales: **${prediction_scaled[0]:,.2f}**")

# Footer
st.markdown("---")
st.markdown("Developed by **Tanish Rajput** | Powered by **Streamlit & Machine Learning** 🚀")
