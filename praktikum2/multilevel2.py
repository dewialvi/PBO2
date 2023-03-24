print("Dewi Alvi Nurfadilah\n210511085\nTI21B\n")

class Drakor:
    def drakor_info(self):
        print("Drakor merupakan serial drama dari Korea Selatan.")

class Judul:
    def judul_info(self):
        print("The Glory adalah drakor dengan rating tertinggi saat ini.")

class Viu(Drakor, Judul):
    pass

# create an object of Bat class
b1 = Viu()

b1.drakor_info()
b1.judul_info()