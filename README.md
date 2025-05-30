# Laporan Proyek Machine Learning - Muhammad Teguh Alfian

## Project Overview - Content-Based Filtering Book System Recommendation <br>
![image](https://github.com/user-attachments/assets/f3e583fa-9ac5-4cf7-91de-e3d51603ba26)<br>
Perkembangan teknologi informasi telah mengubah cara manusia mengakses dan mengonsumsi berbagai jenis konten, termasuk buku. Saat ini, perpustakaan digital, toko buku daring, dan aplikasi pembaca telah menyediakan jutaan judul buku yang dapat diakses kapan saja dan di mana saja. Di satu sisi, hal ini memberikan kebebasan dan fleksibilitas bagi pengguna; namun di sisi lain, justru menciptakan tantangan baru: kelebihan informasi (information overload). Pengguna sering kali kesulitan menemukan buku yang benar-benar sesuai dengan minat, preferensi, atau kebutuhan mereka karena banyaknya pilihan yang tersedia.

Untuk mengatasi tantangan ini, sistem rekomendasi menjadi salah satu solusi yang sangat efektif. Sistem ini dapat menyaring informasi dan memberikan saran yang dipersonalisasi kepada pengguna berdasarkan berbagai pendekatan, seperti collaborative filtering, content-based filtering, dan hybrid approaches. Dalam penelitian ini, content-based filtering menjadi pendekatan yang sangat relevan karena memanfaatkan informasi yang melekat pada item (buku), seperti judul, penulis, dan kategori.

Salah satu metode paling umum untuk memproses dan merepresentasikan data teks adalah teknik Term Frequency-Inverse Document Frequency (TF-IDF). TF-IDF membantu mengidentifikasi kata-kata penting dari teks, kemudian digunakan untuk merepresentasikan buku dalam bentuk vektor. Vektor-vektor ini dapat dibandingkan satu sama lain untuk mengukur tingkat kemiripan antara buku-buku tersebut.

Dalam mengukur kemiripan antar vektor, digunakan beberapa pendekatan matematis, seperti cosine similarity yang menghitung kesamaan arah antara dua vektor, dan euclidean distance yang mengukur jarak absolut antara titik-titik vektor dalam ruang multidimensi. Kedua metode ini memiliki karakteristik masing-masing dalam mengidentifikasi kemiripan, dan penting untuk mengevaluasi efektivitasnya dalam konteks sistem rekomendasi buku.

Dengan menggunakan pendekatan ini, sistem rekomendasi tidak hanya menjadi alat bantu dalam memilih bacaan, tetapi juga dapat meningkatkan pengalaman pengguna secara keseluruhan, meningkatkan kepuasan, keterlibatan (engagement), serta membantu memperluas wawasan pembaca dengan memberikan rekomendasi yang sesuai dengan preferensi mereka.

## Business Understanding

### Problem Statements

- Diperlukan sistem yang mampu memberikan rekomendasi buku secara relevan berdasarkan informasi yang tersedia dalam deskripsi atau metadata buku.
- Tantangan muncul dalam proses ekstraksi informasi penting dari teks deskripsi buku agar dapat direpresentasikan dalam bentuk numerik yang dapat diolah.
- Diperlukan metode pengukuran kemiripan antar buku yang efektif untuk menentukan seberapa mirip satu buku dengan yang lain berdasarkan fitur teks.

### Goals

- Mengembangkan sistem rekomendasi buku berbasis konten (content-based filtering) dengan memanfaatkan deskripsi buku.
- Menerapkan teknik TF-IDF untuk mengekstraksi fitur penting dari teks.
- Mengimplementasikan metode cosine similarity dan euclidean distance untuk menghitung kemiripan antar buku.

### Solution Approach

- Pengumpulan dataset buku.
- Exploratory berdasarkan dataset yang sudah dikumpulkan.
- Data cleaning and preprocessing.
- Ekstraksi fitur dengan TF-IDF.
- Membuat sistem rekomendasi berdasarkan perhitungan Cosine Similarity dan Euclidean Distance.
- Evaluasi dengan membandingkan hasil rekomendasi berdasarkan Cosine Similarity dan Euclidean Distance.
  
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

- Mengetahui informasi singkat dataset seperti melihat nama, jumlah data, dan tipe data di tiap kolom. Hal ini mempermudah proses cleaning.<br>
![image](https://github.com/user-attachments/assets/7debd94c-b8cf-4ff4-9c6f-7f550ed108dc)<br>
- Mengetahui deskripsi statistik dataset untuk melihat keseimbangan dan logisnya data.<br>
![image](https://github.com/user-attachments/assets/51fdfda6-098c-4549-873f-28ef968b9050)<br>
- Visualisasi untuk mengeksplorasi data.
  - Top 10 Berdasarkan Kategori Buku. <br>
  ![image](https://github.com/user-attachments/assets/4bfb727d-d97f-457c-8367-d889d99320d9)<br>
  - Top 10 Penulis dengan Judul Buku Terbanyak.<br>
  ![image](https://github.com/user-attachments/assets/cdb7bd46-74b9-4c00-bcc8-b14878fb3eef)<br>
  - Top 10 Penulis dengan Jumlah Halaman Terbanyak.<br>
  ![image](https://github.com/user-attachments/assets/ee884cd8-6a2d-4fa4-9440-35c2797294ab)<br>
- Data Cleaning:
  - Feature Selection: Memilih kolom yang penting-penting saja. Seperti kolom title, authors, dan categories. Kemudian, kolom-kolom tersebut digabungkan menjadi sebuah kolom baru dengan nama 'combined'. Alasan digabungkan adalah untuk persiapan sebelum diekstraksi fiturnya.<br>
  ![image](https://github.com/user-attachments/assets/b1cc01ba-db54-477a-9785-222d5ce1194d)<br>
  ![image](https://github.com/user-attachments/assets/69cc3302-8bc8-401e-819a-2ab90998af43)<br>
  - Null Handling: Menangani data null dengan string kosong (''). String kosong dipilih karena pada saat ekstraksi fitur, string kosong tidak akan mempengaruhi hasil ekstraksi.

## Modeling

- Ekstraksi Fitur dengan TF-IDF
- Sistem Rekomendasi dengan Cosine Similarity.
  - Definisi: Ukuran kemiripan antara dua vektor berdasarkan sudut (cosine) di antara keduanya, bukan jaraknya. Cosine similarity digunakan untuk mengukur seberapa mirip arah dua vektor dalam ruang multidimensi, tanpa memperhatikan panjangnya (magnitudo). Dalam konteks content-based filtering, semakin tinggi nilai cosine similarity-nya maka semakin tinggi kemiripannya. Sebaliknya, semakin rendah nilai cosine similarity-nya maka semakin rendah kemiripannya.
  - Rumus:<br>
  ![image](https://github.com/user-attachments/assets/bfb02122-bda9-47b7-a759-51ea1dae5ca4)<br>
  - Flow:
  - Hasil Percobaan: <br>
    ![image](https://github.com/user-attachments/assets/eba7c95d-8e0e-458f-86d0-a07019369693)<br>
- Sistem Rekomendasi dengan Euclidean Distance.
  - Definisi: Salah satu metode pengukuran jarak paling dasar dan umum dalam ruang multidimensi. Euclidean Distance mengukur jarak lurus (garis terpendek) antara dua titik dalam ruang vektor. Dalam konteks content-based filtering, semakin pendek distancenya maka semakin tinggi kemiripannya. Sebaliknya, semakin panjang distancenya maka semakin rendah kemiripannya.
  - Rumus:<br>
    ![image](https://github.com/user-attachments/assets/b0abe8eb-b62f-4d32-bb76-6dad907c3277)<br>
  - Flow:<br>
    ![image](https://github.com/user-attachments/assets/de16404f-6322-4933-ba85-cbf44a5aefd3)<br>
    - Dimulai dengan mendefinisikan fungsi recommend_books_euclidean_with_distance yang menerima judul buku dan matriks jarak Euclidean sebagai masukan. Pertama, judul buku masukan diubah menjadi huruf kecil untuk standarisasi. Fungsi kemudian memeriksa apakah judul buku tersebut ada dalam indices (pemetaan judul ke indeks numerik). Jika tidak ditemukan, pesan kesalahan akan dikembalikan.
    - Apabila buku ditemukan, fungsi mengambil indeks numerik buku tersebut dari indices. Dengan indeks ini, seluruh baris yang sesuai dari matriks euclidean_dist_matrix diakses, yang berisi skor jarak Euclidean antara buku yang dicari dengan semua buku lain. Skor-skor ini kemudian diubah menjadi daftar tuple yang masing-masing berisi (indeks buku, skor distance).
    - Daftar skor distance ini kemudian diurutkan dari yang terkecil ke terbesar, karena distance yang lebih kecil menunjukkan kemiripan yang lebih tinggi. Sepuluh skor teratas diambil, dengan mengabaikan skor pertama yang merupakan distance buku itu sendiri dengan dirinya sendiri (yang nilainya nol).
    - Selanjutnya, sebuah daftar kosong bernama recommendations disiapkan. Fungsi kemudian mengulang setiap dari 10 skor distance teratas yang telah diurutkan. Untuk setiap pasangan (indeks buku, skor jarak), informasi detail buku seperti title, author, dan average_rating diambil dari DataFrame df asli dan diubah menjadi sebuah dictionary. Skor Euclidean Distance kemudian ditambahkan sebagai entri baru dalam dictionary informasi buku tersebut. Dictionary yang sudah lengkap ini kemudian ditambahkan ke daftar recommendations. Setelah perulangan selesai, fungsi mengembalikan daftar recommendations ini sebagai sebuah DataFrame Pandas.
  - Hasil Percobaan:<br>
    ![image](https://github.com/user-attachments/assets/a5981552-c546-4811-acf5-41b468934728)<br>
## Evaluation

