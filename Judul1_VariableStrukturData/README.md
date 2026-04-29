# Sistem Peminjaman buku (Linked List)

# a.Judul Program
Sistem peminjaman buku menggunakan linked list

# b.Deskripsi singkat
Sistem peminjaman buku ini adalah program sederhana yang menggunakan Linked List untuk menyimpan data peminjaman. Setiap data berisi nama peminjam, judul buku, dan tanggal pinjam yang tersusun secara berurutan. Sistem ini memungkinkan pengguna untuk menambah, menampilkan, mencari, dan menghapus data peminjaman secara dinamis.

# c.Source code
# Screenshoot source code
Tambahkan gambar source code di bawah ini:
<img width="744" height="909" alt="image" src="https://github.com/user-attachments/assets/b1a97f2c-5cc4-4f11-896c-729799215cd8" />
<img width="721" height="797" alt="image" src="https://github.com/user-attachments/assets/6fcc69f3-9f39-4bc7-a576-f709dd51df78" />
<img width="629" height="758" alt="image" src="https://github.com/user-attachments/assets/d0868e60-e82a-4346-9bc1-3844dce5027b" />
<img width="619" height="584" alt="image" src="https://github.com/user-attachments/assets/9de07294-0971-44b8-83b6-f48125882451" />

# Penjelasan kode
1.Class Node

Digunakan untuk menyimpan data satu transaksi peminjaman buku

Memiliki atribut:

nama → menyimpan nama peminjam
buku → menyimpan judul buku
tanggal → menyimpan tanggal peminjaman
next → menunjuk ke node (data) berikutnya dalam linked list

Class Perpustakaan (Linked List)

Digunakan untuk mengelola seluruh data peminjaman dalam bentuk Singly Linked List

__init__()

Menginisialisasi:

head = None → menandakan bahwa list masih kosong (belum ada data peminjaman)
tambah_peminjaman(nama, buku, tanggal)

Digunakan untuk menambahkan data peminjaman baru

Proses:

Membuat node baru dari data yang diinput
Jika list kosong → node baru menjadi head
Jika tidak kosong →
Traversal ke node terakhir
Node baru ditambahkan di akhir list
tampilkan()

Digunakan untuk menampilkan seluruh data peminjaman

Proses:

Jika head kosong → tampilkan pesan “belum ada data”
Jika ada data →
Mulai dari head
Menelusuri (traversal) hingga node terakhir
Menampilkan setiap data node
cari(nama)

Digunakan untuk mencari data peminjaman berdasarkan nama

Proses:

Traversal dari head ke akhir
Membandingkan nama input dengan data di setiap node
Jika ditemukan → tampilkan data
Jika tidak ditemukan → tampilkan pesan gagal
hapus(nama)

Digunakan untuk menghapus data (simulasi pengembalian buku)

Proses:

Mencari node dengan nama yang sesuai
Jika ditemukan:
Jika node adalah head → pindahkan head ke node berikutnya
Jika bukan → hubungkan node sebelumnya ke node setelahnya
Jika tidak ditemukan → tampilkan pesan
Fungsi main()

Digunakan sebagai program utama (menu interaktif)

Perulangan while True

Digunakan agar program terus berjalan sampai user memilih keluar

Menu Program

Menampilkan pilihan:

Tambah peminjaman
Tampilkan data
Cari peminjam
Kembalikan buku (hapus data)
Keluar
Proses Input User
User memilih menu dengan input angka
Program menjalankan fungsi sesuai pilihan
Percabangan if-elif

Digunakan untuk menentukan aksi berdasarkan pilihan user:

1 → tambah data
2 → tampilkan data
3 → cari data
4 → hapus data
5 → keluar program

# d.Output Program 

# Screenshoot output
<img width="400" height="228" alt="image" src="https://github.com/user-attachments/assets/4d27ad9c-14e6-451f-92ff-ff07c5a11321" />
<img width="383" height="266" alt="image" src="https://github.com/user-attachments/assets/40027a60-28e6-4660-93b2-6040ef5f3901" />
<img width="345" height="267" alt="image" src="https://github.com/user-attachments/assets/0010485e-add5-4a7f-bf64-aec71cebf87a" />
<img width="318" height="223" alt="image" src="https://github.com/user-attachments/assets/1c107bcb-ec62-4f47-8f9d-9fbae66172d3" />
<img width="396" height="208" alt="image" src="https://github.com/user-attachments/assets/1a5e2cdd-5e78-415c-895d-d436c91081c0" />
<img width="320" height="179" alt="image" src="https://github.com/user-attachments/assets/72efd132-e45f-400b-940f-890f71af6ac9" />

Kesimpulan Output
Output program bersifat dinamis (bergantung input user)

Setiap menu mencerminkan operasi Linked List:

Tambah → insert node

Tampil → traversal

Cari → searching

Hapus → delete node

Program ini mensimulasikan sistem nyata peminjaman buku

# e.Link Youtube













