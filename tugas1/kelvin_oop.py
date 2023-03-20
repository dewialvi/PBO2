# Nama : Dewi Alvi Nurfadilah
# NIM : 210511085
# Kelas : TI21B/R2

class KonversiSuhu ():
    def __init__(self,kelvin):
        self.kelvin = kelvin

    def celcius(self):
        C = self.kelvin-273
        return C

    def fahrenheit(self):
        F = ((self.kelvin-273)*(9/5))+32
        return F

    def reamur(self):
        R = (4/5)*(self.kelvin-273)
        return R
    
suhu = KonversiSuhu(30)
celcius = suhu.celcius()
fahrenheit = suhu.fahrenheit()
reamur = suhu.reamur()

print(f'Konversi Kelvin ke Celcius\n\t============\t\nCelcius: {suhu.celcius()} C')

print(f'Konversi Kelvin ke Fahrenheit\n\t============\t\nFahrenheit: {suhu.fahrenheit()} F')

print(f'Konversi Kelvin ke Reamur\n\t============\t\nReamur: {suhu.reamur()} R')

    