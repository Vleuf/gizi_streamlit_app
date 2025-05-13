import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(page_title="GiziApp for Humanity", layout="wide")

# Inisialisasi session state
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

# Fungsi navigasi
def go_to_database():
    st.session_state.current_page = "database"

def go_to_quiz():
    # Reset quiz state before starting
    st.session_state.quiz_score = 0
    st.session_state.quiz_submitted = False
    st.session_state.question_index = 0
    st.session_state.user_answers = []
    st.session_state.current_page = "quiz"

def go_to_home():
    st.session_state.current_page = "beranda"

# CSS Styling for text color white and other enhancements
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
                    url('https://images.pexels.com/photos/5463890/pexels-photo-5463890.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white !important;
    }

    /* Ubah warna label teks seperti 'Pilih bahan pangan' */
    label, .css-1cpxqw2, .css-1y4p8pa, .css-1j6g3l7 {
        color: white !important;
    }

    /* Untuk teks default pada dropdown selectbox */
    .css-1d391kg, .css-1n76uvr, .css-14el2xx {
        color: white !important;
    }

    /* Style tombol sekunder */
    button[kind="secondary"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 2px solid white !important;
        border-radius: 5px !important;
        padding: 0.5em 1em !important;
        font-size: 16px !important;
    }

    button[kind="secondary"]:hover {
        background-color: rgba(255, 255, 255, 0.3) !important;
        color: black !important;
    }

    button:focus {
        outline: none !important;
        box-shadow: none !important;
    }

    /* Dropdown text color */
    .stSelectbox div[role="combobox"] > div {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== HALAMAN BERANDA ====================
if st.session_state.current_page == "beranda":
    st.title("📘 Selamat Datang di GiziApp for Humanity")
    st.markdown("""
    Aplikasi ini memberikan informasi tentang bahan pangan dan kandungan gizinya serta menyediakan kuis tentang gizi. 
    Anda dapat mengeksplorasi database bahan pangan atau menguji pengetahuan Anda melalui kuis.
    Silakan pilih halaman berikut untuk memulai 👇
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.button("📑 Buka Database Bahan Pangan", on_click=go_to_database)
    with col2:
        st.button("🎯 Mulai Kuis Gizi", on_click=go_to_quiz)

# ==================== HALAMAN DATABASE ====================
elif st.session_state.current_page == "database":
    st.title("📋 Database Bahan Pangan")
    st.button("🔙 Kembali ke Beranda", on_click=go_to_home)

    # Baca data dari file CSV
    try:
        df = pd.read_csv("deskripsi_dengan_pengertian.csv")
        bahan_list = [""] + df['Bahan'].dropna().unique().tolist()

        # Pilihan bahan pangan
        menu = st.selectbox("Pilih bahan pangan:", bahan_list)

        # Tampilkan deskripsi jika tersedia
        if menu:
            deskripsi = df[df['Bahan'] == menu]['Deskripsi Lengkap'].values[0]
            st.subheader(f"📝 {menu}")
            st.markdown(deskripsi)

    except FileNotFoundError:
        st.error("❌ File CSV tidak ditemukan. Pastikan file `deskripsi_dengan_pengertian.csv` ada di direktori yang benar.")

# ==================== HALAMAN QUIZ ====================
elif st.session_state.current_page == "quiz":
    # Tombol untuk kembali ke beranda sebelum dan setelah quiz
    st.button("🔙 Kembali ke Beranda", on_click=go_to_home)

    st.title("📘 Kuis Gizi & Pengetahuan Bahan Pangan")

    # Soal kuis (campuran)
    questions = [
        # --- GIZI ---
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
    
        # --- PENGERTIAN / DESKRIPSI ---
        {"question": "11. Tempe dibuat melalui proses apa?", "options": ["Fermentasi", "Perebusan", "Pengeringan"], "answer": "Fermentasi"},
        {"question": "12. Abalone adalah jenis makanan laut yang termasuk dalam kelompok apa?", "options": ["Kerang-kerangan", "Ikan", "Rumput laut"], "answer": "Kerang-kerangan"},
        {"question": "13. Tepung terigu biasanya berasal dari bahan apa?", "options": ["Gandum", "Jagung", "Kedelai"], "answer": "Gandum"},
        {"question": "14. Minyak zaitun diekstrak dari buah zaitun dan dikenal karena?", "options": ["Lemak tak jenuh yang sehat", "Serat tinggi", "Kadar protein tinggi"], "answer": "Lemak tak jenuh yang sehat"},
        {"question": "15. Anggur mengandung antioksidan penting bernama apa?", "options": ["Resveratrol", "Omega-3", "Laktosa"], "answer": "Resveratrol"},
    ]

    # Menampilkan soal satu per satu
    question = questions[st.session_state.question_index]
    
    st.subheader(f"📝 {question['question']}")
    options = st.radio("Pilih jawaban:", question["options"], key=f"q{st.session_state.question_index}", horizontal=True)

    # Menyimpan jawaban pengguna
    if options:
        st.session_state.user_answers.append(options)

    if st.button("✅ Lanjutkan"):
        if options == question["answer"]:
            st.session_state.quiz_score += 1
        
        # Move to the next question
        if st.session_state.question_index < len(questions) - 1:
            st.session_state.question_index += 1
        else:
            st.session_state.quiz_submitted = True

    # Setelah selesai kuis
    if st.session_state.quiz_submitted:
        st.success(f"🎯 Skor Anda: {st.session_state.quiz_score} / 15")
        if st.session_state.quiz_score == 15:
            st.balloons()
        st.button("🔁 Coba Lagi", on_click=lambda: reset_quiz())

    def reset_quiz():
        st.session_state.quiz_score = 0
        st.session_state.quiz_submitted = False
        st.session_state.question_index = 0
        st.session_state.user_answers = []
        go_to_quiz()
