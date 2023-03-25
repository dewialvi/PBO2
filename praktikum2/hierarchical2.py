class DisneyHotstar:
    def __init__(self, judul):
        self.judul = judul
    def get_judul(self):
        return self.judul
class Film(DisneyHotstar):
    def __init__(self, judul, genre):
        super().__init__(judul)
        self.genre = genre
    def get_genre(self):
        return self.genre
class Series(DisneyHotstar):
    def __init__(self, judul, jumlah_episode):
        super().__init__(judul)
        self.jumlah_episode = jumlah_episode
    def get_jumlah_episode(self):
        return self.jumlah_episode
# turunan Hierarchical Inheritance
class Kartun(Film):
    def __init__(self, judul, genre, durasi):
        super().__init__(judul, genre)
        self.durasi = durasi
    def get_durasi(self):
        return self.durasi
# turunan Hierarchical Inheritance
class Marvel(Series):
    def __init__(self, judul, jumlah_episode, rating):
        super().__init__(judul, jumlah_episode)
        self.rating = rating
    def get_rating(self):
        return self.rating