class Circle:
    radius= 0
	
    def Area_Of_Circle(self, radius):
        AreaCircle = 3.14 * radius * radius
        return AreaCircle
    
    def Perimeter_Of_Circle(self, radius):
        PerimeterCircle = 2 * 3.14 * radius
        return PerimeterCircle

my_circle = Circle()
rad = int(input("enter radius here: "))

print("Area of Circle :", my_circle.Area_Of_Circle(rad))

print("Perimeter of Circle :", my_circle.Perimeter_Of_Circle(rad))