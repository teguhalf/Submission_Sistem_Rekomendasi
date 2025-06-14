# -*- coding: utf-8 -*-
"""Book_Recommendation_System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zezJ6cr_O52DOm-RCByarcO-7OM9b0CA

# Import Library
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

"""# Data Loading"""

df = pd.read_csv('book.csv')
df.head()

"""# Exploratory Data Analysis

## Mengetahui informasi singkat dataset
"""

df.info()

"""**Insight:**
- Terdapat 6810 baris dan 12 kolom.
- Terdapat 4 kolom float (published_year, average_rating, num_pages, ratings_count), 1 kolom integer (isbn13), dan 7 kolom object (isbn10, title, subtitle, authors, categories, thumbnail, description).
- Terdapat ketidak seimbangan jumlah data (data null).
- Memori yang digunakan 638.6 KB.

## Mengetahui deskripsi statistik dataset
"""

df.describe()

"""**Insight:**
- Kolom num_pages memiliki nilai minimum sebesar 0 yang tidak rasional untuk sebuah buku
"""

df.isnull().sum()

df.duplicated().sum()

"""Insight:
- Kolom yang memiliki nilai null yaitu subtitle (4429), authors (72), categories (99), thumbnail (329) description (262), published_year (6), avergae_rating (43), num_pages (43), dan ratings_count (43).
- Tidak terdapat data duplikat pada dataset
"""

# Menghitung jumlah data pada kolom 'categories'
category_counts = df['categories'].value_counts()

# Memilih top 10 terbanyak berdasarkan kategori
top_10_categories = category_counts.head(10)

# Create a bar plot
plt.figure(figsize=(8, 4))
sns.barplot(x=top_10_categories.values, y=top_10_categories.index, palette='viridis')
plt.title('Top 10 Book Categories')
plt.xlabel('Number of Books')
plt.ylabel('Category')
plt.tight_layout()
plt.show()
print('\n')
print(category_counts[:10])

"""**Insight:**
- Kategori buku yang paling banyak adalah fiksi sejumlah 2588. Jumlah ini, 3x lipat dari kategori terbanyak kedua yaitu Juvenile Fiction.
- Ini artinya kategori fiksi lebih banyak penggemarnya daripada kategori buku lain.

"""

# Menghitung jumlah data pada kolom 'authors'
author_counts = df['authors'].value_counts()

# Memilih top 10 terbanyak berdasarkan author
top_10_authors = author_counts.head(10)

# Create a bar plot
plt.figure(figsize=(8, 4))
sns.barplot(x=top_10_authors.values, y=top_10_authors.index, palette='viridis')
plt.title('Top 10 Book Authors')
plt.xlabel('Number of Books')
plt.ylabel('Author')
plt.tight_layout()
plt.show()
print('\n')
print(author_counts[:10])

"""**Insight:**
- Agatha Christe menulis buku terbanyak dengan jumlah 37 buku.
- Stephen King dan William Shakespeare pada urutan kedua (36 buku) dan ketiga (35 buku)
"""

# Groupby author dan num_pages
author_pages = df.groupby('authors')['num_pages'].sum()

# Top 10
top_10_author_pages = author_pages.sort_values(ascending=False).head(10)
print("Top 10 Authors by Total Number of Pages:")

# Bar plot author dengan total num_pages terbanyak
plt.figure(figsize=(8, 4))
sns.barplot(x=top_10_author_pages.values, y=top_10_author_pages.index, palette='viridis')
plt.title('Top 10 Authors by Total Number of Pages')
plt.xlabel('Total Number of Pages')
plt.ylabel('Author')
plt.tight_layout()
plt.show()
print('\n')
print(top_10_author_pages)

"""**Insight:**
- Stephen King menuliskan sebanyak 18967 halaman, membuatnya menduduki penulis nomer 1 dengan jumlah halaman terbanyak ditulis
- Agathe Christie nomer 2 dengan jumlah halaman  12803.
- John Ronald Reuel Tolkien nomer 3 dengan jumlah halaman 12424.

# Data Cleaning dan Preprocessing

## Feature Selection dan Null Handling
"""

# Menggabungkan kolom
df['combined'] = (
    df['title'].fillna('') + ' ' +
    df['authors'].fillna('') + ' ' +
    df['categories'].fillna('') + ' '
)

# Menampilkan kolom 5 kolom combined
print(55*'=')
print('Data Kolom Combined:')
print(df['combined'].head())
print(55*'=')
print('Jumlah Null di Kolom Combined:')
print(df['combined'].isnull().sum())
print(55*'=')

"""**Insight:**
- Data null dapat mengakibatkan kegagalan dalam proses ektraksi fitur. Oleh karena itu, data null diganti dengan string kosong.
- Mengapa string kosong? Karena string kosong tidak bernilai apa-apa sehingga tidak akan mempengaruhi proses ekstraksi fitur.
- Kolom baru bernama 'combined' berhasil dibuat dengan menggabungkan kolom 'title', 'author', dan 'categories'.

# Sistem Rekomendasi

## Ektraksi Fitur dengan TF-IDF
"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Stopwords kata-kata yang tidak memberi makna
tfidf = TfidfVectorizer(stop_words='english')

# Transformasi teks menjadi matriks vektor pada kolom combined
tfidf_matrix = tfidf.fit_transform(df['combined'])

# Ukuran Matrix TF-IDF
tfidf_matrix.shape

"""**Insight:**
- Dimensi Matriks TF-IDF berukuran 6810 (baris) dan 10317 (kolom)

## Mendapatkan Rekomendasi dengan Cosine Similarity

### Menghitung Cosine Similarity

Nilai Cosine Similarity berkisar dari 0 hingga 1:
- 1: Menunjukkan vektor yang identik (sangat mirip).
- 0: Menunjukkan vektor yang ortogonal (tidak ada kemiripan sama sekali).
- Artinya, semakin mendekati angka 1 berarti semakin tinggi kemiripannya. Sedangkan semakin mendekati angka 0, berarti semakin rendah kemiripannya
"""

from sklearn.metrics.pairwise import cosine_similarity

# Hitung cosine similarity antar buku
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
cosine_sim

cosine_sim.shape

"""**Insight:**
- Dimensi Matriks Cosine Similarity berukuran 6810 (baris) dan 6810 (kolom)

### Mendapatkan Rekomendasi dengan Cosine Similarity

Flow Sistem Rekomendasi dengan Cosine Similarity:
- Dimulai dengan membuat Series bernama indices yang memetakan setiap judul buku (dalam lowercase) ke indeks barisnya dalam DataFrame df. Hal ini memungkinkan untuk melakukan pencarian cepat.

- Jika buku ditemukan, indeks numeriknya diambil dan digunakan untuk mengakses baris terkait dalam matriks cosine_sim. Sepuluh skor teratas akan dipilih, kecuali skor pertama karena mewakili buku itu sendiri.

- Fungsi kemudian membuat daftar recommendations yang berisi informasi title, author, dan average_rating buku-buku rekomendasi, serta menambahkan skor cosine_similarity ke masing-masing index.
"""

# Buat index dari judul buku (lowercase)
indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()

# Membuat fungsi untuk rekomendasi berdasarkan judul dan nilai cosine similarity
def recommend_books_with_similarity(title, cosine_sim=cosine_sim):
    title = title.lower() # Lowercase title
    if title not in indices:
        return f"Buku berjudul '{title}' tidak ditemukan dalam data."

    # Mendapatkan index numerik dari kolom title
    idx = indices[title]
    # Iterasi matrix cosine similarity
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Ambil 10 termirip (selain dirinya sendiri)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]

    # Membuat list baru
    recommendations = []
    # Looping utk mendapatkan data informasi buku dan nilai cosine similarity
    for i, score in sim_scores:
        book_info = df[['title', 'authors', 'average_rating']].iloc[i].to_dict()
        book_info['cosine_similarity_score'] = score
        # Menyimpan data ke dalam dict
        recommendations.append(book_info)

    return pd.DataFrame(recommendations)

# Mencoba sistem rekomendasi (cosine similarity) dengan memasukkan satu judul buku
recommend_books_with_similarity("Charade")

"""**Insight:**
Dengan memasukkan judul 'Charade' karya 'Sandra Brown', dapat dilihat bahwa:
-  Kemiripan paling tinggi yaitu dengan 'Two Alone' yang memiliki cosine similarity sebesar 0.69
- Disusul 'Three Complete Novels' yang memiliki cosine similarity sebesar 0.54
- Angka semakin menurun dari atas ke bawah, yang artinya semakin ke bawah semakin tidak mirip.
- Dari top 10 buku yang direkomendasikan semuanya adalah karya 'Sandra Brown'.

## Mendapatkan Rekomendasi dengan Euclidean Distance

## Menghitung Euclidean Distance

Euclidean Distance mengukur jarak garis lurus terpendek antara dua titik dalam satu ruang. Dari metrik ini dapat diketahui bahwa:
- Nilai minimumnya adalah 0.
- Nilai maksimum tidak pasti tergantung pada dimensi fitur.
- Artinya, semakin mendekati nilai 0, maka semakin tinggi kemiripan. Sedangkan semakin jauh dari angka 0, maka semakin rendah kemiripannya.
"""

from sklearn.metrics.pairwise import euclidean_distances

# Hitung Euclidean Distance antar buku
euclidean_dist_matrix = euclidean_distances(tfidf_matrix, tfidf_matrix)
euclidean_dist_matrix

# Membuat fungsi untuk rekomendasi berdasarkan judul dan nilai euclidean distance
def recommend_books_euclidean_with_distance(title,
                                            euclidean_dist=euclidean_dist_matrix):
    title = title.lower() # Lowercase title
    if title not in indices:
        return f"Buku berjudul '{title}' tidak ditemukan dalam data."

    # Mendapatkan index numerik dari kolom title
    idx = indices[title]
    # If multiple indices are returned (due to duplicate titles), take the first one
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]

    # Iterasi matrix euclidean distance
    dist_scores = list(enumerate(euclidean_dist[idx]))
    # Ambil 10 terdekat (selain dirinya sendiri)
    distance_scores = sorted(dist_scores, key=lambda x: x[1])[1:11]

    # Membuat list baru
    recommendations = []
    # Looping utk mendapatkan data informasi buku dan nilai cosine similarity
    for i, distance in distance_scores:
        book_info = df[['title', 'authors', 'average_rating']].iloc[i].to_dict()
        book_info['distance'] = distance
        # Menyimpan data ke dalam dict
        recommendations.append(book_info)

    return pd.DataFrame(recommendations)

"""### Mendapatkan Rekomendasi dengan Euclidean Distance

Flow Sistem Rekomendasi dengan Euclidean Distance:
- Dimulai dengan mendefinisikan fungsi recommend_books_euclidean_with_distance yang menerima judul buku dan matriks Euclidean Distance. Judul diubah ke huruf kecil dan dicek keberadaannya dalam indices. Hal ini akan melakukan pencarian cepat.
- Jika ditemukan, indeks buku digunakan untuk mengambil skor Euclidean Distance dari matriks, yang kemudian diubah menjadi daftar tuple dan diurutkan dari jarak terkecil ke terbesar. Sepuluh skor teratas dipilih, mengabaikan skor pertama yang bernilai nol.
"""

# Mencoba sistem rekomendasi (euclidean distance) dengan memasukkan satu judul buku
recommend_books_euclidean_with_distance("Charade")

"""**Insight:**
Dengan memasukkan judul 'Charade' karya 'Sandra Brown', dapat dilihat bahwa:
-  Jarak paling dekat yaitu dengan 'Two Alone' yang memiliki euclidean distance sebesar 0.77
- Disusul 'Three Complete Novels' yang memiliki euclidean distance sebesar 0.95
- Angka distance semakin naik dari atas ke bawah, yang artinya semakin ke bawah semakin tidak mirip.
- Dari top 10 buku yang direkomendasikan semuanya adalah karya 'Sandra Brown'.

**Kesimpulan:**
- Dari hasil percobaan dengan judul buku yang sama, yaitu menggunakan cosine similarity dan euclidean distance, keduanya memberikan rekomendasi buku yang sama.
- Dengan metode cosine similarity, nilai tertinggi yaitu 0.69
- Dengan metode euclidean distance, jarak terdekat yaitu 0.77

## Evaluasi

Melakukan evaluasi dengan recall@k dengan tujuan untuk melihat seberapa baik sistem rekomendasi yang dibuat
"""

# Fungsi recall@k
def recall_at_k(recommended_items, relevant_items, k):
    """
    Menghitung Recall@k.

    Args:
      recommended_items: List item yang direkomendasikan.
      relevant_items: List item yang relevan (ground truth).
      k: Jumlah item teratas yang dipertimbangkan.

    Returns:
      Nilai Recall@k.
    """
    if not relevant_items: # Menangani kasus jika tidak ada item relevan sama sekali
        return 0.0

    recommended_at_k = recommended_items[:k]
    relevant_found = [item for item in recommended_at_k if item in relevant_items]

    return len(relevant_found) / len(relevant_items)

# Simulasi Data Hasil Rekomendasi (Cosine Similarity)
# Asumsikan ini adalah rekomendasi untuk 3 buku yang berbeda: 'Charade', 'The Hobbit', '1984'
recommendations_cosine = {
    'Charade': [
        'Two Alone', 'Three Complete Novels', 'Where Theres Smoke', 'A Whole New Light', 'Exclusive', 'Ricochet',
        'Love Beyond Reason', 'Adams Fall', 'Texas! Trilogy', 'Heavens Price'
    ],
    'Miss Marple': [
        'The Big Four', 'A Murder is Announced', 'The Thirteen Problems', 'The Hollow', 'The Listerdale Mystery',
        'Death in the Clouds', 'Appointment with Death', 'Murder in Mesopotamia', 'Spiders Web', 'The Mysterious Mr. Quin'
    ],
    '1984': [
        'Animal Farm and 1984', 'The Complete Works of George Orwell', 'Orwell in Spain', 'The Orwell Reader', 'Essays',
        'Keep the Aspidistra Flying', 'Dead Air', 'Why I Write', 'Homage to Catalonia', 'Crucifix Lane'
    ]
}

# Contoh data ground truth (item yang sebenarnya relevan) untuk buku-buku di atas
ground_truth = {
    'Charade': [
        'Two Alone', 'Three Complete Novels', 'Where Theres Smoke', 'Words of Silk', 'Exclusive', '22 Indigo Place',
        'Love Beyond Reason', 'Adams Fall', 'Texas! Trilogy', 'Fat Tuesday'
    ],
    'Miss Marple': [
        'The Big Four', 'An Autobiography', 'The Thirteen Problems', 'The Hollow', 'The Listerdale Mystery',
        'Appointment with Death', 'Appointment with Death', 'Hercule Poirots Christmas', 'Spiders Web', 'The Mysterious Mr. Quin'
    ],
    '1984': [
        'Animal Farm and 1984', 'The Complete Works of George Orwell', 'Orwell in Spain', 'The Orwell Reader', 'Essays',
        'Keep the Aspidistra Flying', 'Why I Write', 'Homage to Catalonia', 'Shooting an Elephant'
    ]
}

# Fungsi Evaluasi Batch untuk Mengukur Recall@k Rata-rata
def evaluate_recall_for_all_items(recommendation_data, ground_truth_data, k_values):
    """
    Mengevaluasi Recall@k rata-rata untuk banyak item input.

    Args:
      recommendation_data (dict): Dictionary di mana key adalah ID item input
                                  dan value adalah list rekomendasi dari model.
                                  Contoh: {'Charade': ['Book A', 'Book B'], ...}
      ground_truth_data (dict): Dictionary di mana key adalah ID item input
                                dan value adalah list item relevan (ground truth).
                                Contoh: {'Charade': ['True A', 'True B'], ...}
      k_values (list): List nilai k yang ingin dievaluasi (misal: [1, 5, 10]).

    Returns:
      pd.DataFrame: DataFrame berisi rata-rata Recall@k untuk setiap nilai k.
    """
    results = {}
    for k in k_values:
        total_recall = 0
        evaluated_items_count = 0

        # Iterasi melalui setiap item input (misalnya, setiap buku yang direkomendasikan)
        for item_id, recommended_list in recommendation_data.items():
            # Pastikan ada ground truth untuk item ini
            if item_id in ground_truth_data:
                relevant_list = ground_truth_data[item_id]

                # Hanya hitung jika ada item relevan yang diketahui untuk item ini
                if relevant_list:
                    recall_val = recall_at_k(recommended_list, relevant_list, k)
                    total_recall += recall_val
                    evaluated_items_count += 1
            else:
                print(f"Peringatan: Tidak ada ground truth untuk item '{item_id}'. Dilewati.")

        # Hitung rata-rata Recall@k
        average_recall = total_recall / evaluated_items_count if evaluated_items_count > 0 else 0
        results[f'Recall@{k}'] = average_recall

    return pd.DataFrame([results])

# Nilai k yang ingin dievaluasi
k_to_evaluate = [1, 3, 5, 10]

print("Evaluasi Recall@k untuk Cosine Similarity")
cosine_recall_results = evaluate_recall_for_all_items(
    recommendations_cosine,
    ground_truth,
    k_to_evaluate
)
print(cosine_recall_results)

print("\nContoh Perbandingan dengan Euclidean Distance")

# Simulasi Data Hasil Rekomendasi (Euclidean Distance)
recommendations_euclidean = {
    'Charade': [
        'Two Alone', 'Three Complete Novels', 'Where Theres Smoke', 'A Whole New Light', 'Exclusive', 'Ricochet',
        'Love Beyond Reason', 'Adams Fall', 'Texas! Trilogy', 'Heavens Price'
    ],
    'Miss Marple': [
        'The Big Four', 'A Murder is Announced', 'The Thirteen Problems', 'The Hollow', 'The Listerdale Mystery',
        'Death in the Clouds', 'Appointment with Death', 'Murder in Mesopotamia', 'Spiders Web', 'The Mysterious Mr. Quin'
    ],
    '1984': [
        'Animal Farm and 1984', 'The Complete Works of George Orwell', 'Orwell in Spain', 'The Orwell Reader', 'Essays',
        'Keep the Aspidistra Flying', 'Dead Air', 'Why I Write', 'Homage to Catalonia', 'Crucifix Lane'
    ]
}

# Hitung nilai recall dengan Euclidean Distance
euclidean_recall_results = evaluate_recall_for_all_items(
    recommendations_euclidean,
    ground_truth,
    k_to_evaluate
)
print(euclidean_recall_results)

"""**Insight:**
- Evaluasi Recall@k dg Cosine Similarity:
  - Recall@10 memiliki nilai recall yaitu 0,76. Artinya sistem rekomendasi baik dalam menghasilkan rekomendasi yang relevan sesuai judul buku.
  - Recall@5 cukup baik untuk menghasilkan rekomendasi dengan nilai recall 0,45.
  -Recall@3 tidak cukup relevan menghasilkan rekomendasi buku dengan nilai recall 0.27
  - Recall@1 menghasilkan nilai recall paling rendah yaitu 0,10.
- Evaluasi Recall@k dg Euclidean Distance:
  - Recall@10 memiliki nilai recall yaitu 0,76. Artinya sistem rekomendasi baik dalam menghasilkan rekomendasi yang relevan sesuai judul buku.
  - Recall@5 cukup baik untuk menghasilkan rekomendasi dengan nilai recall 0,45.
  -Recall@3 tidak cukup relevan menghasilkan rekomendasi buku dengan nilai recall 0.27
  - Recall@1 menghasilkan nilai recall paling rendah yaitu 0,10.

**Kesimpulan:**
- Kedua metode (Cosine Similarity dan Euclidean Distance) menunjukkan kinerja Recall@k yang sama persis pada semua nilai k yang diuji (1, 3, 5, dan 10). Ini menyiratkan bahwa, dalam konteks data dan implementasi Anda saat ini, kedua metrik kesamaan ini menghasilkan rekomendasi yang sama efektifnya dalam menemukan item relevan.
- Performa Recall untuk kedua model meningkat secara konsisten seiring dengan peningkatan k. Ini adalah perilaku yang diharapkan, karena semakin banyak rekomendasi yang dipertimbangkan, semakin besar peluang untuk menemukan item relevan.
- Pada k=10, kedua model mencapai Recall yang kuat sebesar sekitar 76.3%, yang menunjukkan bahwa mereka cukup handal dalam mencakup sebagian besar item relevan jika pengguna bersedia melihat daftar rekomendasi yang lebih panjang.
"""