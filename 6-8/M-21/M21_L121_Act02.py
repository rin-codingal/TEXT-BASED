class Vehicle:
	# create init method or constructor
  def __init__(self, speed, mile):
		# bind the arguments
    self.max_speed = speed
    self.mileage = mile

# Object creation
bike = Vehicle(240, 18)

# access the variables inside init method
print("Bike Max Speed:",bike.max_speed)
print("Bike Mileage:", bike.mileage)