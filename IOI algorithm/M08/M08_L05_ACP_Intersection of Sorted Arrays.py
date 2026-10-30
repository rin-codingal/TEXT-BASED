def find_intersection(arr1, arr2):
    """
    Finds the intersection of two sorted arrays using the two-pointer technique.
    Time Complexity: O(n + m)
    Space Complexity: O(min(n, m)) for the result
    """
    intersection_result = []
    i = 0  # Pointer for arr1
    j = 0  # Pointer for arr2
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            # Avoid adding duplicate values if the same element appears multiple times
            if not intersection_result or intersection_result[-1] != arr1[i]:
                intersection_result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
            
    return intersection_result


def run_intersection_project():
    print("=== HARRY'S 'INTERSECTION OF SORTED ARRAYS' PROGRAM ===\n")
    
    try:
        # 1. Take first sorted array from the user
        input1 = input("Enter the first sorted array (space-separated integers): ")
        arr1 = [int(item) for item in input1.split()]
        
        # 2. Take second sorted array from the user
        input2 = input("Enter the second sorted array (space-separated integers): ")
        arr2 = [int(item) for item in input2.split()]
        
        if not arr1 or not arr2:
            print("One or both arrays are empty. Please try again.")
            return
            
        print(f"\nArray 1        : {arr1}")
        print(f"Array 2        : {arr2}")
        
        # 3. Find intersection
        result = find_intersection(arr1, arr2)
        
        print(f"Intersection   : {result}")
        
    except ValueError:
        print("Invalid input! Please ensure you enter valid space-separated integers.")


if __name__ == "__main__":
    run_intersection_project()