class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Jay", 21)

# Menambah atribut address secara dinamis
person.address = "Seattle, Washington DC, AS"

# Mengubah nilai atribut age secara dinamis
person.age = 21

print(person.name)
print(person.age)
print(person.address)