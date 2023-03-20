# Nama : Dewi Alvi Nurfadilah
# NIM : 210511085
# Kelas : TI21B/R2

class KonversiSuhu ():
    def __init__(self,reamur):
        self.reamur = reamur

    def celcius(self):
        C = self.reamur*(5/4)
        return C

    def fahrenheit(self):
        F = (9/4)*self.reamur+32
        return F

    def kelvin(self):
        K = (5/4)*(self.reamur+273)
        return K
    
suhu = KonversiSuhu(30)
celcius = suhu.celcius()
fahrenheit = suhu.fahrenheit()
kelvin = suhu.kelvin()

print(f'Konversi Reamur ke Celcius\n\t============\t\nCelcius: {suhu.celcius()} C')

print(f'Konversi Reamur ke Fahrenheit\n\t============\t\nFahrenheit: {suhu.fahrenheit()} F')

print(f'Konversi Reamur ke Kelvin\n\t============\t\nKelvin: {suhu.kelvin()} K')

    