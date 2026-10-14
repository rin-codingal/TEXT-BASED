# 02-list-sum.py
# Topic: Sorted Check with Recursion, Sum of a List with Recursion

def list_sum(Lst):
    if Lst == []:
        return 0
    return Lst[0] + list_sum(Lst[1:])

input("Recursive sum - add head to sum of tail until empty.  Press Enter ")

print("  list_sum([1, 2, 3]) =", list_sum([1, 2, 3]))
print("  list_sum([4, 5, 6]) =", list_sum([4, 5, 6]))

Lst = [int(x) for x in input("Enter 4 numbers separated by spaces: ").split()]

guess = input("What is the sum of " + str(Lst) + "? ")
input("list_sum adds head to list_sum(tail) until the list is empty.  Press Enter ")

print("  sum:", list_sum(Lst), "  your guess:", guess)