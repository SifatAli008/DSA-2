#Count Derangements

def Count_Derangements(arr, n):
    if n == 0 or n == 1:
        return 0

    if n == 2:
        return 1
    
    return (n - 1) * (Count_Derangements(arr, n - 1) + Count_Derangements(arr, n - 2))

def main():
    arr = [1, 2, 3, 4]
    print("Number of derangements for", len(arr), "elements:", Count_Derangements(arr, len(arr)))

main()
