print("Dewi Alvi Nurfadilah\n210511085\nTI21B\n")


class Idol:
    def __init__(self, nama, posisi):
        self.nama = nama
        self.posisi = posisi
    def rekaman(self):
        print(self.nama, "sedang rekaman")
class Kpop:
    def __init__(self, nama,kegiatan ):
        self.nama = nama
        self.kegiatan = kegiatan
    def latihan(self):
        print(self.nama, "sedang latihan dance")
class IdolKpop(Idol, Kpop):
    def __init__(self, nama, posisi, kegiatan):
        Idol.__init__(self, nama, posisi)
        Kpop.__init__(self, nama, kegiatan)
    def syuting(self):
        print(self.nama, "sedang syuting MV")
idol_kpop = IdolKpop("Jungkook", "main dancer", "rekaman")
idol_kpop.rekaman() # output: Jungkook sedang rekaman
idol_kpop.latihan() # output: Jungkook sedang latihan dance
idol_kpop.syuting() # output: Jungkook sedang syuting MV