#Maximum Sum of Non-Adjacent Elements

def Non_Adjacent_SUM(arr, size, dp):
    if size <= 0:
        return 0
    
    if dp[size] != -1:
        return dp[size]
    
    # Recursive calls to calculate maximum sum by including or excluding the current element
    include = arr[size - 1] + Non_Adjacent_SUM(arr, size - 2, dp)
    exclude = Non_Adjacent_SUM(arr, size - 1, dp)
    
    # Memoization
    dp[size] = max(include, exclude)
    
    return dp[size]

def main():
    arr = [1,2,3,4]
    size = len(arr)
    # Initialize dp array with -1
    dp = [-1] * (size + 1)
    print("Maximum sum of non-adjacent elements:", Non_Adjacent_SUM(arr, size, dp))

main()
