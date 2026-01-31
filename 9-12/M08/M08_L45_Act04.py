class Parrot:    
    # instance attributes
    def __init__(self, nm, h):
        self.name = nm
        self.age = h
        
    def sing(self, song):
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is now dancing"

# instantiate the object
blu = Parrot("Blue", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())