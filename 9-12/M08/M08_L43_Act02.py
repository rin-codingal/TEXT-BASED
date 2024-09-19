diksi = {}

# dictionary with integer keys
diksi = {1: "apple", 2: "ball"}

# dictionary with mixed keys
diksi = {"name": "John", 1: [2, 4, 3]}

diksi = {"name": "Jack", "age": 26}

# Output: Jack
print(diksi["name"])
print(diksi.get("age"))
print()

# update value
diksi["age"] = 27
print(diksi)
print()

# add item
diksi["address"] = "Surabaya"
print(diksi)
print()

# remove particular element
diksi.pop("age")
print(diksi)
print()

# access a particular element
print("Address :", diksi.get("address"))
print()

# remove all the elements
diksi.clear()
print(diksi)
