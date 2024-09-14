def coin_count(coins, target, arr):
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        while target >= coin:
            target -= coin
            arr.append(coin)
            count += 1

    return count, arr if target == 0 else -1

def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    target = 2605
    arr = []
    result, arr = coin_count(coins, target, arr)
    if result != -1:
        print("Minimum number of coins required:", result)
        print(arr)
    else:
        print("Change not possible with given coins.")

main()
