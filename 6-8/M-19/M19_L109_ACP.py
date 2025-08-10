import math

def circumference(r):
  c = 2 * math.pi * r
  print("circumference of circle is",c)

r = float(input("enter radius of circle:"))

circumference(r)