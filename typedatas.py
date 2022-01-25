#dtypes
"""
=>type data yang digunakan untuk spesifik column pada data frame atau bisa juga pada index
    ->biasanya digunakan untuk mengambil tipe data dari suatu column pada data frame
"""
import pandas as pd
file_data="Pandas\winemag-data-130k-v2.csv"
reviews=pd.read_csv(file_data,index_col=0)
pd.set_option('display.max_rows',10)
print(reviews.price.dtype)
print(reviews.dtypes)
#astypes
"""
=>digunakan untuk mentransformasikan sbuah tipe data dari suatu column menjadi tipe data yang di inginkan
"""
print(reviews.points.astype('float64'))
print(reviews.index.dtype)


#missing value
"""
pd.isnull()
pd.notnull()
"""
print(reviews[pd.isnull(reviews.country)])
#replacing nan operator ke sebuah argument yg di kehendaki
"""
fillna("unknown")
"""
print(reviews.region_2)
print(reviews.region_2.fillna("Unknown"))
"""
Atau kita bisa mengisi setiap nilai yang hilang dengan nilai non-null 
pertama yang muncul beberapa saat setelah catatan yang diberikan dalam database. Ini dikenal sebagai strategi pengisian ulang.

Atau, kami mungkin memiliki nilai bukan nol yang ingin kami ganti. Misalnya, sejak kumpulan data ini diterbitkan, 
engulas Kerin O'Keefe telah mengubah pegangan Twitter-nya dari @kerinokeefe menjadi @kerino. 
Salah satu cara untuk mencerminkan hal ini dalam dataset adalah menggunakan metode replace() :
"""
print(reviews.taster_twitter_handle)
print(reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino"))