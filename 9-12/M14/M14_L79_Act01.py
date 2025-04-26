import numpy as np

data_type = [("name", "S15"), ("class", int), ("height", float)]

students_details = [("Jack", 5, 49.5), ("James", 6, 53.7),("Frank", 5, 43.13), ("Amber", 5, 43.21)]

# create a structured array
students = np.array(students_details, dtype=data_type)
print("Original array:")
print(students)
print()

print("Sort by height:")
print(np.sort(students, order="height"))