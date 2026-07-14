# parent class
class Person( object ):	
	# __init__ is known as the constructor		
	def __init__(self, nm, id):
		self.name = nm
		self.idnumber = id
	
	def display(self):
		print("Name: ",self.name)
		print("ID number: ",self.idnumber)

# child class
class Employee(Person):		
	def __init__(self, nam, idnum, salary, pos):
		self.salary = salary
		self.post = pos

		# invoking the __init__ of the parent class
		Person.__init__(self, nam, idnum)

				
# creation of an object variable or an instance
a = Employee("Alexander", 20240815, 25000, "Fulltime employee")	

# calling a method of the class Person using its instance
a.display()
print()