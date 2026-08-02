import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Crop Dictionary
crop_dict = {
    1: "Rice",
    2: "Maize",
    3: "Jute",
    4: "Cotton",
    5: "Coconut",
    6: "Papaya",
    7: "Orange",
    8: "Apple",
    9: "Muskmelon",
    10: "Watermelon",
    11: "Grapes",
    12: "Mango",
    13: "Banana",
    14: "Pomegranate",
    15: "Lentil",
    16: "Blackgram",
    17: "Mungbean",
    18: "Mothbeans",
    19: "Pigeonpeas",
    20: "Kidneybeans",
    21: "Chickpea",
    22: "Coffee"
}

st.title("Crop Recommendation System")

# User Inputs
N = st.number_input("Nitrogen")
P = st.number_input("Phosphorus")
K = st.number_input("Potassium")
temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
ph = st.number_input("pH")
rainfall = st.number_input("Rainfall")

# Prediction Button
if st.button("Predict"):

    features = pd.DataFrame(
        [[N, P, K, temperature, humidity, ph, rainfall]],
        columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    )

    transformed_features = scaler.transform(features)

    prediction = model.predict(transformed_features)[0]

    st.success(f"Recommended Crop : {crop_dict[prediction]}")



