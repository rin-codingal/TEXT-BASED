def selection_sort(arr):
    """
    Sorts an array in ascending order using the Selection Sort algorithm.
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Assume the first element of the unsorted portion is the minimum
        min_index = i
        
        # Find the index of the actual minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first element of the unsorted part
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            
    return arr


def run_selection_sort_project():
    print("=== DAYA'S 'SORT WITH SELECTION' PROGRAM ===\n")
    
    try:
        # Prompt user to enter numbers from the keyboard
        user_input = input("Enter numbers separated by spaces (e.g., 64 25 12 22 11): ")
        
        # Convert the space-separated string into a list of integers
        original_array = [int(item) for item in user_input.split()]
        
        if not original_array:
            print("No numbers were entered. Please try again.")
            return
            
        print(f"\nOriginal array : {original_array}")
        
        # Sort the array using Selection Sort
        sorted_array = selection_sort(original_array.copy())
        
        print(f"Sorted array   : {sorted_array}")
        
    except ValueError:
        print("Invalid input! Please ensure you enter valid integers separated by spaces.")


if __name__ == "__main__":
    run_selection_sort_project()