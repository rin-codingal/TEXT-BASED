class shape: #parent class
    def __init__(self, w, l, n):
        self.width = w
        self.length = l
        self.name = n

    def printdetail(self):
        print("Shape: " + self.name)
        print("Width: ",self.width)
        print("Length: ",self.length)

class rectangle(shape):
    def __init__(self, wi, le):
        shape_name = "rectangle"
        super().__init__(wi, le, shape_name)
    
    def area(self):
        return self.width * self.length

class square(shape):
    def __init__(self, s):
        shape_name = "square"
        super().__init__(s, s, shape_name)

        self.side = s
        
    
    def area(self):
        return self.side * self.side
    
    def printdetail(self):
        print("Shape: " + self.name)
        print("Side: ",self.side)




x = 5
y = 2
print()

rect = rectangle(x,y) #rectangle object
rect.printdetail()
print("area: ",rect.area())

a = 5
print()

sq = square(a) #square object
sq.printdetail()
print("area: ",sq.area())