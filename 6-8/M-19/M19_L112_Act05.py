def check_age(age):
    try:
        # Convert the input to an integer
        age = int(age)
        # Check if the age is a positive integer
        if age < 0:
            raise ValueError("Age cannot be negative.")
        # Check if the age is even or odd
        if age % 2 == 0:
            print("The age {age} is even.")
        else:
            print("The age {age} is odd.")
    
    except ValueError as e:
        print(f"Invalid age entered: {e}")

user_input = input("Enter your age: ")
check_age(user_input)