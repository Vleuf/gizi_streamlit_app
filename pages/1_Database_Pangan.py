import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Aplikasi Gizi", layout="wide")

# Inisialisasi session_state
if "current_page" not in st.session_state:
    st.session_state.current_page = "beranda"

# Fungsi navigasi
def set_page(page):
    st.session_state.current_page = page

# CSS styling tombol transparan dan latar belakang
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

    /* Styling tombol transparan */
    button[kind="secondary"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 2px solid white !important;
        border-radius: 5px !important;
        padding: 0.5em 1em !important;
        font-size: 16px !important;
    }

    /* Hover effect */
    button[kind="secondary"]:hover {
        background-color: rgba(255, 255, 255, 0.3) !important;
        color: black !important;
    }

    /* Hilangkan garis biru saat tombol diklik */
    button:focus {
        outline: none !important;
        box-shadow: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== Halaman Beranda ====================
if st.session_state.current_page == "beranda":
    st.title("📘 Selamat Datang di Aplikasi Perhitungan Gizi")
    st.markdown("""
    Aplikasi ini membantu Anda untuk menghitung nilai gizi dari berbagai bahan pangan berdasarkan berat yang dimasukkan.
    """)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📑 Database Bahan Pangan"):
            set_page("database")
    with col2:
        st.button("📦 Fitur Lain (Coming Soon)")

# ==================== Halaman Database ====================
elif st.session_state.current_page == "database":
    st.title("📋 Database Bahan Pangan")

    if st.button("🔙 Kembali ke Beranda"):
        set_page("beranda")

    menu = st.selectbox("Pilih bahan pangan:", ["", "Nasi Putih", "Telur Ayam", "Tempe", "Tahu", "Daging Ayam"])

    if menu == "Nasi Putih":
        st.subheader("🍚 Nasi Putih")
        st.markdown("Dalam 100 gram: 175 kkal, 39g karbohidrat.")
    elif menu == "Telur Ayam":
        st.subheader("🥚 Telur Ayam")
        st.markdown("Dalam 100 gram: 155 kkal, 13g protein.")
    elif menu == "Tempe":
        st.subheader("🍱 Tempe")
        st.markdown("Dalam 100 gram: 193 kkal, 19g protein.")
    elif menu == "Tahu":
        st.subheader("🍥 Tahu")
        st.markdown("Dalam 100 gram: 80 kkal, 8g protein.")
    elif menu == "Daging Ayam":
        st.subheader("🍗 Daging Ayam")
        st.markdown("Dalam 100 gram: 165 kkal, 31g protein.")
