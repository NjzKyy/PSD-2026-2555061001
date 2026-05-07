# Pencarian jadwal penerbangan
# a. Judul Program
Program Pencarian Jadwal Penerbangan Menggunakan Binary Search
# b. Deskripsi Singkat
Program ini merupakan sistem pencarian jadwal penerbangan yang menerapkan algoritma Binary Search untuk menemukan data penerbangan secara cepat dan efisien. Pengguna dapat mencari jadwal berdasarkan kode penerbangan, kemudian sistem akan menampilkan informasi tujuan, jam keberangkatan, kategori waktu penerbangan, serta posisi data dalam daftar.
# c.Source Code
# Screenshoot Source Code
Tambahkan Gambar Source Code Dibawah Ini : 
<img width="897" height="878" alt="image" src="https://github.com/user-attachments/assets/67ab7f35-7a7a-4ff6-895a-a3109168f8ea" />
<img width="874" height="611" alt="image" src="https://github.com/user-attachments/assets/b7d12176-ca33-4bf8-845a-a1384914470b" />
# Penjelasan Kode
1. Membuat Data Jadwal Penerbangan
jadwal_penerbangan = [
    {"kode": "GA102", "tujuan": "Jakarta", "jam": "07:00"},

Bagian ini berisi daftar jadwal penerbangan dalam bentuk list dan dictionary.

kode = kode penerbangan
tujuan = kota tujuan
jam = jam keberangkatan

Data harus sudah urut berdasarkan kode penerbangan agar Binary Search dapat bekerja.

2. Membuat Fungsi Binary Search
def binary_search(data, target):

Fungsi ini digunakan untuk mencari kode penerbangan tertentu.

3. Menentukan Batas Pencarian
kiri = 0
kanan = len(data) - 1
kiri = indeks awal data
kanan = indeks akhir data

Digunakan sebagai batas area pencarian.

4. Perulangan Pencarian
while kiri <= kanan:

Program akan terus mencari selama area pencarian masih ada.

5. Menentukan Posisi Tengah
tengah = (kiri + kanan) // 2

Mencari indeks tengah dari data.

Binary Search selalu memeriksa data tengah terlebih dahulu.

6. Mengecek Data
if data[tengah]["kode"] == target:

Jika kode penerbangan sama dengan input pengguna, maka data ditemukan.

7. Menggeser Pencarian
elif data[tengah]["kode"] < target:
    kiri = tengah + 1

Jika target lebih besar, pencarian dipindahkan ke kanan.

else:
    kanan = tengah - 1

Jika target lebih kecil, pencarian dipindahkan ke kiri.

8. Jika Data Tidak Ditemukan
return -1

Program mengembalikan -1 jika kode penerbangan tidak ada.

9. Menampilkan Daftar Penerbangan
for i, penerbangan in enumerate(jadwal_penerbangan):

Digunakan untuk menampilkan semua jadwal penerbangan ke layar.

10. Input Pengguna
cari = input("Masukkan kode penerbangan: ").upper()

Pengguna memasukkan kode penerbangan yang ingin dicari.

.upper() digunakan agar huruf otomatis menjadi kapital.

11. Menjalankan Binary Search
hasil = binary_search(jadwal_penerbangan, cari)

Program memanggil fungsi Binary Search untuk mencari data.

12. Menampilkan Hasil
if hasil != -1:

Jika data ditemukan, program menampilkan:

kode penerbangan
tujuan
jam keberangkatan
kategori penerbangan
indeks data

13. Menentukan Kategori Waktu
if jam < 12:

Digunakan untuk menentukan:

Pagi
Siang
Malam

berdasarkan jam keberangkatan.

14. Jika Tidak Ada Data
print("Jadwal penerbangan tidak ditemukan!")

Pesan muncul jika kode penerbangan tidak tersedia dalam sistem.

# d.Output Program
# Screenshoot Output
<img width="514" height="515" alt="image" src="https://github.com/user-attachments/assets/9a6fbee7-dda0-4627-ade1-bad89aad90e6" />
Kesimpulan Output

Program berhasil mencari jadwal penerbangan berdasarkan kode penerbangan yang dimasukkan pengguna menggunakan algoritma Binary Search.

Jika data ditemukan, program menampilkan:

kode penerbangan,
tujuan penerbangan,
jam keberangkatan,
kategori waktu penerbangan (pagi/siang/malam),
dan indeks lokasi data.

Jika kode penerbangan tidak ditemukan, program akan menampilkan pesan bahwa jadwal penerbangan tidak tersedia.

Karena menggunakan Binary Search, proses pencarian menjadi lebih cepat dan efisien pada data yang sudah terurut.
# e. Link Youtube 
https://youtu.be/CyhLikpoy5U?si=O9eAV1usgu8jHnhE



