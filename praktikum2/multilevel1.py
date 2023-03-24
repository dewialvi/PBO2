print("Dewi Alvi Nurfadilah\n210511085\nTI21B\n")


class Film:
    def __init__(self, judul):
        self.judul = judul
    def genre(self):
        print(f"{self.judul} comedy")
class Platform(Film):
    def __init__(self, judul, netflix):
        super().__init__(judul)
        self.netflix = netflix
    def menonton(self):
        print(f"{self.judul} adalah film yang tayang di netflix dengan genre {self.netflix}")
class Rating(Platform):
    def __init__(self, judul, netflix, rate):
        super().__init__(judul, netflix)
        self.rate = rate
    def genre(self):
        print(f"{self.judul} adalah {self.rate} film rating tertinggi ")
rating = Rating("Seoul Vibe", "comedy", "salah satu")
rating.genre() # Output: Seoul Vibe adalah film rating tertinggi
rating.menonton() # Output: Seoul Vibe adalah film yang tayang di netflix dengan genre

