class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print("Fullname: " + self.firstname + " " + self.lastname)

class Student(Person):
  def __init__(self, fn, ln, year):
    super().__init__(fn, ln)
    self.graduationyear = year

x = Student("King", "Indo", 2024)
x.printname()
print("Graduation year:",x.graduationyear)
