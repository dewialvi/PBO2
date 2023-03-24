print("Dewi Alvi Nurfadilah\n210511085\nTI21B\n")

class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Pekerjaan(Person):
    def __init__(self, nama, umur, pekerjaan):
        super().__init__(nama, umur, pekerjaan)
        self.pekerjaan = pekerjaan
    def display_info(self):
        super().display_info()
        print(f"Pekerjaan: {self.pekerjaan}")

class Posisi(Person):
    def __init__(self, nama, umur, posisi):
        super().__init__(nama, umur)
        self.posisi = posisi
    def display_info(self):
        super().display_info()
        print(f"Posisi: {self.posisi}")

class PekerjaanPosisi(Pekerjaan, Posisi):
    def __init__(self, nama, umur, pekerjaan, posisi):
        Pekerjaan.__init__(self, nama, umur, pekerjaan)
        Posisi.__init__(self, nama, umur, posisi)
    def display_info(self):
        super().display_info()
        print(f"Posisi: {self.posisi}")

# contoh penggunaan
pekerjaan_PosisiA = PekerjaanPosisi("Kim Namjoon", 28, "Idol Kpop", "Leader")
pekerjaan_PosisiA.display_info()