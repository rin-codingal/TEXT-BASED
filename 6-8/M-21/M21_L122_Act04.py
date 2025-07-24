class rectangle():
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

rLength = int(input("Enter rectangle length : "))
rBreadth = int(input("Enter rectangle breadth : "))

NewR = rectangle(rLength,rBreadth)

print("Rectangle area: ",NewR.area())