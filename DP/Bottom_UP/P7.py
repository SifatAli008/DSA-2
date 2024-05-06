def Count_Derangements(arr, n, ways):
    ways[1] = 0
    ways[2] = 1
    
    for i in range(3, n+1):
        ways[i] = (i - 1) * (ways[i - 1] + ways[i - 2])

    return ways[n]

def main():
    arr = [3,5,2,1]
    ways = [-1] * (len(arr) + 1)
    print("Number of derangements for", len(arr), "elements:", Count_Derangements(arr, len(arr), ways))

main()
