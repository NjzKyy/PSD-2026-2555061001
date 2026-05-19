class StackArray:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.stack = [None] * self.MAX
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.MAX - 1

    def push(self, data):
        if self.is_full():
            print("Stack penuh")
            return

        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.is_empty():
            print("Stack kosong")
            return None

        data = self.stack[self.top]
        self.top -= 1
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]

    def display(self):
        if self.is_empty():
            print("Stack kosong")
            return

        print("Isi Stack:")
        for i in range(self.top, -1, -1):
            print(self.stack[i])

undo_stack = StackArray()
redo_stack = StackArray()

text = ""

while True:
    print("\n===== TEXT EDITOR =====")
    print("1. Tambah Teks")
    print("2. Undo")
    print("3. Redo")
    print("4. Lihat Text")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambahan = input("Masukkan teks: ")

        undo_stack.push(text)

        text += tambahan

        redo_stack = StackArray()

        print("Teks berhasil ditambahkan")

    elif pilihan == "2":
        if undo_stack.is_empty():
            print("Tidak ada aksi untuk undo")
        else:
            redo_stack.push(text)
            text = undo_stack.pop()
            print("Undo berhasil")

    elif pilihan == "3":
        if redo_stack.is_empty():
            print("Tidak ada aksi untuk redo")
        else:
            undo_stack.push(text)
            text = redo_stack.pop()
            print("Redo berhasil")

    elif pilihan == "4":
        print("\nText saat ini:")
        print(text)

    elif pilihan == "5":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")