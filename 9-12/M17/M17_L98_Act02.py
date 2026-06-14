# Create the two sets of two guest lists
S1 = {'A', 'B', 'C', 'D', 'E'}
S2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

# Find intersection of two sets
intersection = S1.intersection(S2)

# Converting set into list 
# to find total guests to be invited in party
total_guests = list(intersection)

print(f"Total common friends to be invited in party are : {len(total_guests)}")
print(f"Common friends List : {total_guests}")