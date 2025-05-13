import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Pengembang Aplikasi", layout="wide")

# Styling latar belakang dan warna putih untuk teks
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                    url('https://i.pinimg.com/736x/17/be/4b/17be4b934d7008f98b116d0631657b70.jpg');
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

# ======== Teks Nama Pengembang ========
st.title("👨‍💻 Tim Pengembang Aplikasi Perhitungan Gizi")

st.image("kelompok.jpeg", caption="Foto Tim Pengembang", width=500)

st.markdown("""
Aplikasi Perhitungan Gizi dan Database Pangan ini dikembangkan oleh tim yang berkomitmen untuk menyediakan alat yang bermanfaat bagi masyarakat, tenaga kesehatan, dan peneliti di bidang gizi. Berikut adalah nama-nama anggota tim pengembang aplikasi ini:

---

## 🌟 Tim Pengembang Utama

1. **[Nama Pengembang 1]** - _Frontend Developer_
   - Bertanggung jawab atas antarmuka pengguna (UI) dan desain aplikasi menggunakan Streamlit dan CSS.

2. **[Nama Pengembang 2]** - _Backend Developer_
   - Mengelola integrasi dan pengolahan data menggunakan Pandas dan memastikan aplikasi berjalan dengan baik.

3. **[Nama Pengembang 3]** - _Data Scientist_
   - Menganalisis dan memverifikasi data gizi yang digunakan dalam aplikasi serta melakukan pembaruan dan perluasan database.

4. **[Nama Kontributor 1]** - _Pengembang Fitur Perbandingan_
   - Berkontribusi dalam pengembangan fitur perbandingan bahan pangan berdasarkan nilai gizi.

5. **[Nama Kontributor 2]** - _Pengembang Visualisasi Data_
   - Menambahkan fitur visualisasi grafis menggunakan Matplotlib untuk memperlihatkan perbandingan nilai gizi.

---

## 🚀 Pengembangan Lanjutan
Aplikasi ini masih dalam tahap pengembangan dan setiap pengembang baru dipersilakan untuk berkolaborasi dalam peningkatan aplikasi.

---

### Terima kasih kepada semua anggota tim yang telah berkontribusi dalam pengembangan aplikasi ini!
""")
