# --- Assignment Operator (=) ---
# Store the harvest in kg from each of the 5 fields
field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

# --- Arithmetic Operators (+, -, *, /) ---
# Calculate total and average harvest
total   = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest      :", total, "kg")
print("Average per field  :", average, "kg")
print()

# Price per kg is IDR 15,000 — calculate total earnings
price_per_kg = 15000
earnings = total * price_per_kg
print("Total earnings     : IDR.", earnings)
print()

# --- Floor Division (//) and Modulus (%) ---
# Pack the harvest into bags of 25 kg each
bags     = total // 25
leftover = total % 25

print("Full bags packed   :", bags)
print("Leftover grain     :", leftover, "kg")
print()

# --- Comparison Operators (>, <, ==, >=) ---
# Compare this year's harvest with last year
last_year = 500
print("Better than last year?  :", total > last_year)
print("Same as last year?      :", total == last_year)
print("At least as good?       :", total >= last_year)
print()

# --- Assignment Operators (+=, -=) ---
# A bonus field adds 30 kg to the total
total += 30
print("After bonus crop   :", total, "kg")
print()

# Subtract 15 kg saved as seeds for next season
total -= 15
print("After seed reserve :", total, "kg")
print()

# Final bag count after all adjustments
bags = total // 25
print("Final bags packed  :", bags)