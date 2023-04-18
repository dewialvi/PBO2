list_angka = [1, 2, 3, 4, 5]
try:
    value = list_angka[6]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")