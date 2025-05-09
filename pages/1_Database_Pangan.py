import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Database Pangan", layout="wide")

# ======= Inisialisasi session_state =======
if "db_page" not in st.session_state:
    st.session_state.db_page = "beranda"

# ======= Fungsi untuk navigasi tombol =======
def go_to(page):
    st.session_state.db_page = page
    st.rerun()

# ======= Halaman Beranda Database =======
if st.session_state.db_page == "beranda":
    st.title("📘 Database Bahan Pangan")
    st.markdown("""
    Aplikasi ini berisi informasi singkat mengenai bahan pangan umum yang digunakan dalam perhitungan gizi.  
    Silakan pilih bahan pangan di bawah ini untuk melihat kandungan gizinya:
    """)
    
    # Tombol-tombol bahan pangan
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("🍚 Nasi Putih", on_click=go_to, args=("nasi",))
    with col2:
        st.button("🥚 Telur Ayam", on_click=go_to, args=("telur",))
    with col3:
        st.button("🍱 Tempe", on_click=go_to, args=("tempe",))
    
    col4, col5, _ = st.columns(3)
    with col4:
        st.button("🍥 Tahu", on_click=go_to, args=("tahu",))
    with col5:
        st.button("🍗 Daging Ayam", on_click=go_to, args=("ayam",))

    st.markdown("""
    ---  
    *Catatan: Nilai gizi dapat bervariasi tergantung pada cara pengolahan dan jenis bahan pangan.*
    """)

# ======= Halaman Detail Bahan Pangan =======

elif st.session_state.db_page == "nasi":
    st.header("🍚 Nasi Putih")
    st.markdown("""
    Nasi putih adalah sumber karbohidrat utama di Indonesia.  
    Dalam 100 gram, nasi mengandung sekitar:
    - 175 kkal  
    - 39 gram karbohidrat  
    - Sedikit protein dan lemak  
    """)
    st.button("🔙 Kembali", on_click=go_to, args=("beranda",))

elif st.session_state.db_page == "telur":
    st.header("🥚 Telur Ayam")
    st.markdown("""
    Telur merupakan sumber protein hewani yang sangat baik.  
    Dalam 100 gram telur mengandung sekitar:
    - 155 kkal  
    - 13 gram protein  
    """)
    st.button("🔙 Kembali", on_click=go_to, args=("beranda",))

elif st.session_state.db_page == "tempe":
    st.header("🍱 Tempe")
    st.markdown("""
    Tempe adalah sumber protein nabati hasil fermentasi kedelai.  
    Dalam 100 gram tempe mengandung:
    - 193 kkal  
    - 19 gram protein  
    - Lemak sehat  
    """)
    st.button("🔙 Kembali", on_click=go_to, args=("beranda",))

elif st.session_state.db_page == "tahu":
    st.header("🍥 Tahu")
    st.markdown("""
    Tahu memiliki kandungan protein sedang dan cocok untuk makanan rendah kalori.  
    Dalam 100 gram tahu mengandung:
    - 80 kkal  
    - 8 gram protein  
    """)
    st.button("🔙 Kembali", on_click=go_to, args=("beranda",))

elif st.session_state.db_page == "ayam":
    st.header("🍗 Daging Ayam")
    st.markdown("""
    Daging ayam tanpa kulit adalah sumber protein hewani tinggi.  
    Dalam 100 gram daging ayam mengandung:
    - 165 kkal  
    - 31 gram protein  
    - Lemak rendah  
    """)
    st.button("🔙 Kembali", on_click=go_to, args=("beranda",))
