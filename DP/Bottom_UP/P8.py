def Painting_the_Fence(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return k
    
    dp = [0] * (n + 1)
    dp[1] = k
    dp[2] = k * k
    
    # Calculate solutions bottom-up
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)
    
    return dp[n]

def main():
    n = 15
    k = 5
    print(Painting_the_Fence(n, k))

main()
