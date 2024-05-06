def lcs_dp(A, B):
    m = len(A)
    n = len(B)
    # Initialize the DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the DP table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def main():
    A = "longest"
    B = "stone"
    print(lcs_dp(A, B))  # Output should be 4 for "long"

main()
