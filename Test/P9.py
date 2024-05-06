def Coin_change(coins, target):
    coins.sort(reverse=True)
    count = 0
    used = [0] * len(coins) 
    
    for i, coin in enumerate(coins):
        while target >= coin:
            used[i] += 1
            target -= coin
            count += 1

    if target == 0:
        return count, used
    else:
        return -1, None


def main():
    coins = [1, 2, 3, 5]
    target = 11
    count, used = Coin_change(coins, target)
    if count != -1:
        print("Minimum number of coins needed:", count)
        print("Coins used:")
        for i in range(len(coins)):
            if used[i] > 0:
                print(coins[i], ":", used[i])
    else:
        print("It's not possible to make the target amount with the given coins.")
    
main()
