def insertion_sort(arr):
    """
    Sorts an array in ascending order using the Insertion Sort algorithm.
    """
    # Traverse from the second element (index 1) to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of the sorted segment that are greater than the key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Insert the key into its correct position
        arr[j + 1] = key
        
    return arr


def run_insertion_sort_project():
    print("=== JOHN'S 'SORT WITH INSERTION' PROGRAM ===\n")
    
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
            
        print(f"\nOriginal array : {original_array}")
        
        # 3. Sort the array using Insertion Sort
        sorted_array = insertion_sort(original_array.copy())
        
        print(f"Sorted array   : {sorted_array}")
        
    except ValueError:
        print("Invalid input! Please ensure you enter valid integers.")


if __name__ == "__main__":
    run_insertion_sort_project()