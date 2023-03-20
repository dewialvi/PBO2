class Pekerjaan:
    def __init__(self, jenis, posisi):
        self.jenis = jenis
        self.posisi = posisi
    def menyanyi(self):
        print("Jake sedang menyanyi.")
class Idol(Pekerjaan):
    def __init__(self, jenis, posisi, cc):
        super().__init__(jenis, posisi)
        self.cc = cc
    def latihan(self):
        print("Idol ini sedang latihan.")
idolA = Idol("Idol", "boygroup", "main vocal")
idolA.menyanyi() # Output: Jake sedang menyanyi.
idolA.latihan() # Output: Idol ini sedang latihan.