def binary_search_closest(arr, target, exclude_index):
    """
    Helper function using Binary Search to find an element in 'arr' (excluding 'exclude_index')
    whose value is closest to the target.
    """
    left = 0
    right = len(arr) - 1
    closest_index = -1
    min_diff = float('inf')
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Skip the element itself if it's the same index
        if mid == exclude_index:
            # Check neighbors to find a valid alternative
            # For simplicity in binary search, we can search left or right
            if mid + 1 <= right and mid + 1 != exclude_index:
                closest_index = mid + 1
            elif mid - 1 >= left and mid - 1 != exclude_index:
                closest_index = mid - 1
            break
            
        current_val = arr[mid]
        diff = abs(current_val - target)
        
        if diff < min_diff:
            min_diff = diff
            closest_index = mid
            
        if current_val < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return closest_index

def find_nearest_sum_pair(arr, target_sum):
    """
    Finds a pair of numbers in the array whose sum is closest to the target_sum
    using a binary search approach.
    """
    # Binary search requires a sorted array
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    
    if n < 2:
        return None, "Array must contain at least two elements."
        
    closest_pair = (sorted_arr[0], sorted_arr[1])
    min_sum_diff = float('inf')
    
    # Iterate through each element and use binary search to find its best partner
    for i in range(n):
        complement = target_sum - sorted_arr[i]
        
        # Use binary search to find the closest element to 'complement' in the rest of the array
        j = binary_search_closest(sorted_arr, complement, exclude_index=i)
        
        if j != -1 and i != j:
            current_sum = sorted_arr[i] + sorted_arr[j]
            current_diff = abs(current_sum - target_sum)
            
            if current_diff < min_sum_diff:
                min_sum_diff = current_diff
                closest_pair = (sorted_arr[i], sorted_arr[j])
                
    return closest_pair, min_sum_diff


def run_rashmi_search_demo():
    print("=== RASHMI'S NEAREST SUM PAIR SEARCH (BINARY SEARCH) ===\n")
    
    array = [10, 22, 28, 29, 30, 40]
    target_sum = 54
    
    print(f"Original Array : {array}")
    print(f"Target Sum     : {target_sum}\n")
    
    pair, diff = find_nearest_sum_pair(array, target_sum)
    
    print("--- Results ---")
    if pair:
        actual_sum = pair[0] + pair[1]
        print(f"Best Pair Found : {pair[0]} and {pair[1]}")
        print(f"Their Sum       : {actual_sum} (Difference from target: {diff})")
    else:
        print("Could not find a valid pair.")


if __name__ == "__main__":
    run_rashmi_search_demo()