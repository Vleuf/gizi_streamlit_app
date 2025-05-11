import streamlit as st
import pandas as pd

# Konfigurasi
st.set_page_config(page_title="Perhitungan Nilai Gizi", layout="wide")

# Fungsi ganti halaman
def set_page(page_name):
    st.session_state.page = page_name
    

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("database_gizi.csv")

data = load_data()

# Inisialisasi halaman pertama
if "page" not in st.session_state:
    st.session_state.page = "beranda"

# ===================== BERANDA =====================
if st.session_state.page == "beranda":
    st.title("📘 Selamat Datang di Aplikasi Perhitungan Gizi")
    st.markdown("""
    Aplikasi ini membantu Anda menghitung total nilai gizi dari berbagai bahan pangan berdasarkan berat (gram) yang dimasukkan.

    ### Fitur:
    - Pilih beberapa bahan pangan
    - Masukkan jumlah dalam gram
    - Dapatkan total nilai kalori, protein, lemak, dan karbohidrat
    - Lihat detail per bahan

    ---  
    """)
    st.button("➡️ Mulai Perhitungan", on_click=set_page, args=("perhitungan",))

# ===================== PERHITUNGAN =====================
elif st.session_state.page == "perhitungan":
    st.title("Perhitungan Nilai Gizi Berdasarkan Bahan Pangan")
    st.button("🔙 Kembali ke Beranda", on_click=set_page, args=("beranda",))

    # Inisialisasi bahan
    if "bahan_count" not in st.session_state:
        st.session_state.bahan_count = 1
    if "bahan_inputs" not in st.session_state:
        st.session_state.bahan_inputs = [{} for _ in range(st.session_state.bahan_count)]

    # Tombol tambah/hapus
    col_add, col_remove = st.columns([1, 1])
    with col_add:
        if st.button("➕ Tambah Bahan"):
            st.session_state.bahan_count += 1
            st.session_state.bahan_inputs.append({})
    with col_remove:
        if st.button("➖ Hapus Bahan") and st.session_state.bahan_count > 1:
            st.session_state.bahan_count -= 1
            st.session_state.bahan_inputs.pop()

    st.markdown("---")

    # Input bahan dan gram
    input_bahan_gram = []
    for i in range(st.session_state.bahan_count):
        col1, col2 = st.columns([2, 1])
        with col1:
            bahan = st.selectbox(f"Pilih Bahan ke-{i+1}", [""] + data["Bahan"].tolist(), key=f"bahan_{i}")
        with col2:
            if bahan:
                gram = st.number_input("Jumlah (gram)", min_value=0.0, key=f"gram_{i}")
                input_bahan_gram.append((bahan, gram))

    # Tombol hitung
    if st.button("Hitung Total Gizi"):
        total = {"Kalori": 0, "Protein": 0, "Lemak": 0, "Karbohidrat": 0}
        hasil_detail = []

        for bahan, gram in input_bahan_gram:
            matching_rows = data[data["Bahan"] == bahan]
            if not matching_rows.empty and gram > 0:
                row = matching_rows.iloc[0]
                faktor = gram / 100
                total["Kalori"] += row["Kalori"] * faktor
                total["Protein"] += row["Protein"] * faktor
                total["Lemak"] += row["Lemak"] * faktor
                total["Karbohidrat"] += row["Karbohidrat"] * faktor

                hasil_detail.append({
                    "Bahan": bahan,
                    "Gram": gram,
                    "Kalori": row["Kalori"] * faktor,
                    "Protein": row["Protein"] * faktor,
                    "Lemak": row["Lemak"] * faktor,
                    "Karbohidrat": row["Karbohidrat"] * faktor,
                })

        st.subheader("Total Nilai Gizi:")
        for k, v in total.items():
            st.write(f"*{k}:* {v:.2f}")

        if hasil_detail:
            st.subheader("Detail Per Bahan:")
            st.dataframe(pd.DataFrame(hasil_detail)) 

