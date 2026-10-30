def shell_sort(arr):
    """
    Sorts an array in ascending order using the Shell Sort algorithm.
    It works by sorting elements far apart first, progressively reducing the gap.
    """
    n = len(arr)
    # Start with a large gap, then reduce the gap by half each time
    gap = n // 2
    
    while gap > 0:
        # Perform a gapped insertion sort for this gap size
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Shift elements of the gapped sorted segment until the correct location for temp is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                
            # Put temp in its correct place
            arr[j] = temp
            
        # Reduce the gap for the next pass
        gap //= 2
        
    return arr


def run_shell_sort_project():
    print("=== JOHN'S 'SORT WITH SHELL' PROGRAM ===\n")
    
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
        
        # 3. Sort the array using Shell Sort
        sorted_array = shell_sort(original_array.copy())
        
        print(f"Sorted array   : {sorted_array}")
        
    except ValueError:
        print("Invalid input! Please ensure you enter valid integers.")


if __name__ == "__main__":
    run_shell_sort_project()