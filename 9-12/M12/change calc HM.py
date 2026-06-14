def find_combinations(n, coins, index, combination):
    if n == 0:
        print(f"500: {combination[0]}, 100: {combination[1]}, 10: {combination[2]}, 5: {combination[3]}, 1: {combination[4]}")
        return

    if index >= len(coins):
        return

    for count in range(n // coins[index] + 1):
        combination[index] = count
        find_combinations(n - count * coins[index], coins, index + 1, combination)

def main():
    n = int(input("Enter n: "))
    coins = [500, 100, 10, 5, 1]
    combination = [0, 0, 0, 0, 0]  # Initialize combination with zeros
    find_combinations(n, coins, 0, combination)

if __name__ == "__main__":
    main()