def binary_to_decimal():
    print("=== BINARY TO DECIMAL CONVERTER ===")
    
    while True:
        # Prompt user for binary input
        binary_str = input("\nEnter a binary number (0s and 1s only): ").strip()
        
        # Validate that the string contains only '0' and '1'
        if all(char in '01' for char in binary_str) and len(binary_str) > 0:
            break
        else:
            print("Invalid input! Please enter digits consisting only of 0s and 1s.")

    # Method 1: Using Python's built-in int() function with base 2
    decimal_built_in = int(binary_str, 2)

    # Method 2: Manual conversion (Positional notation algorithm)
    # Example for '1011': 1*(2^3) + 0*(2^2) + 1*(2^1) + 1*(2^0) = 11
    decimal_manual = 0
    for index, digit in enumerate(reversed(binary_str)):
        decimal_manual += int(digit) * (2 ** index)

    # Output results
    print("\n--- Results ---")
    print(f"Binary Code    : {binary_str}")
    print(f"Decimal Value  : {decimal_manual}")


if __name__ == "__main__":
    binary_to_decimal()