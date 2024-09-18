class Vehicle:

	# create init method
    def __init__(self, speed, mile):

		# bind the arguments
        self.max_speed = speed
        self.mileage = mile

# Object creation
modelX = Vehicle(240, 18)

# access the variables inside init method
print("Model Max Speed:",modelX.max_speed)
print("Model Mileage:", modelX.mileage)