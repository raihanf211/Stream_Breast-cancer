import pickle
import numpy as np
import streamlit as st
from PIL import Image



## load save model
Model = pickle.load(open('breast_cancer_model.sav', 'rb'))

##import data
image = Image.open("breast.jpg")
st.image(image, use_column_width=True)

## judul web
st.title('Data Mining Prediksi Kanker Payudara Ganas atau Jinak ')
st.text('Muhammad Raihan Fadilah (201351086)')

## atribut
col1, col2, col3 = st.columns(3)

with col1:    
                 radius_mean = st.number_input('Input Nilai radius_mean')

with col2:
                texture_mean  = st.number_input('Input Nilai texture_mean')

with col3:
                perimeter_mean   = st.number_input('Input Nilai perimeter_mean')

with col1:
                area_mean  = st.number_input('Input Nilai area_mean ')

with col2:
                smoothness_mean  = st.number_input('Input Nilai smoothness_mean ')

with col3:
                 compactness_mean   = st.number_input('Input Nilai compactness_mean ')

with col1:
                concavity_mean = st.number_input('Input Nilai concavity_mean ')

with col2:
                concave_points_mean = st.number_input('Input Nilai concave points_mean ')

with col3:
                 symmetry_mean  = st.number_input('Input Nilai symmetry_mean')

with col1:
                 fractal_dimension_mean   = st.number_input(' Input Nilai fractal_dimension_mean ')

with col2:
                 radius_se  = st.number_input('Input Nilai radius_se')

with col3:
                texture_se  = st.number_input('Input Nilai texture_se ')

with col1:
                perimeter_se  = st.number_input('Input Nilai perimeter_se')

with col2:
                area_se  = st.number_input('Input Nilai area_se')

with col3:
                 smoothness_se   = st.number_input('Input Nilai smoothness_se')

with col1:
                compactness_se  = st.number_input('Input Nilai compactness_se ')

with col2:
                concavity_se  = st.number_input('Input Nilai concavity_se')

with col3:
                concave_points_se= st.number_input('Input Nilai concave points_se')

with col1:
                symmetry_se    = st.number_input('Input Nilai symmetry_se')

with col2:
                fractal_dimension_se  = st.number_input('Input Nilai fractal_dimension_se')

with col3:
                radius_worst   = st.number_input('Input Nilai radius_worst')

with col1:
                texture_worst   = st.number_input('Input Nilai texture_worst')

with col2:
                perimeter_worst = st.number_input('Input Nilai perimeter_worst')

with col3:
                area_worst  = st.number_input('Input Nilai area_worst')

with col1:
                smoothness_worst   = st.number_input('Input Nilai smoothness_worst')

with col2:
                compactness_worst = st.number_input('Input Nilai compactness_worst')

with col3:
                concavity_worst   = st.number_input('Input Nilai concavity_worst')

with col1:
                concave_points_worst   = st.number_input('Input Nilai concave points_worst ')

with col2:
                symmetry_worst = st.number_input('Input Nilai symmetry_worst')

with col3:
                fractal_dimension_worst   = st.number_input('Input Nilai fractal_dimension_worst')


# code untuk prediksi
Kanker_payudara_diagnosis ='' 

# Membuat tombol untuk prediksi
if st.button('Prediksi Kanker Payudara'):
    Kanker_Payudara_prediction = Model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])

    if(Kanker_Payudara_prediction[0] == 1):
        Kanker_payudara_diagnosis = 'Pasien terkena Kanker Payudara (Ganas)'
    else :
        Kanker_payudara_diagnosis = 'Pasien terkena Kanker Payudara (Jinak)'

    st.success(Kanker_payudara_diagnosis)