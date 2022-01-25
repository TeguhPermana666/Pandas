"""
Peta memungkinkan kami untuk mengubah data dalam DataFrame atau Seri satu nilai pada satu waktu untuk seluruh kolom. 
Namun, seringkali kita ingin mengelompokkan data kita, dan kemudian melakukan sesuatu yang spesifik untuk kelompok data tersebut.

Seperti yang akan Anda pelajari, kita melakukan ini dengan operasi groupby().
Kami juga akan membahas beberapa topik tambahan, seperti cara yang lebih kompleks untuk mengindeks DataFrames Anda, bersama dengan cara mengurutkan data Anda.
"""
#groupby analysis
"""
Salah satu fungsi yang telah banyak kita gunakan sejauh ini adalah fungsi value_counts(). 
Kita dapat meniru apa yang dilakukan value_counts() dengan melakukan hal berikut:
"""
import pandas as pd
file_path="Pandas\winemag-data-130k-v2.csv"
reviews=pd.read_csv(file_path,index_col=0)
#reviews=reviews.dropna(axis=0)
pd.set_option('display.max_rows',5)
print(reviews)
grup1=reviews.groupby('points').points.count()
print(grup1)
"""
groupby() membuat grup ulasan yang memberikan nilai poin yang sama untuk anggur yang diberikan. 
Kemudian, untuk masing-masing grup ini, kami mengambil kolom poin() dan menghitung berapa kali muncul. value_counts() hanyalah jalan pintas ke operasi groupby() ini.

Kita dapat menggunakan salah satu fungsi ringkasan yang telah kita gunakan sebelumnya dengan data ini. 
Misalnya, untuk mendapatkan wine termurah di setiap kategori nilai poin, kita bisa melakukan hal berikut:
"""
grup2=reviews.groupby('points').price.min()
print(grup2)
"""
Anda dapat menganggap setiap grup yang kami hasilkan sebagai sepotong DataFrame kami yang hanya berisi data dengan nilai yang cocok. DataFrame ini dapat diakses oleh kami secara langsung menggunakan metode apply(), 
dan kami kemudian dapat memanipulasi data dengan cara apa pun yang kami inginkan. Misalnya, berikut adalah salah satu cara
untuk memilih nama wine pertama yang ditinjau dari setiap winery dalam kumpulan data:
"""
grup3=reviews.groupby('winery').apply(lambda df:df.title.iloc[0])
print(grup3)
"""
Untuk kontrol yang lebih mendetail, Anda juga dapat mengelompokkan menurut lebih dari satu kolom.
Sebagai contoh, berikut ini cara kami memilih anggur terbaik menurut negara dan provinsi:
"""
grup4=reviews.groupby(['country','province']).apply(lambda df:df.loc[df.points.idxmax()])
print(grup4)
"""
Metode groupby() lain yang layak disebutkan adalah agg(),
yang memungkinkan Anda menjalankan banyak fungsi berbeda pada DataFrame Anda secara bersamaan.
Misalnya, kita dapat membuat ringkasan statistik sederhana dari kumpulan data sebagai berikut:
"""
grup5=reviews.groupby(['country']).price.agg([len,min,max])
print(grup5)

#Multi_index
"""
Dalam semua contoh yang telah kita lihat sejauh ini, kita telah bekerja dengan objek DataFrame atau Seri dengan indeks label tunggal.
groupby() sedikit berbeda dalam kenyataan bahwa, tergantung pada operasi yang kita jalankan, kadang-kadang akan menghasilkan apa yang disebut multi-indeks.

Multi-indeks berbeda dari indeks biasa karena memiliki beberapa level. Sebagai contoh:
"""
grup6=reviews.groupby(['country','province']).description.agg([len])
print(grup6)
"""
Multi-indeks memiliki beberapa metode untuk menangani struktur berjenjang mereka yang tidak ada untuk indeks tingkat tunggal. 
Mereka juga membutuhkan dua tingkat label untuk mengambil nilai. Berurusan dengan keluaran multi-indeks adalah "gagal" umum bagi pengguna yang baru mengenal panda.

Kasus penggunaan untuk multi-indeks dirinci bersama petunjuk penggunaannya di bagian MultiIndex / Pilihan Lanjutan dari dokumentasi pandas.

Namun, secara umum metode multi-indeks yang paling sering Anda gunakan adalah metode untuk mengonversi kembali ke indeks biasa, metode reset_index() :
"""
grup6=grup6.reset_index()
print(grup6)



#SORTING
"""
Melihat lagi grup 6 kita dapat melihat bahwa pengelompokan
=> mengembalikan data dalam urutan indeks,
bukan dalam urutan nilai. Artinya, ketika mengeluarkan hasil groupby, urutan baris bergantung pada nilai dalam indeks, bukan pada data.

Untuk mendapatkan data sesuai urutan yang diinginkan kita bisa mengurutkannya sendiri. Metode sort_values() berguna untuk ini.
"""
grup6=grup6.sort_values(by='len',ascending=False)
print(grup6)

print(grup6.sort_index())

sort2=grup6.sort_values(by=['country','len'])
print(sort2)