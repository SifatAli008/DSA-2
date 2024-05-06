#Minimum Number of Coins

def main():
    coins = [1, 2, 3, 5]
    amount = 11
    n = len(coins) 
    Ways = [float('inf')] * (amount + 1)
    Ways[0] = 0  # Base case: 0 coins needed to make amount 0
    
    for i in range(1, amount + 1):
        for j in range(n):
            if coins[j] <= i:
                Ways[i] = min(Ways[i], 1 + Ways[i - coins[j]])

    if Ways[amount] == float('inf'):
        print("It's not possible to make", amount, "with the given coins.")
    else:
        print("Minimum number of coins required:", Ways[amount])

main()
