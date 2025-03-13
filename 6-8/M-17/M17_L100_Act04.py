print("Enter the Number of Days: ")
num = int(input())

year = int(num/365)
week = int((num%365)/7)
days = int((num%365)%7)

print(f"Total Number of Year(s): {year}")

print(f"Total Number of Week(s): {week}")

print(f"Total Number of Day(s): {days}")
