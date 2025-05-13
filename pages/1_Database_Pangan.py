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

# Fungsi navigasi
def go_to_database():
    st.session_state.current_page = "database"

def go_to_quiz():
    st.session_state.current_page = "quiz"

def go_to_home():
    st.session_state.current_page = "beranda"

# CSS Styling
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

    label, .css-1cpxqw2, .css-1y4p8pa {
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
    st.markdown("""
    Jawablah 15 soal berikut yang mencakup:
    - **10 soal** tentang kandungan gizi (lemak, protein, vitamin C, zat besi, serat, karbohidrat),
    - **5 soal** tentang pengertian atau deskripsi bahan pangan dari database.
    
    Pilih jawaban yang paling tepat di setiap pertanyaan!
    """)

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

    # Form kuis
    with st.form("kuis_gizi_pengertian"):
        score = 0
        user_answers = []

        for i, q in enumerate(questions):
            st.markdown(q["question"])
            selected = st.radio(f"Jawaban Anda untuk Soal {i+1}:", q["options"], key=f"q{i}")
            user_answers.append((selected, q["answer"]))
            st.markdown("---")

        submitted = st.form_submit_button("✅ Periksa Jawaban")

        if submitted and not st.session_state.quiz_submitted:
            for selected, correct in user_answers:
                if selected == correct:
                    score += 1
            st.session_state.quiz_score = score
            st.session_state.quiz_submitted = True

    # Hasil akhir
    if st.session_state.quiz_submitted:
        st.success(f"🎯 Skor Anda: {st.session_state.quiz_score} / 15")
        if st.session_state.quiz_score == 15:
            st.balloons()
        st.button("🔁 Coba Lagi", on_click=lambda: reset_quiz())

    def reset_quiz():
        st.session_state.quiz_score = 0
        st.session_state.quiz_submitted = False
        go_to_quiz()
