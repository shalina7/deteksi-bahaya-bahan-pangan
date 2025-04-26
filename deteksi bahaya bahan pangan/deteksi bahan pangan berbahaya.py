Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import streamlit as st
... import pandas as pd
... 
... st.set_page_config(page_title="Deteksi Bahan Pangan Berbahaya", layout="wide")
... st.title("🔬 Deteksi Bahan Pangan Palsu & Berbahaya")
... st.caption("Cari bahan pangan berdasarkan ciri-ciri fisik mencurigakan 🚨")
... 
... st.markdown("---")
... 
... # 📥 Membaca CSV otomatis
... try:
...     data = pd.read_csv("bahan_pangan_ciri_fisik.csv")
...     st.success("✅ Data berhasil dimuat otomatis!")
...     st.write(f"Jumlah data: **{data.shape[0]}** bahan pangan")
... 
...     with st.expander("👀 Lihat 10 Data Pertama"):
...         st.dataframe(data.head(10), use_container_width=True)
... except FileNotFoundError:
...     st.error("❗ File CSV tidak ditemukan. Pastikan file 'bahan_pangan_ciri_fisik.csv' ada di folder yang sama.")
