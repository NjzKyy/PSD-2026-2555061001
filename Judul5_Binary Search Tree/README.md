# Sistem Pencarian Data Mahasiswa
# a. Judul Program
Sistem Pencarian Data Mahasiswa
# b. Deskripsi Singkat
Binary Search Tree (BST) merupakan struktur data berbentuk pohon biner yang digunakan untuk menyimpan dan mencari data secara efisien. Pada BST, setiap node memiliki aturan bahwa nilai di sebelah kiri lebih kecil dari node induk, sedangkan nilai di sebelah kanan lebih besar. Dalam dunia nyata, BST sering digunakan pada sistem pencarian data seperti data mahasiswa, kontak telepon, database sederhana, dan sistem ranking karena mampu mempercepat proses pencarian, penambahan, serta pengurutan data secara otomatis.
c. Source Code
<img width="636" height="825" alt="image" src="https://github.com/user-attachments/assets/e7afadd4-6509-400c-acf2-73d4a54963b3" />
<img width="643" height="784" alt="image" src="https://github.com/user-attachments/assets/6616f7dc-10a1-49e2-afca-d737632efeba" />
<img width="461" height="83" alt="image" src="https://github.com/user-attachments/assets/6c6d3337-8da2-477f-8bd2-72e82eea491d" />
# Penjelasan Code
Program dimulai dengan membuat class Node yang berfungsi sebagai tempat penyimpanan data mahasiswa berupa npm dan nama. Setiap node memiliki atribut left dan right untuk menghubungkan node di sebelah kiri dan kanan pada Binary Search Tree (BST). Setelah itu dibuat class BinarySearchTree yang memiliki atribut root sebagai akar pohon. Method insert() digunakan untuk memasukkan data mahasiswa ke dalam BST sesuai aturan BST, yaitu jika nilai npm lebih kecil dari node saat ini maka data ditempatkan di sebelah kiri, sedangkan jika lebih besar maka ditempatkan di sebelah kanan. Method tambah_mahasiswa() digunakan untuk mempermudah proses penambahan data ke dalam pohon.

Selanjutnya program memiliki method search() yang digunakan untuk mencari data mahasiswa berdasarkan NPM. Proses pencarian dilakukan mulai dari root, kemudian bergerak ke kiri atau kanan sesuai perbandingan nilai NPM hingga data ditemukan atau tidak ada lagi node yang diperiksa. Method inorder() digunakan untuk menampilkan seluruh data mahasiswa secara terurut dari NPM terkecil hingga terbesar dengan teknik traversal inorder. Pada bagian program utama dibuat objek BST, kemudian beberapa data mahasiswa dimasukkan ke dalam pohon menggunakan method tambah_mahasiswa(). Setelah itu program menampilkan seluruh data mahasiswa dan melakukan pencarian data berdasarkan NPM tertentu sehingga pengguna dapat mengetahui apakah data mahasiswa tersebut ditemukan atau tidak.
# d. Output Program
<img width="355" height="283" alt="image" src="https://github.com/user-attachments/assets/8ca2078e-793c-47de-9f6d-ccea2f598af9" />

Berdasarkan output program Binary Search Tree (BST) yang dijalankan, sistem berhasil menyimpan dan mengelola data mahasiswa berdasarkan NPM secara terstruktur. Data ditampilkan secara berurutan menggunakan metode inorder traversal, sehingga NPM mahasiswa muncul dari nilai terkecil hingga terbesar. Selain itu, proses pencarian data mahasiswa berdasarkan NPM juga berjalan dengan baik, di mana sistem dapat menemukan data yang dicari dengan lebih cepat dan efisien dibanding pencarian biasa. Hal ini menunjukkan bahwa Binary Search Tree sangat efektif digunakan dalam pengolahan dan pencarian data pada aplikasi dunia nyata seperti sistem akademik atau database mahasiswa.
# e. Link Youtube
https://youtu.be/rERd2eTtLJ0?si=mpIbFnKHl9zI0YF8




