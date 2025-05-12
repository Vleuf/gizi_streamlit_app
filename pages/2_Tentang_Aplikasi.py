import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Selamat Datang", layout="wide")

# Styling latar belakang dan warna putih untuk teks
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                    url('https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=1600');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    label, .css-1cpxqw2, .css-1y4p8pa {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# ======== Teks Asli Perkenalan ========
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
