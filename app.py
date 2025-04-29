import streamlit as st
import pandas as pd

# Load database
df = pd.read_csv("foods.csv")

st.set_page_config(page_title="Perhitungan Nilai Gizi", layout="centered")

st.title("Perhitungan Nilai Gizi Berdasarkan Bahan Pangan")

# Pilih bahan pangan
bahan = st.selectbox("Pilih Bahan Pangan", df["nama"])
jumlah = st.number_input("Masukkan jumlah (gram)", min_value=1.0, value=100.0, step=10.0)

# Ambil data dari database
data_bahan = df[df["nama"] == bahan].iloc[0]

# Hitung nilai gizi per jumlah yang dimasukkan
kalori = data_bahan["kalori"] * jumlah / 100
protein = data_bahan["protein"] * jumlah / 100
lemak = data_bahan["lemak"] * jumlah / 100
karbo = data_bahan["karbohidrat"] * jumlah / 100

# Tampilkan hasil
st.subheader("Hasil Perhitungan")
st.write(f"**{bahan.capitalize()} ({jumlah} gram)**")
st.write(f"- Kalori: **{kalori:.2f}** kkal")
st.write(f"- Protein: **{protein:.2f}** gram")
st.write(f"- Lemak: **{lemak:.2f}** gram")
st.write(f"- Karbohidrat: **{karbo:.2f}** gram")
