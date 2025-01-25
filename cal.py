import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("height in ins" , 100 , 250 , 175)
weight = st.slider("weight in pound" , 40 , 200 , 70)

bmi = weight / ((height / 100) ** 2)
st.write(f"BMI is {bmi :2f}")

st.title("$$$ categories $$$")
st.write("-uderweight:  BMI less than 18.5")
st.write("-Normal weight : BMI between 18.5 and 24.9 ")
st.write("-OverWeight :  BMI between 25.9 and 29.9")
st.write("-Obesity :  BMI 30 or greator")