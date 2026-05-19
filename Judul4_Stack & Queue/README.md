# Sistem Undo dan Redo

# a. Judul Program
Sistem Undo dan Redo Seperti Microsoft Word
# b. Deskripsi Singkat
Program ini merupakan simulasi sederhana sistem Text Editor yang menerapkan struktur data StackArray untuk fitur Undo dan Redo. Program memungkinkan pengguna menambahkan teks, membatalkan perubahan terakhir (undo), serta mengembalikan perubahan yang telah dibatalkan (redo).
# c.Source Code 
# Screenshoot Source Code
Tambahkan Gambar Source Code Dibawah Ini :

<img width="571" height="877" alt="image" src="https://github.com/user-attachments/assets/327c6b65-4790-40a4-9246-51aa0cb8d79e" />
<img width="617" height="823" alt="image" src="https://github.com/user-attachments/assets/bca24f5d-6e3f-4b03-944f-1647e472ab11" />
<img width="552" height="566" alt="image" src="https://github.com/user-attachments/assets/e1e25bae-f492-4e71-bef3-ad0f3af02f62" />

# Penjelasan Kode
Program diawali dengan pembuatan class `StackArray` yang digunakan sebagai struktur data stack berbasis array. Pada bagian `__init__`, program menentukan ukuran maksimum stack melalui variabel `MAX`, membuat array `stack`, dan mengatur `top` bernilai `-1` sebagai tanda bahwa stack masih kosong. Method `is_empty()` digunakan untuk mengecek apakah stack kosong, sedangkan `is_full()` digunakan untuk memastikan stack belum mencapai kapasitas maksimum. Method `push()` berfungsi menambahkan data ke bagian paling atas stack, sementara `pop()` digunakan untuk mengambil dan menghapus data terakhir yang masuk sesuai prinsip LIFO (*Last In First Out*). Selain itu, terdapat method `peek()` untuk melihat data teratas tanpa menghapusnya dan `display()` untuk menampilkan isi stack.

Setelah class stack selesai dibuat, program masuk ke bagian simulasi sistem text editor sederhana yang memanfaatkan dua buah stack, yaitu `undo_stack` dan `redo_stack`. Variabel `text` digunakan untuk menyimpan isi teks saat ini. Stack `undo_stack` berfungsi menyimpan riwayat teks sebelum perubahan dilakukan, sedangkan `redo_stack` digunakan untuk menyimpan data hasil undo yang dapat dikembalikan lagi melalui fitur redo. Penggunaan dua stack ini menggambarkan penerapan stack dalam dunia nyata seperti pada aplikasi Microsoft Word atau Visual Studio Code.

Ketika pengguna memilih menu “Tambah Teks”, program meminta input teks baru dari pengguna. Sebelum teks baru ditambahkan, kondisi teks sebelumnya terlebih dahulu disimpan ke dalam `undo_stack` menggunakan method `push()`. Setelah itu teks baru digabungkan ke variabel `text`. Pada proses ini, `redo_stack` direset kembali menjadi stack kosong karena riwayat redo tidak lagi valid setelah adanya perubahan baru. Dengan cara ini, sistem dapat menyimpan seluruh riwayat perubahan teks sehingga fitur undo dapat bekerja dengan baik.

Pada saat pengguna memilih menu “Undo”, program akan mengambil data terakhir dari `undo_stack` menggunakan method `pop()` lalu mengembalikan isi teks ke kondisi sebelumnya. Sebelum perubahan dilakukan, kondisi teks saat ini disimpan terlebih dahulu ke dalam `redo_stack` agar dapat digunakan kembali pada fitur redo. Sebaliknya, ketika pengguna memilih menu “Redo”, program mengambil data terakhir dari `redo_stack` dan mengembalikannya ke teks utama, sementara kondisi sebelumnya disimpan kembali ke `undo_stack`. Alur ini menunjukkan bagaimana stack bekerja secara bertumpuk dan sangat cocok digunakan pada sistem yang membutuhkan riwayat tindakan seperti undo dan redo.

# d.Output Program

<img width="440" height="639" alt="image" src="https://github.com/user-attachments/assets/9826677d-02f2-44b1-9bd0-6c1ccf68b8c7" />
<img width="453" height="665" alt="image" src="https://github.com/user-attachments/assets/c2bc95d8-0916-4717-b34a-71926f89bb14" />

Kesimpulan Output
Berdasarkan output program, sistem text editor sederhana berhasil menerapkan struktur data StackArray untuk fitur Undo dan Redo. Saat pengguna menambahkan teks, kondisi sebelumnya disimpan ke dalam stack menggunakan metode push(). Ketika fitur Undo dijalankan, data terakhir diambil menggunakan metode pop() sehingga teks kembali ke kondisi sebelumnya sesuai prinsip LIFO.

Selain itu, fitur Redo juga berjalan dengan baik karena data hasil Undo disimpan sementara pada stack Redo. Program menunjukkan bahwa StackArray sangat cocok digunakan dalam sistem dunia nyata yang membutuhkan pengelolaan riwayat aksi, seperti aplikasi text editor, browser history, dan sistem navigasi aplikasi.

# e. Link Youtube
