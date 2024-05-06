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

def coin_count(coins, target, n):
    if target == 0:
        return 0
    
    if target < 0 or n == 0:
        return -1
    
    min_coins = float('inf')
    
    for i in range(n):
        if coins[i] <= target:
            sub_result = coin_count(coins, target - coins[i], n)
            if sub_result != -1:
                min_coins = min(min_coins, sub_result + 1)
    
    return min_coins if min_coins != float('inf') else -1

def main():
    coins = [1, 2, 3, 5]
    target = 11
    n = len(coins)
    print("Minimum number of coins required:", coin_count(coins, target, n))

main()