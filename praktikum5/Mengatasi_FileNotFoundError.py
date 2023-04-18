try:
    with open("materi.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("File yang diminta tidak ditemukan!")
