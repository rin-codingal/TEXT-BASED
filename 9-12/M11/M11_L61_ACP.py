# implemet circuit

a=1
b=0
c=0

# Computing all bitwise operations
aANDb = a & b
bXORc = b ^ c
bORc = b | c
g = bXORc & bORc

# Calculating final result
final = aANDb ^ g

print(f"aANDb ^ bXORc & bORc = {final}")