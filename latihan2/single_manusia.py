class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang presentasi.")
class Kegiatan(Manusia):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim = nim
    def belajar(self):
        print(f"{self.nama} dengan NIM {self.nim} sedang belajar.")
kegiatanA = Kegiatan("Dewi", 20, "210511085")
kegiatanA.berbicara() # Output: Dewi sedang menyanyi.
kegiatanA.belajar() # Output: Dewi dengan NIM 210511085 sedang belajar.