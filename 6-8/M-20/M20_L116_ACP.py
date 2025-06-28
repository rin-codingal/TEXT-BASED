def mutiple_tuple(nums):
    temp = list(nums)
    product = 1 

    for x in temp:
        product = product * x

    return product

nums1 = (4, 3, 2, 2, -1, 18)
print ("Original Tuple: ")
print(nums1)
print()

result1 = mutiple_tuple(nums1)

print("Product - multiplying all the numbers of the said tuple:",result1)
print()

nums2 = (2, 4, 8, 8, 3, 2, 9)
print ("Original Tuple: ")
print(nums2)
print()
result2 = mutiple_tuple(nums2)

print("Product - multiplying all the numbers of the said tuple:",result2)