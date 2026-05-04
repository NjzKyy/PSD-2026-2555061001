def insertion_sort(waktu):
    for i in range(1, len(waktu)):
        key = waktu[i]  
        j = i - 1

        while j >= 0 and waktu[j] > key:
            waktu[j + 1] = waktu[j]
            j -= 1

        waktu[j + 1] = key

def main():
    try:
        n = int(input("Masukkan jumlah data pengiriman: "))
        
        waktu = []
        
        for i in range(n):
            data = float(input(f"Masukkan waktu tempuh pengiriman ke-{i+1} (jam): "))
            waktu.append(data)

        print("\nData sebelum diurutkan:")
        print(waktu)

        insertion_sort(waktu)

        print("\nData setelah diurutkan (tercepat → terlama):")
        print(waktu)

        print("\nPengiriman tercepat:", waktu[0], "jam")
        print("Pengiriman terlambat:", waktu[-1], "jam")

    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

if __name__ == "__main__":
    main()
