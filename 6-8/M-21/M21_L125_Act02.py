from abc import ABC

# create a base class / parent class
class Animal(ABC):
	# should be implemented by all sub-classes
	def move(self):
		pass

# sub classes / child classes
class Human(Animal):
	def move(self):
		print("I can walk and run")

class Snake(Animal):
	def move(self):
		print("I can crawl")

class Dog(Animal):
	def move(self):
		print("I can bark")

class Lion(Animal):
	def move(self):
		print("I can roar")
		
# create object
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()