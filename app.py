import streamlit as st
import pandas as pd
import pickle

# Load model
with open("electricity_overuse_pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

st.title("⚡ Electricity Overuse Predictor")

st.write("Enter your monthly usage details:")

# User inputs
fan = st.number_input("Fan usage (hours/day)", min_value=0)
refrigerator = st.number_input("Refrigerator usage (hours/day)", min_value=0)
ac = st.number_input("AC usage (hours/day)", min_value=0)
lights = st.number_input("Lights usage (hours/day)", min_value=0)
others = st.number_input("Other appliances usage (hours/day)", min_value=0)

state = st.selectbox("State", ["Gujarat", "Bihar", "Tamil Nadu", "Maharashtra", "Karnataka", "Punjab", "Delhi", "Rajasthan", "Haryana", "Uttar Pradesh"])
electricity_company = st.selectbox("Electricity Company", ["TANGEDCO", "PSPCL", "UGVCL", "SBPDCL", 
"MSEDCL", "PGVCL", "MESCOM", "AVVNL", "NBPDCL", "UHBVN", "Tata Power Mumbai", "DHBVN", "BESCOM", 
"Madhyanchal Vidyut Vitran", "JVVNL", "UPPCL", "Tata Power DDL", "BSES Yamuna", "BSES Rajdhani"])


if st.button("Predict"):
    input_df = pd.DataFrame({
        "fan": [fan],
        "refrigerator": [refrigerator],
        "ac": [ac],
        "lights": [lights],
        "others": [others],
        "state": [state],
        "electricity_company": [electricity_company]
    })

    prob = pipeline.predict_proba(input_df)[0][1]

    if prob >= 0.5:
        st.error(f"Ah shit here we go again, Overuse Expected (Probability: {prob:.2f})")
    else:
        st.success(f"Ye buddy, No Overuse Expected (Probability: {prob:.2f})")
