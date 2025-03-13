def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1, 10):
    print(fibonacci(i), end=' ')
print()