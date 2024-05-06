def lcs_dp(i, j, A, B, memo):
    if i == len(A) or j == len(B):
        return 0
    
    if memo[i][j] != -1:
        return memo[i][j]

    if A[i] == B[j]:
        memo[i][j] = 1 + lcs_dp(i + 1, j + 1, A, B, memo)
    else:
        memo[i][j] = max(lcs_dp(i + 1, j, A, B, memo), lcs_dp(i, j + 1, A, B, memo))
    
    return memo[i][j]

def main():
    A = "longest"
    B = "stone"
    memo = [[-1] * (len(B) + 1) for _ in range(len(A) + 1)]
    print(lcs_dp(0, 0, A, B, memo))  # Output should be 4 for "long"

main()
