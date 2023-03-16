class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def info(self):
        print(f"Nama: {self.nama}\nNIM: {self.nim}")
mahasiswaB = Mahasiswa("Dewi Alvi Nurfadilah", "210511085")
mahasiswaB.info()