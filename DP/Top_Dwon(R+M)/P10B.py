def combination_sum(arr, n, target):
    # Base cases
    if target == 0:
        return 1
    
    if n == 0 or target < 0:
        return 0
    
    # If the last element is greater than the target, it can't be included
    if arr[n - 1] > target:
        return combination_sum(arr, n - 1, target)

    # Recursively call the function and return the result
    return combination_sum(arr, n, target - arr[n-1])

def main():
    arr = [1, 2, 5]
    print(combination_sum(arr, len(arr), 5))

main()
