from abc import ABC, abstractmethod

# Create parent class
class Absclass(ABC):
	# Function to print a value
    def display(self,x):
        print("Passed value: ", x)

	# Abstract Method
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

# Create sub class / child class
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

#object of test_class created
test_obj = test_class()

test_obj.task()
test_obj.display(100)