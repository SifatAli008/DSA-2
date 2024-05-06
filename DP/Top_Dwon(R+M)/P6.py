#Rod cutting problem

def rod_cut(arr, n, memo):
    if n == 0:
        return 0
    
    if memo[n] != -1:
        return memo[n]
    
    max_val = float('-inf')
    for i in range(1, n+1):
        max_val = max(max_val, arr[i-1] + rod_cut(arr, n-i, memo))
    
    memo[n] = max_val
    return max_val

def main():
    arr = [1, 5, 6, 9, 11, 12, 14, 16]
    memo = [-1] * (len(arr) + 1)  # Initialize memoization table
    result = rod_cut(arr, len(arr), memo)
    print("Maximum loot amount:", result)

main()

