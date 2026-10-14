# 01-head-tail.py
# Topic: The Head-Tail Pattern, Base Case for Lists

input("Head-tail - head is Lst[0]  tail is Lst[1:]  base case is [].  Press Enter ")

print("  [10, 20, 30]  head:", [10, 20, 30][0], "  tail:", [10, 20, 30][1:])

print("  [5, 15, 25]   head:", [5, 15, 25][0],  "  tail:", [5, 15, 25][1:])

Lst = [int(x) for x in input("Enter 3 numbers separated by spaces: ").split()]

guess = input("What is the head of " + str(Lst) + "? ")
input("Head is Lst[0]  tail is Lst[1:].  Press Enter ")

print("  head:", Lst[0], "  your guess:", guess)