#0/1 knapsack Problem

def knapsack(capacity, ind, weights, prices):
    
    if capacity == 0 or ind == 0: #base
        return 0

    if weights[ind-1] > capacity: #
        return knapsack(capacity, ind - 1, weights, prices)

    not_taking = knapsack(capacity, ind - 1, weights, prices)
    taking = prices[ind - 1] + knapsack(capacity - weights[ind - 1], ind - 1, weights, prices)

    return max(not_taking, taking)

def main():
    weights = [2,3,4,5] #
    prices = [3,4,5,6] #
    capacity = 5                    
    print(knapsack(capacity, len(weights), weights, prices))
    
main()
