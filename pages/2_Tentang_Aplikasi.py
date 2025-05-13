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
🧬 Apa itu GiziApp for Humanity?
GiziApp for Humanity adalah aplikasi web berbasis Streamlit yang berfungsi untuk menghitung kandungan gizi dari berbagai bahan pangan, menggunakan basis data gizi yang terstruktur. Aplikasi ini dikembangkan dengan misi kemanusiaan untuk meningkatkan literasi dan kesadaran gizi melalui teknologi yang mudah diakses.

Berbeda dengan kalkulator kebutuhan energi yang didasarkan pada profil individu (usia, berat badan, aktivitas, dll.), aplikasi ini fokus pada analisis kandungan gizi bahan pangan — seperti beras, telur, daging, sayuran, dan lainnya.

🎯 Tujuan Pengembangan
Tujuan utama dari GiziApp for Humanity antara lain:

Mempermudah akses terhadap data kandungan gizi bahan pangan

Mendukung edukasi gizi di kalangan masyarakat, pelajar, dan profesional kesehatan

Membantu perencanaan menu makanan berbasis data

Mendorong kesadaran konsumsi makanan bergizi dan seimbang

🔍 Fitur-Fitur Utama
1. Pencarian Bahan Pangan
Pengguna dapat mencari berbagai jenis bahan pangan dari database untuk mengetahui kandungan gizinya.

2. Kalkulasi Otomatis
Pengguna bisa memasukkan berat bahan makanan (dalam gram), dan aplikasi akan menghitung nilai kalori, protein, karbohidrat, dan lemak berdasarkan data yang tersedia.

3. Tampilan Tabel Data Gizi
Nilai gizi ditampilkan dalam format tabel yang jelas dan mudah dipahami.

4. Sumber Data Terpercaya
Menggunakan data dari sumber seperti Tabel Komposisi Pangan Indonesia (TKPI) dan sumber internasional lain (jika tersedia).

⚙️ Fungsi Aplikasi
Membantu merancang menu seimbang berdasarkan data nyata.

Digunakan sebagai alat bantu dalam edukasi gizi dan pelatihan masyarakat.

Mendukung pengambilan keputusan berbasis data di bidang gizi dan ketahanan pangan.

🌱 Manfaat
Akses mudah, cepat, dan tanpa biaya

Edukatif untuk masyarakat umum dan tenaga profesional

Meningkatkan kesadaran gizi harian berbasis bukti

Membantu mengganti atau membandingkan bahan pangan secara objektif

⚠️ Catatan Penting
GiziApp for Humanity saat ini masih dalam tahap pengembangan.
Beberapa fitur dan tampilan mungkin belum lengkap atau masih bersifat prototipe.
Tim pengembang berencana melakukan pengembangan lanjutan, termasuk penambahan fitur seperti ekspor data, integrasi dengan grafik, serta perbaikan antarmuka pengguna agar lebih ramah dan intuitif.


""")
