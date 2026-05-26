class Node:
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, npm, nama):

        if root is None:
            return Node(npm, nama)

        if npm < root.npm:
            root.left = self.insert(root.left, npm, nama)

        elif npm > root.npm:
            root.right = self.insert(root.right, npm, nama)

        return root

    def tambah_mahasiswa(self, npm, nama):
        self.root = self.insert(self.root, npm, nama)

    def search(self, root, npm):

        if root is None:
            return None

        if root.npm == npm:
            return root

        if npm < root.npm:
            return self.search(root.left, npm)

        return self.search(root.right, npm)

    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(f"NPM : {root.npm} | Nama : {root.nama}")
            self.inorder(root.right)

bst = BinarySearchTree()

bst.tambah_mahasiswa(2555061005, "Andi")
bst.tambah_mahasiswa(2555061001, "Rizki")
bst.tambah_mahasiswa(2555061008, "Budi")
bst.tambah_mahasiswa(2555061003, "Sinta")
bst.tambah_mahasiswa(2555061007, "Dewi")

print("=== DATA MAHASISWA (INORDER) ===")
bst.inorder(bst.root)

cari_npm = 2555061003

hasil = bst.search(bst.root, cari_npm)

print("\n=== HASIL PENCARIAN ===")

if hasil:
    print(f"Data ditemukan!")
    print(f"NPM  : {hasil.npm}")
    print(f"Nama : {hasil.nama}")
else:
    print("Data tidak ditemukan")