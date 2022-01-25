"""
Pandas digunakan untuk memanipuulasi sebuah data mentah(.csv)

dua core object dalam pandas:
-> data frame
    =>DataFrame adalah sebuah tabel. 
    Ini berisi array entri individu, yang masing-masing memiliki nilai tertentu. Setiap entri sesuai dengan baris (atau catatan) dan kolom.
    "kolom":[isi di setiap baris ->baris1,baris2,baris3],index=["nama_baris"]
-> series
Series, sebaliknya dari data frame, 
adalah urutan nilai data. Jika DataFrame adalah tabel, ->Series adalah daftar. 
Dan sebenarnya Anda dapat membuatnya dengan tidak lebih dari daftar
"""
#create

#import pandas->can many dimension
import pandas as pd
data_frame=pd.DataFrame({"yes":[10,20],"No":[30,40]})
data_frame2=pd.DataFrame({"Bob":["aku suka itu","Aku sangat suka itu"],"Bab":["Fak u","dont like me"]})
data_frame3=pd.DataFrame({"Bob":["Aku suka","Kamu suka"],
                          "Bab":["fak u","Dont me"]}
                         ,index=["Product A","Product B"])

print(data_frame)
print(data_frame2)
print(data_frame3)

#series->only one dimension
series=pd.Series([1,2,3,4,5,6])
print(series)
series2=pd.Series([1,2,3,4],index=["sales","salas","Matas","Mutus"],name="Product A")
print(series2)

#read
file_path="Pandas\winemag-data-130k-v2.csv"
"""
Fungsi pd.read_csv() dilengkapi dengan baik, dengan lebih dari 30 parameter opsional yang dapat Anda tentukan.
Misalnya, Anda dapat melihat dalam kumpulan data ini bahwa file CSV memiliki indeks bawaan, yang tidak diambil oleh pandas secara otomatis. 
Untuk membuat pandas menggunakan kolom itu untuk indeks (alih-alih membuat yang baru dari awal), kita dapat menentukan index_col.
"""
data=pd.read_csv(file_path,index_col=0)
print(data.shape)#untuk mengetahui ukuran dari data
print(data.head())#untuk mengambil data teratas dari data_frame

#write
# data_frame3.to_csv("Pandas\Data_frame3.csv")
