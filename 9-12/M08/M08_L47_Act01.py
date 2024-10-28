# parent class
class Person( object ):	

		# __init__ is known as the constructor		
		def __init__(self, name, idnumber):
				self.name = name
				self.idnumber = idnumber
		def display(self):
				print("Name: ",self.name)
				print("ID number: ",self.idnumber)

# child class
class Employee( Person ):		
		def __init__(self, name, idnumber, salary, post):
				self.salary = salary
				self.post = post

				# invoking the __init__ of the parent class
				Person.__init__(self, name, idnumber)

				
# creation of an object variable or an instance
a = Employee("Alexander", 20240815, 25000, "Fulltime employee")	

# calling a function of the class Person using its instance
a.display()