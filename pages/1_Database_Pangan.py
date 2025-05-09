import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Database Pangan", layout="wide")

# Inisialisasi halaman aktif
if "db_page" not in st.session_state:
    st.session_state.db_page = "beranda"

# Fungsi navigasi tanpa st.rerun
def go_to(page):
    st.session_state.db_page = page

# ===================== BERANDA =====================
st.title("📘 Database Bahan Pangan")
st.markdown("""
Aplikasi ini berisi informasi singkat mengenai bahan pangan umum yang digunakan dalam perhitungan gizi.  
Silakan pilih bahan pangan di bawah ini untuk melihat kandungan gizinya:
""")

# Tampilkan tombol navigasi
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🍚 Nasi Putih"):
        go_to("nasi")
with col2:
    if st.button("🥚 Telur Ayam"):
        go_to("telur")
with col3:
    if st.button("🍱 Tempe"):
        go_to("tempe")

col4, col5, _ = st.columns(3)
with col4:
    if st.button("🍥 Tahu"):
        go_to("tahu")
with col5:
    if st.button("🍗 Daging Ayam"):
        go_to("ayam")

st.markdown("---")
st.markdown("*Catatan: Nilai gizi dapat bervariasi tergantung pada cara pengolahan dan jenis bahan pangan.*")

# ===================== HALAMAN DETAIL =====================
if st.session_state.db_page == "nasi":
    st.subheader("🍚 Nasi Putih")
    st.markdown("""
    Nasi putih adalah sumber karbohidrat utama di Indonesia.  
    Dalam 100 gram, nasi mengandung sekitar:
    - 175 kkal  
    - 39 gram karbohidrat  
    - Sedikit protein dan lemak  
    """)
elif st.session_state.db_page == "telur":
    st.subheader("🥚 Telur Ayam")
    st.markdown("""
    Telur merupakan sumber protein hewani yang sangat baik.  
    Dalam 100 gram telur mengandung sekitar:
    - 155 kkal  
    - 13 gram protein  
    """)
elif st.session_state.db_page == "tempe":
    st.subheader("🍱 Tempe")
    st.markdown("""
    Tempe adalah sumber protein nabati hasil fermentasi kedelai.  
    Dalam 100 gram tempe mengandung:
    - 193 kkal  
    - 19 gram protein  
    - Lemak sehat  
    """)
elif st.session_state.db_page == "tahu":
    st.subheader("🍥 Tahu")
    st.markdown("""
    Tahu memiliki kandungan protein sedang dan cocok untuk makanan rendah kalori.  
    Dalam 100 gram tahu mengandung:
    - 80 kkal  
    - 8 gram protein  
    """)
elif st.session_state.db_page == "ayam":
    st.subheader("🍗 Daging Ayam")
    st.markdown("""
    Daging ayam tanpa kulit adalah sumber protein hewani tinggi.  
    Dalam 100 gram daging ayam mengandung:
    - 165 kkal  
    - 31 gram protein  
    - Lemak rendah  
    """)

# Tombol kembali ke beranda (hanya tampil saat tidak di beranda)
if st.session_state.db_page != "beranda":
    st.markdown("---")
    st.button("🔙 Kembali ke Beranda", on_click=lambda: go_to("beranda"))
