def knapsack(capacity, n, weights, prices, memo):
    
    # Base Case
    if n == 0 or capacity == 0:
        return 0

    # If the value is already calculated, return it
    if memo[n][capacity] != -1:
        return memo[n][capacity]

    # If the weight of the nth item is more than the knapsack capacity, then
    # this item cannot be included in the optimal solution
    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack(capacity, n - 1, weights, prices, memo)
        return memo[n][capacity]
    
    not_taking = knapsack(capacity, n - 1, weights, prices, memo)
    taking = prices[n - 1] + knapsack(capacity - weights[n - 1], n - 1, weights, prices, memo)

    # Return the maximum of two cases:
    # (1) nth item included
    # (2) nth item not included
    memo[n][capacity] = max(not_taking, taking)
    
    return memo[n][capacity]

def main():
    weights = [1, 3, 4, 5]
    prices = [1, 4, 5, 7]
    capacity = 7
    n = len(weights)
    memo = [[-1] * (capacity + 1) for _ in range(n + 1)]
    print(knapsack(capacity, n, weights, prices, memo))

main()
