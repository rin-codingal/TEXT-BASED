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

print("Product - multiplying all the numbers of the said tuple:",mutiple_tuple(nums1))
print()

nums2 = (2, 4, 8, 8, 3, 2, 9)
print ("Original Tuple: ")
print(nums2)
print()
print("Product - multiplying all the numbers of the said tuple:",mutiple_tuple(nums2))