def lcs(i, j, A, B):
    if i == len(A) or j == len(B):
        return 0
    elif A[i] == "0" or B[j] == "0":
        return 0
    elif A[i] == B[j]:
        return 1 + lcs(i + 1, j + 1, A, B)
    else:
        return max(lcs(i + 1, j, A, B), lcs(i, j + 1, A, B))

def main():
    A = "longest"
    B = "stone"
    print(lcs(0, 0, A, B))  # Output should be 4 for "BCAB"

main()