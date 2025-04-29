import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Perhitungan Nilai Gizi Berdasarkan Bahan Pangan")

# Load data dari CSV
@st.cache_data
def load_data():
    return pd.read_csv("database_gizi.csv")

data = load_data()

# Pilih bahan pangan
bahan_pilihan = st.selectbox("Pilih Bahan Pangan:", data["Bahan"].tolist())

# Input jumlah dalam gram
jumlah = st.number_input("Masukkan jumlah (dalam gram):", min_value=1.0, step=1.0)

# Tombol hitung
if st.button("Hitung Nilai Gizi"):
    info = data[data["Bahan"] == bahan_pilihan].iloc[0]
    faktor = jumlah / 100
    kalori = info["Kalori"] * faktor
    protein = info["Protein"] * faktor
    lemak = info["Lemak"] * faktor
    karbo = info["Karbohidrat"] * faktor

    st.subheader(f"Hasil Perhitungan untuk {jumlah}g {bahan_pilihan}")
    st.write(f"*Kalori:* {kalori:.2f} kkal")
    st.write(f"*Protein:* {protein:.2f} g")
    st.write(f"*Lemak:* {lemak:.2f} g")
    st.write(f"*Karbohidrat:* {karbo:.2f} g")
