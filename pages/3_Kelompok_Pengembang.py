import time
import streamlit as st

if st.button("Mulai Proses"):
    with st.spinner("Sedang diproses..."):
        time.sleep(2)
    st.success("Selesai!")


import streamlit as st

st.title("🎉 Ucapan Selamat!")

if st.button("Tekan untuk Merayakan"):
    st.success("Selamat! Kamu berhasil menyelesaikan tugas.")
    st.snow()  # Efek konfeti akan muncul
