import streamlit as st
import pandas as pd

# ========================== Konfigurasi ==========================
st.set_page_config(page_title="GiziApp for Humanity", layout="wide")

# Inisialisasi state
if "current_page" not in st.session_state:
    st.session_state.current_page = "beranda"
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = []

# ========================== Navigasi ==========================
def go_to_home():
    st.session_state.current_page = "beranda"

def go_to_database():
    st.session_state.current_page = "database"

def go_to_quiz():
    st.session_state.quiz_score = 0
    st.session_state.quiz_submitted = False
    st.session_state.question_index = 0
    st.session_state.user_answers = []
    st.session_state.current_page = "quiz"

def reset_quiz():
    st.session_state.quiz_score = 0
    st.session_state.quiz_submitted = False
    st.session_state.question_index = 0
    st.session_state.user_answers = []

# ========================== CSS Styling ==========================
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                    url('https://images.pexels.com/photos/5463890/pexels-photo-5463890.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white !important;
    }
    label, .css-1cpxqw2, .css-1y4p8pa, .css-1j6g3l7, .css-1v0mbdj {
        color: white !important;
    }
    div[role="radiogroup"] label {
        color: white !important;
    }
    .stSelectbox div[role="combobox"] > div {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# ========================== Halaman Beranda ==========================
if st.session_state.current_page == "beranda":
    st.title("📘 Selamat Datang di GiziApp for Humanity")
    st.markdown("""
    Aplikasi ini memberikan informasi tentang bahan pangan dan kandungan gizinya serta menyediakan kuis tentang gizi. 
    Anda dapat mengeksplorasi database bahan pangan atau menguji pengetahuan Anda melalui kuis.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.button("📑 Buka Database Bahan Pangan", on_click=go_to_database)
    with col2:
        st.button("🎯 Mulai Kuis Gizi", on_click=go_to_quiz)

# ========================== Halaman Database ==========================
elif st.session_state.current_page == "database":
    st.title("📋 Database Bahan Pangan")
    st.button("🔙 Kembali ke Beranda", on_click=go_to_home)

    try:
        df = pd.read_csv("deskripsi_dengan_pengertian.csv")
        bahan_list = [""] + df['Bahan'].dropna().unique().tolist()
        menu = st.selectbox("Pilih bahan pangan:", bahan_list)
        if menu:
            deskripsi = df[df['Bahan'] == menu]['Deskripsi Lengkap'].values[0]
            st.subheader(f"📝 {menu}")
            st.markdown(deskripsi)
    except FileNotFoundError:
        st.error("❌ File CSV tidak ditemukan. Pastikan file `deskripsi_dengan_pengertian.csv` ada di folder ini.")

# ========================== Halaman Kuis ==========================
elif st.session_state.current_page == "quiz":
    st.button("🔙 Kembali ke Beranda", on_click=go_to_home)
    st.title("🎯 Kuis Gizi & Pengetahuan Pangan")

    questions = [
        {"question": "1. Apa kandungan gizi utama dari Alpukat?", "options": ["Lemak", "Vitamin C", "Karbohidrat"], "answer": "Lemak"},
        {"question": "2. Apa kandungan gizi utama dari Tempe?", "options": ["Protein", "Serat", "Lemak"], "answer": "Protein"},
        {"question": "3. Apa kandungan gizi utama dari Jeruk?", "options": ["Vitamin C", "Protein", "Zat Besi"], "answer": "Vitamin C"},
        {"question": "4. Apa kandungan gizi utama dari Bayam?", "options": ["Zat Besi", "Vitamin C", "Lemak"], "answer": "Zat Besi"},
        {"question": "5. Apa kandungan gizi utama dari Nasi?", "options": ["Karbohidrat", "Protein", "Zat Besi"], "answer": "Karbohidrat"},
        {"question": "6. Apa kandungan gizi utama dari Brokoli?", "options": ["Vitamin C", "Lemak", "Serat"], "answer": "Vitamin C"},
        {"question": "7. Apa kandungan gizi utama dari Gandum?", "options": ["Serat", "Protein", "Lemak"], "answer": "Serat"},
        {"question": "8. Apa kandungan gizi utama dari Daging Ayam?", "options": ["Protein", "Karbohidrat", "Vitamin C"], "answer": "Protein"},
        {"question": "9. Apa kandungan gizi utama dari Hati Sapi?", "options": ["Zat Besi", "Lemak", "Serat"], "answer": "Zat Besi"},
        {"question": "10. Apa kandungan gizi utama dari Ubi Jalar?", "options": ["Karbohidrat", "Vitamin C", "Lemak"], "answer": "Karbohidrat"},
        {"question": "11. Tempe dibuat melalui proses apa?", "options": ["Fermentasi", "Perebusan", "Pengeringan"], "answer": "Fermentasi"},
        {"question": "12. Abalone adalah jenis makanan laut yang termasuk dalam kelompok apa?", "options": ["Kerang-kerangan", "Ikan", "Rumput laut"], "answer": "Kerang-kerangan"},
        {"question": "13. Tepung terigu biasanya berasal dari bahan apa?", "options": ["Gandum", "Jagung", "Kedelai"], "answer": "Gandum"},
        {"question": "14. Minyak zaitun diekstrak dari buah zaitun dan dikenal karena?", "options": ["Lemak tak jenuh yang sehat", "Serat tinggi", "Kadar protein tinggi"], "answer": "Lemak tak jenuh yang sehat"},
        {"question": "15. Anggur mengandung antioksidan penting bernama apa?", "options": ["Resveratrol", "Omega-3", "Laktosa"], "answer": "Resveratrol"},
    ]

    if not st.session_state.quiz_submitted:
        idx = st.session_state.question_index
        question = questions[idx]
        st.subheader(question["question"])
        user_choice = st.radio("Pilih jawaban:", question["options"], key=f"q_{idx}")

        if st.button("✅ Lanjutkan"):
            if idx >= len(st.session_state.user_answers):
                st.session_state.user_answers.append(user_choice)
                if user_choice == question["answer"]:
                    st.session_state.quiz_score += 1

            if idx + 1 < len(questions):
                st.session_state.question_index += 1
            else:
                st.session_state.quiz_submitted = True

    if st.session_state.quiz_submitted:
        st.success(f"🎯 Skor Anda: {st.session_state.quiz_score} / {len(questions)}")
        if st.session_state.quiz_score == len(questions):
            st.balloons()
        col1, col2 = st.columns(2)
        with col1:
            st.button("🔁 Coba Lagi", on_click=go_to_quiz)
        with col2:
            st.button("🏠 Kembali ke Beranda", on_click=go_to_home)
