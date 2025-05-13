import time
import streamlit as st

if st.button("Mulai Proses"):
    with st.spinner("Sedang diproses..."):
        time.sleep(2)
    st.success("Selesai!")
