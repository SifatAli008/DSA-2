def Coin_change(coins_quantities, target):
                            
    coins_quantities.sort(reverse=True)
    count = 0
    used = [0] * len(coins_quantities)

    for i, (coin, quantity) in enumerate(coins_quantities): 
        while target >= coin and quantity > 0: 
            used[i] += 1 
            target -= coin   
            count += 1 
            coins_quantities[i] = (coin, quantity - 1)

    if target == 0:
        return count, used
    else:
        return -1, None


def main():
    coins = [1, 2, 3, 5] 
    quantities = [2, 3, 1, 2] 
    
    coins_quantities = list(zip(coins, quantities)) 
    target = 11
    
    count, used = Coin_change(coins_quantities, target)
    
    if count != -1:
        print("Minimum number of coins needed:", count)
        print("Coins used:")
        for i, (coin, _) in enumerate(coins_quantities):
            if used[i] > 0:
                print(coin, ":", used[i])
    else:
        print("It's not possible to make the target amount with the given coins.")

main()
