def coin_change(coins, amount, size, Ways):
    
    if amount == 0:
        return 1
    
    if amount < 0 or size <= 0:
        return 0
    
    if Ways[size][amount] != 0:
        return Ways[size][amount]
    
    taken = coin_change(coins, amount, size - 1, Ways)
    not_taken = coin_change(coins, amount - coins[size - 1], size, Ways)
    
    Ways[size][amount] = taken + not_taken
    return Ways[size][amount]

def main():
    coins = [1, 2, 3, 5]
    amount = 11
    n = len(coins) 
    Ways = [[0] * (amount + 1) for _ in range(n + 1)]
    total_ways = coin_change(coins, amount, n, Ways)
    print("Total number of ways to make", amount, "with the given coins:", total_ways)

main()
