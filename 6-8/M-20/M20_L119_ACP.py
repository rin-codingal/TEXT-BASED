num = int(input("You want odd and even numbers under what value? : "))

odd_list = [i for i in range(num) if i%2!=0] 
print("List of odd numbers:", odd_list)
print()

even_list = [i for i in range(num) if i%2==0]
print("List of even numbers:", even_list)
print()

fruits = ['apple', 'banana', 'mango', 'papaya', 'grapes']
Fruits = [x[0].upper()+x[1:] for x in fruits]
print(("Fruits as proper nouns :", Fruits))