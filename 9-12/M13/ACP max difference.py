def find_max_difference(nums):
    if not nums or len(nums) < 2:
        return 0
    
    # Initialize min and max with the first element
    min_val = nums[0]
    max_val = nums[0]
    
    # Single pass to find both extremes
    for num in nums:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
            
    return max_val - min_val

numbers = [10, 3, 5, 20, 1, 8]
result = find_max_difference(numbers)

print(f"The maximum difference is: {result}") # Output: 19 (20 - 1)