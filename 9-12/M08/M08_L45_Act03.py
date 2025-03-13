class Parrot:
    # class static attribute
    species = "bird"

    # instance attribute
    def __init__(self, nm, h):
        self.name = nm
        self.age = h

# instantiate the Parrot class
blue = Parrot("Blue", 10)
jell = Parrot("Jelly", 15)

# access the class attributes
print("Blue is a ",blue.species)
print("Jelly is also a ",jell.species)
print()

# access the instance attributes
print(f"{blue.name} is {blue.age} years old")
print(f"{jell.name} is {jell.age} years old")