def main():
    limit = int(input("Enter the limit: "))
    count = 0
    count_coins = [0] * 4

    coins = [
        {"coinName": "Quarters", "value": 25},
        {"coinName": "Dimes", "value": 10},
        {"coinName": "Nickels", "value": 5},
        {"coinName": "Pennies", "value": 1}
    ]

    coins.sort(key=lambda x: x["value"], reverse=True)

    print("Limit:", limit)

    for coin in coins:
        while limit >= coin["value"]:
            count_coins[count] += 1
            limit -= coin["value"]
        count += 1

    print("Total:", count, "cents")

    for i in range(len(coins)):
        print(coins[i]["coinName"], "count:", count_coins[i])


main()
