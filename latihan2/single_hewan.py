class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama, "bergerak")

class Kucing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Guk!")
        
kucingA = Kucing("Yeontan", 2, "Teacup Pomeranian")
kucingA.bergerak() # output: Yeontan bergerak
kucingA.bersuara() # output: Guk!