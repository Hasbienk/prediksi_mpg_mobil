import streamlit as st
import joblib
import numpy as np

model = joblib.load('model_mpg.pkl')

st.title("🚗 Prediksi Efisiensi Bahan Bakar Kendaraan (MPG)")
st.write("Masukkan spesifikasi mobil untuk memprediksi konsumsi bahan bakarnya (miles per gallon).")

cylinders = st.number_input("Jumlah Silinder", min_value=2, max_value=12, value=4, step=1)
displacement = st.number_input("Displacement / Volume Mesin (cubic inches)", min_value=50.0, max_value=500.0, value=150.0)
horsepower = st.number_input("Horsepower (HP)", min_value=40.0, max_value=300.0, value=100.0)
weight = st.number_input("Berat Kendaraan (lbs)", min_value=1500, max_value=6000, value=3000, step=1)
acceleration = st.number_input("Akselerasi (0-60 mph dalam detik)", min_value=5.0, max_value=30.0, value=15.0)
model_year = st.number_input("Tahun Model (contoh: 70 untuk 1970)", min_value=70, max_value=82, value=76, step=1)
origin = st.selectbox("Asal Negara", options=[1, 2, 3], format_func=lambda x: {1: "Amerika", 2: "Eropa", 3: "Asia"}[x])

if st.button("Prediksi MPG"):
    input_data = np.array([[cylinders, displacement, horsepower, weight, acceleration, model_year, origin]])
    prediction = model.predict(input_data)
    st.success(f"Prediksi Konsumsi Bahan Bakar: **{prediction[0]:.2f} MPG**")
