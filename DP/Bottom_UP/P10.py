def combination_sum(arr, target):
    dp = [0] * (target + 1)
    dp[0] = 1 
    
    for num in arr:
        for i in range(num, target + 1):
            dp[i] += dp[i - num]
    
    return dp[target]

def main():
    arr = [1, 2, 3, 5]
    target = 11
    result = combination_sum(arr, target)
    print(f"The number of combinations to achieve the target sum of {target} is: {result}")

main()
