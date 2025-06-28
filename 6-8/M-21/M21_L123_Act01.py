class Vehicle: # parent class
    def __init__(self, nm, speed, mile):
        self.name = nm
        self.max_speed = speed
        self.mileage = mile

class Bus(Vehicle): #child class
    pass

School_bus = Bus("School Volvo", 180, 12)

print("Vehicle Name: ", School_bus.name, "\nSpeed: ", School_bus.max_speed, "\nMileage: ", School_bus.mileage)