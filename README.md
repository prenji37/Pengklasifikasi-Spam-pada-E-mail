# Deteksi Spam/Ham Email

Aplikasi ini adalah sistem deteksi email spam menggunakan berbagai algoritma pembelajaran mesin seperti SVM, KNN, dan Naive Bayes. Sistem ini dilengkapi dengan antarmuka pengguna berbasis Python `tkinter` untuk memudahkan penggunaan.

---

## 📂 Struktur Proyek

- **`GUI YA versi py.py`**: File utama aplikasi berbasis GUI.
- **`GUI YA.ipynb`**: Versi Jupyter Notebook dari aplikasi.
- **`Makalah Laporan_Kelompok 6_Pemrosesan Teks.pdf`**: Laporan proyek dalam format PDF.
- **`Makalah Laporan_Kelompok 6_Pemrosesan Teks.docx`**: Laporan proyek dalam format Word.
- **`Naive_model.pkl`**: Model Naive Bayes untuk deteksi spam.
- **`svm_model.pkl`**: Model SVM dengan TF-IDF.
- **`w2v_model.bin`**: Model Word2Vec untuk ekstraksi fitur.
- **`detection_result.csv`**: File hasil deteksi yang disimpan secara otomatis.
- **`ppt kelompok 6 22A.pdf`**: File presentasi kelompok.
- **`gambar/`**: Direktori berisi aset gambar untuk antarmuka pengguna.

---

## 🛠️ Fitur Utama

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
- Hasil deteksi akan disimpan secara otomatis ke dalam file `detection_result.csv`.

---

## 📊 Hasil Akurasi

| Algoritma  | Ekstraksi Fitur | Akurasi |
|------------|-----------------|---------|
| KNN        | TF-IDF          | 74%     |
| KNN        | Word2Vec        | 91%     |
| Naive Bayes| TF-IDF          | 92%     |
| Naive Bayes| Word2Vec        | 97%     |
| SVM        | TF-IDF          | 98%     |
| SVM        | Word2Vec        | 88%     |

Dari hasil tersebut, **SVM dengan TF-IDF** memiliki akurasi terbaik sebesar **98%**.

---

## 🚀 Cara Menggunakan

1. Pastikan Anda memiliki Python 3.x dan library yang dibutuhkan (lihat di bawah).
2. Jalankan aplikasi dengan perintah berikut:
   ```bash
   python "GUI YA versi py.py"
3. Masukkan teks email yang ingin dideteksi.
4. Pilih algoritma dari menu dropdown.
5. Klik tombol Detect untuk melihat hasil.
6. Gunakan tombol Clear untuk menghapus teks.

## 📦Library yang Digunakan
- `tkinter`  untuk antarmuka pengguna.
- `Scikit-learn`  untuk pembelajaran mesin.
- `Gensim untuk`  ekstraksi fitur Word2Vec.
- `Spacy`  untuk pemrosesan teks.
- `Num2Words`  untuk konversi angka menjadi teks.
