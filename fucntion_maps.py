import pandas as pd
"""
Dalam tutorial terakhir, kita mempelajari cara memilih data yang relevan dari DataFrame atau Seri.
Mengambil data yang benar dari representasi data kami sangat penting untuk menyelesaikan pekerjaan, seperti yang kami tunjukkan dalam latihan.
Namun, data tidak selalu keluar dari memori dalam format yang kita inginkan. 

=>Terkadang kita harus melakukan lebih banyak pekerjaan sendiri untuk memformatnya untuk tugas yang ada. 
Tutorial ini akan mencakup berbagai operasi yang dapat kita terapkan pada data kita untuk mendapatkan input yang "tepat".
"""
pd.set_option('Max_rows',5)
import numpy as py
file_path="Pandas\winemag-data-130k-v2.csv"
reviews=pd.read_csv(file_path,index_col=0)
reviews=reviews.dropna(axis=0)
print(reviews)

#summary functions
"""
Pandas menyediakan banyak 
"fungsi ringkasan" sederhana (bukan nama resmi) yang merestrukturisasi data dalam beberapa cara yang berguna. Misalnya, pertimbangkan metode deskripsikan() :
describe()
Metode ini menghasilkan ringkasan tingkat tinggi dari atribut kolom yang diberikan.
Ini adalah tipe-sadar/type-aware, artinya outputnya berubah berdasarkan tipe data input. 
Output di atas hanya masuk akal untuk data numerik; untuk data string inilah yang kami dapatkan:
"""
#->describe sebuah data frame pada column yg berkaitan
print(reviews.taster_name.describe())
print(reviews.points.describe())
#->describe sebuah titik penting yg ingin ditampilkan pada column yg berkaitan
print(reviews.points.mean())
print(reviews.price.describe())
#->to see unique value=>mencetak sebuah value yang tidak sama
print(reviews.taster_name.unique())
#melihat kemunculan unique value di setiap fruekuensi
print(reviews.taster_name.value_counts()) 

#Maps
"""
Peta adalah istilah, dipinjam dari matematika, untuk fungsi yang mengambil satu set nilai dan "memetakan" mereka ke set nilai lainnya.
Dalam ilmu data kita sering memiliki kebutuhan untuk membuat representasi baru dari data yang ada, atau untuk mengubah data dari format sekarang ke format yang kita inginkan nanti.
Peta adalah yang menangani pekerjaan ini, menjadikannya sangat penting untuk menyelesaikan pekerjaan Anda!
"""
#dua cara dalam mapping methods yang sering digunakan:
"""
=>map() adalah yang pertama, dan sedikit lebih sederhana.
Misalnya, anggaplah kita ingin mempertahankan skor anggur yang diterima menjadi 0. Kita dapat melakukan ini sebagai berikut:

Fungsi yang Anda teruskan ke map() harus mengharapkan nilai tunggal dari Seri (nilai poin, dalam contoh di atas), 
dan mengembalikan versi yang diubah dari nilai tersebut. map() mengembalikan Seri baru di mana semua nilai telah diubah oleh fungsi Anda.


=>apply() adalah metode yang setara jika kita ingin mengubah seluruh DataFrame dengan memanggil metode khusus di setiap baris
"""
reviews_points_means=reviews.points.mean()
print(reviews_points_means)
mapping=reviews.points.map(lambda p:p-reviews_points_means)#lambda p merunjuk ke indexing points columns yg mana setiap p - reviews_points_means 

print("Sebelum mapping:\n",reviews.points)
print("Mapping:\n",mapping)


def reman_points(row):
    row.points=row.points-reviews_points_means
    return row

applying=reviews.apply(reman_points,axis=1)
print(applying.points)
"""
Jika kita telah memanggil reviews.apply() dengan axis='index', 
maka alih-alih meneruskan fungsi untuk mengubah setiap baris, kita perlu memberikan fungsi untuk mengubah setiap kolom.
Perhatikan bahwa map() dan apply() masing-masing mengembalikan Seri dan DataFrames yang baru dan diubah. 
Mereka tidak mengubah data asli yang mereka panggil. Jika kita melihat ulasan baris pertama, kita dapat melihat bahwa itu masih memiliki nilai poin aslinya.
"""
#cek apakah data sudah berubah?, jika reviews nya yg di assigment baru ada perihal berubah datanya
print(reviews.head(1))
"""
review_points_mean = reviews.points.mean()
reviews.points=reviews.points - review_points_mean

Dalam kode ini kami melakukan operasi antara banyak nilai di sisi kiri (semuanya di Seri) dan satu nilai di sisi kanan (nilai rata-rata). 
Pandas melihat ekspresi ini dan mengetahui bahwa kita harus mengurangi nilai rata-rata itu dari setiap nilai dalam kumpulan data.

Pandas juga akan mengerti apa yang harus dilakukan jika kita melakukan operasi ini antara Seri dengan panjang yang sama.
Misalnya, cara mudah untuk menggabungkan informasi negara dan wilayah dalam kumpulan data adalah dengan melakukan hal berikut:
"""
print(reviews.country +" - "+ reviews.region_1)