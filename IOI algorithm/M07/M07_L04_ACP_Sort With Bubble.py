def bubble_sort(arr):
    """
    Sorts an array in ascending order using the Bubble Sort algorithm.
    Optimized with a 'swapped' flag to exit early if already sorted.
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no two elements were swapped by inner loop, the array is already sorted
        if not swapped:
            break
            
    return arr


def run_bubble_sort_project():
    print("=== DAYA'S 'SORT WITH BUBBLE' PROGRAM ===\n")
    
    try:
        # Prompt user to enter numbers from the keyboard
        user_input = input("Enter numbers separated by spaces (e.g., 64 34 25 12 22 11 90): ")
        
        # Convert the space-separated string into a list of integers
        original_array = [int(item) for item in user_input.split()]
        
        if not original_array:
            print("No numbers were entered. Please try again.")
            return
            
        print(f"\nOriginal array : {original_array}")
        
        # Create a copy to sort (or sort in place)
        sorted_array = bubble_sort(original_array.copy())
        
        print(f"Reversed/Sorted: {sorted_array}")
        
    except ValueError:
        print("Invalid input! Please ensure you enter valid integers separated by spaces.")


if __name__ == "__main__":
    run_bubble_sort_project()