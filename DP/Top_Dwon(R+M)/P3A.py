

def coin_change(coins, amount, size, Ways):
    
    if amount == 0:
        return 0
    
    if amount < 0 or size <= 0:
        return float('inf')
    
    if Ways[size][amount] != 0:
        return Ways[size][amount]
    
    way1 = coin_change(coins, amount, size - 1, Ways)
    way2 = 1 + coin_change(coins, amount - coins[size - 1], size, Ways)
    Ways[size] = min(way1, way2)
    return Ways[size][amount]

def main():
    coins = [1, 2, 3, 5]
    amount = 11
    n = len(coins) 
    Ways = [[0] * (amount + 1) for _ in range(n + 1)]
    min_coins = coin_change(coins, amount, n, Ways)
    if min_coins == float('inf'):
        print("It's not possible to make", amount, "with the given coins.")
    else:
        print("Minimum number of coins required:", min_coins)

main()

