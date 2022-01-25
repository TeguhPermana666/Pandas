import pandas as pd
file_path="Pandas\winemag-data-130k-v2.csv"
data=pd.read_csv(file_path,index_col=0)#index_col=0 ->set data ditampilkan dari column di index 0
pd.set_option('Max_rows',5)#set data yang ditampilkan adalah 5 baris

#Native accessors
"""
=> native accessors Objek menyediakan cara yang baik untuk mengindeks data. Pandas membawa semua ini, yang membantu membuatnya mudah untuk memulai
"""
# consider the data frame:
print(data)
#->mengakses data pada columns yang diperulkan(specific data)
print(data.country)
#->or
print(data['country'])
#->data frame di set default untuk manipulasi data pada pandas maka:
#kolom-pertama, baris-kedua
print(data['country'][1]) 


#indexing in pandas
"""
digunkan untuk memilih data pada pandas yang mana dapat dilakukan dengan menggunkan sebuah accesor operator:
-iloc
-loc
"""
#->index-based selection
"""
=>memilih data berdasarkan posisi numeriknya dalam data. iloc mengikuti paradigma ini.
.iloc[baris,kolom]
->baris-pertama, kolom-kedua
"""
print(data.iloc[:,2])
print(data.iloc[:3,0])
print(data.iloc[0:3,0:2])
#or
print(data.iloc[[0,1,2],0])
#ambil data dari belakang
print(data.iloc[-5:])


#->label-based selection
"""
figunakan pada prafigma loc pradigma
=>pemilihan berbasis label

iloc secara konseptual lebih sederhana daripada loc karena mengabaikan indeks kumpulan data. 
Saat kita menggunakan iloc, kita memperlakukan dataset seperti matriks besar (daftar daftar),
matriks yang harus kita indeks berdasarkan posisinya. loc, sebaliknya,
menggunakan informasi dalam indeks untuk melakukan pekerjaannya. 
Karena kumpulan data Anda biasanya memiliki indeks yang berarti,
biasanya lebih mudah untuk melakukan sesuatu menggunakan loc.
Misalnya, inilah satu operasi yang jauh lebih mudah menggunakan loc:
"""
print(data.loc[:,["title","variety","winery"]])
#eror -> print(data.iloc[:,["title","variety","winery"]])
#eror -> print(data.iloc[:,"title"])


#Manipulating index
"""
Label-based selection derives memperoleh kekuatannya dari label dalam indeks. Secara kritis, indeks yang kami gunakan tidak dapat diubah.
Kita dapat memanipulasi indeks dengan cara apa pun yang kita inginkan.

Metode set_index() dapat digunakan untuk melakukan pekerjaan tersebut. Inilah yang terjadi ketika kita menyetel_index ke bidang judul:

"""
kata=data.set_index("title")
print(kata)

#conditional selection
"""
Sejauh ini kami telah mengindeks berbagai langkah data, menggunakan properti struktural DataFrame itu sendiri.
Namun, untuk melakukan hal-hal yang menarik dengan data, seringkali kita perlu mengajukan pertanyaan berdasarkan kondisi.

Misalnya, anggaplah kita tertarik secara khusus pada anggur yang lebih baik dari rata-rata yang diproduksi di Italia.

Kita bisa mulai dengan memeriksa apakah setiap anggur itu Italia atau bukan:
"""
#1.true/false
print(kata.country=="italy")
#data yang keluar hanya yang berkaitan dengan italy
print(data.loc[data.country=="Italy"])
#->bisa juga ditambah dengan condtional lainnya dengan menggunakan tanda & atau bisa juga dengan |
print(data.loc[(data.country=="Italy") & (data.points >=90)])

"""
Yang pertama adalah isin. isin memungkinkan Anda memilih data yang nilainya "ada dalam" daftar nilai.
Misalnya, inilah cara kami menggunakannya untuk memilih anggur hanya dari Italia atau Prancis:
"""
#isin()
print(data.loc[data.country.isin(["Italy","France"])])
#or 
print(data.loc[(data.country=="Italy") | (data.country=="France")])

"""
Yang kedua isnull (dan pendampingnya notnull). Metode ini memungkinkan Anda menyorot nilai yang (atau tidak) kosong (NaN). Misalnya, 
untuk menyaring anggur yang tidak memiliki label harga di kumpulan data, inilah yang akan kami lakukan:
"""
#print(data.loc[(data.designation!="NaN")])->tidak mau harus pakai notnull()
print(data.loc[data.designation.notnull()])

#assign
data['critic']='everyone'
print(data['critic'])

data['index_backward']=range(len(data),0,-1)
                        #banyak data(sequence),stop,start
print(data['index_backward'])

data['index_forward']=range(len(data))

print(data)

#data.to_csv('Pandas\Indexing_output.csv')