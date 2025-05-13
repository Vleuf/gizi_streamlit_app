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
st.title("🧮 Aplikasi Perhitungan Gizi dan Database Pangan")

st.markdown("""
**Aplikasi Perhitungan Gizi dan Database Pangan** adalah aplikasi berbasis web yang dirancang untuk membantu pengguna menghitung kandungan gizi dari berbagai **bahan pangan** menggunakan basis data gizi yang akurat dan terverifikasi. Aplikasi ini membantu masyarakat, pelajar, tenaga gizi, hingga peneliti untuk mengetahui kandungan nutrisi dari berbagai jenis bahan makanan secara cepat dan mudah.

Aplikasi ini dibangun menggunakan teknologi **Streamlit**, sehingga tampilannya sederhana, responsif, dan dapat diakses langsung melalui web tanpa instalasi.

---

## 🎯 Tujuan Pengembangan Aplikasi

Tujuan utama dari aplikasi ini adalah:

1. **Menyediakan akses mudah terhadap data gizi pangan**
   - Banyak masyarakat dan tenaga kesehatan yang membutuhkan data cepat mengenai nilai gizi bahan makanan.
   - Aplikasi ini menjawab kebutuhan tersebut secara praktis.

2. **Meningkatkan literasi gizi berbasis data**
   - Digunakan sebagai sarana edukasi dalam memahami nilai gizi dari makanan sehari-hari.

3. **Mendukung program intervensi gizi dan ketahanan pangan**
   - Dapat digunakan oleh lembaga pendidikan, LSM, dan pemerhati gizi untuk merancang menu dan program pangan.

---

## 🔍 Fitur Utama

Beberapa fitur unggulan aplikasi ini antara lain:

### 📦 1. Pencarian Bahan Pangan
   Pengguna dapat memasukkan nama bahan makanan seperti "beras", "ayam", "bayam", dll. Sistem akan menampilkan data gizi yang relevan dari database yang tersedia.

### 🧮 2. Kalkulasi Gizi Otomatis
   Setelah memilih bahan pangan, pengguna bisa memasukkan jumlah berat (gram) dari makanan tersebut. Aplikasi akan menghitung total kandungan energi (kalori), protein, lemak, karbohidrat, dan zat gizi mikro (jika tersedia).

### 🗂️ 3. Database Pangan Terstruktur
   Informasi nutrisi didasarkan pada **data pangan lokal dan/atau internasional**, seperti Tabel Komposisi Pangan Indonesia (TKPI). Data tersaji dalam bentuk tabel yang mudah dipahami dan dapat digunakan untuk keperluan akademis.

### 📊 4. Perbandingan dan Rekomendasi
   Aplikasi memungkinkan pengguna membandingkan beberapa bahan pangan berdasarkan nilai gizinya. Berguna untuk merancang substitusi makanan yang lebih bergizi.

---

## ⚙️ Fungsi Utama Aplikasi

- **Edukasi Gizi**: Cocok untuk siswa, mahasiswa, guru, dan masyarakat umum yang ingin belajar tentang nilai gizi makanan.
- **Perencanaan Menu**: Membantu ahli gizi atau rumah tangga dalam menyusun menu makanan seimbang.
- **Evaluasi Konsumsi Pangan**: Bisa digunakan untuk menilai nilai gizi dari makanan yang dikonsumsi harian atau mingguan.

---

## 🌱 Manfaat Penggunaan

- ✅ Akses informasi gizi cepat dan mudah  
- ✅ Dapat digunakan dalam pelatihan, workshop, dan pengajaran gizi  
- ✅ Gratis dan berbasis web – tidak butuh instalasi  
- ✅ Mendukung transparansi dan akurasi data dalam dunia gizi  
- ✅ Membantu menyusun program intervensi gizi berbasis data

---

## ⚠️ Catatan Pengembangan

> **Aplikasi ini masih dalam tahap pengembangan.**  
> Beberapa fitur dan tampilan mungkin belum lengkap atau masih bersifat prototipe.  
> Tim pengembang berencana melakukan **pengembangan lanjutan**, termasuk:
> - Penambahan lebih banyak data bahan pangan  
> - Visualisasi nilai gizi dalam bentuk grafik  
> - Fitur ekspor data hasil kalkulasi  
> - Antarmuka pengguna yang lebih intuitif dan interaktif

---
""")
