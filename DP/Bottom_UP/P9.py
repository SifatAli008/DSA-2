def knapsack_bottom_up(capacity, weights, prices):
    n = len(weights)
    # Initialize a table to store the maximum value that can be obtained for
    # each subproblem of capacity i and using the first j items.
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight is more than the current capacity,
            # we can't include it, so we just use the previous value.
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Otherwise, we consider including the item, and we take the maximum
                # value between including it and not including it.
                dp[i][w] = max(dp[i - 1][w], prices[i - 1] + dp[i - 1][w - weights[i - 1]])

    return dp[n][capacity]


def main():
    weights = [5, 4, 6, 3]
    prices = [11, 10, 12, 9]
    capacity = 8
    print(knapsack_bottom_up(capacity, weights, prices))

main()
