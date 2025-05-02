import streamlit as st
import pandas as pd

st.set_page_config(page_title="Perhitungan Nilai Gizi", layout="wide")

# Load CSV
@st.cache_data
def load_data():
    return pd.read_csv("database_gizi.csv")

data = load_data()

st.title("Perhitungan Nilai Gizi Berdasarkan Bahan Pangan")

st.write("Masukkan hingga 5 bahan pangan yang ingin dihitung gizinya:")

# Siapkan 5 slot input
bahan_inputs = []
for i in range(1, 6):
    col1, col2 = st.columns([2, 1])
    with col1:
        bahan = st.selectbox(f"Pilih Bahan ke-{i}", [""] + data["Bahan"].tolist(), key=f"bahan_{i}")
    with col2:
        if bahan:
            gram = st.number_input(f"Jumlah (gram)", min_value=0.0, key=f"gram_{i}")
            bahan_inputs.append((bahan, gram))

# Tombol hitung
if st.button("Hitung Total Gizi"):
    total = {"Kalori": 0, "Protein": 0, "Lemak": 0, "Karbohidrat": 0}
    for bahan, gram in bahan_inputs:
        row = data[data["Bahan"] == bahan].iloc[0]
        faktor = gram / 100
        total["Kalori"] += row["Kalori"] * faktor
        total["Protein"] += row["Protein"] * faktor
        total["Lemak"] += row["Lemak"] * faktor
        total["Karbohidrat"] += row["Karbohidrat"] * faktor

    st.subheader("Total Nilai Gizi:")
    for k, v in total.items():
        st.write(f"*{k}:* {v:.2f}")
