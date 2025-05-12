import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Selamat Datang", layout="wide")

# Styling konsisten
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)),
                    url('https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=1600');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white !important;
    }

    .title-text {
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .intro-text {
        font-size: 20px;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    ul {
        margin-top: 0.5em;
    }

    li {
        margin-bottom: 0.5em;
    }
    </style>
""", unsafe_allow_html=True)

# Teks Perkenalan
st.markdown('<p class="title-text">📘 Selamat Datang di Aplikasi Perhitungan Gizi</p>', unsafe_allow_html=True)

st.markdown("""
<div class="intro-text">
Aplikasi ini membantu Anda menghitung total nilai gizi dari berbagai bahan pangan berdasarkan berat (gram) yang dimasukkan.

### Fitur:
<ul>
  <li>✅ Pilih beberapa bahan pangan</li>
  <li>✅ Masukkan jumlah dalam gram</li>
  <li>✅ Dapatkan total nilai kalori, protein, lemak, dan karbohidrat</li>
  <li>✅ Lihat detail per bahan</li>
</ul>

Gunakan menu navigasi atau scroll untuk melanjutkan ke fitur berikutnya.
</div>
""", unsafe_allow_html=True)
