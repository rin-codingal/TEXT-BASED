def calculate_time_complexity():
    code_snippet = '''
for i in range(n):
    for j in range(i):
        print(i, j)
    '''

    print("Analyzing the code snippet:")
    print(code_snippet)

    print("The code snippet has nested loops:")
    print("Outer loop: O(n)")
    print("Inner loop: O(i)")

    print("\nCombining, the time complexity is O(n^2).")

if __name__ == "__main__":
    calculate_time_complexity()