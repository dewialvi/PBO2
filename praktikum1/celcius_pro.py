# Nama    : Dewi Alvi Nurfadilah
# NIM     : 210511085
# Kelas   : TI21B/R2


class Suhu:
    @staticmethod
    def celcius_to_fahrenheit(c):
        f = (9/5) * c + 32
        return f
    
    @staticmethod
    def celcius_to_kelvin(c):
        k = c + 273.15
        return k

    @staticmethod
    def celcius_to_reamur(c):
        r = (4/5) * c
        return r


# Contoh penggunaan
C = 90
F = Suhu.celcius_to_fahrenheit(C)
K = Suhu.celcius_to_kelvin(C)
R = Suhu.celcius_to_reamur(C)

print("Konversi", C, "derajat Celcius = ", F, "derajat Fahrenheit,")
print("Konversi", C, "derajat Celcius = ", K, "derajat Kelvin,")
print("Konversi", C, "derajat Celcius = ", R, "derajat Reamur,")