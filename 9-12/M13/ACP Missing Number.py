def find_missing_number(nums):
    # Since one number is missing, n is len(nums) + 1
    n = len(nums) + 1
    
    # Mathematical expected sum: (n * (n + 1)) / 2
    expected_sum = n * (n + 1) // 2
    
    # Actual sum of elements in the array
    actual_sum = sum(nums)
    
    return expected_sum - actual_sum

my_list = [1, 2, 3, 5, 6] # '4' is missing
missing = find_missing_number(my_list)

print(f"The missing number is: {missing}")