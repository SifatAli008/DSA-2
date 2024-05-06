def combination_sum(arr, n, target, ways, chosen):
    if target == 0:
        print(chosen)
        return 1

    if n == 0:
        return 0

    if ways[n - 1] != -1:
        return ways[n - 1]

    if arr[n - 1] > target:
        return combination_sum(arr, n - 1, target, ways, chosen)

    # Choose the current element
    chosen.append(arr[n - 1])
    taken = combination_sum(arr, n - 1, target - arr[n - 1], ways, chosen)
    # Backtrack: Unchoose the current element
    chosen.pop()

    not_taken = combination_sum(arr, n - 1, target, ways, chosen)

    ways[n - 1] = taken + not_taken

    return ways[n - 1]


def main():
    arr = [1, 2]
    ways = [-1] * (len(arr) + 1)
    chosen = []
    print(combination_sum(arr, len(arr), 3, ways, chosen))

main()

