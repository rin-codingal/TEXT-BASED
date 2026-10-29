def Last_Occurence(arr, target):
    """
    Finds the last index of a target item using Linear Search.
    Searches backwards from the end of the array for optimal efficiency.
    """
    # Iterate from the last index (len(arr) - 1) down to 0, with a step of -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i  # Found the last occurrence, return its index
            
    return -1  # Return -1 if the target is not found

def run_lap_search_tracker():
    print("=== SAKSHAM'S LINEAR SEARCH: LAST INDEX FINDER ===\n")
    
    # Sample Array and Target
    array = [10, 23, 45, 70, 45, 12, 45, 90]
    target = 45
    
    print(f"Given Array : {array}")
    print(f"Target Item : {target}")
    
    # Perform search
    last_index = Last_Occurence(array, target)
    
    # Display results
    print("\n--- Search Result ---")
    if last_index != -1:
        print(f"Success! The last occurrence of element '{target}' is at index: {last_index}")
        print(f"Verification: array[{last_index}] = {array[last_index]}")
    else:
        print(f"Element '{target}' was not found in the array.")


if __name__ == "__main__":
    run_lap_search_tracker()