print("Dewi Alvi Nurfadilah\n210511085\nTI21B\n")

class Film:
    def __init__(self, genre, platform):
        self.genre = genre
        self.platform = platform
    def menonton(self):
        print("V sedang menonton.")
class Kegiatan(Film):
    def __init__(self, genre, platform, cc):
        super().__init__(genre, platform)
        self.cc = cc
    def melihat(self):
        print("Jay sedang melihat film di Netflix.")
kegiatanA = Kegiatan("kegiatan", "action", "netflix")
kegiatanA.menonton() # Output: V sedang menonton.
kegiatanA.melihat() # Output: Jay sedang melihat film di Netflix.