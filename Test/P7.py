def combination_sum(arr, n, target, ways):
    if target == 0:
        return 1
    
    if n == 0:
        return 0
    
    if ways[target][n] != -1:
        return ways[target][n]
    
    if arr[n - 1] > target:
        ways[target][n] = combination_sum(arr, n - 1, target, ways)
    else:
        ways[target][n] = combination_sum(arr, n - 1, target, ways) + combination_sum(arr, n, target - arr[n - 1], ways)
    
    return ways[target][n]

def main():
    arr = [1, 2, 3, 5]
    target_sum = 11
    ways = [[-1] * (len(arr) + 1) for _ in range(target_sum + 1)]
    print(combination_sum(arr, len(arr), target_sum, ways))

main()
