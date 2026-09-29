def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    # Check divisibility up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_two_digit_primes():
    # 2-digit numbers range from 10 to 99 inclusive
    two_digit_primes = [num for num in range(10, 100) if is_prime(num)]
    return two_digit_primes

if __name__ == "__main__":
    primes = get_two_digit_primes()
    
    print("=== TWO-DIGIT PRIME NUMBERS ===")
    print(f"Found {len(primes)} prime numbers between 10 and 99:\n")
    
    # Print formatted in rows of 7 numbers for clear reading
    for i in range(0, len(primes), 7):
        print("  ".join(f"{p:2d}" for p in primes[i:i+7]))