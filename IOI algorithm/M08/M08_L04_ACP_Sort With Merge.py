def merge(left_arr, right_arr):
    """
    Merges two sorted sub-arrays into a single sorted array.
    """
    sorted_arr = []
    i = 0  # Pointer for left_arr
    j = 0  # Pointer for right_arr
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1
            
    # Append any remaining elements from either half
    sorted_arr.extend(left_arr[i:])
    sorted_arr.extend(right_arr[j:])
    
    return sorted_arr


def merge_sort(arr):
    """
    Sorts an array in ascending order using the Merge Sort algorithm (Divide and Conquer).
    """
    # Base case: an array of length 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr
        
    # Find the midpoint and divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    # Merge the sorted halves back together
    return merge(sorted_left, sorted_right)


def run_merge_sort_project():
    print("=== SHEETAL'S 'SORT WITH MERGE' PROGRAM ===\n")
    
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
        
        # 3. Sort the array using Merge Sort
        sorted_array = merge_sort(original_array)
        
        print(f"Sorted array   : {sorted_array}")
        
    except ValueError:
        print("Invalid input! Please ensure you enter valid integers.")


if __name__ == "__main__":
    run_merge_sort_project()