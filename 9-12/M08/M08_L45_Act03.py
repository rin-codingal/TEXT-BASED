class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blue = Parrot("Blue", 10)
jell = Parrot("Jelly", 15)

# access the class attributes
print("Blue is a {}".format(blue.species))
print("Jelly is also a {}".format(jell.species))
print()

# access the instance attributes
print("{} is {} years old".format( blue.name, blue.age))
print("{} is {} years old".format( jell.name, jell.age))

