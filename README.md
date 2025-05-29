# Laporan Proyek Machine Learning - Muhammad Teguh Alfian

## Project Overview - Sistem Rekomendasi Buku dengan TF-IDF 

Di era digital saat ini, jumlah buku yang tersedia terus meningkat secara eksponensif, baik dalam bentuk fisik maupun digital. Hal ini seringkali menimbulkan tantangan bagi pembaca untuk menemukan buku yang relevan dan sesuai dengan preferensi mereka. Sistem rekomendasi buku menjadi solusi krusial untuk mengatasi information overload ini, membantu pengguna menemukan bacaan baru, dan meningkatkan pengalaman membaca mereka.

Metode content-based filtering adalah salah satu pendekatan populer dalam sistem rekomendasi. Metode ini bekerja dengan menganalisis karakteristik item (buku) untuk merekomendasikan item yang serupa dengan yang disukai pengguna di masa lalu. Dengan kata lain, jika seorang pengguna menyukai buku fiksi ilmiah, sistem akan merekomendasikan buku fiksi ilmiah lainnya berdasarkan fitur-fitur yang dimiliki buku tersebut.

Dalam implementasi sistem rekomendasi content-based filtering, ekstraksi fitur adalah langkah penting untuk mengubah data teks (seperti judul, deskripsi, penulis, dan kategori) menjadi representasi numerik yang dapat diproses oleh algoritma. Salah satu teknik ekstraksi fitur yang efektif untuk data teks adalah TF-IDF (Term Frequency-Inverse Document Frequency). TF-IDF memberikan bobot pada kata-kata berdasarkan seberapa sering kata tersebut muncul dalam suatu dokumen (buku) dan seberapa jarang kata tersebut muncul di seluruh korpus dokumen. Ini membantu mengidentifikasi kata kunci yang paling relevan untuk setiap buku.

Setelah fitur diekstraksi, cosine similarity digunakan untuk mengukur kemiripan antara dua vektor fitur. Semakin tinggi nilai cosine similarity antara dua buku, semakin mirip kedua buku tersebut. Dengan demikian, sistem dapat mengidentifikasi buku-buku yang secara semantik paling dekat dengan buku yang disukai pengguna, sehingga menghasilkan rekomendasi yang relevan dan personal.

## Business Understanding

### Problem Statements

- Diperlukan metode efektif untuk mengekstraksi fitur dari data tekstual buku (judul, deskripsi, penulis, dan kategori) menggunakan metode TF-IDF guna merepresentasikan konten buku secara numerik.
- Diperlukan pengukuran tingkat kemiripan antar buku berdasarkan fitur yang diekstraksi menggunakan cosine similarity.
- Sistem rekomendasi berbasis content-based filtering dengan ekstraksi fitur TF-IDF dan cosine similarity perlu dikembangkan agar dapat memberikan rekomendasi buku yang relevan dan personal kepada pengguna.

### Goals

- Menganalisis dan mengimplementasikan metode TF-IDF untuk mengekstraksi fitur dari data tekstual buku.
- Mengimplementasikan perhitungan cosine similarity untuk mengukur kemiripan antara buku-buku berdasarkan fitur yang diekstraksi.
- Membangun sistem rekomendasi buku berbasis content-based filtering yang mampu merekomendasikan buku-buku yang relevan berdasarkan preferensi pengguna.

### Solution Approach


## Data Understanding

- Kumpulan data ini merupakan kumpulan informasi komprehensif tentang buku, yang dirancang untuk digunakan dalam sistem rekomendasi dan pengembangan chatbot. Kumpulan data ini mencakup detail tentang berbagai macam buku, sehingga cocok untuk berbagai aplikasi di bidang pembelajaran mesin, pemrosesan bahasa alami, dan kecerdasan buatan.
- Terdapat 6810 baris dan 12 kolom.
- Kondisi dataset tidak ada data duplikat, tapi ada missing value pada beberapa kolom seperti subtitle, authors, categories, thumbnails, description, published_year, average_rating, num_pages, dan ratings_count. Sehingga diperlukan cleaning terhadap beberapa kolom tersebut.
- Link Dataset: [Kaggle](https://www.kaggle.com/datasets/abdallahwagih/books-dataset).
 
Variabel-variabel pada Books Dataset adalah sebagai berikut:
- isbn13: Nomor ISBN (International Standard Book Number) versi 13 digit yang unik untuk setiap buku. 
- isbn10: Nomor ISBN versi 10 digit. Ini juga merupakan identifikasi unik untuk buku, tetapi dalam format yang lebih lama.
- title: Judul buku. 
- subtitle: Subjudul buku, jika ada. 
- authors: Nama penulis buku.
- categories: Kategori atau genre buku. 
- thumbnail: URL atau lokasi gambar thumbnail buku. 
- description: Deskripsi atau ringkasan tentang buku.
- published_year: Tahun penerbitan buku.
- average_rating: Rata-rata penilaian buku berdasarkan ulasan. 
- num_pages: Jumlah halaman dalam buku.
- ratings_count: Jumlah total penilaian yang diterima buku.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data beserta insight atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.
