class Indonesia():
    def capital(self):
        print("Jakarta is the capital of Indonesia.")
 
    def language(self):
        print("Bahasa Indonesia is the national language of Indonesia.")
 
    def type(self):
        print("Indonesia is a developing country.")
 
# Class 2
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
 
# Object Creation
obj_ind = Indonesia()
obj_usa = USA()

# Common Interface
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
    print()