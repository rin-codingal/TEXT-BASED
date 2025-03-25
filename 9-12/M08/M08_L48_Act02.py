class Computer:

    def __init__(self): #constructor
        self.__maxprice = 900 #__ means private variable

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer() #create object
c.sell()
print()

print("try to update maxprice directly")
# change the price
c.__maxprice = 750
c.sell()
print()

print("after using method setMaxPrice:")
# using setter function
c.setMaxPrice(1000)
c.sell()

