def Non_Adjacent_SUM(arr, size):
    if size <= 0:
        return 0
    if size == 1:
        return arr[0]
    if size == 2:
        return max(arr[0], arr[1])
    
    # Initialize dp array to store maximum sum up to each index
    dp = [0] * size
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    
    for i in range(2, size):
        # For each element, we have two options:
        # 1. Exclude the current element and take the maximum sum from the previous element
        # 2. Include the current element and take the maximum sum from two positions before
        dp[i] = max(dp[i-1], arr[i] + dp[i-2])
    
    return dp[size-1]

def main():
    arr = [3, 2, 7, 10]
    size = len(arr)
    print("Maximum sum of non-adjacent elements:", Non_Adjacent_SUM(arr, size))

main()
