#Greedy Coin Change
def coin_count(coins, target):
    coins.sort(reverse=True)  
    count = 0

    for coin in coins:
        while target >= coin:
            target -= coin
            count += 1

    return count if target == 0 else -1

def main():
    coins = [1, 2, 3, 5]
    target = 11
    print("Minimum number of coins required:", coin_count(coins, target))

main()
