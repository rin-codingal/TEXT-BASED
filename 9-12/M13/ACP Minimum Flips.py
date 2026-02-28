def min_flips_to_make_same(arr):
    if not arr:
        return 0
    
    # We count how many times the value changes in the array
    # Each change represents the start of a new group
    zero_groups = 0
    one_groups = 0
    
    # Check the first element to initialize the count
    if arr[0] == 0:
        zero_groups += 1
    else:
        one_groups += 1
        
    for i in range(1, len(arr)):
        # If the current element is different from the previous, a new group starts
        if arr[i] != arr[i-1]:
            if arr[i] == 0:
                zero_groups += 1
            else:
                one_groups += 1
                
    # The minimum flips is the smaller of the two group counts
    return min(zero_groups, one_groups)

test_arr = [1, 0, 0, 0, 1, 1, 0, 1, 0, 1]
# Groups of 1s: [1], [1,1], [1], [1] -> 4 groups
# Groups of 0s: [0,0,0], [0], [0]    -> 3 groups

flips = min_flips_to_make_same(test_arr)
print(f"Minimum flips needed: {flips}")