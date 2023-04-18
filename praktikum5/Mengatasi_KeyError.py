dictionary = {"jay": 1, "jake": 2, "jungwon": 3}
try:
    value = dictionary["heeseung"]
except KeyError:
    print("Key yang diminta tidak ditemukan pada dictionary!")
