import streamlit as st
import joblib
import numpy as np
import json

st.set_page_config(page_title="House Price Prediction", layout="centered")

@st.cache_resource
def load_model():
    return joblib.load("housepriceprediction.pkl")

@st.cache_data
def load_columns():
    with open("columns.json", "r") as f:
        return json.load(f)

model = load_model()
data = load_columns()

st.markdown("<h1 style='text-align: center;'>House Price Prediction</h1>", unsafe_allow_html=True)
st.image("https://i.postimg.cc/mrsQTCLz/hpp.gif", width=520)

all_columns = data['data_columns']
non_location_cols = ['total_sqft', 'bath', 'bhk']
location_columns = [col for col in all_columns if col not in non_location_cols]

area = st.number_input("__Area(Square Feet)__", min_value=300, max_value=10000, step=50)
bhk = st.selectbox("BHK", options=[1, 2, 3, 4, 5], index=0)
bath = st.selectbox("Bath Room", options=[1, 2, 3, 4, 5], index=0)
location = st.selectbox("Location", location_columns)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Predict Price"):
        try:
            loc_index = all_columns.index(location)
        except ValueError:
            loc_index = -1

        x = np.zeros(len(all_columns))
        x[0] = area
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1

        prediction = round(model.predict([x])[0], 2)

        st.markdown(
            f"<div style='color: green; font-weight: bold;'>Estimated House Price: ₹ {prediction} Lakhs</div>",
            unsafe_allow_html=True
        )
