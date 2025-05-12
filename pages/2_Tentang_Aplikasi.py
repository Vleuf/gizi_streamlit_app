import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Selamat Datang", layout="wide")

# Styling untuk halaman pembuka
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)),
                    url('https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=1600');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
    }

    .intro-text {
        font-size: 24px;
        font-weight: 300;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    .title-text {
        font-size: 38px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== HALAMAN PERKENALAN ====================
st.markdown('<p class="title-text">🌿 Aplikasi Perhitungan Gizi dan Informasi Pangan</p>', unsafe_allow_html=True)

st.markdown("""
<div class="intro-text">
Selamat datang di aplikasi interaktif yang membantu Anda memahami kandungan gizi dari berbagai bahan makanan!  
Aplikasi ini dirancang untuk:
<ul>
  <li>💡 Memberikan informasi gizi lengkap dari berbagai bahan pangan.</li>
  <li>📊 Membantu menghitung total kalori, protein, lemak, dan karbohidrat berdasarkan porsi Anda.</li>
  <li>🥗 Menyediakan database makanan populer di Indonesia secara ringkas dan mudah diakses.</li>
</ul>
Klik tombol di bawah ini untuk mulai menjelajah!
</div>
""", unsafe_allow_html=True)

# Tombol Navigasi
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("➡️ Mulai Perhitungan Gizi"):
        st.session_state.page = "perhitungan"
with col2:
    if st.button("📋 Lihat Database Bahan Pangan"):
        st.session_state.current_page = "database"
