#Fractional knapsack

def knapsack(capacity, weights, prices):
    n = len(weights)
    value_per_weight = [(prices[i] / weights[i], weights[i], prices[i]) for i in range(n)]
    value_per_weight.sort(reverse=True)
    
    total_value = 0
    
    for value_per_unit, weight, value in value_per_weight:
    
        if capacity == 0:
            break
        
        # Take the whole item if possible
        if weight <= capacity:
            total_value += value
            capacity -= weight
        
        # Take a fraction of the item to fill the knapsack
        else:
            fraction = capacity / weight
            total_value += value * fraction
            capacity -= weight * fraction 
    
    return total_value

def main():
    weights = [2, 3, 4, 5]
    prices = [3, 4, 5, 6]
    capacity = 5             
    print(knapsack(capacity, weights, prices))
    
main()
