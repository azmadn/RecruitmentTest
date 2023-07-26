# RecruitmentTest


# Questions 1 
- ## **What is wrong with the above code?** 
Pada fungsi tersebut ada kesalahan untuk mengatasi perkalian nilai negatif. karena kondisi loop hanya diperuntukkan untuk x > 0. pada kode tersebut dapat diperbaiki dan diberikan kondisi saat nilai negatif.

- ## **If you find it wrong, please fix the code above without using the “*” or “/”  operator or Absolute call?**
        Perbaikan fungsi dapat diliat pada file "multiply.py"

- ## **As part of our development process we test all methods at a code level. Which input values would you use to do the testing?**
Untuk menguji kode tersebut dapat dilakukan dengan beberapa skenario berikut :
1. **jika nilai x dan y positif** <br>
multiply(5,7) -> output diharapkan 35 <br>
multiply(3,7) -> output diharapkan 21
2. **jika nilai x atau y bernilai negatif** <br>
multiply(-3,5) -> output diharapkan -15 <br>
multiply(3,-5) -> output diharapkan -15
3. **jika nilai (x atau y) = 0** <br>
multiply(0,10) -> output diharapkan 0<br>
multiply(7,0) -> output diharapkan 0
4. **jika nilai x dan y negatif** <br>
multiply(-4, -6) -> Hasil yang diharapkan: 24 <br>
        
- ## For later discussion: What else worries you as you fix this problem?
1. **Kinerja** : <br>
Implementasi dari kode tersebut adalah menggunakan penambahan berulang, sehingga untuk nilai yang besar metode ini mungkin saja akan menjadi lambat.
2. **Validasi masukan** : <br>
Pada kode tersebut hanya mengimplementasi nilai bulat. sehingga validasi harus dilakukan untuk memastikan bahwa nilai yang dimaksukkan adalah nilai integer pada fungsi tersebut.

# Questions 2
- ## **What would be the output of the following select statements?**  <br>
1. **Select USA.NAME, EU.NAME From USA, EU Where USA.ID = EU.ID** <br>

|   NAME |   NAME |
|--------|--------|
| Thomas | Thomas |
2. **Select USA.NAME, EU.NAME From USA left join EU on (USA.ID = EU.ID)** <br>

|   NAME |   NAME |
|--------|--------|
| Thomas | Thomas |
|  Cindy | (null) |
3. **Select USA.NAME, EU.NAME From USA, EU** <br>

|   NAME |     NAME |
|--------|----------|
| Thomas |   Thomas |
|  Cindy |   Thomas |
| Thomas | Francois |
|  Cindy | Francois |
    
- ## **For later discussion: we use those tables to keep track of our European and American customers.  Please provide a critique to that table design (is it good?  How could it be better?)** <br>
Dari design tabel tersebut saya melihat ada beberapa masalah yang dapat diperbaiki yaitu : <br>
1. **Kolom Negara Asal Pelanggan**  <br>
Tabel tidak memiliki kolom untuk menyimpan informasi tentang negara asal pelanggan. Hal ini dapat dimungkinkan menjadi masalah dikemudian hari jika ingin melakukan analisis berdasarkan negara asal pelanggan.<br>
**Solusi** : Dapat ditambahkan kolom baru yaitu "COUNTRY" pada kedua tabel.
2.  **Kurangnya Kolom Primary Key dan Penamaan Kolom** <br>
Tabel terebut tidak memiliki kolom primary key untuk mengidentifikasi setiap baris dengan jelas sehingga dapat menyebabkan konflik dan masalah dalam query data.<br>
**Solusi**  : Pastikan bahwa ID dalam setiap tabel unik dan tidak tumpang tindih dengan tabel lain, dan juga memberikan nama yang lebih deskriptif seperti perubahan pada kolom NAME atau ID menjadi **CustomerName** dan **CustomerId** atau untuk penambahan **COUNTRY** menjadi **CustomerCountry** dsb.
            

# Questions 3
- ## **Write the content of the method below that counts the maximum number of levels in a given tree. Please notice that this is NOT counting the TOTAL number of nodes, but counting the DEPTH.**
        Algoritma kodingan dapat diliat pada file 'calculateDepth.py'


# Question 4
- ## **Do you have any recommendations to improve the performance?  Feel free to change the above method.**
Untuk mengimprove performa dari metode tersebut dapat kita lakukan dengan membuat tipe data menjadi set(). 

Pada kasus 1, Dimana bagA memiliki **banyak** elemen dan bagB memiliki **sedikit** elemen, performa metode intersect tersebut memiliki kompleksitas waktu yang relatif rendah. <br>

Sedangkan pada kasus 2, Dimana bagA memiliki **sedikit** elemen dan bagB memiliki **banyak** elemen. performa metode intersect tesebut akan memiliki kendala dikarenakan setiap elemen bagA harus melintasi seluruh bagB untuk memeriksa kedalamannya yang mengakibatkan kompleksitas waktu yang tinggi. <br>

Maka dari itu, untuk meningkatkan performa dari fungsi intersect tesebut dapat dimodifikasi dengan mengubah bagB menjadi tipe data **set**. <br>

        Perubahan dapat dilihat pada 'performance.py'

Mengubah bagB menjadi set dilakukan karena pada fungsi intersect dilakukan pencarian elemen dari bagA dalam bagB.

# Question 5
- ## **Please write a method to print out ALL the Prime numbers between 2 and 100.**

        Algoritma kodingan dapat diliat pada file 'findPrime.py'