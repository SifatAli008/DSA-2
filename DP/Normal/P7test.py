#Count Derangements

def Count_Derangements(n):
    if n == 0 or n == 1:
        return 0

    if n == 2:
        return 1
    
    return (n - 1) * (Count_Derangements(n - 1) + Count_Derangements(n - 2))

def main():
    n = 4
    print("Number of derangements for", n, "elements:", Count_Derangements(n))

main()