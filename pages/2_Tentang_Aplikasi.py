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
🧮 Aplikasi Perhitungan Gizi dan Database Pangan
Aplikasi Perhitungan Gizi dan Database Pangan adalah aplikasi berbasis web yang dirancang untuk membantu pengguna menghitung kandungan gizi dari berbagai bahan pangan menggunakan basis data gizi yang tersusun secara ilmiah. Aplikasi ini tidak ditujukan untuk menghitung kebutuhan energi berdasarkan usia atau aktivitas fisik, melainkan fokus pada analisis nutrisi makanan dari bahan mentah atau olahan secara kuantitatif.

🎯 Tujuan Pengembangan
Aplikasi ini dikembangkan untuk menjawab beberapa kebutuhan berikut:

Menyediakan akses cepat dan mudah ke informasi kandungan gizi dari bahan pangan.

Mendukung proses edukasi gizi berbasis data di berbagai level—individu, akademik, dan institusional.

Membantu tenaga gizi, peneliti, guru, dan masyarakat umum dalam perencanaan menu sehat.

Mengintegrasikan teknologi dalam pemantauan dan pemilihan pangan yang lebih bijak.

🧩 Fitur-Fitur Utama
1. 🔍 Pencarian Bahan Pangan
Pengguna dapat mencari berbagai jenis bahan pangan, seperti sayur, buah, daging, dan lainnya, dari daftar database yang tersedia.

2. 🧮 Perhitungan Kandungan Gizi Otomatis
Setelah memilih bahan pangan, pengguna cukup memasukkan jumlah dalam gram, dan aplikasi akan menampilkan:

Kalori (kkal)

Protein (gram)

Lemak (gram)

Karbohidrat (gram)

Informasi lain bila tersedia (serat, vitamin, zat besi)

3. 📊 Tabel Komposisi Pangan
Data ditampilkan dalam format tabel yang rapi dan mudah dianalisis.

4. 🗂️ Basis Data Terverifikasi
Menggunakan referensi dari Tabel Komposisi Pangan Indonesia (TKPI) dan/atau sumber data resmi lainnya.

⚙️ Fungsi Aplikasi dalam Kehidupan Sehari-hari
Sebagai alat bantu edukasi gizi di sekolah, universitas, atau pelatihan masyarakat.

Untuk menyusun menu bergizi seimbang dengan pilihan bahan yang tepat.

Digunakan oleh tenaga gizi dalam perhitungan diet atau intervensi pangan.

Sebagai referensi cepat saat ingin mengecek kandungan nutrisi dari makanan.

🌱 Manfaat Penggunaan
✅ Edukatif dan mudah digunakan oleh siapa saja

✅ Tidak membutuhkan instalasi—cukup akses lewat web

✅ Mengurangi ketergantungan pada dokumen cetak atau kalkulasi manual

✅ Mendukung program intervensi gizi berbasis data dan bukti

⚠️ Catatan Pengembangan
Aplikasi ini masih dalam tahap pengembangan awal.
Beberapa fitur belum sepenuhnya tersedia, dan antarmuka pengguna masih bersifat dasar.
Rencana ke depan mencakup:

Penambahan lebih banyak data bahan pangan

Visualisasi gizi dalam bentuk grafik

Fitur ekspor data hasil kalkulasi

Integrasi menu diet otomatis
""")
