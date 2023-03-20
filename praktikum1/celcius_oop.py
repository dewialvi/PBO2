# Nama : Dewi Alvi Nurfadilah
# NIM : 210511085
# Kelas : TI21B/R2

class KonversiSuhu ():
    def __init__(self,celcius):
        self.celcius = celcius

    def fahrenheit(self):
        F = (5/9)*self.celcius+32
        return F

    def kelvin(self):
        K = self.celcius+273
        return K

    def reamur(self):
        R = (4/5)*self.celcius
        return R
    
suhu = KonversiSuhu(30)
fahrenheit = suhu.fahrenheit()
kelvin = suhu.kelvin()
reamur = suhu.reamur()

print(f'Konversi Celcius ke Fahrenheit\n\t============\t\nFahrenheit: {suhu.fahrenheit()} F')

print(f'Konversi Celcius ke Kelvin\n\t============\t\nKelvin: {suhu.kelvin()} K')

print(f'Konversi Celcius ke Reamur\n\t============\t\nReamur: {suhu.reamur()} Re')

    