def LCS_length(X, Y):
    m = len(X)
    n = len(Y)

    # Creating a table to store the lengths of LCSes of substrings
    L = [[0] * (n + 1) for i in range(m + 1)]

    # Building the L[m+1][n+1] table in a bottom-up fashion
    for i in range(m + 1):
        for j in range(n + 1):            
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # LCS length is the last entry in the table
    return L[m][n]


def main():
    str1 = ['a', 'b', 'c', 'd']
    str2 = ['a', 'b', 'd', 'd', 'e', 'a', 'c']
    result_length = LCS_length(str1, str2)
    print("Length of Longest Common Subsequence:", result_length)


main()
