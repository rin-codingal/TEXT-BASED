def sort_array(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example usage
a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sorted_array = sort_array(a)
print()
print("Sorted array:", sorted_array)
print()