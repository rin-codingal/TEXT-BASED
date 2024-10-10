x = 5
y = 9
z = 1

print()
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print()

x = x ^ y
y = x ^ y
x = x ^ y

y = y ^ z
z = y ^ z
y = y ^ z

print("--- After Number Swapping ---")

print()
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print()