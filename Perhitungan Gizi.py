import streamlit as st
import pandas as pd
import time

# Konfigurasi
st.set_page_config(page_title="Perhitungan Nilai GIZI", layout="wide")

# Fungsi ganti halaman
def set_page(page_name):
    st.session_state.page = page_name
    if page_name == "perhitungan":
        st.balloons()  # 🎈 Efek balon saat pindah ke halaman perhitungan
    elif page_name == "beranda":
        st.balloons()  # 🎈 Efek balon saat kembali ke beranda

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("database_gizi.csv")

data = load_data()

# Inisialisasi halaman pertama
if "page" not in st.session_state:
    st.session_state.page = "beranda"

# Inisialisasi bahan
if "bahan_count" not in st.session_state:
    st.session_state.bahan_count = 1
if "bahan_inputs" not in st.session_state:
    st.session_state.bahan_inputs = [{} for _ in range(st.session_state.bahan_count)]

# CSS Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
                    url('https://images.pexels.com/photos/4551832/pexels-photo-4551832.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white !important;
    }

    button[kind="secondary"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 2px solid white !important;
        border-radius: 5px !important;
        padding: 0.5em 1em !important;
        font-size: 16px !important;
    }

    button[kind="secondary"]:hover {
        background-color: rgba(255, 255, 255, 0.3) !important;
        color: black !important;
    }

    button:focus {
        outline: none !important;
        box-shadow: none !important;
    }

    label, .css-1cpxqw2, .css-1y4p8pa {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# ===================== BERANDA =====================
if st.session_state.page == "beranda":
    st.title("\U0001F4D8 Selamat Datang di Halaman Perhitungan Gizi")
    st.markdown("""
    Aplikasi ini membantu Anda menghitung total nilai gizi dari berbagai bahan pangan berdasarkan berat (gram) yang dimasukkan.

    ### Fitur:
    - Pilih beberapa bahan pangan
    - Masukkan jumlah dalam gram
    - Dapatkan total nilai kalori, protein, lemak, karbohidrat, serat, kalsium, zat besi, dan vitamin C
    - Lihat detail per bahan

    ---  
    """)
    st.button("\u27a1\ufe0f Mulai Perhitungan", on_click=set_page, args=("perhitungan",))

# ===================== PERHITUNGAN =====================
elif st.session_state.page == "perhitungan":
    st.title("Perhitungan Nilai Gizi Berdasarkan Bahan Pangan")
    st.button("\U0001F519 Kembali ke Beranda", on_click=set_page, args=("beranda",))

    # Tombol tambah/hapus
    col_add, col_remove = st.columns([1, 1])
    with col_add:
        if st.button("\u2795 Tambah Bahan"):
            st.session_state.bahan_count += 1
            st.session_state.bahan_inputs.append({})
    with col_remove:
        if st.button("\u2796 Hapus Bahan") and st.session_state.bahan_count > 1:
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

    # Tombol hitung dengan spinner loading
    if st.button("Hitung Total Gizi"):
        with st.spinner('Menghitung total nilai gizi...'):
            time.sleep(2)
            st.snow()

            total = {
                "Kalori": 0, "Protein": 0, "Lemak": 0, "Karbohidrat": 0,
                "Serat": 0, "Kalsium": 0, "Zat Besi": 0, "Vitamin C": 0
            }
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
                    total["Serat"] += row["Serat"] * faktor
                    total["Kalsium"] += row["Kalsium"] * faktor
                    total["Zat Besi"] += row["Zat Besi"] * faktor
                    total["Vitamin C"] += row["Vitamin C"] * faktor

                    hasil_detail.append({
                        "Bahan": bahan,
                        "Gram": gram,
                        "Kalori": row["Kalori"] * faktor,
                        "Protein": row["Protein"] * faktor,
                        "Lemak": row["Lemak"] * faktor,
                        "Karbohidrat": row["Karbohidrat"] * faktor,
                        "Serat": row["Serat"] * faktor,
                        "Kalsium": row["Kalsium"] * faktor,
                        "Zat Besi": row["Zat Besi"] * faktor,
                        "Vitamin C": row["Vitamin C"] * faktor,
                    })

            st.subheader("Total Nilai Gizi:")
            for k, v in total.items():
                satuan = "kkal" if k == "Kalori" else "g" if k in ["Protein", "Lemak", "Karbohidrat", "Serat"] else "mg"
                st.write(f"*{k}:* {v:.2f} {satuan}")

            if hasil_detail:
                st.subheader("Detail Per Bahan:")
                st.dataframe(pd.DataFrame(hasil_detail))

            # --- Saran berdasarkan hasil total ---
            st.subheader("\U0001F4A1 Saran Nutrisi dan Penjelasan:")

            saran = []
            penjelasan = []

            if total["Kalori"] < 1500:
                saran.append("- Tambahkan makanan sumber energi seperti nasi, mie, roti gandum, ubi jalar, pisang, alpukat, atau granola.")
                penjelasan.append("Kekurangan kalori menyebabkan tubuh tidak memiliki cukup energi untuk menjalankan aktivitas harian. Gejala termasuk kelelahan, berat badan turun drastis, konsentrasi menurun, dan bisa mempengaruhi keseimbangan hormon tubuh.")

            if total["Protein"] < 50:
                saran.append("- Tambahkan telur, dada ayam, tempe, tahu, ikan, daging sapi tanpa lemak, susu, yogurt, atau edamame.")
                penjelasan.append("Kekurangan protein bisa menyebabkan kehilangan massa otot, mudah sakit, penyembuhan luka lambat, rambut rontok, dan gangguan pertumbuhan terutama pada anak-anak.")

            if total["Lemak"] < 40:
                saran.append("- Tambahkan kacang almond, kenari, minyak zaitun, biji chia, ikan salmon, atau santan.")
                penjelasan.append("Lemak penting untuk penyerapan vitamin larut lemak (A, D, E, K), fungsi otak, dan produksi hormon. Kekurangan lemak dapat menyebabkan kulit kering, ketidakseimbangan hormon, dan gangguan pada sistem saraf.")

            if total["Serat"] < 20:
                saran.append("- Tambahkan sayur seperti brokoli, bayam, wortel, serta buah seperti apel, pir, pepaya, dan biji-bijian utuh.")
                penjelasan.append("Serat membantu pencernaan, mengontrol gula darah, dan menurunkan kolesterol. Kekurangannya bisa menyebabkan sembelit, peningkatan risiko penyakit jantung, dan gangguan metabolisme.")

            if total["Kalsium"] < 800:
                saran.append("- Tambahkan susu, yogurt, keju, brokoli, kale, tahu, tempe, ikan sarden atau salmon bertulang.")
                penjelasan.append("Kalsium penting untuk tulang dan gigi kuat, serta fungsi otot dan saraf. Kekurangan kalsium dapat menyebabkan osteoporosis, kram otot, dan gangguan detak jantung.")

            if total["Zat Besi"] < 14:
                saran.append("- Tambahkan hati ayam, daging merah, bayam, kacang merah, lentil, telur, atau sereal yang difortifikasi zat besi.")
                penjelasan.append("Zat besi penting untuk membentuk hemoglobin. Kekurangannya menyebabkan anemia yang ditandai dengan lemas, pucat, detak jantung cepat, dan sesak napas.")

            if total["Vitamin C"] < 60:
                saran.append("- Tambahkan jeruk, kiwi, stroberi, mangga, jambu biji, paprika merah, atau tomat.")
                penjelasan.append("Vitamin C penting untuk sistem imun, penyembuhan luka, dan penyerapan zat besi. Kekurangannya menyebabkan sariawan, gusi berdarah, dan skorbut (pada kasus parah).")

            if saran:
                st.markdown("### ✅ Saran:")
                for item in saran:
                    st.markdown(item)

                st.markdown("### ℹ️ Penjelasan Dampak Kekurangan:")
                for item in penjelasan:
                    st.markdown(f"- {item}")
            else:
                st.success("\U0001F389 Asupan gizi Anda sudah mencukupi dari bahan yang dipilih.")
