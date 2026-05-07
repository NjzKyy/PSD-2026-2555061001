jadwal_penerbangan = [
    {"kode": "GA102", "tujuan": "Jakarta", "jam": "07:00"},
    {"kode": "GA210", "tujuan": "Bandung", "jam": "08:30"},
    {"kode": "ID301", "tujuan": "Surabaya", "jam": "09:15"},
    {"kode": "JT404", "tujuan": "Medan", "jam": "10:45"},
    {"kode": "LA550", "tujuan": "Bali", "jam": "12:00"},
    {"kode": "QZ701", "tujuan": "Yogyakarta", "jam": "14:20"},
    {"kode": "SJ880", "tujuan": "Makassar", "jam": "16:10"},
    {"kode": "TR999", "tujuan": "Batam", "jam": "18:00"}
]

def binary_search(data, target):
    kiri = 0
    kanan = len(data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if data[tengah]["kode"] == target:
            return tengah
        elif data[tengah]["kode"] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return -1

print("=" * 50)
print("     SISTEM PENCARIAN JADWAL PENERBANGAN")
print("=" * 50)

print("\nDaftar Jadwal Penerbangan:")
for i, penerbangan in enumerate(jadwal_penerbangan):
    print(f"{i+1}. {penerbangan['kode']} - "
          f"{penerbangan['tujuan']} ({penerbangan['jam']})")

cari = input("\nMasukkan kode penerbangan yang dicari: ").upper()

hasil = binary_search(jadwal_penerbangan, cari)

print("\nHASIL PENCARIAN")
print("-" * 30)

if hasil != -1:
    data = jadwal_penerbangan[hasil]

    jam = int(data["jam"].split(":")[0])

    if jam < 12:
        kategori = "Penerbangan Pagi"
    elif jam < 17:
        kategori = "Penerbangan Siang"
    else:
        kategori = "Penerbangan Malam"

    print(f"Kode Penerbangan : {data['kode']}")
    print(f"Tujuan            : {data['tujuan']}")
    print(f"Jam Keberangkatan : {data['jam']}")
    print(f"Kategori          : {kategori}")
    print(f"Indeks Data       : {hasil}")
else:
    print("Jadwal penerbangan tidak ditemukan!")