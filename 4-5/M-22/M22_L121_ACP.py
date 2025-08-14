class Dog:
  species = "Dog"
  def __init__(self, name, age):
    self.name= name
    self.age= age

Blacky = Dog("Blacky", 8)

Mars = Dog("Mars", 10)

print(f"Blacky Is A {Blacky.species}")
print(f"Mars Is Also A {Mars.species}")
print(f"Blacky Is {Blacky.age} Years Old" )
print(f"{Mars.name} Is {Mars.age} Years Old")