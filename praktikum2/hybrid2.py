class Makanan:
    def __init__(self, nama, jenis, ):
        self.nama = nama
        self.jenis = jenis
    def get_info(self):
        print("nama:", self.nama)
        print("jenis:", self.jenis)
# Single Inheritance
class Asal(Makanan):
    def __init__(self, nama, jenis, daerah):
        super().__init__(nama, jenis, )
        self.daerah = daerah
    def get_info(self):
        super().get_info()
        print("Berasal dari:", self.daerah)
# Single Inheritance
class Variasi(Makanan):
    def __init__(self, nama, jenis, variasi, harga):
        super().__init__(nama, jenis, )
        self.variasi = variasi
        self.harga = harga
    def get_info(self):
        super().get_info()
        print("Variasi:", self.variasi)
        print("Harga:", self.harga)
# Multiple Inheritance
class Rasa(Variasi, Asal):
    def __init__(self, nama, jenis, variasi, harga, daerah, 
rasa):
        Variasi.__init__(self, nama, jenis, variasi, harga)
        Asal.__init__(self, nama, jenis, daerah)
        self.rasa = rasa
    def get_info(self):
        super().get_info()
        print("Berasal dari Daerah:", self.daerah)
        print("Rasanya:", self.rasa)
