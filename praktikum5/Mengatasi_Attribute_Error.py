class Idol:
    def __init__(self, nama, posisi):
        self.nama = nama
        self.posisi = posisi
idol = Idol("Jay", "vocalist")
try:
    print(idol.kpop)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")
