class Robot:

    # class attribute
    species = "robot"

    # instance attribute
    def __init__(self, nm, ori):
        self.name = nm
        self.origin = ori
    
    def introduction(self):
        print("Hi I am a ",self.species)
    
    def details(self):
        print("My name is", self.name)
        print("I made in ", self.origin)

tom = Robot("Tom","Japan")
jerry = Robot("Jerry","Italy")

tom.introduction()
tom.details()
print()

jerry.introduction()
jerry.details()
