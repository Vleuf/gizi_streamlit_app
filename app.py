import streamlit as st
import pandas as pd

# Set up the page configuration
st.set_page_config(page_title="Perhitungan Nilai Gizi", layout="wide")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("database_gizi.csv")

data = load_data()

# Perhitungan Nilai Gizi
if page == "Perhitungan Nilai Gizi":
    st.title("Perhitungan Nilai Gizi Berdasarkan Bahan Pangan")

    st.write("Masukkan bahan pangan yang ingin dihitung gizinya:")

    # Cek jika 'bahan_inputs' sudah ada di session state, jika belum, buat list kosong
    if 'bahan_inputs' not in st.session_state:
        st.session_state.bahan_inputs = []

    # Fungsi untuk menambah bahan input
    def add_input():
        st.session_state.bahan_inputs.append(("", 0))

    # Fungsi untuk menghapus bahan input
    def remove_input(index):
        del st.session_state.bahan_inputs[index]

    # Tombol untuk menambah bahan input
    add_button = st.button("Tambah Bahan Pangan", on_click=add_input)

    # Menampilkan input bahan pangan yang bisa ditambah atau dikurangi
    for idx, (bahan, gram) in enumerate(st.session_state.bahan_inputs):
        col1, col2 = st.columns([2, 1])
        with col1:
            bahan = st.selectbox(f"Pilih Bahan ke-{idx + 1}", [""] + data["Bahan"].tolist(), key=f"bahan_{idx}")
        with col2:
            if bahan:
                gram = st.number_input(f"Jumlah (gram)", min_value=0.0, key=f"gram_{idx}")
                st.session_state.bahan_inputs[idx] = (bahan, gram)

        # Tombol untuk menghapus bahan input
        if len(st.session_state.bahan_inputs) > 1:
            remove_button = st.button(f"Hapus Bahan {idx + 1}", key=f"remove_{idx}", on_click=remove_input, args=(idx,))

    # Tombol hitung
    if st.button("Hitung Total Gizi"):
        total = {"Kalori": 0, "Protein": 0, "Lemak": 0, "Karbohidrat": 0}
        for bahan, gram in st.session_state.bahan_inputs:
            if bahan:
                row = data[data["Bahan"] == bahan].iloc[0]
                faktor = gram / 100
                total["Kalori"] += row["Kalori"] * faktor
                total["Protein"] += row["Protein"] * faktor
                total["Lemak"] += row["Lemak"] * faktor
                total["Karbohidrat"] += row["Karbohidrat"] * faktor

        st.subheader("Total Nilai Gizi:")
        for k, v in total.items():
            st.write(f"*{k}:* {v:.2f}")
