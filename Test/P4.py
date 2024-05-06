def combination_sum(arr, target):
    dp = [0] * (target + 1)
    dp[0] = 1  # There is one way to make a sum of 0, which is by not choosing any element
    
    for num in arr:
        for i in range(num, target + 1):
            dp[i] += dp[i - num]
    
    return dp[target]

def main():
    arr = [1, 2, 3, 5]
    target = 11
    print("Number of combinations:", combination_sum(arr, target))

main()
