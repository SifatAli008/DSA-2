def Count_Derangements(arr, n,ways):
    if n == 0 or n == 1:
        return 0

    if n == 2:
        return 1
    
    if ways[n - 1] == -1:
         ways[n-1]= (n - 1) * (Count_Derangements(arr, n - 1,ways) + Count_Derangements(arr, n - 2,ways))

    return ways[n-1]

def main():
    arr = [1, 2, 3, 4]
    ways = [-1] * (len(arr) + 1)
    print("Number of derangements for", len(arr), "elements:", Count_Derangements(arr, len(arr),ways))

main()
