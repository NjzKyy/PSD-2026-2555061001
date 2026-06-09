reservasi = {
    101: {
        "nama": "Rizki Novreza",
        "lama_menginap": 3,
        "status": "Check-in"
    },
    102: {
        "nama": "Alfarel Brilliant",
        "lama_menginap": 2,
        "status": "Check-in"
    },
    103: {
        "nama": "Ridho Saputra",
        "lama_menginap": 5,
        "status": "Booking"
    }
}

while True:
    print("\n=== SISTEM RESERVASI HOTEL ===")
    print("1. Lihat Data Kamar")
    print("2. Cari Data Kamar")
    print("3. Tambah Reservasi")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\nDaftar Reservasi:")
        for kamar, data in reservasi.items():
            print(f"\nKamar : {kamar}")
            print(f"Nama  : {data['nama']}")
            print(f"Lama Menginap : {data['lama_menginap']} hari")
            print(f"Status: {data['status']}")

    elif pilihan == "2":
        kamar = int(input("Masukkan nomor kamar: "))

        if kamar in reservasi:
            data = reservasi[kamar]
            print("\nData Ditemukan")
            print(f"Nama  : {data['nama']}")
            print(f"Lama Menginap : {data['lama_menginap']} hari")
            print(f"Status: {data['status']}")
        else:
            print("Kamar tidak memiliki reservasi.")

    elif pilihan == "3":
        kamar = int(input("Nomor kamar: "))
        nama = input("Nama tamu: ")
        lama = int(input("Lama menginap (hari): "))

        reservasi[kamar] = {
            "nama": nama,
            "lama_menginap": lama,
            "status": "Booking"
        }

        print("Reservasi berhasil ditambahkan.")

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")