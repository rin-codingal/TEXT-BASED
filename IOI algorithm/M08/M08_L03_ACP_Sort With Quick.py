def partition(arr, low, high):
    """
    Partitions the array around a pivot (using the last element as the pivot).
    Elements smaller than the pivot are placed to its left, and larger elements to its right.
    """
    pivot = arr[high]
    i = low - 1  # Pointer for smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
            
    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_helper(arr, low, high):
    """
    Recursive helper function for Quick Sort.
    """
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)


def quick_sort(arr):
    """
    Initiates the Quick Sort algorithm on the array.
    """
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def run_quick_sort_project():
    print("=== SHEETAL'S 'SORT WITH QUICK' PROGRAM ===\n")
    
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
        
        # 3. Sort the array using Quick Sort
        sorted_array = quick_sort(original_array.copy())
        
        print(f"Sorted array   : {sorted_array}")
        
    except ValueError:
        print("Invalid input! Please ensure you enter valid integers.")


if __name__ == "__main__":
    run_quick_sort_project()