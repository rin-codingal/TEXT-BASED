def reverse_array_demonstration():
    original_array = [6, 5, 4, 3, 2, 1]

    # Method 1: Python Slicing [::-1] (Most idiomatic & concise)
    reversed_slicing = original_array[::-1]

    # Method 2: In-place Two-Pointer Swap Algorithm (Standard Computer Science approach)
    reversed_two_pointer = original_array.copy()
    left = 0
    right = len(reversed_two_pointer) - 1
    
    while left < right:
        # Swap elements at left and right pointers
        reversed_two_pointer[left], reversed_two_pointer[right] = (
            reversed_two_pointer[right],
            reversed_two_pointer[left],
        )
        left += 1
        right -= 1

    # Method 3: Using the built-in reversed() function
    reversed_builtin = list(reversed(original_array))

    # Display the primary required output
    print("Original array :", original_array)
    print("Reversed array :", reversed_slicing)


if __name__ == "__main__":
    reverse_array_demonstration()