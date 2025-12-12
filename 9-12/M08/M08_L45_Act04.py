class Parrot:
    
    # instance attributes
    def __init__(self, nm, h):
        self.name = nm
        self.age = h
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blue", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())