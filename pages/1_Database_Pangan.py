import streamlit as st

st.set_page_config(page_title="Database Pangan")

st.title("Database Bahan Pangan")

st.markdown("Pilih bahan pangan untuk melihat informasi gizi:")

bahan = st.selectbox(
    "Pilih bahan pangan",
    ["Nasi Putih", "Telur Ayam", "Tempe", "Tahu", "Daging Ayam"]
)

st.markdown("---")

if bahan == "Nasi Putih":
    st.header("🍚 Nasi Putih")
    st.markdown("""
    Nasi putih adalah sumber karbohidrat utama di Indonesia.  
    Dalam 100 gram, nasi mengandung sekitar:
    - 175 kkal  
    - 39 gram karbohidrat  
    - Sedikit protein dan lemak  
    """)

elif bahan == "Telur Ayam":
    st.header("🥚 Telur Ayam")
    st.markdown("""
    Telur merupakan sumber protein hewani yang sangat baik.  
    Dalam 100 gram telur mengandung sekitar:
    - 155 kkal  
    - 13 gram protein  
    """)

elif bahan == "Tempe":
    st.header("🍱 Tempe")
    st.markdown("""
    Tempe adalah sumber protein nabati hasil fermentasi kedelai.  
    Dalam 100 gram tempe mengandung:
    - 193 kkal  
    - 19 gram protein  
    - Lemak sehat  
    """)

elif bahan == "Tahu":
    st.header("🍥 Tahu")
    st.markdown("""
    Tahu memiliki kandungan protein sedang dan cocok untuk makanan rendah kalori.  
    Dalam 100 gram tahu mengandung:
    - 80 kkal  
    - 8 gram protein  
    """)

elif bahan == "Daging Ayam":
    st.header("🍗 Daging Ayam")
    st.markdown("""
    Daging ayam tanpa kulit adalah sumber protein hewani tinggi.  
    Dalam 100 gram daging ayam mengandung:
    - 165 kkal  
    - 31 gram protein  
    - Lemak rendah  
    """)

st.markdown("---")
st.caption("*Catatan: Nilai gizi dapat bervariasi tergantung pada cara pengolahan dan jenis bahan pangan.*")
