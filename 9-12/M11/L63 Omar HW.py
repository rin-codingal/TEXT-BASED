def reverse_bits(num):
    binary_representation = bin(num)[2:]
    reversed_binary = binary_representation[::-1]
    reversed_number = int(reversed_binary, 2)
    
    return reversed_number

original_number = int(input("Enter your original number: "))
result = reverse_bits(original_number)

print(f"Reversed Number: {result} ({bin(result)[2:]})")