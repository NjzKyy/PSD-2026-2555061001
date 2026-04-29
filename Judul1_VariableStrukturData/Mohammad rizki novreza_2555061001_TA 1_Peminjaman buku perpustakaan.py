class Node:
    def __init__(self, nama, buku, tanggal):
        self.nama = nama
        self.buku = buku
        self.tanggal = tanggal
        self.next = None


class Perpustakaan:
    def __init__(self):
        self.head = None

    def tambah_peminjaman(self, nama, buku, tanggal):
        new_node = Node(nama, buku, tanggal)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print("Peminjaman berhasil ditambahkan!")

    def tampilkan(self):
        if self.head is None:
            print("Belum ada data peminjaman.")
            return

        temp = self.head
        print("\n=== Data Peminjaman ===")
        while temp:
            print(f"Nama: {temp.nama}")
            print(f"Buku: {temp.buku}")
            print(f"Tanggal: {temp.tanggal}")
            print("-" * 20)
            temp = temp.next

    def cari(self, nama):
        temp = self.head
        ditemukan = False

        while temp:
            if temp.nama.lower() == nama.lower():
                print("Data ditemukan:")
                print(f"Nama: {temp.nama}")
                print(f"Buku: {temp.buku}")
                print(f"Tanggal: {temp.tanggal}")
                ditemukan = True
                break
            temp = temp.next

        if not ditemukan:
            print("Data tidak ditemukan.")

    def hapus(self, nama):
        temp = self.head
        prev = None

        while temp:
            if temp.nama.lower() == nama.lower():
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next

                print("Data berhasil dihapus (buku dikembalikan).")
                return

            prev = temp
            temp = temp.next

        print("Data tidak ditemukan.")
        
def main():
    perpus = Perpustakaan()

    while True:
        print("\n=== SISTEM PERPUSTAKAAN ===")
        print("1. Tambah Peminjaman")
        print("2. Tampilkan Data")
        print("3. Cari Peminjam")
        print("4. Kembalikan Buku (Hapus)")
        print("5. Keluar")

        pilih = input("Pilih: ")

        if pilih == '1':
            nama = input("Nama: ")
            buku = input("Judul Buku: ")
            tanggal = input("Tanggal Pinjam: ")
            perpus.tambah_peminjaman(nama, buku, tanggal)

        elif pilih == '2':
            perpus.tampilkan()

        elif pilih == '3':
            nama = input("Masukkan nama yang dicari: ")
            perpus.cari(nama)

        elif pilih == '4':
            nama = input("Nama yang mengembalikan: ")
            perpus.hapus(nama)

        elif pilih == '5':
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
