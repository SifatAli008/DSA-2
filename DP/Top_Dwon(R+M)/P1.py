#Nth Fibo

def fibo(num, dp):
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    if dp[num] != -1:
        return dp[num]
    
    dp[num]=  fibo(num - 1, dp) + fibo(num - 2, dp)
    return dp[num]

def main():
    n = 5
    dp = [-1] * (n + 1) #memory
    result = fibo(n, dp)
    print(result)
main()
