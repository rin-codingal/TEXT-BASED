def merge_sorted_arrays(arr1, arr2):
    """
    Merges two sorted arrays into a single sorted array using two pointers.
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    merged_array = []
    i = 0  # Pointer for arr1
    j = 0  # Pointer for arr2
    
    # Compare elements from both arrays and append the smaller one
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
            
    # If there are remaining elements in arr1, append them
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
        
    # If there are remaining elements in arr2, append them
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
        
    return merged_array


def run_merge_demo():
    print("=== MERGE TWO SORTED ARRAYS PROJECT ===\n")
    
    # Sample sorted arrays
    array1 = [1, 3, 5, 7, 9]
    array2 = [2, 4, 6, 8, 10, 12]
    
    print(f"First Sorted Array  : {array1}")
    print(f"Second Sorted Array : {array2}")
    
    # Merge arrays
    result = merge_sorted_arrays(array1, array2)
    
    print(f"\nMerged Sorted Array : {result}")


if __name__ == "__main__":
    run_merge_demo()