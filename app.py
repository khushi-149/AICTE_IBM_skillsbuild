import streamlit as st
import joblib
import numpy as np  # Corrected import alias

# App title
st.title("💼 Salary Prediction App")

st.divider()

st.write("This app estimates the salary of employees based on years at the company and job rate.")

# Input fields
years = st.number_input("🕒 Enter the years at the company:", value=1, step=1, min_value=0)
jobrate = st.number_input("📈 Enter the job rate:", value=3.5, step=0.5, min_value=0.0)

# Feature vector
x = [years, jobrate]

# Load the trained model
model = joblib.load("Linearmodel.pkl")

st.divider()

# Prediction button
predict = st.button("🔮 Press the button to predict salary")

st.divider()

# Prediction logic
if predict:
    st.balloons()  # Fun effect!
    
    x1 = np.array([x])  # Convert input to numpy array for prediction
    prediction = model.predict(x1)  # Make prediction
    
    # Display result
    st.success(f"💰 Estimated Salary: **${prediction[0]:,.2f}**")
else:
    st.info("Please press the button above to make a prediction.")
