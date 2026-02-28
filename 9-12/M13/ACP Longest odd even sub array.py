def longest_alternating_subarray(nums):
    if not nums:
        return 0
    
    max_len = 1
    current_len = 1
    
    for i in range(1, len(nums)):
        # Check if the current and previous elements have different parity
        # (Even-Odd or Odd-Even)
        if (nums[i] % 2) != (nums[i-1] % 2):
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            # Reset the streak if they have the same parity
            current_len = 1
            
    return max_len

arr1 = [1, 2, 3, 4, 5, 7, 8] 
# Alternating: [1, 2, 3, 4, 5] -> Length 5
# Then 5 and 7 are both odd, streak breaks.

result = longest_alternating_subarray(arr1)
print(f"Length of the longest alternating subarray: {result}")