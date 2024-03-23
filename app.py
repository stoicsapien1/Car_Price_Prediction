import pandas as pd
import datetime
import streamlit as st
import sklearn
from sklearn.ensemble import GradientBoostingRegressor as xgb
import pickle
import joblib
model = joblib.load("Car_Price_Predictor")

st.markdown("""
    <div style="display: flex; justify-content: center;">
        <h1 style="color: #007BFF; font-family: 'Arial', sans-serif;">
            Car Price Prediction Using ML 🚗
        </h1>
    </div>
""", unsafe_allow_html=True)

image_url = "https://i.postimg.cc/NGTfM6Rn/Car-pic.jpg"

# Center the image using CSS
st.markdown(
    f'<div style="display: flex; justify-content: center;">'
    f'<img src="{image_url}" width="200" style="max-width:50%;">'
    f'</div>',
    unsafe_allow_html=True
)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
st.write(" ")
st.write('''Are you planning to sell your car? 🚗

Are you worried about its resale value? Then you can use this web app to find out its resale value!''')
st.write(" ")
p1=st.number_input("[1] What is the ex-showroom proce of the Car(In Lakhs)",2.5,25.0,step=1.0)
p2=st.number_input("[2] What is distance completed by Car in kilometers?",100,100000,step=100)
s1=st.radio('[3] What is the Fuel-Type?', options=['Petrol', 'Diesel', 'CNG'], 
          horizontal=True)
if s1=="Petrol":
    p3=0
elif s1=="Diesel":
    p3=1
elif s1=="CNG":
    p3=2
s2=st.radio('[4] Are you Dealer or Individual?', options=["Dealer","Individual"])
if s2=="Dealer":
    p4=0
elif s2=="Individual":
    p4=1
s3=st.radio('[5] What is the transmission Type?', options=["Manual","Automatic"])
if s3=="Manual":
    p5=0
elif s3=="Automatic":
    p5=1
p6=st.slider("[6] Number of owners the car previolusly had?",0,3)
date_time=datetime.datetime.now()
years=st.number_input("[7] In which year Car was purchased?",1990,date_time.year)
p7=date_time.year-years


def predict_price(p1, p2, p3, p4, p5, p6, p7):
    input_features = [[p1, p2, p3, p4, p5, p6, p7]]
    prediction = model.predict(input_features)
    return round(prediction[0],2)

# Add Predict button
if st.button('Predict'):
    predicted_price = predict_price(p1, p2, p3, p4, p5, p6, p7)
    st.write(f"Predicted car price (in Lakhs): {predicted_price}")
st.write(" ")
st.write(" ")
st.write("Made with ❤️ by Belal Ahmed Siddiqui")