# Deteksi Spam/Ham Email

Aplikasi ini adalah sistem deteksi email spam menggunakan berbagai algoritma pembelajaran mesin seperti SVM, KNN, dan Naive Bayes. Sistem ini dilengkapi dengan antarmuka pengguna berbasis Python `tkinter` untuk memudahkan penggunaan.

## Fitur Utama

### 1. Input Teks Email
- Masukkan teks email yang ingin dianalisis.

### 2. Pemilihan Algoritma
- Pilih algoritma deteksi:
  - **Support Vector Machine (SVM)**
  - **K-Nearest Neighbors (KNN)**
  - **Naive Bayes**

### 3. Deteksi Spam/Ham
- Klik tombol `Detect` untuk mengetahui hasil klasifikasi.

### 4. Hapus Teks
- Gunakan tombol `Clear` untuk membersihkan input.

### 5. Simpan Hasil
- Hasil deteksi akan disimpan secara otomatis ke dalam file CSV.

## Struktur Proyek

### File Utama
- **`spam_detector.py`**: File utama untuk menjalankan aplikasi.

### Model
- **`svm_model.pkl`**: Model SVM dengan TF-IDF.
- **`Naive_model.pkl`**: Model Naive Bayes.

### Library yang Digunakan
- `tkinter` untuk antarmuka pengguna.
- `Scikit-learn` untuk pembelajaran mesin.
- `Gensim` untuk ekstraksi fitur Word2Vec.
- `Spacy` untuk pemrosesan teks.
- `Num2Words` untuk konversi angka menjadi teks.

## Cara Menggunakan

1. Jalankan aplikasi dengan perintah:
   ```bash
   python spam_detector.py

2. Masukkan teks email yang ingin dideteksi.
3. Pilih algoritma dari menu dropdown.
4. Klik tombol Detect untuk melihat hasil.
5. Gunakan tombol Clear untuk menghapus teks.

## Hasil Akurasi
Algoritma	Ekstraksi Fitur	Akurasi
- KNN	TF-IDF	74%
- KNN	Word2Vec	91%
- Naive Bayes	TF-IDF	92%
- Naive Bayes	Word2Vec	97%
- SVM	TF-IDF	98%
- SVM	Word2Vec	88%

**Dari hasil tersebut, SVM dengan TF-IDF memiliki akurasi terbaik sebesar 98%.**
