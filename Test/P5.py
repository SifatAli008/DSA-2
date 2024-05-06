def combination_sum(arr, n, target, current_combination, all_combinations):
    if target == 0:
        all_combinations.append(list(current_combination))
        return
    
    if n == 0 or target < 0:
        return
    
    # Case 1: Include current element
    current_combination.append(arr[n - 1])
    combination_sum(arr, n, target - arr[n - 1], current_combination, all_combinations)
    current_combination.pop()  # Backtrack
    
    # Case 2: Exclude current element
    combination_sum(arr, n - 1, target, current_combination, all_combinations)

def print_combinations(arr, target):
    all_combinations = []
    combination_sum(arr, len(arr), target, [], all_combinations)
    for combination in all_combinations:
        print(combination)

def main():
    arr = [1, 2, 3, 5]
    target = 11
    print_combinations(arr, target)

main()
