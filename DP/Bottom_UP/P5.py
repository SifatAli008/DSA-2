#House Robbery Problem
# Given an array that determines the money stored in each,Find the maximume money can be robbed such that no two adjucent house are robbed


def house_loot(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    
    return dp[n-1]

def main():
    arr = [2, 7, 3, 1, 4, 2, 1, 8]
    result = house_loot(arr, len(arr))
    print("Maximum loot amount:", result)

main()
