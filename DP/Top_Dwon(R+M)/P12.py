def catalan(n, memo):
    if n <= 1:
        return 1

    if memo[n] != -1:
        return memo[n]

    res = 0
    for i in range(n):
        res += catalan(i, memo) * catalan(n - i - 1, memo)

    memo[n] = res
    return res

n = 3
memo = [-1] * (n + 1)  # Corrected size of memo
result = catalan(n, memo)
print("Catalan(" + str(n) + ") =", result)
