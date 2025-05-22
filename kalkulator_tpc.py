import streamlit as st
import random

# Menu
with st.popover("Menu"):
    menu = st.radio("Pilih Halaman", ["Home", "Kalkulator Total Plate Count", "Tentang Kami"])

# Tambahkan background image & style
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/736x/73/e6/3f/73e63f3961ed68e42e4628c8155ecd38.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 0px;
        border-radius: 10px;
        margin-top: 5%;
    }
    .title {
        color: Black;
        text-align: center;
    }
    h3 {
        color: Black;
    }
    .custom-text {
        color: Black;
        font-size: 16px;
        font-family: 'Calibri', 'Segoe UI', sans-serif;
    }
    .fakta-seru {
        position: fixed;
        bottom: 10px;
        left: 10px;
        background-color: rgba(255,255,255,0.9);
        padding: 12px 18px;
        border-radius: 10px;
        font-size: 14px;
        font-family: 'Segoe UI', sans-serif;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
        max-width: 300px;
    }
    </style>
""", unsafe_allow_html=True)

# Fakta Seru
fakta_list = [
    "🧫 Bakteri bisa bereproduksi dalam hitungan menit!",
    "🔬 TPC digunakan untuk mengukur keamanan pangan.",
    "🦠 Beberapa bakteri bisa bertahan di lingkungan ekstrem.",
    "💡 Pasteurisasi membantu menurunkan jumlah mikroba berbahaya.",
    "🍽️ Mencuci tangan yang benar bisa mencegah penyebaran bakteri berbahaya.",
    "🧪 TPC sering digunakan dalam pengujian produk susu, air, dan makanan olahan.",
    "🌡️ Suhu penyimpanan yang tepat dapat memperlambat pertumbuhan bakteri.",
]
fakta_acak = random.choice(fakta_list)

# Halaman: Home
if menu == "Home":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">🧫 Welcome To Calculator TPC 🦠</h1>', unsafe_allow_html=True)
    st.write("Website ini membantu menghitung **Total Plate Count (TPC)** atau jumlah koloni bakteri per mL sampel cair. Gunakan menu di atas untuk mulai.")

    st.markdown("---")
    st.subheader("📚 Apa Itu TPC?")
    st.markdown("""
    **Total Plate Count (TPC)** adalah metode untuk menghitung jumlah total bakteri hidup dalam suatu sampel. Pengujian ini penting untuk menilai kebersihan, kualitas, dan keamanan produk pangan atau air minum.

    Dalam industri pangan, TPC digunakan sebagai indikator:
    - Efektivitas proses sanitasi dan sterilisasi
    - Kualitas bahan baku dan produk akhir
    - Stabilitas penyimpanan produk

    Semakin tinggi nilai TPC, semakin besar potensi kontaminasi mikroba yang bisa membahayakan kesehatan konsumen dan menurunkan umur simpan produk.
    """)

    st.subheader("🔍 Kenapa Pengujian Mikrobiologi Itu Penting?")
    st.markdown("""
    Pengujian mikrobiologi sangat penting untuk:
    - **Melindungi konsumen** dari keracunan makanan
    - **Menjaga reputasi produsen**
    - **Memenuhi standar mutu & regulasi pangan**
    - **Mencegah kerugian ekonomi akibat produk rusak atau ditarik dari pasar**

    Oleh karena itu, pengujian seperti TPC sangat krusial dalam setiap tahapan produksi pangan, mulai dari bahan baku hingga distribusi.
    """)
    st.markdown("---")

    st.markdown(f'<div class="fakta-seru"><strong>Fakta Seru:</strong><br>{fakta_acak}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Halaman: Kalkulator Total Plate Count
elif menu == "Kalkulator Total Plate Count":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">🔢 Kalkulator Total Plate Count</h1>', unsafe_allow_html=True)

    st.write("Masukkan data pengamatan laboratorium:")

    st.subheader("🔬 Data Pengenceran 1")
    koloni_1a = st.number_input("Jumlah koloni cawan 1 - Simplo:", min_value=0, step=1, key="koloni_1a")
    koloni_1b = st.number_input("Jumlah koloni cawan 1 - Duplo (opsional):", min_value=0, step=1, key="koloni_1b")
    koloni_1c = st.number_input("Jumlah koloni cawan 1 - Triplo (opsional):", min_value=0, step=1, key="koloni_1c")
    pengenceran_1 = st.number_input("Faktor pengenceran cawan 1 (misal 10⁻³ → isi 1000):", min_value=1, step=1, key="pengenceran_1")

    st.subheader("🔬 Data Pengenceran 2")
    koloni_2a = st.number_input("Jumlah koloni cawan 2 - Simplo:", min_value=0, step=1, key="koloni_2a")
    koloni_2b = st.number_input("Jumlah koloni cawan 2 - Duplo (opsional):", min_value=0, step=1, key="koloni_2b")
    koloni_2c = st.number_input("Jumlah koloni cawan 2 - Triplo (opsional):", min_value=0, step=1, key="koloni_2c")
    pengenceran_2 = st.number_input("Faktor pengenceran cawan 2 (misal 10⁻³ → isi 1000):", min_value=1, step=1, key="pengenceran_2")

    if st.button("Hitung TPC"):
        koloni_list_1 = [k for k in [koloni_1a, koloni_1b, koloni_1c] if k > 0]
        rata_1 = koloni_1a if koloni_1b == 0 and koloni_1c == 0 else sum(koloni_list_1) / len(koloni_list_1)

        koloni_list_2 = [k for k in [koloni_2a, koloni_2b, koloni_2c] if k > 0]
        rata_2 = koloni_2a if koloni_2b == 0 and koloni_2c == 0 else sum(koloni_list_2) / len(koloni_list_2)

        tpc1 = rata_1 / pengenceran_1
        tpc2 = rata_2 / pengenceran_2
        rata_rata_tpc = (tpc1 + tpc2) / 2

        st.write(f"✅ TPC dari cawan 1: **{tpc1:.4f} CFU/mL**")
        st.write(f"✅ TPC dari cawan 2: **{tpc2:.4f} CFU/mL**")
        st.success(f"🔢 Rata-rata Total Plate Count (TPC): **{rata_rata_tpc:.4f} CFU/mL**")
        st.info("Bakteri udah dihitung, sekarang waktunya kamu santai dulu! ☕🦠")

    st.markdown('</div>', unsafe_allow_html=True)

# Halaman: Tentang Kami
elif menu == "Tentang Kami":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">👨‍🔬 Tentang Kami</h1>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Kami dari kelompok 6 kelas 1E2 Penjaminan Mutu Industri Pangan membuat website ini untuk menghitung Total Plate Count (TPC) secara cepat dan akurat. Kami sangat terbuka terhadap masukan, kritik, maupun saran demi peningkatan dan pengembangan web ini ke depannya. Jangan ragu untuk menghubungi kami!</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">💻 Dibuat menggunakan Python & Streamlit.</p>', unsafe_allow_html=True)

    st.markdown('''
        <div style="text-align: center;">
            <img src="https://i.pinimg.com/736x/2e/49/ba/2e49baed7b89068c1c1747e623b5e916.jpg" alt="This Is Us!!" style="width: 60%; border-radius: 15px; margin-top: 20px;">
            <p class="custom-text"><strong>This Is Us!!</strong></p>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
