# Pengurutan Data Waktu Tempuh Pengiriman Barang
# a. Judul Program
Pengurutan Data Waktu Tempuh Pengiriman Barang Menggunakan Algoritma Insertion Sort untuk Optimasi Logistik
# b. Deskripsi Singkat
Program ini dirancang untuk mengelola dan mengurutkan data waktu tempuh pengiriman barang dalam sistem logistik menggunakan algoritma Insertion Sort. Data berupa waktu pengiriman dalam jam dimasukkan oleh pengguna, kemudian diproses untuk diurutkan dari yang tercepat hingga yang terlama.
# c.Source Code
# Screenshoot source code
Tambahkan gambar source code di bawah ini:
<img width="921" height="874" alt="image" src="https://github.com/user-attachments/assets/cd86f3e5-f471-4b54-99d6-5ccb2366ec92" />
# Penjelasan kode
1. Fungsi insertion_sort

Digunakan untuk mengurutkan data waktu tempuh pengiriman menggunakan metode Insertion Sort

Memiliki parameter:
waktu : list yang berisi data waktu tempuh pengiriman (dalam jam)
Proses:
Perulangan dimulai dari indeks ke-1
Data pada indeks tersebut disimpan sebagai key
Membandingkan key dengan data sebelumnya
Jika data sebelumnya lebih besar digeser ke kanan
Key dimasukkan ke posisi yang sesuai
Tujuan:

Mengurutkan data dari waktu tercepat ke terlama (ascending)

2. Fungsi main()

Digunakan sebagai program utama

Input Data

Program meminta jumlah data:

n = jumlah pengiriman

Kemudian user memasukkan waktu tempuh:

Disimpan dalam list waktu
Bertipe float (karena bisa desimal)
Proses:
Membuat list kosong waktu
Menggunakan perulangan untuk input data
Menyimpan setiap input ke dalam list
Menampilkan Data Awal
Menampilkan data sebelum diurutkan
Bertujuan untuk melihat perbandingan sebelum dan sesudah sorting
Proses Sorting
Memanggil fungsi insertion_sort(waktu)
Data diurutkan menggunakan algoritma insertion sort
Menampilkan Data Setelah Sorting
Data ditampilkan dari tercepat ke terlama
Memudahkan analisis efisiensi pengiriman
Analisis Sederhana
Data pertama (waktu[0]) → pengiriman tercepat
Data terakhir (waktu[-1]) → pengiriman paling lama
Penanganan Error
Menggunakan try-except
Jika input bukan angka → tampilkan pesan error

3. Struktur Algoritma Insertion Sort
Langkah-langkah:
Ambil satu data sebagai key
Bandingkan dengan data sebelumnya
Geser data yang lebih besar ke kanan
Masukkan key ke posisi yang tepat
Ulangi hingga seluruh data terurut

4. Perulangan (for)

Digunakan untuk:

Mengakses setiap elemen dalam list
Melakukan proses penyisipan (insertion)

5. Perulangan (while)

Digunakan untuk:

Membandingkan key dengan elemen sebelumnya
Menggeser data sampai posisi yang tepat ditemukan

6. Tujuan Program

Program ini dibuat untuk:

Mengurutkan waktu tempuh pengiriman barang
Membantu optimasi logistik
Menentukan prioritas pengiriman tercepat
Menganalisis efisiensi distribusi

7. Alur Program Secara Keseluruhan
Program dimulai dari main()
User memasukkan jumlah data
User memasukkan waktu tempuh pengiriman
Data disimpan dalam list
Data ditampilkan sebelum sorting
Data diurutkan menggunakan insertion sort
Data ditampilkan setelah sorting
Program menampilkan waktu tercepat dan terlama
Program selesai
# d.Output Program
# Screenshoot Output
<img width="578" height="380" alt="image" src="https://github.com/user-attachments/assets/d6c5f29b-8782-4d1b-9835-897731db42ef" />
Kesimpulan Output

Data waktu tempuh pengiriman berhasil diurutkan dari tercepat ke terlama menggunakan Insertion Sort

Pengguna dapat dengan mudah mengetahui prioritas pengiriman yang paling efisien

Informasi pengiriman tercepat dan terlama membantu analisis kinerja logistik

Program mendukung pengambilan keputusan dalam optimasi distribusi barang
# e.Link youtube
https://youtu.be/RqBgsLaLY80?si=oUHFGoCNgTVZfi_L

