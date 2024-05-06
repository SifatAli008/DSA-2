#Minimum Number of Coins
def main():
    coins = [1, 5, 7]
    amount = 8
    n = len(coins)
    Ways = [[float('inf')] * (amount + 1) for _ in range(n)]  # Initialize a 2D list
    Ways[0][0] = 0  # Base case: 0 coins needed to make amount 0

    for i in range(n):
        for j in range(amount + 1):
            if i == 0:  # Special handling for the first coin
                if coins[i] > j:
                    Ways[i][j] = float('inf')
                else:
                    Ways[i][j] = j // coins[i]
            else:
                if coins[i] > j:
                    Ways[i][j] = Ways[i - 1][j]
                else:
                    Ways[i][j] = min(Ways[i - 1][j], 1 + Ways[i][j - coins[i]])

    if Ways[n - 1][amount] == float('inf'):
        print("It's not possible to make", amount, "with the given coins.")
    else:
        print("Minimum number of coins required:", Ways[n - 1][amount])

main()
