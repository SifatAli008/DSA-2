def count_ways(arr, target):
    ways = [0] * (target + 1)
    ways[0] = 1

    for i in range(len(arr)):
        for j in range(arr[i], target + 1):
            ways[j] += ways[j - arr[i]]

    return ways[target]

def main():
    arr = [1, 2, 3, 5]
    target = 11
    ways = count_ways(arr, target)
    print("Number of ways to make", target, "using array elements:", ways)


main()
