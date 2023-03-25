class Youtube:
    def __init__(self, nama, jenis, ):
        self.nama = nama
        self.jenis = jenis
    def get_info(self):
        print("nama:", self.nama)
        print("jenis:", self.jenis)
# Single Inheritance
class Channel(Youtube):
    def __init__(self, nama, jenis, subscriber):
        super().__init__(nama, jenis, )
        self.subscriber = subscriber
    def get_info(self):
        super().get_info()
        print("Jumlah:", self.subscriber)
# Single Inheritance
class Konten(Youtube):
    def __init__(self, nama, jenis, konten, viewers):
        super().__init__(nama, jenis, )
        self.konten = konten
        self.viewers = viewers
    def get_info(self):
        super().get_info()
        print("konten:", self.konten)
        print("viewers:", self.viewers)
# Multiple Inheritance
class Trending(Konten, Channel):
    def __init__(self, nama, jenis, konten, viewers, subscriber, 
trending):
        Konten.__init__(self, nama, jenis, konten, viewers)
        Channel.__init__(self, nama, jenis, subscriber)
        self.trending = trending
    def get_info(self):
        super().get_info()
        print("Berapa subscriber:", self.subscriber)
        print("Trending ke:", self.trending)
