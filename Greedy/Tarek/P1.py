#coin Change Algorithms

def coinChange(coins, target):
    coins.sort()
    count = 0
    used = [0] * len(coins)

    for i, coin in enumerate(coins):  # Fixing the syntax error
        while target >= coin:  # Fixing the logic
            used[i] += 1
            target -= coin
            count += 1

    if target == 0:
        return count, used
    else:
        return -1, used

def main():
    coins = [1, 2, 3, 5]
    target = 11
    count, used = coinChange(coins, target)
    if count != -1:
        print("Minimum number of coins needed:", count)
        print("Coins used:", used)
    else:
        print("Change not possible")

main()
