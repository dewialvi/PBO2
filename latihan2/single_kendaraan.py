class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    def berkendara(self):
        print("Kendaraan ini sedang melaju.")
class SepedaMotor(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
    def berjalan(self):
        print("Sepeda motor ini sedang berjalan.")
motorA = SepedaMotor("Sepeda Motor", "Honda", "Hitam", 150)
motorA.berkendara() # Output: Kendaraan ini sedang melaju.
motorA.berjalan() # Output: Sepeda motor ini sedang berjalan.