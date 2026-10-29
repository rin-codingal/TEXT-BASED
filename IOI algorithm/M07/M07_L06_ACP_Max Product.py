def find_max_product_pair(arr):
    """
    Finds the pair of elements with the maximum product in an array.
    Uses sorting to easily evaluate both largest positives and lowest negatives.
    """
    n = len(arr)
    if n < 2:
        return None, "Array must contain at least two elements."
        
    # Sort the array in ascending order
    arr.sort()
    
    # The maximum product can be:
    # 1. Product of the two largest numbers at the end of the sorted array
    # 2. Product of the two smallest numbers at the start (in case of large negative numbers)
    prod_end = arr[n - 1] * arr[n - 2]
    prod_start = arr[0] * arr[1]
    
    if prod_end > prod_start:
        return (arr[n - 2], arr[n - 1]), prod_end
    else:
        return (arr[0], arr[1]), prod_start


def run_max_product_project():
    print("=== DAYA'S 'MAX PRODUCT' PROGRAM ===\n")
    
    try:
        # Prompt user to enter numbers from the keyboard
        user_input = input("Enter numbers separated by spaces (e.g., 1 10 -5 2 -7): ")
        
        # Convert the space-separated string into a list of integers
        original_array = [int(item) for item in user_input.split()]
        
        if len(original_array) < 2:
            print("Please enter at least two numbers to find a pair.")
            return
            
        print(f"\nOriginal array : {original_array}")
        
        # Find the pair with the maximum product
        pair, max_product = find_max_product_pair(original_array.copy())
        
        print(f"Max Product Pair : {pair[0]} and {pair[1]}")
        print(f"Maximum Product  : {max_product}")
        
    except ValueError:
        print("Invalid input! Please ensure you enter valid integers separated by spaces.")


if __name__ == "__main__":
    run_max_product_project()