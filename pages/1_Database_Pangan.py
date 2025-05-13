import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(page_title="Database GIZI", layout="wide")

# Inisialisasi session state
if "current_page" not in st.session_state:
    st.session_state.current_page = "beranda"

# Fungsi navigasi
def go_to_database():
    st.session_state.current_page = "database"
    st.balloons()  # 🎈 Efek balon saat buka database

def go_to_home():
    st.session_state.current_page = "beranda"
    st.balloons()  # 🎈 Efek balon saat kembali ke beranda

# CSS Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
                    url('https://images.pexels.com/photos/5463890/pexels-photo-5463890.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');
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

# ==================== HALAMAN BERANDA ====================
if st.session_state.current_page == "beranda":
    st.title("📘 Selamat Datang di Halaman Database Pangan")
    st.markdown("""
    Halaman ini menyediakan informasi mengenai berbagai bahan pangan, 
    termasuk kandungan gizi dan deskripsi lengkapnya. 
    Anda dapat memilih bahan pangan dari daftar untuk melihat penjelasan detail mengenai manfaat dan kandungan gizinya.
    
    Di bawah ini, Anda dapat memilih bahan pangan untuk melihat penjelasan lengkap mengenai manfaat dan nilai gizinya. 
    Informasi ini sangat berguna untuk merancang pola makan yang sehat dan seimbang, baik untuk kebutuhan pribadi maupun keluarga Anda.

    Silakan tekan pada daftar berikut untuk mulai eksplorasi 👇
    """)
    st.button("📑 Buka Database Bahan Pangan", on_click=go_to_database)

# ==================== HALAMAN DATABASE ====================
elif st.session_state.current_page == "database":
    st.title("📋 Database Bahan Pangan")
    st.button("🔙 Kembali ke Beranda", on_click=go_to_home)

    # Baca data dari file CSV
    try:
        df = pd.read_csv("deskripsi_dengan_pengertian.csv")
        bahan_list = [""] + df['Bahan'].dropna().unique().tolist()

        # Pilihan bahan pangan
        menu = st.selectbox("Pilih bahan pangan:", bahan_list)

        # Tampilkan deskripsi jika tersedia
        if menu:
            deskripsi = df[df['Bahan'] == menu]['Deskripsi Lengkap'].values[0]
            st.subheader(f"📝 {menu}")
            st.markdown(deskripsi)

    except FileNotFoundError:
        st.error("❌ File CSV tidak ditemukan. Pastikan file deskripsi_dengan_pengertian.csv ada di direktori yang benar.")
