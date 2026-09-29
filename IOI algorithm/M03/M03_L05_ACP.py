import math

def calculate_gcd(a, b):
    """Calculate Greatest Common Divisor using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def find_lcm():
    print("=== LEAST COMMON MULTIPLE (LCM) CALCULATOR ===\n")
    
    # 1. Input collection & validation
    try:
        num1 = int(input("Enter the first positive integer : "))
        num2 = int(input("Enter the second positive integer: "))
        
        if num1 <= 0 or num2 <= 0:
            print("Please enter positive integers greater than zero.")
            return
    except ValueError:
        print("Invalid input! Please enter valid whole numbers.")
        return

    # 2. Identify highest and smallest number
    highest = max(num1, num2)
    smallest = min(num1, num2)

    # 3. Method 1: Using the mathematical formula LCM(a, b) = (a * b) / GCD(a, b)
    gcd = calculate_gcd(highest, smallest)
    lcm_formula = (highest * smallest) // gcd

    # 4. Method 2: Python built-in math.lcm() for double-checking
    lcm_builtin = math.lcm(highest, smallest)

    # 5. Output results
    print("\n--- Summary ---")
    print(f"Highest Number  : {highest}")
    print(f"Smallest Number : {smallest}")
    print(f"GCD / HCF       : {gcd}")
    print(f"Calculated LCM  : {lcm_formula}")


if __name__ == "__main__":
    find_lcm()