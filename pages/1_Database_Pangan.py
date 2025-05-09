import streamlit as st

st.set_page_config(page_title="Database Pangan")

st.title("Database Bahan Pangan")

# Pilihan menu
menu = st.selectbox(
    "Pilih halaman:",
    ["Beranda", "Nasi Putih", "Telur Ayam", "Tempe", "Tahu", "Daging Ayam"]
)

st.markdown("---")

# Konten berdasarkan pilihan
if menu == "Beranda":
    st.header("📘 Selamat Datang di Database Bahan Pangan")
    st.markdown("""
    Aplikasi ini berisi informasi singkat mengenai bahan pangan umum yang digunakan dalam perhitungan gizi.  
    Silakan pilih bahan pangan dari menu di atas untuk melihat detail kandungan gizinya.
    
    **Daftar bahan pangan:**
    - Nasi Putih
    - Telur Ayam
    - Tempe
    - Tahu
    - Daging Ayam

    ---
    *Catatan: Nilai gizi dapat bervariasi tergantung pada cara pengolahan dan jenis bahan pangan.*
    """)

elif menu == "Nasi Putih":
    st.header("🍚 Nasi Putih")
    st.markdown("""
    Nasi putih adalah sumber karbohidrat utama di Indonesia.  
    Dalam 100 gram, nasi mengandung sekitar:
    - 175 kkal  
    - 39 gram karbohidrat  
    - Sedikit protein dan lemak  
    """)

elif menu == "Telur Ayam":
    st.header("🥚 Telur Ayam")
    st.markdown("""
    Telur merupakan sumber protein hewani yang sangat baik.  
    Dalam 100 gram telur mengandung sekitar:
    - 155 kkal  
    - 13 gram protein  
    """)

elif menu == "Tempe":
    st.header("🍱 Tempe")
    st.markdown("""
    Tempe adalah sumber protein nabati hasil fermentasi kedelai.  
    Dalam 100 gram tempe mengandung:
    - 193 kkal  
    - 19 gram protein  
    - Lemak sehat  
    """)

elif menu == "Tahu":
    st.header("🍥 Tahu")
    st.markdown("""
    Tahu memiliki kandungan protein sedang dan cocok untuk makanan rendah kalori.  
    Dalam 100 gram tahu mengandung:
    - 80 kkal  
    - 8 gram protein  
    """)

elif menu == "Daging Ayam":
    st.header("🍗 Daging Ayam")
    st.markdown("""
    Daging ayam tanpa kulit adalah sumber protein hewani tinggi.  
    Dalam 100 gram daging ayam mengandung:
    - 165 kkal  
    - 31 gram protein  
    - Lemak rendah  
    """)

