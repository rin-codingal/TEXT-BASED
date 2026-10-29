def binary_search(arr, target):
    """
    Searches for the target element in a sorted array using Binary Search.
    Returns the index of the target if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Find the middle index (prevents integer overflow in other languages, best practice)
        mid = left + (right - left) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
            
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
            
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
            
    return -1  # Target is not present in the array


def run_binary_search_demo():
    print("=== BINARY SEARCH ALGORITHM DEMO ===\n")
    
    # Input array must be sorted for binary search to work correctly
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    
    print(f"Sorted Array : {sorted_array}")
    print(f"Target Item  : {target}")
    
    # Perform binary search
    index = binary_search(sorted_array, target)
    
    # Display results
    print("\n--- Search Result ---")
    if index != -1:
        print(f"Success! Element '{target}' found at index: {index}")
        print(f"Verification: sorted_array[{index}] = {sorted_array[index]}")
    else:
        print(f"Element '{target}' was not found in the array.")


if __name__ == "__main__":
    run_binary_search_demo()