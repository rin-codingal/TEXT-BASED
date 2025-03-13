import numpy as np

data_type = [("name", "S15"), ("grade", int), ("weight", float)]
students_details = [("Jerome", 7, 53.5), ("Nicole", 9, 60.5),("Shawn", 5, 64.10), ("Tasya", 11, 57.11)]

# create a structured array
students = np.array(students_details, dtype=data_type)   
print("Original array:")
print(students)
print()

print("Sort by weight:")
print(np.sort(students, order="weight"))