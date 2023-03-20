# Nama : Dewi Alvi Nurfadilah
# NIM : 210511085
# Kelas : TI21B/R2

class KonversiSuhu ():
    def __init__(self,fahrenheit):
        self.fahrenheit = fahrenheit

    def celcius(self):
        C = (5/9)*self.fahrenheit-32
        return C

    def kelvin(self):
        K = (5/9)*(self.fahrenheit-32)+273
        return K

    def reamur(self):
        R = (4/9)*(self.fahrenheit-32)
        return R
    
suhu = KonversiSuhu(30)
celcius = suhu.celcius()
kelvin = suhu.kelvin()
reamur = suhu.reamur()

print(f'Konversi Fahrenheit ke Celcius\n\t============\t\nCelcius: {suhu.celcius()} C')

print(f'Konversi Fahrenheit ke Kelvin\n\t============\t\nKelvin: {suhu.kelvin()} K')

print(f'Konversi Fahrenheit ke Reamur\n\t============\t\nReamur: {suhu.reamur()} R')

    