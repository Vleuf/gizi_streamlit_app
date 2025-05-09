import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(page_title="Aplikasi Gizi", layout="wide")

# ==================== Inisialisasi session_state ====================
if "current_page" not in st.session_state:
    st.session_state.current_page = "beranda"

# Fungsi untuk mengatur halaman aktif
def set_page(page):
    st.session_state.current_page = page

# ==================== Styling ====================
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)),
                    url('https://wallpapers.com/images/high/food-4k-tmi8md4hnk20df1u.webp');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white !important;
    }
    st.markdown("""
    <style>
    .custom-button {
        background-color: rgba(255, 255, 255, 0.15); /* transparan keputihan */
        color: white;
        padding: 0.5em 1em;
        border: 2px solid white;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        transition: 0.3s;
    }

    .custom-button:hover {
        background-color: white;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== Halaman Beranda ====================
if st.session_state.current_page == "beranda":
    st.title("📘 Selamat Datang di Aplikasi Perhitungan Gizi")
    st.markdown("""
    Aplikasi ini membantu Anda untuk menghitung nilai gizi dari berbagai bahan pangan berdasarkan berat yang dimasukkan.

    Pilih salah satu menu di bawah ini untuk melanjutkan:
    """, unsafe_allow_html=True)

    # Tombol kustom menggunakan HTML
    col1, _ = st.columns([1, 3])
    with col1:
        st.markdown(f"""
            <button class="custom-button" onclick="window.location.reload(); window.parent.postMessage({{ type: 'streamlit:setComponentValue', key: 'current_page', value: 'database' }}, '*')">
                📑 Database Bahan Pangan
            </button>
        """, unsafe_allow_html=True)

        # Fallback button if HTML button doesn't work
        if st.button("📑 Klik jika tombol atas tidak bekerja", key="fallback_db"):
            set_page("database")

# ==================== Halaman Database Bahan Pangan ====================
elif st.session_state.current_page == "database":
    st.title("📋 Database Bahan Pangan")

    if st.button("🔙 Kembali ke Beranda"):
        set_page("beranda")

    menu = st.selectbox(
        "Pilih bahan pangan untuk melihat detail kandungan gizinya:",
        ["", "Nasi Putih", "Telur Ayam", "Tempe", "Tahu", "Daging Ayam"]
    )

    if menu == "Nasi Putih":
        st.header("🍚 Nasi Putih")
        st.markdown("""
        Nasi putih adalah sumber karbohidrat utama di Indonesia.  
        Dalam 100 gram, nasi mengandung sekitar:
        - 175 kkal  
        - 39 gram karbohidrat  
        - Sedikit protein dan lemak  
        """)
    elif menu == "Telur Ayam":
        st.header("🥚 Telur Ayam")
        st.markdown("""
        Telur merupakan sumber protein hewani yang sangat baik.  
        Dalam 100 gram telur mengandung sekitar:
        - 155 kkal  
        - 13 gram protein  
        """)
    elif menu == "Tempe":
        st.header("🍱 Tempe")
        st.markdown("""
        Tempe adalah sumber protein nabati hasil fermentasi kedelai.  
        Dalam 100 gram tempe mengandung:
        - 193 kkal  
        - 19 gram protein  
        - Lemak sehat  
        """)
    elif menu == "Tahu":
        st.header("🍥 Tahu")
        st.markdown("""
        Tahu memiliki kandungan protein sedang dan cocok untuk makanan rendah kalori.  
        Dalam 100 gram tahu mengandung:
        - 80 kkal  
        - 8 gram protein  
        """)
    elif menu == "Daging Ayam":
        st.header("🍗 Daging Ayam")
        st.markdown("""
        Daging ayam tanpa kulit adalah sumber protein hewani tinggi.  
        Dalam 100 gram daging ayam mengandung:
        - 165 kkal  
        - 31 gram protein  
        - Lemak rendah  
        """)
