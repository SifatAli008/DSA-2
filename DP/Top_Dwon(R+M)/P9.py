def knapsack(capacity, ind, weights, prices, memo):
    
    if memo[ind][capacity] != -1:
        return memo[ind][capacity]

    if capacity == 0 or ind == 0:
        memo[ind][capacity] = 0
        return 0

    if weights[ind - 1] > capacity:
        memo[ind][capacity] = knapsack(capacity, ind - 1, weights, prices, memo)
        return memo[ind][capacity]

    not_taking = knapsack(capacity, ind - 1, weights, prices, memo)
    taking = prices[ind - 1] + knapsack(capacity - weights[ind - 1], ind - 1, weights, prices, memo)

    memo[ind][capacity] = max(not_taking, taking)
    return memo[ind][capacity]

def main():
    weights = [1, 3, 4, 5]
    prices = [1, 4, 5, 7]
    capacity = 7
    n = len(weights)
    # Initialize memoization table with -1
    memo = [[-1] * (capacity + 1) for _ in range(n + 1)]
    print( knapsack(capacity, n, weights, prices, memo))

main()
