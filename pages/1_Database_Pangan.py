import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Aplikasi Gizi", layout="wide")

# Inisialisasi session state
if "current_page" not in st.session_state:
    st.session_state.current_page = "beranda"

# Fungsi navigasi
def go_to_database():
    st.session_state.current_page = "database"

def go_to_home():
    st.session_state.current_page = "beranda"

# CSS Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
                    url('https://wallpapers.com/images/high/food-4k-tmi8md4hnk20df1u.webp');
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
    st.title("📘 Selamat Datang di Aplikasi Perhitungan Gizi")
    st.markdown("Aplikasi ini membantu Anda menghitung nilai gizi dari berbagai bahan makanan.")

    # Navigasi ke database dengan 1 klik (tanpa error)
    st.button("📑 Buka Database Bahan Pangan", on_click=go_to_database)

# ==================== HALAMAN DATABASE ====================
elif st.session_state.current_page == "database":
    st.title("📋 Database Bahan Pangan")
    st.button("🔙 Kembali ke Beranda", on_click=go_to_home)

    menu = st.selectbox(
        "Pilih bahan pangan:",
        [
            "", "Nasi Putih", "Telur Ayam", "Tempe", "Tahu", "Daging Ayam",
            "Ikan Tuna", "Daging Sapi", "Kentang", "Wortel", "Bayam", "Apel",
            "Pisang", "Susu Sapi", "Keju", "Yogurt"
        ]
    )

    data_gizi = {
        "Nasi Putih": {"kalori": 175, "karbohidrat": 39, "protein": 3, "lemak": 0.3},
        "Telur Ayam": {"kalori": 155, "protein": 13, "lemak": 11, "karbohidrat": 1.1},
        "Tempe": {"kalori": 193, "protein": 19, "lemak": 11, "karbohidrat": 9},
        "Tahu": {"kalori": 80, "protein": 8, "lemak": 4, "karbohidrat": 2},
        "Daging Ayam": {"kalori": 165, "protein": 31, "lemak": 3.6, "karbohidrat": 0},
        "Ikan Tuna": {"kalori": 144, "protein": 30, "lemak": 1.0, "karbohidrat": 0},
        "Daging Sapi": {"kalori": 250, "protein": 26, "lemak": 17, "karbohidrat": 0},
        "Kentang": {"kalori": 77, "protein": 2, "lemak": 0.1, "karbohidrat": 17},
        "Wortel": {"kalori": 41, "protein": 0.9, "lemak": 0.2, "karbohidrat": 10},
        "Bayam": {"kalori": 23, "protein": 2.9, "lemak": 0.4, "karbohidrat": 3.6},
        "Apel": {"kalori": 52, "protein": 0.3, "lemak": 0.2, "karbohidrat": 14},
        "Pisang": {"kalori": 89, "protein": 1.1, "lemak": 0.3, "karbohidrat": 23},
        "Susu Sapi": {"kalori": 61, "protein": 3.2, "lemak": 3.3, "karbohidrat": 5},
        "Keju": {"kalori": 402, "protein": 25, "lemak": 33, "karbohidrat": 1.3},
        "Yogurt": {"kalori": 59, "protein": 10, "lemak": 0.4, "karbohidrat": 3.6}
    }

    if menu and menu in data_gizi:
        gizi = data_gizi[menu]
        st.subheader(f"🍽️ {menu}")
        st.markdown(f"""
        Dalam 100 gram **{menu.lower()}** mengandung:
        - **{gizi['kalori']} kkal**
        - **{gizi['protein']} g protein**
        - **{gizi['lemak']} g lemak**
        - **{gizi['karbohidrat']} g karbohidrat**
        """)

