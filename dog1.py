class Dog:
    species = "Canis Familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)
print(buddy.name)
print(buddy.age)
print(buddy.species)
print(miles.species)
buddy.name = "Bino"
print(buddy.name)