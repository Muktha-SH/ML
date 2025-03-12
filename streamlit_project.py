import streamlit as st
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load the model
model_path = 'project_workout'  # Ensure model file name is correct
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model file not found. Please check the file path.")
    st.stop()

# App title
st.title("Calorie Coach: Your Personal Workout Analyzer")
st.write("Helping You Track, Analyze, and Achieve Your Fitness Goals")
'''
from PIL import Image
img = Image.open('/Users/muktha/Downloads/WhatsApp Image 2025-01-08 at 12.51.55 PM.jpeg')
st.image(img,width = 800)
'''

# Input grid
col1, col2, col3 = st.columns(3)

with col1:
    Gender = st.selectbox('Select your gender:', ['Male', 'Female'])  # Dropdown for predefined categories
    Age = st.number_input('Enter your age:', min_value=0, max_value=120, step=1)
    Duration = st.number_input('Enter workout duration (in minutes):', min_value=0, max_value=300, step=1)

with col2:
    Height = st.number_input('Enter your height (in cm):', min_value=50.0, max_value=250.0, step=0.1)
    Weight = st.number_input('Enter your weight (in kg):', min_value=10.0, max_value=200.0, step=0.1)

with col3:
    Heart_Rate = st.slider('Select your heart rate (in bpm):', min_value=30, max_value=220, value=75, step=1)
    Body_Temp = st.slider('Select your body temperature (in °C):', min_value=30.0, max_value=45.0, value=37.0, step=0.1)

# Encode gender
label_encoder = LabelEncoder()
gender_categories = ['Male', 'Female']
label_encoder.fit(gender_categories)
Gender_encoded = label_encoder.transform([Gender])[0]  # Encoded as a single value

# Predict button
if st.button('Check Prediction'):
    try:
        # Ensure the input is a 2D array
        input_data = [[Gender_encoded, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]]
        predicted = model.predict(input_data)
        st.success(f"woohoo!! you have burned {predicted[0]:.2f} calories,keep going 👏🏼.")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
