Deteksi Spam pada Email
Proyek ini bertujuan untuk mengembangkan sistem klasifikasi teks untuk mendeteksi apakah sebuah email termasuk spam atau bukan. Sistem ini menggunakan beberapa algoritma pembelajaran mesin dan metode ekstraksi fitur untuk memproses dan menganalisis data email.

Daftar Isi
Pendahuluan
Fitur dan Teknologi
Cara Penggunaan
Hasil dan Analisis
Kesimpulan
Referensi
Pendahuluan
Email spam adalah pesan elektronik yang tidak diinginkan dan dapat mengganggu pengguna. Proyek ini bertujuan untuk:

Membersihkan data email dari informasi yang tidak relevan.
Mengklasifikasikan email berdasarkan kategori spam dan non-spam.
Mengevaluasi performa algoritma untuk menentukan metode terbaik.
Metode yang digunakan mencakup ekstraksi fitur seperti TF-IDF dan Word2Vec, serta algoritma klasifikasi seperti K-Nearest Neighbors (KNN), Support Vector Machine (SVM), dan Naive Bayes.

Fitur dan Teknologi
Ekstraksi Fitur: TF-IDF, Word2Vec
Algoritma Klasifikasi:
K-Nearest Neighbors (KNN)
Support Vector Machine (SVM)
Naive Bayes
Library Python:
Scikit-learn
Gensim
Spacy
Num2Words
Cara Penggunaan
Input Email: Masukkan teks email yang ingin dideteksi ke dalam aplikasi.
Pilih Algoritma: Pilih salah satu algoritma yang tersedia (SVM, KNN, Naive Bayes).
Proses Deteksi: Klik tombol "Detect" untuk memproses teks.
Hasil: Aplikasi akan menampilkan apakah email termasuk spam atau tidak.
Kode lengkap dapat ditemukan di file spam_detector.py.

Hasil dan Analisis
KNN:
TF-IDF: Akurasi 74%
Word2Vec: Akurasi 91%
Naive Bayes:
TF-IDF: Akurasi 92%
Word2Vec: Akurasi 97%
SVM:
TF-IDF: Akurasi 98%
Word2Vec: Akurasi 88%
Dari hasil ini, model SVM dengan TF-IDF menunjukkan performa terbaik dengan akurasi 98%.

Kesimpulan
Proyek ini berhasil mengimplementasikan sistem deteksi spam dengan performa yang tinggi. Metode terbaik yang ditemukan adalah SVM dengan TF-IDF. Sistem ini dapat membantu meningkatkan efisiensi pengelolaan email dan keamanan komunikasi.
