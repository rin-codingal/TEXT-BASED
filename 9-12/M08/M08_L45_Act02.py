class student:
	#static feature
	grade = 11
	name = "Penguin"
	
	def introduction(self): #method 1
		print("Hi I am a student")

	def details(self): #method 2
		print("My name is", self.name)
		print("I study in Grade", self.grade)

ob = student() #create new object
ob.introduction()
ob.details()