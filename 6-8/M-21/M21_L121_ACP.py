class Dog:
	# Class Variable
	animal = 'dog'			

	# The init method or constructor
	def __init__(self, bred, colour):
	
		# Instance Variable	
		self.breed = bred
		self.color = colour	
	
# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print()

print('Buzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

print()

# Class variables can be accessed using class
# name also
print("Accessing class variable using class name")
print(Dog.animal)	
