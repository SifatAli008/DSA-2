def knapsack(capacity, weights, prices):
    n = len(weights)
    value_per_weight = [(prices[i] / weights[i], weights[i], prices[i]) for i in range(n)]
    value_per_weight.sort()
    total_value = 0
    selected_items = []

    for value_per_unit, weight, value in value_per_weight:
        if capacity == 0:
            break
        
        if weight <= capacity:
            total_value += value
            capacity -= weight
            selected_items.append((weight, value))
            
        else:
            fraction = capacity / weight
            total_value += value * fraction
            selected_items.append((fraction * weight, value))
            capacity = 0

    return total_value, selected_items

def main():
    weights = [1, 2, 4, 5]
    prices = [7, 15, 34, 40]
    capacity = 4
    total_profit, selected_items = knapsack(capacity, weights, prices)

    print("Selected items:")
    for i, (weight, value) in enumerate(selected_items):
        print(f"Item {i+1}: {weight} kg {value} taka")

    print(f"Total profit: {total_profit} taka")

main()