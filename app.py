import streamlit as st

import joblib as jl
import pandas as pd

model = jl.load('dtc_model.joblib')

st.set_page_config(page_title='Mid Test', layout='wide')

st.title('Weather Classification ⛅')
st.header('Using Decision Tree Classifier from Scikit-Learn', divider='violet')

precipitation = st.text_input('Precipitation', '')
temp_max = st.text_input('Maximum Temperature', '')
temp_min = st.text_input('Minimum Temperature', '')
wind = st.text_input('Wind Speed', '')

def predict():
    x = {
        'precipitation' : [precipitation],
        'temp_max' : [temp_max],
        'temp_min' : [temp_min],
        'wind' : [wind]
    }

    x = pd.DataFrame(x)

    model = jl.load('dtc_model.joblib')
    try:
        pred = model.predict(x)

        if pred == 0:
            result = 'Drizzle'
        elif pred == 1:
            result = 'Rain'
        elif pred == 2:
            result = 'Sun'
        elif pred == 3:
            result = 'Snow'
        elif pred == 4:
            result = 'Fog'
        else:
            st.error('Something Wrong')

        st.success(result)
    except:
        st.error('Something Wrong')

    

st.button('Predict', on_click=predict)