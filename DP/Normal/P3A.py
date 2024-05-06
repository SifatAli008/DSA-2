#Minimum Number of Coins
#[1,2,3,5]=11
#1-5,3-2=11
#2-5,1-1=11
#3-3,1-2=11
#4-2,3-1=11
#5-2,1-1=11
#6-1,1-5=11
#7-1,2-2=11
#8-1,1-3=11    
#9-1,1-2=11
#11-1=11

def coin_change(coins, amount, size):
    if amount == 0:
        return 0
    if amount < 0 or size < 0:#if not possible then infinty
        return float('inf')
    
    not_taken = coin_change(coins, amount, size - 1)
    
    taken  = 1 + coin_change(coins, amount - coins[size - 1], size)
    
    return min(not_taken, taken)


def main():
    coins = [2,3,5,6]
    amount = 10
    n = len(coins)
    min_coins = coin_change(coins, amount, n)
    if min_coins == float('inf'):
        print("It's not possible to make", amount, "with the given coins.")
    else:
        print("Minimum number of coins required:", min_coins)

main()

