import pandas as pd
pd.set_option('max_rows', 5)
reviews = pd.read_csv("Pandas/winemag-data-130k-v2.csv", index_col=0)

#rename column
reviews=reviews.rename(columns={"title":"judul"})
print(reviews)
#rename index
reviews=reviews.rename(index={0:'pertama',1:'kedua'})
print(reviews)
#rename axis
reviews=reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
print(reviews)


#combine
"""
Saat melakukan operasi pada kumpulan data, terkadang kita perlu menggabungkan DataFrame dan/atau Seri yang berbeda dengan cara yang tidak sepele. 
Pandas memiliki tiga metode inti untuk melakukan ini. Untuk meningkatkan kompleksitas,
ini adalah concat(), join(), dan merge(). Sebagian besar yang dapat dilakukan merge() juga dapat dilakukan dengan lebih sederhana dengan join(),
jadi kita akan menghilangkannya dan fokus pada dua fungsi pertama di sini.

Metode penggabungan yang paling sederhana adalah concat(). Diberikan daftar elemen, fungsi ini akan menyatukan elemen-elemen tersebut di sepanjang sumbu.

Ini berguna ketika kita memiliki data dalam objek DataFrame atau Seri yang berbeda tetapi memiliki bidang (kolom) yang sama. 
Salah satu contoh: kumpulan data Video YouTube, yang membagi data berdasarkan negara asal 
(misalnya Kanada dan Inggris Raya, dalam contoh ini). Jika kita ingin mempelajari beberapa negara secara bersamaan, kita dapat menggunakan concat() untuk menyatukannya:
"""
canadian_yutub=pd.read_csv('Pandas\CAvideos.csv')
british_yutub=pd.read_csv('Pandas\GBvideos.csv')
combine1=pd.concat([canadian_yutub,british_yutub])
print(combine1)
"""
Penggabung paling tengah dalam hal kompleksitas adalah join(). join() memungkinkan Anda menggabungkan objek DataFrame berbeda yang memiliki indeks yang sama.
Misalnya, untuk menarik video yang kebetulan sedang ngetren pada hari yang sama di Kanada dan Inggris Raya, kita dapat melakukan hal berikut:
"""
left=canadian_yutub.set_index(['title','trending_date'])
right=british_yutub.set_index(['title','trending_date'])
join1=left.join(right,lsuffix='_CAN',rsuffix='_UK')#suffix digunakan untuk menambahkan belakangan data berdasarkan data di median column (kiri, kanan)
print(join1)
"""
Parameter lsuffix dan rsuffix diperlukan di sini karena data memiliki nama kolom yang sama di kumpulan data Inggris dan Kanada.
Jika ini tidak benar (karena, katakanlah, kami telah mengganti namanya sebelumnya) kami tidak akan membutuhkannya.
"""