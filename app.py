import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="MindGuard AI", page_icon="🧠")

# --- JUDUL & TAMPILAN ---
st.title("🧠 MindGuard: Mental Health Tracker")
st.write("Deteksi dini tingkat stres Anda berdasarkan pola aktivitas digital.")

# --- SIMULASI MODEL (Supaya Langsung Jalan) ---
# Di aplikasi nyata, model ini akan dilatih dengan data historis
def load_model():
    # Data dummy untuk melatih model instan
    data = pd.DataFrame({
        'typing_speed': [45, 20, 50, 15, 35, 10],
        'social_media': [2, 7, 1, 8, 3, 9],
        'sleep_hours': [8, 4, 7, 3, 7, 2],
        'target': [0, 1, 0, 1, 0, 1] # 0=Normal, 1=Stres
    })
    model = RandomForestClassifier()
    model.fit(data[['typing_speed', 'social_media', 'sleep_hours']], data['target'])
    return model

model = load_model()

# --- INPUT PENGGUNA (Formulir Aplikasi) ---
st.subheader("Data Aktivitas Hari Ini")
with st.form("input_form"):
    typing = st.slider("Kecepatan Mengetik (WPM)", 10, 60, 40)
    social = st.number_input("Durasi Media Sosial (Jam)", 0, 24, 3)
    sleep = st.number_input("Durasi Tidur (Jam)", 0, 24, 7)
    
    submitted = st.form_submit_button("Analisis Kesehatan Mental")

# --- LOGIKA PREDIKSI ---
if submitted:
    prediction = model.predict([[typing, social, sleep]])
    
    st.divider()
    if prediction[0] == 1:
        st.error("⚠️ Peringatan: Tingkat stres Anda terdeteksi Tinggi.")
        st.write("Saran: Ambil waktu istirahat sejenak, lakukan meditasi, atau hubungi konselor.")
    else:
        st.success("✅ Kondisi Anda terlihat Normal.")
        st.write("Pertahankan pola hidup sehat dan istirahat yang cukup!")
