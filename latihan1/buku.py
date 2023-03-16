class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    def info(self):
        print(f"Judul: {self.judul}\nPenulis: {self.penulis}")
bukuA = Buku("I Want To Die But I Want To Eat Tteokpokki", "Baek Se Hee")
bukuA.info()
