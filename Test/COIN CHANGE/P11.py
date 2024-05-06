def coin_change(coins, target):
    if target == 0:
        return 0, []

    min_coins = float('inf')
    used_coin = []

    for coin in coins:
        if coin <= target:
            sub_result, used = coin_change(coins, target - coin)
            if sub_result != -1:
                if sub_result + 1 < min_coins:
                    min_coins = sub_result + 1
                    used_coin = [coin] + used

    if min_coins == float('inf'):
        return -1, []
    else:
        return min_coins, used_coin

def main():
    coins = [1, 2, 3, 5]  
    target = 11
    result, used_coin = coin_change(coins, target)
    print("Minimum number of coins required:", result)
    print("Used coins:", used_coin)

main()
