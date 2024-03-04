#ALTERNATIVE QUESTION 01.1: Thieves in warehouse

def thieves_in_warehouse(boxes, thieves):
    boxes.sort(key=lambda x: x[2] / x[1], reverse=True)  # Sort boxes by value-to-weight ratio (descending)
    thieves.sort(reverse=True)  # Sort thieves by capacity (descending)
    total_thieves = 0

    for i, thief_capacity in enumerate(thieves, start=1):
        thief_profit = 0
        thief_items = []
        remaining_capacity = thief_capacity

        print(f"Thief {i}:")
        for item in boxes[:]:
            if item[1] <= remaining_capacity:
                print(f"Taking {item[0]}: {item[1]} kg {item[2]} taka")
                thief_profit += item[2]
                thief_items.append(item)
                remaining_capacity -= item[1]
                boxes.remove(item)

        print(f"Thief {i} profit: {thief_profit} taka\n")
        if thief_items:
            total_thieves += 1

    if total_thieves == 0:
        print("No thief could steal from the warehouse.")

    return total_thieves

def main():
    boxes = [("silver-dust", 300, 4), ("gold-dust", 2000, 8), ("salt", 80, 10), ("sugar", 89, 10)]
    thieves = [100, 150]  # Capacity of each thief's knapsack

# Calculate the number of thieves needed to empty the warehouse
    required_thieves = thieves_in_warehouse(boxes, thieves)
    print(f"Total {required_thieves} thieves stole from the warehouse.")

# Print remaining items
    if boxes:
        print("Still following items are left:")
        for item in boxes:
            print(f"    {item[0]}: {item[1]} kg {item[2]} taka")
    else:
        print("No items left in the warehouse.")

main()