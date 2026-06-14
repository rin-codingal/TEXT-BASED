class Vehicles:
	# Constructor
	def __init__(vehicleType):
		print('Vehicles is a ', vehicleType)

class Car(Vehicles):

	# Constructor
	def __init__(self):
		Vehicles.__init__('Car')

# Driver's code
print(issubclass(Car, Vehicles))
print(issubclass(Car, list))
print(issubclass(Car, Car))
print(issubclass(Car, (list, Vehicles)))
