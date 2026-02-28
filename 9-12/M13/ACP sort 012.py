def sort_012(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            # Swap current element with the low pointer
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # 1 is in the right place for now, just move mid
            mid += 1
        else: # nums[mid] == 2
            # Swap current element with the high pointer
            nums[mid], nums[high] = nums[high], nums[mid]
            # Don't increment mid here because the swapped 
            # value from 'high' needs to be inspected
            high -= 1
            
    return nums

arr = [2, 0, 2, 1, 1, 0]
sorted_arr = sort_012(arr)

print(f"Sorted array: {sorted_arr}")