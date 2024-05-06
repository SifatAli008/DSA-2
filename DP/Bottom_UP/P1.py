#fibo
def main():
    dp = [0] * 6  
    dp[1] = 1
    
    for i in range(2, 6):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    print(dp[5])  # Print the 6th Fibonacci number

main()
