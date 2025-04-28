class Parrot:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, nm, h):
        self.name = nm
        self.age = h

# create the object of the Parrot class
blu = Parrot("Blue", 10)
woo = Parrot("Wooey", 15)

# access the class attributes
print(f"Blue is a {blu.species}")
print(f"Wooey is also a {woo.species}")

# access the instance attributes
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")
