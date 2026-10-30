def rotate_left(arr, k):
    """
    Rotates an array to the left by k positions.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not arr:
        return arr
    
    n = len(arr)
    k = k % n  # Handles cases where k is greater than the array size
    
    # Slicing technique for left rotation
    return arr[k:] + arr[:k]


def run_rotate_array_project():
    print("=== 'ROTATE ARRAY WITH INPUTS' PROGRAM ===\n")
    
    try:
        # 1. Take array size from the user
        size = int(input("Enter the size of the array: "))
        if size <= 0:
            print("Array size must be a positive integer greater than zero.")
            return
            
        # 2. Take array elements from the user
        user_input = input(f"Enter {size} space-separated integers: ")
        original_array = [int(item) for item in user_input.split()]
        
        if len(original_array) != size:
            print(f"Note: You entered {len(original_array)} elements, but specified size was {size}.")
            
        if not original_array:
            print("No elements were entered. Please try again.")
            return
            
        print(f"\nOriginal array      : {original_array}")
        
        # 3. Rotate 1 place to the left
        rotated_1 = rotate_left(original_array, 1)
        print(f"Rotated 1 place left : {rotated_1}")
        
        # 4. Rotate 2 places to the left
        rotated_2 = rotate_left(original_array, 2)
        print(f"Rotated 2 places left: {rotated_2}")
        
    except ValueError:
        print("Invalid input! Please ensure you enter valid integers.")


if __name__ == "__main__":
    run_rotate_array_project()