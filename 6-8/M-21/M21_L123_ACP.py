class Vehicle:
    def __init__(self, name, mile, volume):
        self.name = name
        self.mileage = mile
        self.capacity = volume

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())