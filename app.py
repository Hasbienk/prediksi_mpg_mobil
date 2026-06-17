import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="Prediksi Efisiensi Bahan Bakar",
    page_icon=":material/local_gas_station:",
    layout="centered"
)

model = joblib.load('model_mpg.pkl')

st.title("Prediksi Efisiensi Bahan Bakar Kendaraan")
st.caption("Model Machine Learning (Random Forest Regressor) — Dataset Auto MPG")

st.divider()

st.markdown("Masukkan spesifikasi teknis kendaraan untuk memprediksi konsumsi bahan bakarnya dalam satuan **MPG (Miles Per Gallon)**.")

st.write("")

with st.form("prediction_form"):
    st.subheader(":material/settings: Spesifikasi Mesin")
    col1, col2 = st.columns(2)

    with col1:
        cylinders = st.number_input(
            "Jumlah Silinder",
            min_value=2, max_value=12, value=4, step=1
        )
        displacement = st.number_input(
            "Displacement (cubic inches)",
            min_value=50.0, max_value=500.0, value=150.0
        )
        horsepower = st.number_input(
            "Horsepower (HP)",
            min_value=40.0, max_value=300.0, value=100.0
        )

    with col2:
        weight = st.number_input(
            "Berat Kendaraan (lbs)",
            min_value=1500, max_value=6000, value=3000, step=1
        )
        acceleration = st.number_input(
            "Akselerasi 0–60 mph (detik)",
            min_value=5.0, max_value=30.0, value=15.0
        )
        model_year = st.number_input(
            "Tahun Model (mis. 70 = 1970)",
            min_value=70, max_value=82, value=76, step=1
        )

    origin = st.selectbox(
        "Asal Negara Produksi",
        options=[1, 2, 3],
        format_func=lambda x: {1: "Amerika", 2: "Eropa", 3: "Asia"}[x]
    )

    submitted = st.form_submit_button(
        ":material/analytics: Prediksi MPG",
        use_container_width=True,
        type="primary"
    )

if submitted:
    input_data = np.array([[cylinders, displacement, horsepower, weight, acceleration, model_year, origin]])
    prediction = model.predict(input_data)[0]

    st.divider()
    st.subheader(":material/insights: Hasil Prediksi")

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Konsumsi Bahan Bakar", f"{prediction:.2f} MPG")
    with col_b:
        km_per_liter = prediction * 0.425144
        st.metric("Setara Km/Liter", f"{km_per_liter:.2f} km/L")
    with col_c:
        if prediction >= 30:
            kategori = "Efisien"
        elif prediction >= 20:
            kategori = "Sedang"
        else:
            kategori = "Kurang Efisien"
        st.metric("Kategori Efisiensi", kategori)

    st.caption("Catatan: prediksi dihasilkan oleh model Random Forest Regressor yang dilatih pada dataset Auto MPG (UCI Machine Learning Repository).")

st.write("")
st.divider()
st.caption("Dibuat sebagai bagian dari Project Studi Kasus Mata Kuliah Artificial Intelligence.")
