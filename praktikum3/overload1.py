class merchandise:
    def __init__(self, fare):
        self.fare = fare

    def __add__(self, other):
        return self.fare+other.fare

album = merchandise(700000)
lightstick = merchandise(800000)
total = album+lightstick
print(f'\nHarga Total: {str(total)}\n')